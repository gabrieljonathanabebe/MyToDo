# todoapp/clients/api/deps.py

import todoapp.core.factories as factories
from todoapp.clients.api import http_results
from todoapp.core.factories import ToDoServices
from todoapp.core.services import UserService
from todoapp.domain.todo_list import ToDoList


def get_user_service() -> UserService:
    return factories.build_user_service()


def get_todo_services(username: str) -> ToDoServices:
    return factories.build_todo_services(username)


def get_open_todo(
    username: str, todo_id: str
) -> tuple[ToDoServices, ToDoList]:
    services = get_todo_services(username)
    todo_res = services.todos.open_todo(todo_id)
    if not todo_res.ok or todo_res.data is None:
        http_results.raise_http_error(todo_res)
    return services, todo_res.data