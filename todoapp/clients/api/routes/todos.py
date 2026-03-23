from fastapi import APIRouter, Depends, status

from todoapp.clients.api.deps import get_service
import todoapp.clients.api.schemas as api_sc
import todoapp.clients.api.adapters as api_ad
import todoapp.clients.api.http_errors as http_errors
from todoapp.core.services import ToDoService
from todoapp.core.results import Code


router = APIRouter()


@router.get('/todos', response_model=list[api_sc.ToDoListItemResponse])
def get_todos(
    service: ToDoService = Depends(get_service)
) -> list[api_sc.ToDoListItemResponse]:
    res = service.list_todos()
    if res.code == Code.OK and res.data is not None:
        return [
            api_ad.to_todo_list_item_response(item) for item in res.data
        ]
    http_errors.raise_for_result(res)


@router.post(
    '/todos',
    response_model=api_sc.ToDoListItemResponse,
    status_code=status.HTTP_201_CREATED
)
def create_todo(
    body: api_sc.CreateToDoRequest,
    service: ToDoService = Depends(get_service)
) -> api_sc.ToDoListItemResponse:
    res = service.new_todo(body.title)
    if res.code == Code.CREATED and res.data is not None:
        return api_ad.to_todo_list_item_response