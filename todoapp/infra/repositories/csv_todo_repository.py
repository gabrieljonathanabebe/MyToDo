import json
from uuid import uuid4
from datetime import datetime, timezone

import pandas as pd
from pathlib import Path

import todoapp.infra.adapters.task as task_ad
import todoapp.infra.adapters.todo_summary as summary_ad
from todoapp.domain.todo_list import ToDoList
from todoapp.domain.models import ToDoSummary


class CsvToDoRepository:
    def __init__(self, DATA_DIR: Path):
        self.DATA_DIR = DATA_DIR

    # ===== META METHODS ==================================================
    def _meta_path(self) -> Path:
        return self.DATA_DIR / 'todo_summary.json'
    
    def _save_todo_summary(self, items: list[ToDoSummary]) -> None:
        path = self._meta_path()
        data = summary_ad.to_storage(items)
        with path.open('w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)

    def _load_todo_summary(self) -> list[ToDoSummary]:
        path = self._meta_path()
        # if metadata for todos already exists
        if path.exists():
            with path.open('r', encoding='utf-8') as f:
                data = json.load(f)
            return summary_ad.from_storage(data)
        # if metadata for todos not exists
        items: list[ToDoSummary] = []
        for csv_file in sorted(self.DATA_DIR.glob('*.csv')):
            df = pd.read_csv(csv_file)
            title = csv_file.stem
            tasks = task_ad.from_storage(df)
            created_ts = csv_file.stat().st_mtime
            created_at = datetime.fromtimestamp(created_ts, tz=timezone.utc)
            todo = ToDoList(
                title=title,
                todo_id=str(uuid4()),
                tasks=tasks,
                created_at=created_at,
                updated_at=created_at
            )
            items.append(ToDoSummary.from_todo(todo))
        self._save_todo_summary(items)
        return items
    
    def update_todo_summary(self, todo: ToDoList) -> None:
        items = self._load_todo_summary()
        updated_items = []
        for item in items:
            if item.id == todo.id:
                updated_items.append(ToDoSummary.from_todo(todo))
            else:
                updated_items.append(item)
        self._save_todo_summary(updated_items)
    
    def register_todo_summary(self, todo: ToDoList) -> None:
        items = self._load_todo_summary()
        items.append(ToDoSummary.from_todo(todo))
        self._save_todo_summary(items)

    def get_todo_summary_by_id(self, todo_id: str) -> ToDoSummary | None:
        items = self._load_todo_summary()
        return next((item for item in items if item.id == todo_id), None)
    
    def get_todo_summary_by_title(self, title: str) -> ToDoSummary | None:
        items = self._load_todo_summary()
        return next((item for item in items if item.title == title), None)

    
    # ===== TODO METHODS ==================================================
    def load_todo(self, todo_id: str) -> ToDoList | None:
        todo_summary = self.get_todo_summary_by_id(todo_id)
        if todo_summary is None:
            return None
        path = self.DATA_DIR / f'{todo_summary.title}.csv'
        if not path.exists():
            return None
        df = pd.read_csv(path)
        tasks = task_ad.from_storage(df)
        return ToDoList.from_summary(todo_summary, tasks)
    
    def save_todo(self, todo: ToDoList) -> None:
        path = self.DATA_DIR / f'{todo.title}.csv'
        df = task_ad.to_storage(todo.tasks)
        df.to_csv(path, index=False)

    def delete_todo(self, todo_id: str) -> bool:
        items = self._load_todo_summary()
        item = self.get_todo_summary_by_id(todo_id)
        if item is None:
            return False
        path = self.DATA_DIR / f'{item.title}.csv'
        if path.exists():
            path.unlink()
        items = [item for item in items if item.id != todo_id]
        self._save_todo_summary(items)
        return True

    def get_todos(self) -> list[ToDoSummary]:
        items = self._load_todo_summary()
        return sorted(items, key=lambda item: item.updated_at, reverse=True)