import todoapp.core.config as cfg
from todoapp.core.services import ToDoService, UserService
from todoapp.domain.models import User
from todoapp.infra.repositories import CsvToDoRepository, JsonUserRepository


def build_user_service() -> UserService:
    repo = JsonUserRepository(cfg.USERS_FILE)
    return UserService(repo)


def build_todo_service(user: User) -> ToDoService:
    user_data_dir = cfg.get_user_data_dir(user.username)
    user_data_dir.mkdir(parents=True, exist_ok=True)
    repo = CsvToDoRepository(user_data_dir)
    return ToDoService(repo)