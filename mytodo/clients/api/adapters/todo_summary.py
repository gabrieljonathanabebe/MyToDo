# mytodo/clients/api/adapters/todo_summary.py

from mytodo.clients.api.schemas import ToDoSummaryResponse
from mytodo.domain.models import ToDoSummary


def to_summary_response(item: ToDoSummary) -> ToDoSummaryResponse:
    return ToDoSummaryResponse(
        id=item.id,
        title=item.title,
        created_at=item.created_at,
        updated_at=item.updated_at,
        task_count=item.task_count,
    )
