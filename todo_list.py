from datetime import date
import pandas as pd
from pathlib import Path

import schema as sc
import ui

class ToDoList:
    def __init__(self, title: str):
        self.title: str = title
        self.columns: list[str] = sc.COLUMNS
        self.header_align: list[str] = sc.HEADER_ALIGN
        self.cell_align: list[str] = sc.CELL_ALIGN
        self.rows: list[dict] = []
        self.widths = {}


    def compute_days_left(self, due: date) -> int:
        return (due - date.today()).days
    

    def get_widths(self, display_rows: list[dict]) -> tuple:
        # 1. Get col widths
        col_widths = {}
        for col in self.columns:
            col_fields = [
                display_row.get(col, '') for display_row in display_rows
            ]
            col_fields.append(col)
            col_widths[col] = max(len(str(v)) for v in col_fields) + 2
        # 2. Get total width of the table
        table_width = [sum(w + 1 for w in col_widths.values()) - 1]
        # 3. Collect them in a tuple and return
        return col_widths, table_width
    
    def get_display_rows(self) -> list[dict]:
        display_rows = []
        for row in self.rows:
            display_row = row.copy()
            due = display_row.get('Due', '')
            display_row['Days Left'] = self.compute_days_left(due)
            display_rows.append(display_row)
        return display_rows


    def render_table(self):
        '''
        Main method to render the table.
        1) Collect the inline rows and all data in general.
        2) Determinate the widths based on all data.
        3) Render the frames based on the widths and fill them with the data.
        '''
        # 1)
        display_rows = self.get_display_rows()
        # 2)
        col_widths, table_width = self.get_widths(display_rows)
        # 3)
        ui.border(col_widths)
        ui.title(plain=self.title, total_width=table_width[0])
        ui.border(col_widths)
        ui.table_header(columns=self.columns, col_widths=col_widths)
        ui.border(col_widths)
        display_rows = [sc.format_row(display_row) for display_row in display_rows]
        ui.multi_rows(
            display_rows=display_rows,
            columns=self.columns,
            col_widths=col_widths,
            vertical_padding=True
        )
        ui.border(col_widths)


    def add_task(self):
        task = input('Please enter the task: ')
        priority = input('Which priority does the task have? ')
        status = 'open'
        due = input(
            'By when does the task have to be completed(D.M.YYYY)? '
        )
        new_row = {
            'Id': max(row.get('Id', 0) for row in self.rows) + 1,
            'Task': task,
            'Priority': priority,
            'Status': status,
            'Due': due,
        }
        new_row = sc.parse_row(new_row)
        self.rows.append(new_row)


    def delete_task(self) -> None:
        target_id = int(input(
            'Select the Id for the task to be deleted: '
        ))
        detected = False
        for row in self.rows:
            if row['Id'] == target_id:
                self.rows.remove(row)
                detected = True
        if not detected:
            print('Please select an existing Id. ')
            return self.delete_task()


    def sort_todo(self, reverse: bool = False) -> None:
        sort_key = input('Sorted by? ')
        order = input(f'Sort {sort_key} ascending(asc) or descending(desc)? ')
        if order == 'desc':
            reverse = True
        try:
            self.rows.sort(key=lambda x: x[sort_key.capitalize()], reverse=reverse)
            ui.success('Sorted successfully.')
        except KeyError:
            ui.error('Invalid column, try again.')
            self.sort_todo()


    def assign_new_ids(self) -> None:
        for i, row in enumerate(self.rows, 1):
            row['Id'] = i


    def save_todo(self, DATA_DIR: Path) -> None:
        path = DATA_DIR / f'{self.title}.csv'
        export_table = [sc.format_row(row) for row in self.rows]
        df = pd.DataFrame(export_table)
        df.to_csv(path, index=False)
        ui.success(f'To-Do-List successfully saved in {path}')


    @classmethod
    def load_todo(cls, title: str, DATA_DIR: Path):    
        path = DATA_DIR / f'{title}.csv'
        df = pd.read_csv(path)
        obj = cls(title)
        obj.rows = df.to_dict(orient='records')
        obj.rows = [sc.parse_row(row) for row in obj.rows]
        return obj