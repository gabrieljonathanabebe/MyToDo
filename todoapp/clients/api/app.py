from fastapi import Depends, FastAPI, HTTPException, status

from todoapp.clients.api.deps import get_service
import todoapp.clients.api.schemas as api_sc
import todoapp.clients.api.adapters as api_ad
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
    if res.code == Code.ALREADY_EXISTS:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='ToDo already exists.'
        )
    raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail='Unexpected service result.'
    )


@app.get('/todos/{title}', response_model=api_sc.ToDoDetailResponse)
def get_todo_by_title(
    title: str,
    service: ToDoService = Depends(get_service)
) -> api_sc.ToDoDetailResponse:
    res = service.open_todo_by_title(title)
    if res.code == Code.OK and res.data is not None:
        return api_ad.to_todo_detail_response(res.data)
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='ToDo not found.'
    )


@app.post(
    '/todos/{title}/tasks',
    response_model=api_sc.TaskResponse,
    status_code=status.HTTP_201_CREATED
)
def create_task(
    title: str,
    body: api_sc.CreateTaskRequest,
    service: ToDoService = Depends(get_service)
):
    todo_res = service.open_todo_by_title(title)
    if todo_res.code != Code.OK or todo_res.data is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='ToDo not found.'
        )
    res = service.add_task(
        todo_res.data,
        description=body.description,
        priority=str(body.priority),
        due=body.due.isoformat() if body.due else None
    )
    if res.code == Code.OK and res.data is not None:
        return api_ad.to_task_response(res.data)
    if res.code == Code.INVALID_INPUT:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=res.msg
        )
    raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail='Unexpected service result.'
    )