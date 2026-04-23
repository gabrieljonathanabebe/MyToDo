# todoapp/clients/cli/states/exit.py

from todoapp.clients.cli import ui
from .base import AppStateBase, AppLike


class ExitState(AppStateBase):
    def render(self, app: AppLike):
        ui.success("Goodbye 👋")
        app.running = False
