import adapters
from models import Task
from .layout import table_border, table_row, table_title, table_header
from .style import italic, bold


def make_table(title: str, tasks: list[Task]) -> list[str]:
    table = []
    display_spec = adapters.get_display_spec()
    fields = [d[0] for d in display_spec]
    labels = [d[1] for d in display_spec]
    aligns = [d[2] for d in display_spec]
    widths = [d[3] for d in display_spec]
    table_width = sum(w+1 for w in widths) - 1
    table.append(table_border(widths))
    table.append(table_title(title, table_width))
    table.append(table_border(widths))
    table.append(table_header(labels, widths))
    table.append(table_border(widths))
    for task in tasks:
        serialized_task = adapters.to_display(task)
        cells = [serialized_task[field] for field in fields]
        row = table_row(cells, widths, aligns)
        table.append(row)
    table.append(table_border(widths))
    return table