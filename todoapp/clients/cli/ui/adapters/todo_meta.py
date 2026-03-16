# todoapp/clients/cli/ui/adapters/todo_meta.py

from todoapp.domain.models import ToDoMeta
import todoapp.clients.cli.ui.specs as specs
from .base import to_display_row


def todo_meta_to_row(meta: ToDoMeta) -> dict[str, str]:
    row = to_display_row(meta, specs.TODO_META_SPEC)
    row['created_at'] = row['created_at'][:10]
    row['updated_at'] = row['updated_at']
    return row