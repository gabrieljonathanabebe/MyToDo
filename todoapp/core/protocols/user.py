# todoapp/core/protocols/user.py

from typing import Protocol
from todoapp.domain.models import User


class UserRepository(Protocol):
    def list_users(self) -> list[User]:
        ...

    def get_by_username(self, username: str) -> User | None:
        ...

    def save_user(self, user: User) -> None:
        ...