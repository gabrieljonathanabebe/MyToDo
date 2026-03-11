import todoapp.clients.api.schemas as api_schemas
from todoapp.domain.todo_list import ToDoList
from todoapp.domain.models import Task


def to_task_response(task: Task) -> api_schemas.TaskResponse:
    return api_schemas.TaskResponse(
        id=task.id,
        description=task.description,
        priority=int(task.priority),
        status=task.status.value,
        due=task.due,
        days_left=task.days_left
    )

def to_todo_detail_response(
    todo: ToDoList
) -> api_schemas.ToDoDetailResponse:
    return api_schemas.ToDoDetailResponse(
        title=todo.title,
        tasks=[to_task_response(task) for task in todo.tasks]
    )