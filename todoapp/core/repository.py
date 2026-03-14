from typing import Protocol

from todoapp.domain.todo_list import ToDoList
from todoapp.domain.models import ToDoMeta

class ToDoRepository(Protocol):
    def load_todo(self, todo_id: str) -> ToDoList | None:
        ...

    def save_todo(self, todo: ToDoList) -> None:
        ...

    def delete_todo(self, todo_id: str) -> bool:
        ...
    
    def list_todos(self) -> list[ToDoMeta]:
        ...

    def register_todo_meta(self, todo: ToDoList) -> None:
        ...

    def get_todo_meta_by_id(self, todo_id: str) -> ToDoMeta | None:
        ...

    def get_todo_meta_by_title(self, title: str) -> ToDoMeta | None:
        ...