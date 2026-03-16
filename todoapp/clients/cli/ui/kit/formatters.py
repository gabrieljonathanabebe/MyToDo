from datetime import datetime, timezone

from todoapp.domain.models import Status, Priority
from .style import red, yellow, green


# ===== TASK FORRMATTER ========================================
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
    
# ===== TODO FORRMATTER ========================================
def format_title(title: str) -> str:
    return title[:1].upper() + title[1:] if title else title


def format_relative_datetime(dt: datetime) -> str:
    now = datetime.now(timezone.utc)
    delta = now - dt
    total_seconds = int(delta.total_seconds())
    minutes = total_seconds // 60
    hours = total_seconds // 3600
    days = delta.days
    weeks = days // 7
    months = days // 30
    if total_seconds < 60:
        return 'just now'
    if minutes < 60:
        return f'{minutes} min ago'
    if hours < 24:
        return f'{hours} h ago'
    if days < 7:
        return f'{days} d ago'
    if weeks < 5:
        return f'{weeks} wk ago'
    if months < 12:
        return f'{months} mo ago'
    return dt.strftime('%Y-%m-%d')