from fastapi import Depends, FastAPI, HTTPException, status

from todoapp.clients.api.deps import get_service
from todoapp.clients.api.schemas import (
    CreateToDoRequest,
    ToDoResponse,
    TaskResponse,
    ToDoDetailResponse,
    CreateTaskRequest
)
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
    '/todos', response_model=ToDoResponse, status_code=status.HTTP_201_CREATED
)
def create_todo(
    body: CreateToDoRequest,
    service: ToDoService = Depends(get_service)
) -> ToDoResponse:
    res = service.new_todo(body.title)
    if res.code == Code.CREATED and res.data is not None:
        return ToDoResponse(title=res.data.title)
    if res.code == Code.ALREADY_EXISTS:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='ToDo already exists.'
        )
    raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail='Unexpected service result.'
    )


@app.get('/todos/{title}', response_model=ToDoDetailResponse)
def get_todo_by_title(
    title: str,
    service: ToDoService = Depends(get_service)
) -> ToDoDetailResponse:
    res = service.open_todo_by_title(title)
    if res.code == Code.OK and res.data is not None:
        tasks = [
            TaskResponse(
                id=task.id,
                description=task.description,
                priority=int(task.priority),
                status=task.status.value,
                due=task.due,
                days_left=task.days_left
            )
            for task in res.data.tasks
        ]
        return ToDoDetailResponse(
            title=res.data.title,
            tasks=tasks
        )
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='ToDo not found.'
    )


@app.post(
    '/todos/{title}/tasks',
    response_model=TaskResponse,
    status_code=status.HTTP_201_CREATED
)
def create_task(
    title: str,
    body: CreateTaskRequest,
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
        return TaskResponse(
            id=res.data.id,
            description=res.data.description,
            priority=int(res.data.priority),
            status=res.data.status.value,
            due=res.data.due,
            days_left=res.data.days_left
        )
    if res.code == Code.INVALID_INPUT:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=res.msg
        )
    raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail='Unexpected service result.'
    )