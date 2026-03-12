from pydantic import ValidationError

from todoapp.domain.todo_list import ToDoList
from todoapp.domain.models import Task, ToDoListItem
from .repository import ToDoRepository
from .results import Result, Code


class ToDoService:
    def __init__(self, repo: ToDoRepository):
        self.repo = repo


    # ===== REPO SERVICES =====================================
    def list_todos(self) -> Result[list[ToDoListItem]]:
        return Result(Code.OK, data=self.repo.list_todos())

    def open_todo_by_choice(self, choice: str) -> Result[ToDoList]:
        items = self.list_todos().data or []
        try:
            index = int(choice) - 1
        except ValueError:
            return Result(Code.INVALID_INPUT, 'Invalid selection.')
        if index < 0 or index >= len(items):
            return Result(Code.NOT_FOUND, 'Invalid selection.')
        item = items[index]
        todo = self.repo.load_todo(item.title)
        if todo is None:
            return Result(Code.NOT_FOUND, 'ToDo not found.')
        return Result(Code.OK, data=todo)
    
    def open_todo_by_title(self, title: str) -> Result[ToDoList]:
        todo = self.repo.load_todo(title)
        if todo is None:
            return Result(Code.NOT_FOUND, 'ToDo not found')
        return Result(Code.OK, data=todo)
    
    def delete_todo_by_choice(self, choice: str) -> Result[None]:
        items = self.list_todos().data or []
        try:
            index = int(choice) - 1
        except ValueError:
            return Result(Code.INVALID_INPUT, 'Invalid selection.')
        if index < 0 or index >= len(items):
            return Result(Code.NOT_FOUND, 'Invalid selection.')
        item = items[index]
        deleted = self.repo.delete_todo(item.title)
        if not deleted:
            return Result(Code.NOT_FOUND, 'ToDo not found.')
        return Result(Code.OK, f'{item.title} deleted.')


    # ===== DOMAIN SERVICES ===================================
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
            self.repo.save_todo(todo)
            return Result(Code.OK, f'Task {new_task.id} added.', data=new_task)
        except ValidationError as e:
            first_error = e.errors()[0]
            field = first_error['loc'][0]
            msg = first_error['msg']
            return Result(
                Code.INVALID_INPUT, f'{field.capitalize()}: {msg}'
            )

    def sort_todo(self, todo: ToDoList, key: str, reverse: bool) -> Result[None]:
        try:
            todo.sort_todo(key, reverse)
            self.repo.save_todo(todo)
            return Result(Code.OK, f'Sorting by {key}')
        except AttributeError:
            return Result(Code.INVALID_INPUT, f'Key "{key}" not found.')

    def delete_task(self, todo: ToDoList, target_id: str) -> Result[None]:
        try:
            ok = todo.delete_task(int(target_id))
            if not ok:
                return Result(Code.NOT_FOUND, f'ID {target_id} not found.')
            self.repo.save_todo(todo)
            return Result(Code.OK, f'Task {target_id} deleted.')
        except ValueError:
            return Result(Code.INVALID_INPUT, f'"{target_id}" is not a valid input.')
    
    def assign_new_ids(self, todo: ToDoList) -> Result[None]:
        count = todo.assign_new_ids()
        self.repo.save_todo(todo)
        return Result(Code.OK, f'Reassigned {count} IDs.')
    
    def toggle_status(self, todo: ToDoList, task_id: str) -> Result[None]:
        try:
            ok = todo.toggle_status(int(task_id))
            if not ok:
                return Result(Code.NOT_FOUND, f'Task {task_id} not found.')
            self.repo.save_todo(todo)
            return Result(Code.OK, f'Toggle status for Task {task_id}.')
        except ValueError:
            return Result(Code.INVALID_INPUT, f'"{task_id} is not a valid input.')

    # ===== NEW TO-DO ============================================
    def new_todo(self, title: str) -> Result[ToDoList]:
        if title in [item.title for item in self.list_todos().data]:
            return Result(Code.ALREADY_EXISTS, f'{title} already exists.')
        new_todo = ToDoList(title)
        self.repo.save_todo(new_todo)
        self.repo.register_todo(title)
        return Result(Code.CREATED, f'{new_todo.title} created.', data=new_todo)