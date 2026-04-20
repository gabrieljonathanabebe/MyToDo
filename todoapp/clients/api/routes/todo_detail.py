# todoapp/clients/api/routes/todo_detail.py

from fastapi import APIRouter, status

from todoapp.clients.api import deps, http_errors
import todoapp.clients.api.adapters as api_ad
from todoapp.clients.api.schemas import (
    CreateTaskRequest,
    UpdateTaskStatusRequest,
    UpdateTaskDescriptionRequest,
    SortTasksRequest,
    TaskResponse,
    ToDoDetailResponse,
    UpdateTaskPriorityRequest,
    UpdateTaskDueRequest
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
    res = service.create_task(
        todo_res.data,
        description=body.description,
        priority=str(body.priority.value),
        due=body.due.isoformat() if body.due else None
    )
    if res.ok and res.data is not None:
        return api_ad.to_task_response(res.data)
    http_errors.raise_for_result(res)


@router.delete(
    '/users/{username}/todos/{todo_id}/tasks/{task_id}',
    status_code=status.HTTP_200_OK
)
def delete_task(
    username: str,
    todo_id: str,
    task_id: str
) -> dict[str, str]:
    service = deps.get_todo_service(username)
    todo_res = service.open_todo(todo_id)
    if not todo_res.ok or todo_res.data is None:
        http_errors.raise_for_result(todo_res)
    res = service.delete_task(todo_res.data, task_id)
    if res.ok:
        return {'message': res.msg}
    http_errors.raise_for_result(res)


@router.patch(
    '/users/{username}/todos/{todo_id}/tasks/{task_id}/status',
    status_code=status.HTTP_200_OK
)
def update_task_status(
    username: str,
    todo_id: str,
    task_id: str,
    body: UpdateTaskStatusRequest
) -> dict[str, str]:
    service = deps.get_todo_service(username)
    todo_res = service.open_todo(todo_id)
    if not todo_res.ok or todo_res.data is None:
        http_errors.raise_for_result(todo_res)
    res = service.update_task_status(
        todo_res.data,
        task_id=task_id,
        status=body.status.value
    )
    if res.ok:
        return {'message': res.msg}
    http_errors.raise_for_result(res)


@router.patch(
    '/users/{username}/todos/{todo_id}/sort',
    status_code=status.HTTP_200_OK
)
def sort_tasks(
    username: str,
    todo_id: str,
    body: SortTasksRequest
) -> dict[str, str]:
    service = deps.get_todo_service(username)
    todo_res = service.open_todo(todo_id)
    if not todo_res.ok or todo_res.data is None:
        http_errors.raise_for_result(todo_res)
    res = service.sort_tasks(
        todo_res.data,
        key=body.key,
        reverse=body.reverse
    )
    if res.ok:
        return {'message': res.msg}
    http_errors.raise_for_result(res)


@router.patch(
    '/users/{username}/todos/{todo_id}/tasks/{task_id}/description',
    status_code=status.HTTP_200_OK
)
def update_task_description(
    username: str,
    todo_id: str,
    task_id: str,
    body: UpdateTaskDescriptionRequest
) -> dict[str, str]:
    service = deps.get_todo_service(username)
    todo_res = service.open_todo(todo_id)
    if not todo_res.ok or todo_res.data is None:
        http_errors.raise_for_result(todo_res)
    res = service.update_task_description(
        todo_res.data,
        task_id=task_id,
        description=body.description
    )
    if res.ok:
        return {'message': res.msg}
    http_errors.raise_for_result(res)


@router.patch(
    '/users/{username}/todos/{todo_id}/tasks/{task_id}/priority',
    status_code=status.HTTP_200_OK
)
def update_task_priority(
    username: str,
    todo_id: str,
    task_id: str,
    body: UpdateTaskPriorityRequest
) -> dict[str, str]:
    service = deps.get_todo_service(username)
    todo_res = service.open_todo(todo_id)
    if not todo_res.ok or todo_res.data is None:
        http_errors.raise_for_result(todo_res)
    res = service.update_task_priority(
        todo_res.data,
        task_id=task_id,
        priority=body.priority
    )
    if res.ok:
        return {'message': res.msg}
    http_errors.raise_for_result(res)


@router.patch(
    '/users/{username}/todos/{todo_id}/tasks/{task_id}/due',
    status_code=status.HTTP_200_OK
)
def update_task_due(
    username: str,
    todo_id: str,
    task_id: str,
    body: UpdateTaskDueRequest
) -> dict[str, str]:
    service = deps.get_todo_service(username)
    todo_res = service.open_todo(todo_id)
    if not todo_res.ok or todo_res.data is None:
        http_errors.raise_for_result(todo_res)
    res = service.update_task_due(
        todo_res.data,
        task_id=task_id,
        due=body.due
    )
    if res.ok:
        return {'message': res.msg}
    http_errors.raise_for_result(res)