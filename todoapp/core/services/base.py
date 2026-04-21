# todoapp/core/services/base.py

from datetime import datetime, timezone

from todoapp.domain.todo_list import ToDoList
from todoapp.core.protocols import ToDoRepository
from todoapp.core.services.errors import InvalidInputError
from todoapp.core.services.messages import ToDoMessage


class BaseToDoService:
    def __init__(self, repo: ToDoRepository):
        self.repo = repo


    def _parse_task_id(self, task_id: str) -> int:
        if not task_id.strip():
            raise InvalidInputError(
                ToDoMessage.invalid_task_id(task_id)
            )
        return task_id
        

    def _persist_created_todo(self, todo: ToDoList) -> None:
        self.repo.save_todo(todo)
        self.repo.register_todo_summary(todo)


    def _touch_and_save_todo(self, todo: ToDoList) -> None:
        todo.updated_at = datetime.now(timezone.utc)
        self.repo.save_todo(todo)
        self.repo.update_todo_summary(todo)