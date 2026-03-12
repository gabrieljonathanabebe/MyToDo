from typing import Protocol

from todoapp.domain.todo_list import ToDoList
from todoapp.domain.models import ToDoListItem

class ToDoRepository(Protocol):
    def load_todo(self, title: str) -> ToDoList | None:
        ...

    def save_todo(self, todo: ToDoList) -> None:
        ...
    
    def list_todos(self) -> list[ToDoListItem]:
        ...

    def register_todo(self, title: str) -> ToDoListItem:
        ...

    def delete_todo(self, title: str) -> bool:
        ...