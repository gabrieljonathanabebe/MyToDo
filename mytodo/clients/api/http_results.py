# mytodo/clients/api/http_results.py

from typing import TypeVar

from fastapi import HTTPException, status

from mytodo.core.results import Result, Code


T = TypeVar("T")


HTTP_STATUS_BY_CODE = {
    Code.INVALID_INPUT: status.HTTP_400_BAD_REQUEST,
    Code.UNAUTHORIZED: status.HTTP_401_UNAUTHORIZED,
    Code.NOT_FOUND: status.HTTP_404_NOT_FOUND,
    Code.ALREADY_EXISTS: status.HTTP_409_CONFLICT,
}


def raise_http_error(res: Result) -> None:
    if res.ok:
        raise ValueError("raise_http_error() should only be used for error results.")
    status_code = HTTP_STATUS_BY_CODE.get(
        res.code, status.HTTP_500_INTERNAL_SERVER_ERROR
    )
    detail = res.msg or "Unexpected error."
    raise HTTPException(status_code=status_code, detail=detail)


def unwrap_result(res: Result[T]) -> T:
    if res.ok and res.data is not None:
        return res.data
    raise_http_error(res)


def ok_message(res: Result[object]) -> dict[str, str]:
    if res.ok:
        return {"message": res.msg}
    raise_http_error(res)
