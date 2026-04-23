from __future__ import annotations
from typing import TYPE_CHECKING
from datetime import datetime

from pydantic import BaseModel


if TYPE_CHECKING:
    from todoapp.domain.todo_list import ToDoList


class ToDoSummary(BaseModel):
    id: str
    title: str
    task_count: int
    created_at: datetime
    updated_at: datetime

    @classmethod
    def from_todo(cls, todo: ToDoList) -> ToDoSummary:
        return cls(
            id=todo.id,
            title=todo.title,
            task_count=len(todo.tasks),
            created_at=todo.created_at,
            updated_at=todo.updated_at,
        )
