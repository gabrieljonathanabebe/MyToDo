from todoapp.domain.models import Task


MODEL_FIELDS = set(Task.model_fields.keys())
EXTRA_FIELDS = {'days_left'}

DISPLAY_SPEC = [
    {
        'field': 'id',
        'label': 'ID',
        'width': 5,
        'align': 'center'
    },
    {
        'field': 'description',
        'label': 'Description',
        'width': 25,
        'align': 'left'
    },
    {
        'field': 'priority',
        'label': 'Priority',
        'width': 11,
        'align': 'center'
    },
    {
        'field': 'status',
        'label': 'Status',
        'width': 9,
        'align': 'center'
    },
    {
        'field': 'due',
        'label': 'Due',
        'width': 13,
        'align': 'center'
    },
    {
        'field': 'days_left',
        'label': 'Days left',
        'width': 11,
        'align': 'center'
    },
]


# ===== VALIDATOR =======================================================
def _validate_display_spec() -> None:
    for spec in DISPLAY_SPEC:
        field = spec['field']
        if field not in MODEL_FIELDS and field not in EXTRA_FIELDS:
            raise RuntimeError(f'Unknown display field "{field}"')
        
_validate_display_spec()


# ===== GETTER FOR SPECS =================================================
def get_fields() -> list:
    return [spec['field'] for spec in DISPLAY_SPEC]

def get_labels() -> list:
    return [spec['label'] for spec in DISPLAY_SPEC]

def get_widths() -> list:
    return [spec['width'] for spec in DISPLAY_SPEC]

def get_aligns() -> list:
    return [spec['align'] for spec in DISPLAY_SPEC]