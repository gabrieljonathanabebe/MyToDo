from dataclasses import dataclass
from typing import Callable, Any


@dataclass
class ColumnSpec:
    label: str
    width: int
    align: str = "left"
    formatter: Callable[[Any], str] | None = None


class TableSpec:
    def __init__(self, spec: dict[str, ColumnSpec]):
        self.spec = spec

    @property
    def fields(self) -> list[str]:
        return list(self.spec.keys())

    @property
    def labels(self) -> list[str]:
        return [col.label for col in self.spec.values()]

    @property
    def widths(self) -> list[int]:
        return [col.width for col in self.spec.values()]

    @property
    def aligns(self) -> list[str]:
        return [col.align for col in self.spec.values()]

    def formatter(self, field) -> Callable[[Any], str] | None:
        return self.spec[field].formatter

    def validate_spec(self, MODEL_FIELDS: list[str]):
        MODEL_FIELDS = set(MODEL_FIELDS)
        for field in self.spec.keys():
            if field not in MODEL_FIELDS:
                raise RuntimeError(f'Unknown display field "{field}".')
