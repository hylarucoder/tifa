import functools
import json
from typing import Optional, List

from fastapi import FastAPI
from fastapi.responses import Response
from mypy_extensions import TypedDict


class ApiResult:
    def __init__(self, value, status_code=200, next_page=None):
        self.value = value
        self.status_code = status_code
        self.nex_page = next_page

    def to_response(self):
        return Response(
            json.dumps(self.value, ensure_ascii=False),  # TODO: polish
            status_code=self.status_code,
            # mimetype="application/json",
        )


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


class TifaFastApi(FastAPI):
    pass
