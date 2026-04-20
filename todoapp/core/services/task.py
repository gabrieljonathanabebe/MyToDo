# todoapp/core/services/task.py

from datetime import date

from todoapp.domain.todo_list import ToDoList
from todoapp.domain.models import Task, Status
from todoapp.core.results import Result, Code
from todoapp.core.services.base import BaseToDoService
from todoapp.core.services.errors import NotFoundError, InvalidInputError
from todoapp.core.services.messages import ToDoMessage
from todoapp.core.services.responses import Success, ok, created, resultify


class TaskService(BaseToDoService):
    @resultify
    def create_task(
        self, todo: ToDoList, description: str,
        priority: str, due: str | None
    ) -> Success[Task]:
        new_task = todo.create_task(
            description=description,
            priority=priority,
            due=due
        )
        self._touch_and_save_todo(todo)
        return created(ToDoMessage.task_created(new_task.id), data=new_task)

        
    @resultify
    def delete_task(self, todo: ToDoList, task_id: str) -> Success[None]:
        parsed_task_id = self._parse_task_id(task_id)
        is_deleted = todo.delete_task(parsed_task_id)
        if not is_deleted:
            raise NotFoundError(ToDoMessage.task_not_found(task_id))
        self._touch_and_save_todo(todo)
        return ok(ToDoMessage.task_deleted(task_id))
    

    @resultify
    def sort_tasks(
        self, todo: ToDoList, key: str, reverse: bool
    ) -> Success[None]:
        try:
            todo.sort_tasks(key, reverse)
        except AttributeError:
            raise InvalidInputError(f'Key {key} not found.')
        self._touch_and_save_todo(todo)
        return ok(f'Sorting by {key}')
    

    @resultify    
    def update_task_description(
        self, todo: ToDoList, task_id: str, description: str
    ) -> Success[None]:
        parsed_task_id = self._parse_task_id(task_id)
        is_updated = todo.update_task_description(parsed_task_id, description)
        if not is_updated:
            raise NotFoundError(ToDoMessage.task_not_found(task_id))
        self._touch_and_save_todo(todo)
        return ok(ToDoMessage.task_updated(task_id))
    

    @resultify
    def update_task_priority(
        self, todo: ToDoList, task_id: str, priority: int
    ) -> Success[None]:
        parsed_task_id = self._parse_task_id(task_id)
        is_updated = todo.update_task_priority(parsed_task_id, priority)
        if not is_updated:
            raise NotFoundError(ToDoMessage.task_not_found(task_id))
        self._touch_and_save_todo(todo)
        return ok(ToDoMessage.task_updated(task_id))
    

    @resultify
    def update_task_status(
        self, todo: ToDoList, task_id: str, status: str
    ) -> Success[None]:
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
    def update_task_due(
        self, todo: ToDoList, task_id: str, due: date | None
    ) -> Success[None]:
        parsed_task_id = self._parse_task_id(task_id)
        is_updated = todo.update_task_due(parsed_task_id, due)
        if not is_updated:
            raise NotFoundError(ToDoMessage.task_not_found(task_id))
        self._touch_and_save_todo(todo)
        return ok(ToDoMessage.task_updated(task_id))


    @resultify
    def toggle_status(self, todo: ToDoList, task_id: str) -> Success[None]:
        parsed_task_id = self._parse_task_id(task_id)
        is_toggled = todo.toggle_status(parsed_task_id)
        if not is_toggled:
            raise NotFoundError(ToDoMessage.task_not_found(task_id))
        self._touch_and_save_todo(todo)
        return ok(ToDoMessage.task_status_toggled(task_id))
    

    def assign_new_ids(self, todo: ToDoList) -> Result[None]:
        count = todo.assign_new_ids()
        self._touch_and_save_todo(todo)
        return Result(Code.OK, f'Reassigned {count} IDs.')