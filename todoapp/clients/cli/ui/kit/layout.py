from typing import Callable
import re

import todoapp.clients.cli.ui.kit.formatters as formatters
from .style import italic, bold


ANSI_RE = re.compile(r"\x1b\[[0-9;]*m")


# ===== PRIMITIVES ==============================================
def strip_ansi(s: str) -> str:
    return ANSI_RE.sub("", s)


def visible_len(s: str) -> int:
    return len(strip_ansi(s))


def clip(text: str, width: int) -> str:
    inner_width = width - 2
    if visible_len(text) <= inner_width:
        return text
    plain = strip_ansi(text)
    return plain[: inner_width - 3] + "..."


def padding(text: str, width: int, align: str = "left") -> str:
    inner_width = width - 2
    text = clip(text, width)
    vis_len = visible_len(text)
    if vis_len < inner_width:
        pad = inner_width - vis_len
    else:
        pad = 0
    if align == "right":
        return (" " * pad) + text
    elif align == "center":
        left = pad // 2
        right = pad - left
        return (" " * left) + text + (" " * right)
    else:
        return text + (" " * pad)


def single_cell_line(
    text: str,
    width: int,
    align: str = "left",
    style: Callable[[str], str] | None = None,
) -> str:
    line = padding(text, width, align)
    if style is not None:
        line = style(line)
    return "| " + line + " |"


def multi_cell_line(
    cells: list[str],
    widths: list[int],
    aligns: list[str],
    style: Callable[[str], str] | None = None,
) -> str:
    line = [
        padding(cell, width, align) for cell, width, align in zip(cells, widths, aligns)
    ]
    if style is not None:
        line = [style(l) for l in line]
    return "| " + " | ".join(line) + " |"


def empty_line(width: int) -> str:
    return single_cell_line("Empty", width, "center", style=bold)


# ===== TABLE LAYOUT ============================================
def table_border(widths: list[int]) -> str:
    return "+" + "+".join(["-" * w for w in widths]) + "+"


def table_title(title: str, width: int) -> str:
    return single_cell_line(formatters.format_title(title), width, "center", style=bold)


def table_header(labels: list[str], widths: list[str]) -> str:
    return multi_cell_line(
        labels, widths, aligns=["left" for _ in range(len(labels))], style=italic
    )


def table_row(cells: list[str], widths: list[str], aligns: list[str]) -> str:
    return multi_cell_line(cells, widths, aligns, style=italic)
