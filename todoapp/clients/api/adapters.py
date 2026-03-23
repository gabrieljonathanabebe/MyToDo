import todoapp.clients.api.schemas as api_sc
from todoapp.domain.todo_list import ToDoList
from todoapp.domain.models import Task, ToDoListItem


def to_todo_list_item_response(
    item: ToDoListItem
) -> api_sc.ToDoListItemResponse:
    return api_sc.ToDoListItemResponse(
        id=item.id,
        title=item.title,
        created_at=item.created_at
    )


def to_task_response(task: Task) -> api_sc.TaskResponse:
    return api_sc.TaskResponse(
        id=task.id,
        description=task.description,
        priority=int(task.priority),
        status=task.status.value,
        due=task.due,
        days_left=task.days_left
    )

def to_todo_detail_response(
    todo: ToDoList
) -> api_sc.ToDoDetailResponse:
    return api_sc.ToDoDetailResponse(
        title=todo.title,
        tasks=[to_task_response(task) for task in todo.tasks]
    )