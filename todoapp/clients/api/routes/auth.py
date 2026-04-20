# todoapp/clients/api/routes/auth.py

from fastapi import APIRouter, Depends, status

from todoapp.clients.api import deps, http_results
import todoapp.clients.api.adapters as api_ad
from todoapp.clients.api.schemas.auth import (
    LoginRequest, RegisterRequest, UserResponse
)
from todoapp.core.services import UserService


router = APIRouter()


@router.post('/login', response_model=UserResponse)
def login(
    body: LoginRequest,
    service: UserService = Depends(deps.get_user_service)
) -> UserResponse:
    res = service.authenticate(body.username, body.password)
    if res.ok and res.data is not None:
        return api_ad.to_user_response(res.data)
    http_results.raise_http_error(res)


@router.post(
    '/register',
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
def register(
    body: RegisterRequest,
    service: UserService = Depends(deps.get_user_service)
) -> UserResponse:
    res = service.register_user(body.username, body.password)
    if res.ok and res.data is not None:
        return api_ad.to_user_response(res.data)
    http_results.raise_http_error(res)