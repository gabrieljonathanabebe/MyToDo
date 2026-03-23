from dataclasses import dataclass
from enum import Enum
from typing import Generic, Optional, TypeVar

T = TypeVar('T')

class Code(str, Enum):
    OK = 'OK'
    CREATED = 'CREATED'
    INVALID_INPUT = 'INVALID_INPUT'
    NOT_FOUND = 'NOT_FOUND'
    ALREADY_EXISTS = 'ALREADY_EXISTS'
    IO_ERROR = 'IO_ERROR'
    UNAUTHORIZED = 'UNAUTHORIZED'


@dataclass
class Result(Generic[T]):
    code: Code
    msg: str = ''
    data: Optional[T] = None

    @property
    def ok(self) -> bool:
        return self.code in {Code.OK, Code.CREATED}