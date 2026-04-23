# todoapp/clients/api/schemas/auth.py

from pydantic import BaseModel


# ===== REQUESTS ==============================================================
class LoginRequest(BaseModel):
    username: str
    password: str


class RegisterRequest(BaseModel):
    username: str
    password: str


# ===== RESPONSES =============================================================
class UserResponse(BaseModel):
    id: str
    username: str
