from .main_menu import MainMenuState
from .list_overview import ListOverviewState
from .list_menu import ListMenuState
from .exit import ExitState

def set_state(name : str):
    states = {
        'main': MainMenuState,
        'overview': ListOverviewState,
        'list_menu': ListMenuState,
        'exit': ExitState
    }
    try:
        return states[name]()
    except KeyError:
        raise ValueError(f'Unknown state: {name}')