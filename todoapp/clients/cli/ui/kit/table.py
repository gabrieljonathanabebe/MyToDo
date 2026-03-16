# todoapp/clients/cli/ui/kit/table.py
from typing import Any, Callable


from todoapp.domain.models import Task
from .layout import (
    table_border, table_row, table_title, table_header, empty_line
)
from todoapp.clients.cli.ui.specs import TableSpec

def make_table(
    title: str,
    objects: list[Any],
    spec: TableSpec,
    adapter: Callable[[Any], dict[str, str]],
    use_ui_index: bool = False
) -> list[str]:
    table = []
    fields = spec.fields
    labels = spec.labels
    widths = spec.widths
    aligns = spec.aligns
    table_width = sum(w + 1 for w in widths) - 1
    table.append(table_border(widths))
    table.append(table_title(title, table_width))
    table.append(table_border(widths))
    table.append(table_header(labels, widths))
    table.append(table_border(widths))
    if not objects:
        table.append(empty_line(table_width))
        table.append(table_border(widths))
        return table
    for i, obj in enumerate(objects, 1):
        row_data = adapter(obj)
        if use_ui_index and 'id' in row_data:
            row_data['id'] = str(i)
        cells = [row_data[field] for field in fields]
        row = table_row(cells, widths, aligns)
        table.append(row)
    table.append(table_border(widths))
    return table