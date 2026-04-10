from __future__ import annotations

from typing import Optional
from uuid import uuid4
from datetime import datetime, timezone

from .models import ToDoSummary, Task, Status


class ToDoList:
    def __init__(
        self,
        title: str,
        todo_id: str | None = None,
        tasks: Optional[list[Task]] = None,
        created_at: datetime | None = None,
        updated_at: datetime | None = None
    ):
        self.title = title
        self.id = todo_id
        self.tasks = tasks or []
        self.created_at = created_at
        self.updated_at = updated_at

    @classmethod
    def create_new(cls, title: str) -> ToDoList:
        now = datetime.now(timezone.utc)
        return cls(
            title=title,
            todo_id=str(uuid4()),
            tasks=[],
            created_at=now,
            updated_at=now
        )
    
    @classmethod
    def from_summary(
        cls,
        todo_summary: ToDoSummary,
        tasks: Optional[list[Task]] = None
    ) -> ToDoList:
        return cls(
            title=todo_summary.title,
            todo_id=todo_summary.id,
            tasks=tasks or [],
            created_at=todo_summary.created_at,
            updated_at=todo_summary.updated_at
        )


    def next_id(self) -> int:
        return (max((t.id for t in self.tasks), default=0) + 1)
    
    def add_task(
        self, description: str, priority: str, due: str | None
    ) -> Task:
        new = Task(
            id=self.next_id(),
            description=description,
            priority=priority,
            status=Status.open,
            due=due
        )
        self.tasks.append(new)
        return new
    
    def delete_task(self, task_id: int) -> bool:
        length_before = len(self.tasks)
        self.tasks = [t for t in self.tasks if t.id != task_id]
        return len(self.tasks) != length_before
    
    def set_status(self, task_id: int, status: Status) -> bool:
        task = next((t for t in self.tasks if t.id == task_id), None)
        if task is None:
            return False
        task.status = status
        return True
    
    def sort_todo(self, key: str, reverse: bool = False) -> None:
        with_value = [t for t in self.tasks if getattr(t, key) is not None]
        without_value = [t for t in self.tasks if getattr(t, key) is None]
        with_value.sort(key=lambda t: getattr(t, key), reverse=reverse)
        without_value.sort(key=lambda t: t.id)
        self.tasks = with_value + without_value

    def assign_new_ids(self) -> int:
        for i, t in enumerate(self.tasks, 1):
            t.id = i
        return len(self.tasks)
    
    def toggle_status(self, task_id: int) -> bool:
        task = next((t for t in self.tasks if t.id == task_id), None)
        if task is None:
            return False
        task.status = Status.done if task.status == Status.open else Status.open
        return True