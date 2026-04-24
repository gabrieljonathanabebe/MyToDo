from .login import LoginState
from .todo_summary import ToDoSummaryState
from .todo_detail import ToDoDetailState
from .exit import ExitState


def set_state(name: str):
    states = {
        "login": LoginState,
        "todo_summary": ToDoSummaryState,
        "todo_detail": ToDoDetailState,
        "exit": ExitState,
    }
    try:
        return states[name]()
    except KeyError:
        raise ValueError(f"Unknown state: {name}")
