# mytodo/clients/cli/ui/adapters/todo_summary.py

from mytodo.domain.models import ToDoSummary
import mytodo.clients.cli.ui.specs as specs
from .base import to_display_row


def todo_summary_to_row(meta: ToDoSummary) -> dict[str, str]:
    row = to_display_row(meta, specs.TODO_SUMMARY_SPEC)
    row["created_at"] = row["created_at"][:10]
    row["updated_at"] = row["updated_at"]
    return row
