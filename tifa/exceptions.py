from typing import Optional, List

from mypy_extensions import TypedDict
from starlette.requests import Request
from starlette.responses import JSONResponse

from tifa.api import ApiResult


class ErrorDict(TypedDict):
    message: str
    code: int


class ApiException(Exception):
    code: Optional[int] = None
    message: Optional[str] = None
    errors: Optional[List[ErrorDict]] = None

    status = 400

    def __init__(self, message, status=None, code=None, errors=None):
        self.message = message or self.message
        self.status = status or self.status
        self.code = code or self.code
        self.errors = errors or self.errors

    def to_result(self):
        rv = {"message": self.message}
        if self.errors:
            rv["errors"] = self.errors
        if self.code:
            rv["code"] = self.code
        return ApiResult(rv, status_code=self.status)


class NotAuthorized(ApiException):
    status = 401


class NotFound(ApiException):
    status = 404
    message = "resource not found"


class InvalidToken(ApiException):
    pass


class AuthExpired(ApiException):
    pass


class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name


def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."},
    )