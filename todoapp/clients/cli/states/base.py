# todoapp/clients/cli/states/base.py

from __future__ import annotations
from typing import Optional, Protocol, TYPE_CHECKING, Callable

from todoapp.clients.cli import ui

if TYPE_CHECKING:
    from todoapp.domain.todo_list import ToDoList
    from todoapp.domain.models import User
    from todoapp.core.services import ToDoService, UserService


class AppLike(Protocol):
    service: Optional[ToDoService]
    user_service: UserService
    running: bool
    current_todo: Optional[ToDoList]
    current_user: Optional[User]

    def goto(self, state_name: str) -> None: ...

    def flash(self, kind: str, msg: str) -> None: ...


class AppStateBase:
    name = ""
    WIDTH = 30

    def __init__(self) -> None:
        self.options: dict[str, dict[str, Callable | str]] = {}

    # ===== COMMON RENDER HELPERS =============================================
    def _render_options(self, intro: str = "\n Press:") -> None:
        ui.info(intro)
        for cmd, meta in self.options.items():
            ui.info(f"  - {cmd} for {meta['label']}")
        ui.info("")

    # ===== COMMON COMMANDS ===================================================
    def _cmd_exit(self, app: AppLike) -> None:
        app.goto("exit")

    def _cmd_logout(self, app: AppLike) -> None:
        app.current_user = None
        app.current_todo = None
        app.service = None
        app.flash("info", "Logged out.")
        app.goto("login")

    # ===== DEFAULT INPUT HANDLING ============================================
    def handle_input(self, app: AppLike, cmd: str) -> None:
        cmd = cmd.strip().lower()
        entry = self.options.get(cmd)
        if not entry:
            app.flash("error", "Unknown command.")
            return
        handler = entry["handler"]
        handler(app)

    # ===== ABSTRACT RENDER ===================================================
    def render(self, app: AppLike) -> None:
        raise NotImplementedError
