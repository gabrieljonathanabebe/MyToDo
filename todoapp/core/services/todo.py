from datetime import datetime, timezone

from pydantic import ValidationError

from todoapp.domain.todo_list import ToDoList
from todoapp.domain.models import Task, ToDoSummary, Status
from todoapp.core.protocols import ToDoRepository
from todoapp.core.results import Result, Code


class ToDoService:
    def __init__(self, repo: ToDoRepository):
        self.repo = repo


    # ===== TODO QUERIES ===============================================
    def list_todos(self) -> Result[list[ToDoSummary]]:
        return Result(Code.OK, data=self.repo.list_todos())
    
    def open_todo(self, todo_id: str) -> Result[ToDoList]:
        todo = self.repo.load_todo(todo_id)
        if todo is None:
            return Result(Code.NOT_FOUND, 'ToDo not found.')
        return Result(Code.OK, data=todo)
    
    def new_todo(self, title: str) -> Result[ToDoList]:
        existing_meta = self.repo.get_todo_summary_by_title(title)
        if existing_meta is not None:
            existing_todo = self.repo.load_todo(existing_meta.id)
            if existing_todo is None:
                return Result(Code.NOT_FOUND, 'ToDo not found.')
            return Result(
                Code.ALREADY_EXISTS,
                f'{title} already exists.',
                data=existing_todo
            )
        new_todo = ToDoList.create_new(title)
        self._persist_new_todo(new_todo)
        return Result(
            Code.CREATED, f'{new_todo.title} created.', data=new_todo
        )
    
    def delete_todo(self, todo_id: str) -> Result[None]:
        meta = self.repo.get_todo_summary_by_id(todo_id)
        if meta is None:
            return Result(Code.NOT_FOUND, 'ToDo not found.')
        if not self.repo.delete_todo(todo_id):
            return Result(Code.NOT_FOUND, 'ToDo not found.')
        return Result(Code.OK, f'ToDo "{meta.title}" deleted.')


    # ===== TASK COMMANDS ===============================================
    def add_task(
        self, todo: ToDoList, description: str,
        priority: str, due: str | None
    ) -> Result[Task]:
        try:
            new_task = todo.add_task(
                description=description,
                priority=priority,
                due=due
            )
            self._touch_and_save_todo(todo)
            return Result(Code.OK, f'Task {new_task.id} added.', data=new_task)
        except ValidationError as e:
            first_error = e.errors()[0]
            field = first_error['loc'][0]
            msg = first_error['msg']
            return Result(
                Code.INVALID_INPUT, f'{field.capitalize()}: {msg}'
            )
        

    def delete_task(self, todo: ToDoList, target_id: str) -> Result[None]:
        try:
            ok = todo.delete_task(int(target_id))
            if not ok:
                return Result(Code.NOT_FOUND, f'ID {target_id} not found.')
            self._touch_and_save_todo(todo)
            return Result(Code.OK, f'Task {target_id} deleted.')
        except ValueError:
            return Result(
                Code.INVALID_INPUT, f'"{target_id}" is not a valid input.'
            )
        

    def set_task_status(
        self, todo: ToDoList, task_id: str, status: str
    ) -> Result[None]:
        try:
            target_id = int(task_id)
        except ValueError:
            return Result(Code.INVALID_INPUT, f'"{task_id}" is not a valid input.')
        try:
            target_status = Status(status)
        except ValueError:
            return Result(Code.INVALID_INPUT, f'"{status}" is not a valid status.')
        ok = todo.set_status(target_id, target_status)
        if not ok:
            return Result(Code.NOT_FOUND, f'Task {task_id} not found.')
        self._touch_and_save_todo(todo)
        return Result(
            Code.OK, f'Task {task_id} status updated to "{target_status.value}"'
        )
    

    def sort_tasks(self, todo: ToDoList, key: str, reverse: bool) -> Result[None]:
        try:
            todo.sort_tasks(key, reverse)
            self._touch_and_save_todo(todo)
            return Result(Code.OK, f'Sorting by {key}')
        except AttributeError:
            return Result(Code.INVALID_INPUT, f'Key "{key}" not found.')


        

    
    def assign_new_ids(self, todo: ToDoList) -> Result[None]:
        count = todo.assign_new_ids()
        self._touch_and_save_todo(todo)
        return Result(Code.OK, f'Reassigned {count} IDs.')
    
    def toggle_status(self, todo: ToDoList, task_id: str) -> Result[None]:
        try:
            ok = todo.toggle_status(int(task_id))
            if not ok:
                return Result(Code.NOT_FOUND, f'Task {task_id} not found.')
            self._touch_and_save_todo(todo)
            return Result(Code.OK, f'Toggle status for Task {task_id}.')
        except ValueError:
            return Result(Code.INVALID_INPUT, f'"{task_id} is not a valid input.')


    # ===== INTERNAL PERSIST HELPER ========================================
    def _persist_new_todo(self, todo: ToDoList) -> None:
        self.repo.save_todo(todo)
        self.repo.register_todo_summary(todo)

    def _touch_and_save_todo(self, todo: ToDoList) -> None:
        todo.updated_at = datetime.now(timezone.utc)
        self.repo.save_todo(todo)
        self.repo.update_todo_summary(todo)