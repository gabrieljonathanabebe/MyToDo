# todoapp/clients/api/routes/todo_detail.py

from fastapi import APIRouter, status

from todoapp.clients.api import deps, http_results
import todoapp.clients.api.adapters as api_ad
from todoapp.clients.api.schemas import (
    CreateTaskRequest,
    UpdateTaskStatusRequest,
    UpdateTaskDescriptionRequest,
    SortTasksRequest,
    TaskResponse,
    ToDoDetailResponse,
    UpdateTaskPriorityRequest,
    UpdateTaskDueRequest,
)


router = APIRouter()


@router.get("", response_model=ToDoDetailResponse)
def get_todo_detail(username: str, todo_id: str) -> ToDoDetailResponse:
    services = deps.get_todo_services(username)
    todo = http_results.unwrap_result(services.todos.open_todo(todo_id))
    return api_ad.to_detail_response(todo)


@router.post("/tasks", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(username: str, todo_id: str, body: CreateTaskRequest) -> TaskResponse:
    services, todo = deps.get_open_todo(username, todo_id)
    task = http_results.unwrap_result(
        services.tasks.create_task(
            todo,
            description=body.description,
            priority=str(body.priority.value),
            due=body.due.isoformat() if body.due else None,
            notes=body.notes,
        )
    )
    return api_ad.to_task_response(task)


@router.delete("/tasks/{task_id}", status_code=status.HTTP_200_OK)
def delete_task(username: str, todo_id: str, task_id: str) -> dict[str, str]:
    services, todo = deps.get_open_todo(username, todo_id)
    res = services.tasks.delete_task(todo, task_id)
    service = deps.get_todo_services(username)
    return http_results.ok_message(res)


@router.patch("/tasks/{task_id}/status", status_code=status.HTTP_200_OK)
def update_task_status(
    username: str, todo_id: str, task_id: str, body: UpdateTaskStatusRequest
) -> dict[str, str]:
    services, todo = deps.get_open_todo(username, todo_id)
    res = services.tasks.update_task_status(
        todo, task_id=task_id, status=body.status.value
    )
    return http_results.ok_message(res)


@router.patch("/sort", status_code=status.HTTP_200_OK)
def sort_tasks(username: str, todo_id: str, body: SortTasksRequest) -> dict[str, str]:
    services, todo = deps.get_open_todo(username, todo_id)
    res = services.tasks.sort_tasks(todo, key=body.key, reverse=body.reverse)
    return http_results.ok_message(res)


@router.patch("/tasks/{task_id}/description", status_code=status.HTTP_200_OK)
def update_task_description(
    username: str, todo_id: str, task_id: str, body: UpdateTaskDescriptionRequest
) -> dict[str, str]:
    services, todo = deps.get_open_todo(username, todo_id)
    res = services.tasks.update_task_description(
        todo, task_id=task_id, description=body.description
    )
    return http_results.ok_message(res)


@router.patch("/tasks/{task_id}/priority", status_code=status.HTTP_200_OK)
def update_task_priority(
    username: str, todo_id: str, task_id: str, body: UpdateTaskPriorityRequest
) -> dict[str, str]:
    services, todo = deps.get_open_todo(username, todo_id)
    res = services.tasks.update_task_priority(
        todo, task_id=task_id, priority=body.priority
    )
    return http_results.ok_message(res)


@router.patch("/tasks/{task_id}/due", status_code=status.HTTP_200_OK)
def update_task_due(
    username: str, todo_id: str, task_id: str, body: UpdateTaskDueRequest
) -> dict[str, str]:
    services, todo = deps.get_open_todo(username, todo_id)
    res = services.tasks.update_task_due(todo, task_id=task_id, due=body.due)
    return http_results.ok_message(res)
