from __future__ import annotations
from typing import TYPE_CHECKING
from datetime import datetime

from pydantic import BaseModel


if TYPE_CHECKING:
    from todoapp.domain.todo_list import ToDoList


class ToDoMeta(BaseModel):
    id: str
    title: str
    created_at: datetime

    @classmethod
    def from_todo(cls, todo: ToDoList) -> ToDoMeta:
        return cls(
            id=todo.id,
            title=todo.title,
            created_at=todo.created_at
        )