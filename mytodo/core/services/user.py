# mytodo/core/services/user.py

from uuid import uuid4

from mytodo.core.results import Result, Code
from mytodo.core.protocols import UserRepository
from mytodo.domain.models import User


class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def _normalize_username(self, username: str) -> str:
        return username.strip().lower()

    def list_users(self) -> Result[list[User]]:
        return Result(Code.OK, data=self.repo.list_users())

    def get_user(self, username: str) -> User | None:
        return self.repo.get_by_username(username)

    def authenticate(self, username: str, password: str) -> Result[User]:
        username = self._normalize_username(username)
        user = self.repo.get_by_username(username)
        if user is None:
            return Result(Code.UNAUTHORIZED, "Invalid username or password")
        if user.password != password:
            return Result(Code.UNAUTHORIZED, "Invalid username or password")
        return Result(Code.OK, f"Welcome back, {user.username}.", data=user)

    def register_user(self, username: str, password: str) -> Result[User]:
        username = self._normalize_username(username)
        existing_user = self.repo.get_by_username(username)
        if existing_user is not None:
            return Result(
                Code.ALREADY_EXISTS,
                f'Username "{existing_user.username}" already exists.',
            )
        user = User(id=str(uuid4()), username=username, password=password)
        self.repo.save_user(user)
        return Result(Code.CREATED, f'User "{user.username}" created.', data=user)
