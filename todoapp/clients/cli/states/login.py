# todoapp/clients/cli/states/login.py

from todoapp.clients.cli import ui, prompts
import todoapp.core.factories as factories
from .base import AppStateBase, AppLike


class LoginState(AppStateBase):
    def __init__(self) -> None:
        super().__init__()
        self.name = "WELCOME"
        self.options = {
            "l": {
                "label": "Login",
                "handler": self._cmd_login,
            },
            "r": {
                "label": "Register",
                "handler": self._cmd_register,
            },
            "x": {
                "label": "Exit",
                "handler": self._cmd_exit,
            },
        }

    # ===== RENDER ============================================================
    def render(self, app: AppLike) -> None:
        ui.info("=" * 30)
        ui.info(" Welcome to ToDoScope ")
        ui.info("=" * 30)
        ui.info(" Please login or register.\n")
        self._render_options()

    # ===== COMMANDS ==========================================================
    def _cmd_login(self, app: AppLike) -> None:
        username = prompts.prompt_username()
        password = prompts.prompt_password()
        res = app.user_service.authenticate(username, password)
        if not res.ok:
            app.flash("error", res.msg)
            return
        app.current_user = res.data
        app.service = factories.build_todo_service(res.data.username)
        app.flash("success", res.msg)
        app.goto("todo_summary")

    def _cmd_register(self, app: AppLike) -> None:
        username = prompts.prompt_username()
        password = prompts.prompt_password()
        res = app.user_service.register_user(username, password)
        if not res.ok:
            app.flash("error", res.msg)
            return
        app.current_user = res.data
        app.service = factories.build_todo_service(res.data.username)
        app.flash("success", res.msg)
        app.goto("todo_summary")
