# todoapp/clients/api/routes/todo_summary.py

from fastapi import APIRouter, status

from todoapp.clients.api import deps
import todoapp.clients.api.http_errors as http_errors
import todoapp.clients.api.adapters as api_ad
from todoapp.clients.api.schemas import (
    CreateToDoRequest,
    ToDoSummaryResponse
)
from todoapp.core.results import Code
from todoapp.domain.models import ToDoSummary


router = APIRouter()


@router.get(
    '/users/{username}/todos',
    response_model=list[ToDoSummaryResponse]
)
def get_todos(username: str) -> list[ToDoSummaryResponse]:
    service = deps.get_todo_service(username)
    res = service.get_todos()
    if res.ok and res.data is not None:
        return [api_ad.to_summary_response(summary) for summary in res.data]
    http_errors.raise_for_result(res)


@router.post(
    '/users/{username}/todos',
    response_model=ToDoSummaryResponse,
    status_code=status.HTTP_201_CREATED
)
def create_todo(
    username: str,
    body: CreateToDoRequest
) -> ToDoSummaryResponse:
    service = deps.get_todo_service(username)
    res = service.create_todo(body.title)
    if res.code == Code.CREATED and res.data is not None:
        summary = ToDoSummary.from_todo(res.data)
        return api_ad.to_summary_response(summary)
    http_errors.raise_for_result(res)


@router.delete(
    '/users/{username}/todos/{todo_id}',
    status_code=status.HTTP_200_OK
)
def delete_todo(
    username: str,
    todo_id: str
) -> dict[str, str]:
    service = deps.get_todo_service(username)
    res = service.delete_todo(todo_id)
    if res.ok:
        return {'message': res.msg}
    http_errors.raise_for_result(res)