# todoapp/clients/api/deps.py

import todoapp.core.factories as factories
from todoapp.core.factories import ToDoServices
from todoapp.core.services import UserService


def get_user_service() -> UserService:
    return factories.build_user_service()

def get_todo_services(username: str) -> ToDoServices:
    return factories.build_todo_services(username)