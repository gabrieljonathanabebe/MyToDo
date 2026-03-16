# todoapp/clients/cli/ui/specs/todo_meta.py

from todoapp.domain.models import ToDoMeta
from .base import ColumnSpec, TableSpec


MODEL_FIELDS = list(ToDoMeta.model_fields.keys())

TODO_META_SPEC = TableSpec({
    'id': ColumnSpec(
        'ID', 5, 'right'
    ),
    'title': ColumnSpec(
        'Title', 25
    ),
    'created_at': ColumnSpec(
        'Created', 12, 'center'
    )
})

TODO_META_SPEC.validate_spec(MODEL_FIELDS)