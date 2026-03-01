from typing import Callable
from .style import italic, bold


# ===== PRIMITIVES ==============================================
def clip(text: str, width: int) -> str:
    if '\x1b[' in text:
        return text
    if len(text) + 2 > width:
        text = text[:width - 5] + '...'
    return text

def padding(text: str, width: int, align: str = 'left') -> str:
    text = clip(text, width)
    if align == 'center':
        return text.center(width - 2)
    elif align == 'right':
        return text.rjust(width - 2)
    else:
        return text.ljust(width - 2)
    
def single_cell_line(
    text: str, width: int, align: str = 'left',
    style: Callable[[str], str] | None = None
) -> str:
    line = padding(text, width, align)
    if style is not None:
        line = style(line)
    return '| ' + line + ' |'

def multi_cell_line(
    cells: list[str], widths: list[str], aligns: list[str],
    style: Callable[[str], str] | None = None
) -> str:
    line = [
        padding(cell, width, align)
        for cell, width, align in zip(cells, widths, aligns)
    ]
    if style is not None:
        line = [style(l) for l in line]
    return '| ' + ' | '.join(line) + ' |'

def empty_line(width: int) -> str:
    return single_cell_line('Empty', width, 'center', style=bold)


# ===== MENU LAYOUT =============================================
def menu_border(width: int) -> str:
    return '+' + '-' * width + '+'

def menu_title(title: str, width: int) -> str:
    return single_cell_line(title.upper(), width, 'center', style=bold)

def menu_data(data: dict[str, str], width: int) -> list[str]:
    display_data = []
    display_data.append(single_cell_line('Options:', width, style=bold))
    for cmd, label in data.items():
        line = single_cell_line(f' {cmd} → {label}', width, style=italic)
        display_data.append(line)
    return display_data




# ===== TABLE LAYOUT ============================================
def table_border(widths: list[int]) -> str:
    return '+' + '+'.join(['-' * w for w in widths]) + '+'

def table_title(title: str, width: int) -> str:
    return single_cell_line(title.capitalize(), width, 'center', style=bold)

def table_header(labels: list[str], widths: list[str]) -> str:
    return multi_cell_line(
        labels, widths, aligns=['left' for _ in range(len(labels))], style=italic
    )

def table_row(cells: list[str], widths: list[str], aligns: list[str]) -> str:
    return multi_cell_line(cells, widths, aligns, style=italic)