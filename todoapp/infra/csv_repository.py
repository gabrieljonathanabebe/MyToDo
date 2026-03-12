import json
from uuid import uuid4
from datetime import datetime, timezone

import pandas as pd
from pathlib import Path

import todoapp.infra.adapters.task_storage as task_ad
import todoapp.infra.adapters.todo_index as index_ad
from todoapp.domain.todo_list import ToDoList
from todoapp.domain.models import ToDoListItem


class CsvRepository:
    def __init__(self, DATA_DIR: Path):
        self.DATA_DIR = DATA_DIR

    def _index_path(self) -> Path:
        return self.DATA_DIR / 'todo_index.json'
    
    def _save_index(self, items: list[ToDoListItem]) -> None:
        path = self._index_path()
        data = index_ad.to_storage(items)
        with path.open('w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)

    def _load_index(self) -> list[ToDoListItem]:
        path = self._index_path()
        if path.exists():
            with path.open('r', encoding='utf-8') as f:
                data = json.load(f)
            return index_ad.from_storage(data)
        items: list[ToDoListItem] = []
        for csv_file in sorted(self.DATA_DIR.glob('*.csv')):
            title = csv_file.stem
            created_ts = csv_file.stat().st_mtime
            created_at = datetime.fromtimestamp(created_ts)
            item = ToDoListItem(
                id=str(uuid4()),
                title=title,
                created_at=created_at
            )
            items.append(item)
        self._save_index(items)
        return items
    
    def register_todo(self, title: str) -> ToDoListItem:
        items = self._load_index()
        item = ToDoListItem(
            id=str(uuid4()),
            title=title,
            created_at=datetime.now(timezone.utc)
        )
        items.append(item)
        self._save_index(items)
        return item

    def load_todo(self, title: str) -> ToDoList | None:
        path = self.DATA_DIR / f'{title}.csv'
        if not path.exists():
            return None
        df = pd.read_csv(path)
        tasks = task_ad.from_storage(df)
        return ToDoList(title, tasks=tasks)
    
    def save_todo(self, todo: ToDoList) -> None:
        path = self.DATA_DIR / f'{todo.title}.csv'
        df = task_ad.to_storage(todo.tasks)
        df.to_csv(path, index=False)

    def list_todos(self) -> list[ToDoListItem]:
        items = self._load_index()
        return sorted(items, key=lambda item: item.title.lower())
    
    def delete_todo(self, title: str) -> bool:
        path = self.DATA_DIR / f'{title}.csv'
        if not path.exists():
            return False
        path.unlink()
        items = self._load_index()
        items = [item for item in items if item.title != title]
        self._save_index(items)
        return True