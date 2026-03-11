from fastapi import HTTPException, status

from todoapp.core.results import Result, Code


HTTP_STATUS_BY_CODE = {
    Code.INVALID_INPUT: status.HTTP_400_BAD_REQUEST,
    Code.NOT_FOUND: status.HTTP_404_NOT_FOUND,
    Code.ALREADY_EXISTS: status.HTTP_409_CONFLICT
}


def raise_for_result(res: Result) -> None:
    if res.ok:
        raise ValueError('raise_for_result() should only be used for error results.')
    status_code = HTTP_STATUS_BY_CODE.get(
        res.code,
        status.HTTP_500_INTERNAL_SERVER_ERROR
    )
    detail = res.msg or 'Unexpected error.'
    raise HTTPException(status_code=status_code, detail=detail)