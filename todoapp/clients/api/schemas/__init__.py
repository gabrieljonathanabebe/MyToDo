# todoapp/clients/api/schemas/__init__.py

from .auth import LoginRequest, RegisterRequest, UserResponse
from .todo_summary import CreateToDoRequest, ToDoSummaryResponse
from .todo_detail import (
    CreateTaskRequest,
    UpdateTaskStatusRequest,
    TaskResponse,
    ToDoDetailResponse,
)