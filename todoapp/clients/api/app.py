from fastapi import Depends, FastAPI, status

from todoapp.clients.api.deps import get_service
import todoapp.clients.api.schemas as api_sc
import todoapp.clients.api.adapters as api_ad
import todoapp.clients.api.http_errors as http_errors
from todoapp.core.service import ToDoService
from todoapp.core.results import Code


app = FastAPI(title='ToDo App')

@app.get('/')
def home() -> dict[str, str]:
    return {
        'message': 'Welcome to the ToDo API',
        'docs': '/docs'
    }


@app.get('/health')
def health() -> dict[str, str]:
    return {'status': 'ok'}


@app.get('/todos')
def get_todos(service: ToDoService = Depends(get_service)) -> dict[str, str]:
    res = service.list_todos()
    return res.data


@app.post(
    '/todos',
    response_model=api_sc.ToDoResponse,
    status_code=status.HTTP_201_CREATED
)
def create_todo(
    body: api_sc.CreateToDoRequest,
    service: ToDoService = Depends(get_service)
) -> api_sc.ToDoResponse:
    res = service.new_todo(body.title)
    if res.code == Code.CREATED and res.data is not None:
        return api_sc.ToDoResponse(title=res.data.title)
    http_errors.raise_for_result(res)


@app.get('/todos/{title}', response_model=api_sc.ToDoDetailResponse)
def get_todo_by_title(
    title: str,
    service: ToDoService = Depends(get_service)
) -> api_sc.ToDoDetailResponse:
    res = service.open_todo_by_title(title)
    if res.code == Code.OK and res.data is not None:
        return api_ad.to_todo_detail_response(res.data)
    http_errors.raise_for_result(res)


@app.post(
    '/todos/{title}/tasks',
    response_model=api_sc.TaskResponse,
    status_code=status.HTTP_201_CREATED
)
def create_task(
    title: str,
    body: api_sc.CreateTaskRequest,
    service: ToDoService = Depends(get_service)
) -> api_sc.TaskResponse:
    todo_res = service.open_todo_by_title(title)
    if todo_res.code != Code.OK or todo_res.data is None:
        http_errors.raise_for_result(todo_res)
    res = service.add_task(
        todo_res.data,
        description=body.description,
        priority=str(body.priority),
        due=body.due.isoformat() if body.due else None
    )
    if res.code == Code.OK and res.data is not None:
        return api_ad.to_task_response(res.data)
    http_errors.raise_for_result(res)