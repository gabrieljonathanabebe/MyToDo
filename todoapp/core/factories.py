from dataclasses import dataclass

import todoapp.core.config as cfg
from todoapp.core.services import ToDoService, TaskService, UserService
from todoapp.infra.repositories import CsvToDoRepository, JsonUserRepository


@dataclass
class ToDoServices:
    todos: ToDoService
    tasks: TaskService



def build_user_service() -> UserService:
    repo = JsonUserRepository(cfg.USERS_FILE)
    return UserService(repo)


def build_todo_services(username: str) -> ToDoServices:
    user_data_dir = cfg.get_user_data_dir(username)
    user_data_dir.mkdir(parents=True, exist_ok=True)
    repo = CsvToDoRepository(user_data_dir)
    return ToDoServices(
        todos=ToDoService(repo),
        tasks=TaskService(repo),
    )