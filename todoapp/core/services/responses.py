# todoapp/core/services/responses.py

from dataclasses import dataclass
from functools import wraps
from collections.abc import Callable
from typing import Generic, Optional, TypeVar

from pydantic import ValidationError

from todoapp.core.results import Code, Result
from todoapp.core.services.errors import ServiceError


T = TypeVar('T')

@dataclass
class Success(Generic[T]):
    code: Code
    message: str = ''
    data: Optional[T] = None


# ===== SUCCESS ===============================================================
def ok(message: str = '', data: Optional[T] = None) -> Success[T]:
    return Success(code=Code.OK, message=message, data=data)

def created(message: str = '', data: Optional[T] = None) -> Success[T]:
    return Success(code=Code.CREATED, message=message, data=data)

def result_from_success(success: Success[T]) -> Result[T]:
    return Result(success.code, success.message, success.data)


# ===== ERROR =================================================================
def result_from_service_error(error: ServiceError) -> Result[None]:
    return Result(error.code, error.message)

def result_from_validation_error(error: ValidationError) -> Result[None]:
    first_error = error.errors()[0]
    field = first_error['loc'][0]
    message = first_error['msg']
    return Result(Code.INVALID_INPUT, f'{field.capitalize()}: {message}')


def resultify(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            success = func(*args, **kwargs)
            return result_from_success(success)
        except ServiceError as error:
            return result_from_service_error(error)
        except ValidationError as error:
            return result_from_validation_error(error)
    return wrapper