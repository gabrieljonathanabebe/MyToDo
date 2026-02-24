from typing import Optional

from models import Task, Status


class ToDoList:
    def __init__(self, title: str, tasks: Optional[list[Task]] = None):
        self.title: str = title
        self.tasks: list[Task] = tasks or []

    def next_id(self) -> int:
        return (max((t.id for t in self.tasks), default=0) + 1)
    
    def add_task(
        self, task: str, priority: str, due: str | None
    ) -> Task:
        new = Task(
            id=self.next_id(),
            task=task,
            priority=priority,
            status=Status.open,
            due=due
        )
        self.tasks.append(new)
        return new
    
    def delete_task(self, target_id: int) -> bool:
        length_before = len(self.tasks)
        self.tasks = [t for t in self.tasks if t.id != target_id]
        return len(self.tasks) != length_before
    
    def sort_todo(self, key: str, reverse: bool = False) -> bool:
        try:
            self.tasks.sort(key=lambda t: getattr(t, key), reverse=reverse)
            return True
        except AttributeError:
            return False

    def assign_new_ids(self) -> None:
        for i, t in enumerate(self.tasks, 1):
            t.id = i