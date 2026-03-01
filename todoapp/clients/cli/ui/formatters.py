from todoapp.domain.models import Status
from .style import red, yellow, green

def format_status(status: Status) -> str:
    if status == Status.done:
        return green(status.value)
    if status == Status.open:
        return yellow(status.value)
    if status == Status.cancelled:
        return red(status.value)