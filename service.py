from typing import Optional
from datetime import date

from domain import ToDoList
from models import Task
from repository import CsvRepository
from results import Result, Code


class ToDoService:
    def __init__(self, repo: CsvRepository):
        self.repo = repo
    # ===== REPO WRAPPER ======================================
    def list_todo_titles(self) -> dict[str, str]:
        return self.repo.list_todo_titles()
    
    def open_todo_by_choice(self, choice: str) -> Result[ToDoList]:
        titles = self.repo.list_todo_titles()
        title = titles.get(choice)
        if title is None:
            return Result(Code.NOT_FOUND, 'Invalid selection.')
        todo = self.repo.load_todo(title)
        if todo is None:
            return Result(Code.NOT_FOUND, 'List file not found.')
        return Result(Code.OK, data=todo)
    
    def open_todo_by_title(self, title: str) -> Result[ToDoList]:
        todo = self.repo.load_todo(title)
        if todo is None:
            return Result(Code.NOT_FOUND, 'List file not found')
        return Result(Code.OK, data=todo)


    # ===== DOMAIN SERVICES ===================================
    def add_task(
        self, todo: ToDoList, task: str,
        priority: str, due: str | None
    ) -> Task:
        new_task = todo.add_task(
            task=task,
            priority=priority,
            due=due
        )
        self.repo.save_todo(todo)
        return new_task

    def sort_todo(self, todo: ToDoList, key: str, reverse: bool) -> Result[None]:
        ok = todo.sort_todo(key, reverse)
        if not ok:
            return Result(Code.INVALID_INPUT, f'Key "{key}" not found.')
        self.repo.save_todo(todo)
        return Result(Code.OK, f'Sorting by {key}')
    
    def delete_task(self, todo: ToDoList, target_id: int) -> bool:
        ok = todo.delete_task(target_id)
        if not ok:
            return False
        self.repo.save_todo(todo)
        return True
    
    def assign_new_ids(self, todo: ToDoList) -> int:
        count = todo.assign_new_ids()
        self.repo.save_todo(todo)
        return count

    # ===== NEW TO-DO ============================================
    def new_todo(self, title: str) -> ToDoList:
        todo = ToDoList(title)
        self.repo.save_todo(todo)
        return todo