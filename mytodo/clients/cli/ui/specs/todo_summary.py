# mytodo/clients/cli/ui/specs/todo_summary.py

from mytodo.domain.models import ToDoSummary
from .base import ColumnSpec, TableSpec
import mytodo.clients.cli.ui.kit.formatters as formatters


MODEL_FIELDS = list(ToDoSummary.model_fields.keys())

TODO_SUMMARY_SPEC = TableSpec(
    {
        "id": ColumnSpec(label="ID", width=5, align="center"),
        "title": ColumnSpec(label="Title", width=25, formatter=formatters.format_title),
        "task_count": ColumnSpec(label="Tasks", width=7, align="center"),
        "created_at": ColumnSpec(label="Created", width=14, align="center"),
        "updated_at": ColumnSpec(
            label="Updated", width=14, formatter=formatters.format_relative_datetime
        ),
    }
)

TODO_SUMMARY_SPEC.validate_spec(MODEL_FIELDS)
