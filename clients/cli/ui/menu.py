from .layout import menu_border, menu_title, menu_data
from .style import italic, bold


def make_menu(
    title: str, width: int, data: dict[str | int, str]
) -> list[str]:
    display_menu = []
    display_menu.append(menu_border(width))
    display_menu.append(menu_title(title,width))
    display_menu.append(menu_border(width))
    display_data = menu_data(data, width)
    display_menu = display_menu + display_data
    display_menu.append(menu_border(width))
    return display_menu