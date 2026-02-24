from __future__ import annotations
from typing import Optional, Protocol, TYPE_CHECKING

if TYPE_CHECKING:
    from domain import ToDoList
    from service import ToDoService

class AppLike(Protocol):
    service: ToDoService
    running: bool
    current_todo: Optional[ToDoList]

    def goto(self, state_name: str) -> None:
        ...

    def flash(self, kind: str, msg: str) -> None:
        ...


class AppStateBase:
    name = ''
    WIDTH = 30

    def render(self, app: AppLike) -> None:
        raise NotImplementedError
    
    def handle_input(self, app: AppLike, cmd: str) -> None:
        raise NotImplementedError
    


