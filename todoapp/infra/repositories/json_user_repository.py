import json
from pathlib import Path

from todoapp.domain.models import User
import todoapp.infra.adapters.user as user_ad


class JsonUserRepository:
    def __init__(self, path: Path):
        self.path = path

    def _load(self) -> list[User]:
        if not self.path.exists():
            return []
        with self.path.open("r", encoding="utf-8") as f:
            data = json.load(f)
        return user_ad.from_storage(data)

    def _save(self, users: list[User]) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        data = user_ad.to_storage(users)
        with self.path.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    def list_users(self) -> list[User]:
        return self._load()

    def get_by_username(self, username: str) -> User | None:
        users = self._load()
        return next((user for user in users if user.username == username), None)

    def save_user(self, user: User) -> None:
        users = self._load()
        users.append(user)
        self._save(users)
