# todoapp/domain/models/user.py

from pydantic import BaseModel


class User(BaseModel):
    id: str
    username: str
    password: str