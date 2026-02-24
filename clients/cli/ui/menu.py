from .layout import menu_border, menu_title, menu_options
from .style import italic, bold


def make_menu(
    title: str, width: int, options: dict[str | int, str]
) -> list[str]:
    display_menu = []
    display_menu.append(menu_border(width))
    display_menu.append(menu_title(title,width))
    display_menu.append(menu_border(width))
    display_options = menu_options(options, width)
    display_menu = display_menu + display_options
    display_menu.append(menu_border(width))
    return display_menu