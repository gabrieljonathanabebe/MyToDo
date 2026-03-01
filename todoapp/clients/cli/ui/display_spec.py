from typing import Any, Callable

from todoapp.domain.models import Task
from . import formatters


MODEL_FIELDS = set(Task.model_fields.keys())
EXTRA_FIELDS = {'days_left'}

DISPLAY_SPEC = {
    'id': {
        'label': 'ID',
        'width': 5,
        'align': 'center'
    },
    'description': {
        'label': 'Description',
        'width': 25,
        'align': 'left'     
    },
    'priority': {
        'label': 'Priority',
        'width': 10,
        'align': 'center',
        'formatter': formatters.format_priority
    },
    'status': {
        'label': 'Status',
        'width': 8,
        'align': 'center',
        'formatter': formatters.format_status   
    },
    'due': {
        'label': 'Due',
        'width': 12,
        'align': 'center'       
    },
    'days_left': {
        'label': 'Days left',
        'width': 11,
        'align': 'center'      
    }
}


# ===== VALIDATOR =======================================================
def _validate_display_spec() -> None:
    for field in DISPLAY_SPEC.keys():
        if field not in MODEL_FIELDS and field not in EXTRA_FIELDS:
            raise RuntimeError(f'Unknown display field "{field}"')
        
_validate_display_spec()


# ===== GETTER FOR SPECS =================================================
def get_fields() -> list[str]:
    return list(DISPLAY_SPEC.keys())

def get_labels() -> list[str]:
    return [meta['label'] for _, meta in DISPLAY_SPEC.items()]

def get_widths() -> list[int]:
    return [meta['width'] for _, meta in DISPLAY_SPEC.items()]

def get_aligns() -> list[str]:
    return [meta['align'] for _, meta in DISPLAY_SPEC.items()]

def get_formatter(field: str) -> Callable[[Any], str]:
    return DISPLAY_SPEC[field].get('formatter')