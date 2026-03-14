from todoapp.domain.models import Task
from .layout import (
    table_border, table_row, table_title, table_header, empty_line
)
from . import display_spec
from . import display

def make_table(title: str, tasks: list[Task]) -> list[str]:
    table = []
    fields = display_spec.get_fields()
    labels = display_spec.get_labels()
    widths = display_spec.get_widths()
    aligns = display_spec.get_aligns()
    table_width = sum(w+1 for w in widths) - 1
    table.append(table_border(widths))
    table.append(table_title(title, table_width))
    table.append(table_border(widths))
    table.append(table_header(labels, widths))
    table.append(table_border(widths))
    if not tasks:
        table.append(empty_line(table_width))
        table.append(table_border(widths))
        return table
    for task in tasks:
        serialized_task = display.to_display_row(task)
        cells = [serialized_task[field] for field in fields]
        row = table_row(cells, widths, aligns)
        table.append(row)
    table.append(table_border(widths))
    return table