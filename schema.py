from datetime import datetime

SCHEMA = {
    'Id': {
        'parse': lambda v: int(v) if v else None,
        'format': lambda v: str(v) if v is not None else ''
    },
    'Task': {
        'parse': lambda v: v.strip(),
        'format': lambda v: v
    },
    'Priority': {
        'parse': lambda v: int(v) if v else None,
        'format': lambda v: str(v) if v is not None else ''
    },
    'Status': {
        'parse': lambda v: v.lower(),
        'format': lambda v: v
    },
    'Due': {
        'parse': lambda v: datetime.strptime(v, '%d.%m.%Y').date() if v else None,
        'format': lambda v: v.strftime('%d.%m.%Y') if v else ''
    },
    'Days Left': {
        'parse': lambda v: v if v else None,
        'format': lambda v: str(v) if v else ''
    }
}

COLUMNS = ['Id', 'Task', 'Priority', 'Status', 'Due', 'Days Left']

HEADER_ALIGN = {col: "left" for col in COLUMNS}
CELL_ALIGN = {col: "center" for col in COLUMNS}
CELL_ALIGN["Task"] = "left"


def parse_row(row: dict) -> dict:
    return {
        col: SCHEMA[col]['parse'](row.get(col, ''))
        for col in SCHEMA if col in row
    }


def format_row(row: dict) -> dict:
    return {
        col: SCHEMA[col]['format'](row.get(col))
        for col in SCHEMA if col in row
    }