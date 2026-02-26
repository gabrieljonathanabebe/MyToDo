import pandas as pd
from pathlib import Path

import adapters
from domain import ToDoList


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

    def list_todo_titles(self) -> dict[str, str]:
        todo_titles = sorted([t.stem for t in self.DATA_DIR.glob('*.csv')])
        return {str(i + 1): title for i, title in enumerate(todo_titles)}
        
    def delete_todo_by_choice(self, choice: str) -> bool:
        listed_todo_titles = self.list_todo_titles()
        selected_title = listed_todo_titles.get(choice)
        path = self.DATA_DIR / f'{selected_title}.csv'
        pass

    def load(title: str, DATA_DIR: Path) -> ToDoList:
        path = DATA_DIR / f'{title}.csv'
        df = pd.read_csv(path)
        tasks = adapters.from_storage(df)
        todo = ToDoList(title, tasks=tasks)
        return todo