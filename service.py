from typing import Optional
from datetime import date

from domain import ToDoList
from models import Task, Priority
from repository import CsvRepository


class ToDoService:
    def __init__(self, repo: CsvRepository):
        self.repo = repo

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

    def sort_todo(self, todo: ToDoList, key: str, reverse: bool) -> bool:
        ok = todo.sort_todo(key, reverse)
        if not ok:
            return False
        self.repo.save_todo(todo)
        return True
    
    def delete_task(self, todo: ToDoList, target_id: int) -> bool:
        ok = todo.delete_task(target_id)
        if not ok:
            return False
        self.repo.save_todo(todo)
        return True
    
    def assign_new_ids(self, todo: ToDoList) -> None:
        todo.assign_new_ids()
        self.repo.save_todo(todo)

    # ===== NEW TO-DO ============================================
    def new_todo(self, title: str) -> ToDoList:
        todo = ToDoList(title)
        self.repo.save_todo(todo)
        return todo