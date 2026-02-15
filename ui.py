from typing import Callable, Any

from my_utils import ansi


# ===== FONT STYLES ==============================
def colorize(color: str, msg: str) -> None:
    print(f'{color}{msg}{ansi.RESET}')

def italic(plain: str) -> str:
    return f'{ansi.ITALIC}{plain}{ansi.RESET}'

def bold(plain: str) -> str:
    return f'{ansi.BOLD}{plain}{ansi.RESET}'

def colorize_red(msg: str) -> None:
    colorize(ansi.RED, msg)

def colorize_yellow(msg: str) -> None:
    colorize(ansi.YELLOW, msg)

def colorize_green(msg: str) -> None:
    colorize(ansi.GREEN, msg)


# ===== INFOS ====================================
def error(msg: str) -> None:
    colorize_red(msg)

def warning(msg: str) -> None:
    colorize_yellow(msg)

def success(msg: str) -> None:
    colorize_green(msg)


# ===== HELPER ===================================
def as_list(x: Any) -> list:
    if not isinstance(x, list):
        return [x]
    return x

def get_widths(
    display_rows: list[dict], columns: list[str]
) -> tuple[dict[str, int], int]:
    col_widths = {}
    for col in columns:
        col_cells = [
            display_row.get(col, '') for display_row in display_rows
        ]
        col_cells.append(col)
        col_widths[col] = max(len(str(c)) for c in col_cells) + 2
    table_width = sum(w + 1 for w in col_widths.values()) - 1
    return col_widths, table_width


# ===== PRIMITIVES ================================
def make_border(width: int | list[int]) -> str:
    width = [width] if isinstance(width, int) else width
    return '+' + '+'.join(['-' * w for w in width]) + '+'

def pad(text: str, width: int, align: str = 'left') -> str:
    if align == 'center':
        return text.center(width - 2)
    elif align == 'right':
        return text.rjust(width - 2)
    else:
        return text.ljust(width - 2)
    
def make_line(
    text: str | list[str],
    width: int | list[int],
    align: str | list[str] = "left",
    style: Callable[[str], str] | None = None,
) -> str:
    cells = as_list(text)
    widths = as_list(width)
    aligns = as_list(align)
    padded_cells = [
        pad(cell, width, align)
        for cell, width, align in zip(cells, widths, aligns)
    ]
    if style:
        padded_cells = [style(c) for c in padded_cells]
    return '| ' + ' | '.join(padded_cells) + ' |'


# ===== TABLE COMPONENTS ==========================
def make_table_title(title: str, width: int) -> str:
    return make_line(title.capitalize(), width, 'center', style=bold)

def make_table_header(
    columns: list[str], widths: list[str], header_aligns: list[str]
) -> str:
    return make_line(columns, widths, header_aligns, style=italic)

def make_table(
    title: str, display_rows: list[dict],
    columns: list[str], col_widths: dict[str, list[int]],
    header_aligns: dict[str, str], cell_aligns: dict[str, str]
) -> list[str]:
    # 1)
    table = []
    # 2)
    col_widths, table_width = get_widths(display_rows, columns)
    col_widths = list(col_widths.values())
    header_aligns = list(header_aligns.values())
    cell_aligns = list(cell_aligns.values())
    # 3)
    table.append(make_border(table_width))
    table.append(make_table_title(title, table_width))
    table.append(make_border(table_width))
    table.append(make_table_header(columns, col_widths, header_aligns))
    table.append(make_border(table_width))
    for display_row in display_rows:
        cells = list(display_row.values())
        row = make_line(cells, col_widths, cell_aligns, style=italic)
        table.append(row)
    table.append(make_border(table_width))
    return table


# ===== MENU ==========================================
def make_menu_title(title: str, width: int) -> str:
    return make_line(title.upper(), width, 'center', style=bold)

def make_menu(
        menu_title: str, cmd_dict: dict[str, str], width: int
) -> list[str]:
    menu = []
    menu.append(make_border(width))
    menu.append(make_menu_title(menu_title,width))
    menu.append(make_border(width))
    menu.append(make_line('Options:', width, style=bold))
    for cmd, label in cmd_dict.items():
        line = make_line(f' {cmd} → {label}', width, style=italic)
        menu.append(line)
    menu.append(make_border(width))
    return menu