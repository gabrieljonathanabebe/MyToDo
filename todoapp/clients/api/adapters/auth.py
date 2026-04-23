# todoapp/clients/api/adapters/auth.py

from todoapp.clients.api.schemas import UserResponse
from todoapp.domain.models import User


def to_user_response(user: User) -> UserResponse:
    return UserResponse(id=user.id, username=user.username)
