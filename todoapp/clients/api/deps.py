# todoapp/clients/api/deps.py

import todoapp.core.factories as factories
from todoapp.core.services import UserService, ToDoService


def get_user_service() -> UserService:
    return factories.build_user_service()

def get_todo_service(username: str) -> ToDoService:
    return factories.build_todo_service(username)