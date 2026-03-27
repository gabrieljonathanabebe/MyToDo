# todoapp/clients/api/routes/todo_detail.py

from fastapi import APIRouter, status

from todoapp.clients.api import deps, http_errors
import todoapp.clients.api.adapters as api_ad
from todoapp.clients.api.schemas import (
    CreateTaskRequest,
    TaskResponse,
    ToDoDetailResponse
)


router = APIRouter()


@router.get(
    '/users/{username}/todos/{todo_id}',
    response_model=ToDoDetailResponse
)
def get_todo_detail(
    username: str,
    todo_id: str
) -> ToDoDetailResponse:
    service = deps.get_todo_service(username)
    res = service.open_todo(todo_id)
    if res.ok and res.data is not None:
        return api_ad.to_detail_response(res.data)
    http_errors.raise_for_result(res)


@router.post(
    '/users/{username}/todos/{todo_id}/tasks',
    response_model=TaskResponse,
    status_code=status.HTTP_201_CREATED
)
def create_task(
    username: str,
    todo_id: str,
    body: CreateTaskRequest
) -> TaskResponse:
    service = deps.get_todo_service(username)
    todo_res = service.open_todo(todo_id)
    if not todo_res.ok or todo_res.data is None:
        http_errors.raise_for_result(todo_res)
    res = service.add_task(
        todo_res.data,
        description=body.description,
        priority=str(body.priority),
        due=body.due.isoformat() if body.due else None
    )
    if res.ok and res.data is not None:
        return api_ad.to_task_response(res.data)
    http_errors.raise_for_result(res)