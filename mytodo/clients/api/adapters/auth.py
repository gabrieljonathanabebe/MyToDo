# mytodo/clients/api/adapters/auth.py

from mytodo.clients.api.schemas import UserResponse
from mytodo.domain.models import User


def to_user_response(user: User) -> UserResponse:
    return UserResponse(id=user.id, username=user.username)
