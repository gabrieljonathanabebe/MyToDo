import pandas as pd
from pathlib import Path

from todoapp.infra import adapters
from todoapp.domain.todo_list import ToDoList


class CsvRepository:
    def __init__(self, DATA_DIR: Path):
        self.DATA_DIR = DATA_DIR

    def load_todo(self, title: str) -> ToDoList:
        path = self.DATA_DIR / f'{title}.csv'
        df = pd.read_csv(path)
        tasks = adapters.from_storage(df)
        return ToDoList(title, tasks=tasks)
    
    def save_todo(self, todo: ToDoList) -> None:
        path = self.DATA_DIR / f'{todo.title}.csv'
        df = adapters.to_storage(todo.tasks)
        df.to_csv(path, index=False)

    def list_todos(self) -> dict[str, str]:
        todos = sorted([t.stem for t in self.DATA_DIR.glob('*.csv')])
        return {str(i + 1): title for i, title in enumerate(todos)}

    def delete_todo(self, title: str) -> bool:
        path = self.DATA_DIR / f'{title}.csv'
        if not path.exists():
            return False
        path.unlink()
        return True

    def load(title: str, DATA_DIR: Path) -> ToDoList:
        path = DATA_DIR / f'{title}.csv'
        df = pd.read_csv(path)
        tasks = adapters.from_storage(df)
        todo = ToDoList(title, tasks=tasks)
        return todo