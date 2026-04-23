from todoapp.domain.models import Task
from .base import ColumnSpec, TableSpec
import todoapp.clients.cli.ui.kit.formatters as formatters


EXTRA_FIELDS = ["days_left"]
MODEL_FIELDS = list(Task.model_fields.keys()) + EXTRA_FIELDS

TASK_SPEC = TableSpec(
    {
        "id": ColumnSpec("ID", 5, "center"),
        "description": ColumnSpec("Description", 25),
        "priority": ColumnSpec("Priority", 10, "center", formatters.format_priority),
        "status": ColumnSpec("Status", 8, "center", formatters.format_status),
        "due": ColumnSpec("Due", 12, "center"),
        "days_left": ColumnSpec("Days left", 11, "center"),
    }
)

TASK_SPEC.validate_spec(MODEL_FIELDS)
