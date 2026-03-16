# todoapp/clients/cli/ui/specs/todo_meta.py

from todoapp.domain.models import ToDoMeta
from .base import ColumnSpec, TableSpec
import todoapp.clients.cli.ui.kit.formatters as formatters


MODEL_FIELDS = list(ToDoMeta.model_fields.keys())

TODO_META_SPEC = TableSpec({
    'id': ColumnSpec(
        label='ID',
        width=5,
        align='center'
    ),
    'title': ColumnSpec(
        label='Title',
        width=25,
        formatter=formatters.format_title
    ),
    'created_at': ColumnSpec(
        label='Created',
        width=12,
        align='center'
    )
})

TODO_META_SPEC.validate_spec(MODEL_FIELDS)