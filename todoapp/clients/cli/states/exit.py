from .base import AppStateBase, AppLike

class ExitState(AppStateBase):
    def render(self, app: AppLike):
        print('Goodbye 👋')
        app.running = False

    def handle_input(self, app, cmd: str):
        pass