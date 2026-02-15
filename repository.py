from typing import Any
import pandas as pd
from pathlib import Path

from todo_list import ToDoList
import schema as sc


def save(todo_list: ToDoList, DATA_DIR: Path) -> None:
    parsed_table = todo_list.table
    formatted_table = [sc.format_row(row) for row in parsed_table]
    df = pd.DataFrame(formatted_table)
    df.to_csv(DATA_DIR / f'{todo_list.title}.csv', index=False)