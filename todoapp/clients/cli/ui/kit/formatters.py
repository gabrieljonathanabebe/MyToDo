from todoapp.domain.models import Status, Priority
from .style import red, yellow, green

def format_status(status: Status) -> str:
    if status == Status.done:
        return green(status.value)
    if status == Status.open:
        return yellow(status.value)
    if status == Status.cancelled:
        return red(status.value)
    
def format_priority(priority: Priority) -> str:
    if priority == Priority.low:
        return green(priority.value)
    if priority == Priority.medium:
        return yellow(priority.value)
    if priority == Priority.high:
        return red(priority.value)