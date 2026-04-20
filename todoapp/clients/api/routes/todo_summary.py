# todoapp/clients/api/routes/todo_summary.py

from fastapi import APIRouter, status

from todoapp.clients.api import deps
import todoapp.clients.api.http_results as http_results
import todoapp.clients.api.adapters as api_ad
from todoapp.clients.api.schemas import (
    CreateToDoRequest,
    ToDoSummaryResponse
)
from todoapp.domain.models import ToDoSummary


router = APIRouter()


@router.get(
    '/users/{username}/todos',
    response_model=list[ToDoSummaryResponse]
)
def get_todos(username: str) -> list[ToDoSummaryResponse]:
    services = deps.get_todo_services(username)
    summaries = http_results.unwrap_result(services.todos.get_todos())
    return [api_ad.to_summary_response(summary) for summary in summaries]


@router.post(
    '/users/{username}/todos',
    response_model=ToDoSummaryResponse,
    status_code=status.HTTP_201_CREATED
)
def create_todo(
    username: str,
    body: CreateToDoRequest
) -> ToDoSummaryResponse:
    services = deps.get_todo_services(username)
    todo = http_results.unwrap_result(services.todos.create_todo(body.title))
    summary = ToDoSummary.from_todo(todo)
    return api_ad.to_summary_response(summary)


@router.delete(
    '/users/{username}/todos/{todo_id}',
    status_code=status.HTTP_200_OK
)
def delete_todo(
    username: str,
    todo_id: str
) -> dict[str, str]:
    services = deps.get_todo_services(username)
    res = services.todos.delete_todo(todo_id)
    return http_results.ok_message(res)