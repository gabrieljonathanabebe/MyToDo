# mytodo/clients/api/adapters/todo_detail.py

from mytodo.clients.api.schemas import TaskResponse, ToDoDetailResponse
from mytodo.domain.models import Task
from mytodo.domain.todo_list import ToDoList


def to_task_response(task: Task) -> TaskResponse:
    return TaskResponse(
        id=task.id,
        description=task.description,
        priority=task.priority.name,
        status=task.status.value,
        due=task.due,
        days_left=task.days_left,
        created_at=task.created_at,
        updated_at=task.updated_at,
        completed_at=task.completed_at,
        notes=task.notes,
        lead_time_seconds=task.lead_time_seconds,
    )


def to_detail_response(todo: ToDoList) -> ToDoDetailResponse:
    return ToDoDetailResponse(
        id=todo.id,
        title=todo.title,
        tasks=[to_task_response(task) for task in todo.tasks],
    )
