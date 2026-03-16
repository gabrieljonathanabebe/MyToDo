import json
from uuid import uuid4
from datetime import datetime, timezone

import pandas as pd
from pathlib import Path

import todoapp.infra.adapters.task as task_ad
import todoapp.infra.adapters.todo_meta as meta_ad
from todoapp.domain.todo_list import ToDoList
from todoapp.domain.models import ToDoMeta


class CsvRepository:
    def __init__(self, DATA_DIR: Path):
        self.DATA_DIR = DATA_DIR

    # ===== META METHODS ==================================================
    def _meta_path(self) -> Path:
        return self.DATA_DIR / 'todo_meta.json'
    
    def _save_todo_meta(self, items: list[ToDoMeta]) -> None:
        path = self._meta_path()
        data = meta_ad.to_storage(items)
        with path.open('w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)

    def _load_todo_meta(self) -> list[ToDoMeta]:
        path = self._meta_path()
        # if metadata for todos already exists
        if path.exists():
            with path.open('r', encoding='utf-8') as f:
                data = json.load(f)
            return meta_ad.from_storage(data)
        # if metadata for todos not exists
        items: list[ToDoMeta] = []
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
            items.append(ToDoMeta.from_todo(todo))
        self._save_todo_meta(items)
        return items
    
    def update_todo_meta(self, todo: ToDoList) -> None:
        items = self._load_todo_meta()
        updated_items = []
        for item in items:
            if item.id == todo.id:
                updated_items.append(ToDoMeta.from_todo(todo))
            else:
                updated_items.append(item)
        self._save_todo_meta(updated_items)
    
    def register_todo_meta(self, todo: ToDoList) -> None:
        items = self._load_todo_meta()
        items.append(ToDoMeta.from_todo(todo))
        self._save_todo_meta(items)

    def get_todo_meta_by_id(self, todo_id: str) -> ToDoMeta | None:
        items = self._load_todo_meta()
        return next((item for item in items if item.id == todo_id), None)
    
    def get_todo_meta_by_title(self, title: str) -> ToDoMeta | None:
        items = self._load_todo_meta()
        return next((item for item in items if item.title == title), None)

    
    # ===== TODO METHODS ==================================================
    def load_todo(self, todo_id: str) -> ToDoList | None:
        todo_meta = self.get_todo_meta_by_id(todo_id)
        if todo_meta is None:
            return None
        path = self.DATA_DIR / f'{todo_meta.title}.csv'
        if not path.exists():
            return None
        df = pd.read_csv(path)
        tasks = task_ad.from_storage(df)
        return ToDoList.from_meta(todo_meta, tasks)
    
    def save_todo(self, todo: ToDoList) -> None:
        path = self.DATA_DIR / f'{todo.title}.csv'
        df = task_ad.to_storage(todo.tasks)
        df.to_csv(path, index=False)

    def delete_todo(self, todo_id: str) -> bool:
        items = self._load_todo_meta()
        item = self.get_todo_meta_by_id(todo_id)
        if item is None:
            return False
        path = self.DATA_DIR / f'{item.title}.csv'
        if path.exists():
            path.unlink()
        items = [item for item in items if item.id != todo_id]
        self._save_todo_meta(items)
        return True

    def list_todos(self) -> list[ToDoMeta]:
        items = self._load_todo_meta()
        return sorted(items, key=lambda item: item.title.lower())