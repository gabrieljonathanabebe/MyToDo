# todoapp/clients/api/adapters/todo_detail.py

from todoapp.clients.api.schemas import TaskResponse, ToDoDetailResponse
from todoapp.domain.models import Task
from todoapp.domain.todo_list import ToDoList


def to_task_response(task: Task) -> TaskResponse:
    return TaskResponse(
        id=task.id,
        description=task.description,
        priority=int(task.priority),
        status=task.status.value,
        due=task.due,
        days_left=task.days_left
    )

def to_detail_response(todo: ToDoList) -> ToDoDetailResponse:
    return ToDoDetailResponse(
        id=todo.id,
        title=todo.title,
        tasks=[to_task_response(task) for task in todo.tasks]
    )