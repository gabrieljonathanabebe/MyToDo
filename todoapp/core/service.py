from pydantic import ValidationError

from todoapp.domain.todo_list import ToDoList
from todoapp.domain.models import Task
from todoapp.infra.csv_repository import CsvRepository
from .results import Result, Code


class ToDoService:
    def __init__(self, repo: CsvRepository):
        self.repo = repo


    # ===== REPO WRAPPER ======================================
    def list_todos(self) -> Result[dict[str, str]]:
        return Result(Code.OK, data=self.repo.list_todos())

    def open_todo_by_choice(self, choice: str) -> Result[ToDoList]:
        title = self.list_todos().data.get(choice)
        if title is None:
            return Result(Code.NOT_FOUND, 'Invalid selection.')
        todo = self.repo.load_todo(title)
        if todo is None:
            return Result(Code.NOT_FOUND, 'List file not found.')
        return Result(Code.OK, data=todo)
    
    def open_todo_by_title(self, title: str) -> Result[ToDoList]:
        todo = self.repo.load_todo(title)
        if todo is None:
            return Result(Code.NOT_FOUND, 'List file not found')
        return Result(Code.OK, data=todo)
    
    def delete_todo_by_choice(self, choice: str) -> Result[None]:
        title = self.list_todos().data.get(choice)
        if title is None:
            return Result(Code.INVALID_INPUT, 'Invalid selection.')
        deleted = self.repo.delete_todo(title)
        if not deleted:
            return Result(Code.NOT_FOUND, 'List file not found.')
        return Result(Code.OK, f'{title} deleted.')


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

    # ===== NEW TO-DO ============================================
    def new_todo(self, title: str) -> Result[ToDoList]:
        if title in self.list_todos().data.values():
            return Result(Code.ALREADY_EXISTS)
        new_todo = ToDoList(title)
        self.repo.save_todo(new_todo)
        return Result(Code.CREATED, f'{new_todo.title} created.', data=new_todo)