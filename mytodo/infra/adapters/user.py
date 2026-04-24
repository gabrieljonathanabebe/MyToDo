from typing import Any
from mytodo.domain.models import User


def from_storage(data: list[dict[str, Any]]) -> list[User]:
    return [User.model_validate(item) for item in data]


def to_storage(users: list[User]) -> list[dict[str, Any]]:
    return [user.model_dump(mode="json") for user in users]
