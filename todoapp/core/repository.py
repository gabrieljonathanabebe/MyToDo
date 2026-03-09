from typing import Protocol

from todoapp.domain.todo_list import ToDoList

class ToDoRepository(Protocol):
    def load_todo(self, title: str) -> ToDoList | None:
        ...

    def save_todo(self, todo: ToDoList) -> None:
        ...
    
    def list_todos(self) -> dict[str, str]:
        ...

    def delete_todo(self, title: str) -> bool:
        ...