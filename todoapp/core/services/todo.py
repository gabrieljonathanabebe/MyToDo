# todoapp/core/services/todo.py

from datetime import datetime, date, timezone

from todoapp.domain.todo_list import ToDoList
from todoapp.domain.models import Task, ToDoSummary, Status
from todoapp.core.protocols import ToDoRepository
from todoapp.core.results import Result, Code
from todoapp.core.services.errors import (
    NotFoundError,
    InvalidInputError,
    AlreadyExistsError
)
from todoapp.core.services.messages import ToDoMessage
from todoapp.core.services.responses import ok, resultify, created


class ToDoService:
    def __init__(self, repo: ToDoRepository):
        self.repo = repo

    # ===== PRIVATE HELPERS ===================================================
    def _parse_task_id(self, task_id: str) -> int:
        try:
            return int(task_id)
        except ValueError:
            raise InvalidInputError(ToDoMessage.invalid_task_id(task_id))
        
    def _persist_create_todo(self, todo: ToDoList) -> None:
        self.repo.save_todo(todo)
        self.repo.register_todo_summary(todo)

    def _touch_and_save_todo(self, todo: ToDoList) -> None:
        todo.updated_at = datetime.now(timezone.utc)
        self.repo.save_todo(todo)
        self.repo.update_todo_summary(todo)


    # ===== TODO QUERIES ===============================================
    def get_todos(self) -> Result[list[ToDoSummary]]:
        return Result(Code.OK, data=self.repo.get_todos())
    
    @resultify
    def open_todo(self, todo_id: str) -> Result[ToDoList]:
        todo = self.repo.load_todo(todo_id)
        if todo is None:
            raise NotFoundError(ToDoMessage.todo_not_found())
        return ok(data=todo)

    @resultify
    def create_todo(self, title: str) -> Result[ToDoList]:
        existing_summary = self.repo.get_todo_summary_by_title(title)
        if existing_summary is not None:
            raise AlreadyExistsError(ToDoMessage.todo_already_exists(title))
        create_todo = ToDoList.create_new(title)
        self._persist_create_todo(create_todo)
        return created(ToDoMessage.todo_created(create_todo.title), data=create_todo)
    

    @resultify
    def delete_todo(self, todo_id: str) -> Result[None]:
        summary = self.repo.get_todo_summary_by_id(todo_id)
        if summary is None:
            raise NotFoundError(ToDoMessage.todo_not_found())
        if not self.repo.delete_todo(todo_id):
            raise NotFoundError(ToDoMessage.todo_not_found())
        return ok(ToDoMessage.todo_deleted(summary.title))


    # ===== TASK COMMANDS ===============================================
    @resultify
    def create_task(
        self, todo: ToDoList, description: str,
        priority: str, due: str | None
    ) -> Result[Task]:
        new_task = todo.create_task(
            description=description,
            priority=priority,
            due=due
        )
        self._touch_and_save_todo(todo)
        return created(ToDoMessage.task_created(new_task.id), data=new_task)

        
    @resultify
    def delete_task(self, todo: ToDoList, task_id: str) -> Result[None]:
        parsed_task_id = self._parse_task_id(task_id)
        is_deleted = todo.delete_task(parsed_task_id)
        if not is_deleted:
            raise NotFoundError(ToDoMessage.task_not_found(task_id))
        self._touch_and_save_todo(todo)
        return ok(ToDoMessage.task_deleted(task_id))
    

    @resultify
    def sort_tasks(
        self, todo: ToDoList, key: str, reverse: bool
    ) -> Result[None]:
        try:
            todo.sort_tasks(key, reverse)
        except AttributeError:
            raise InvalidInputError(f'Key {key} not found.')
        self._touch_and_save_todo(todo)
        return ok(f'Sorting by {key}')
        
    
    @resultify
    def update_task_status(
        self, todo: ToDoList, task_id: str, status: str
    ) -> Result[None]:
        parsed_task_id = self._parse_task_id(task_id)
        try:
            target_status = Status(status)
        except ValueError:
            raise InvalidInputError(ToDoMessage.invalid_status(status))
        is_updated = todo.set_status(parsed_task_id, target_status)
        if not is_updated:
            raise NotFoundError(ToDoMessage.task_not_found(task_id))
        self._touch_and_save_todo(todo)
        return ok(
            ToDoMessage.task_status_updated(task_id, target_status.value)
        )
        
    
    @resultify    
    def update_task_description(
        self, todo: ToDoList, task_id: str, description: str
    ) -> Result[None]:
        parsed_task_id = self._parse_task_id(task_id)
        is_updated = todo.update_task_description(parsed_task_id, description)
        if not is_updated:
            raise NotFoundError(ToDoMessage.task_not_found(task_id))
        self._touch_and_save_todo(todo)
        return ok(ToDoMessage.task_updated(task_id))


    @resultify
    def update_task_due(
        self, todo: ToDoList, task_id: str, due: date | None
    ) -> Result[None]:
        parsed_task_id = self._parse_task_id(task_id)
        is_updated = todo.update_task_due(parsed_task_id, due)
        if not is_updated:
            raise NotFoundError(ToDoMessage.task_not_found(task_id))
        self._touch_and_save_todo(todo)
        return ok(ToDoMessage.task_updated(task_id))
    

    @resultify
    def update_task_priority(
        self, todo: ToDoList, task_id: str, priority: int
    ) -> Result[None]:
        parsed_task_id = self._parse_task_id(task_id)
        is_updated = todo.update_task_priority(parsed_task_id, priority)
        if not is_updated:
            raise NotFoundError(ToDoMessage.task_not_found(task_id))
        self._touch_and_save_todo(todo)
        return ok(ToDoMessage.task_updated(task_id))

    
    def assign_new_ids(self, todo: ToDoList) -> Result[None]:
        count = todo.assign_new_ids()
        self._touch_and_save_todo(todo)
        return Result(Code.OK, f'Reassigned {count} IDs.')
    
        
    @resultify
    def toggle_status(self, todo: ToDoList, task_id: str) -> Result[None]:
        parsed_task_id = self._parse_task_id(task_id)
        is_toggled = todo.toggle_status(parsed_task_id)
        if not is_toggled:
            raise NotFoundError(ToDoMessage.task_not_found(task_id))
        self._touch_and_save_todo(todo)
        return ok(ToDoMessage.task_status_toggled(task_id))