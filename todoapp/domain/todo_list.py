from typing import Optional

from .models import Task, Status


class ToDoList:
    def __init__(self, title: str, tasks: Optional[list[Task]] = None):
        self.title: str = title
        self.tasks: list[Task] = tasks or []

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