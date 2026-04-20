# todoapp/core/services/todo.py

from todoapp.core.services.base import BaseToDoService
from todoapp.domain.todo_list import ToDoList
from todoapp.domain.models import ToDoSummary
from todoapp.core.results import Result, Code
from todoapp.core.services.errors import (
    NotFoundError,
    AlreadyExistsError
)
from todoapp.core.services.messages import ToDoMessage
from todoapp.core.services.responses import ok, resultify, created


class ToDoService(BaseToDoService):
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
        self._persist_created_todo(create_todo)
        return created(ToDoMessage.todo_created(create_todo.title), data=create_todo)
    

    @resultify
    def delete_todo(self, todo_id: str) -> Result[None]:
        summary = self.repo.get_todo_summary_by_id(todo_id)
        if summary is None:
            raise NotFoundError(ToDoMessage.todo_not_found())
        if not self.repo.delete_todo(todo_id):
            raise NotFoundError(ToDoMessage.todo_not_found())
        return ok(ToDoMessage.todo_deleted(summary.title))