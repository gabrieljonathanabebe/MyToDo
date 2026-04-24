# mytodo/clients/cli/ui/adapters/task.py

from mytodo.domain.models import Task
import mytodo.clients.cli.ui.specs as specs
from .base import to_display_row, to_display_value


def task_to_row(task: Task) -> dict[str, str]:
    row = to_display_row(task, specs.TASK_SPEC)
    row["days_left"] = to_display_value(task.days_left)
    return row
