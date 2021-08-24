import enum
from typing import Optional

from fastapi.responses import ORJSONResponse
from starlette.requests import Request


class HttpCodeEnum(enum.Enum):
    OK = 200
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    SERVER_ERROR = 500


class BizCodeEnum(enum.Enum):
    # 业务状态码
    OK = "100200"
    FAIL = "100500"
    NOT_EXISTS = "100404"


error_message = {
    HttpCodeEnum.BAD_REQUEST.name: "错误请求",
    HttpCodeEnum.UNAUTHORIZED.name: "未授权",
    HttpCodeEnum.FORBIDDEN.name: "权限不足",
    HttpCodeEnum.NOT_FOUND.name: "未找到资源",
    HttpCodeEnum.SERVER_ERROR.name: "服务器异常",
    BizCodeEnum.FAIL: "未知错误",
}


class ApiException(Exception):
    status_code = HttpCodeEnum.BAD_REQUEST.value
    biz_code = BizCodeEnum.FAIL
    code: Optional[int]
    detail: Optional[str] = None

    def __init__(self, detail, status_code=None, biz_code=None, errors=None):
        self.status_code = status_code or self.status_code
        self.code = self.status_code or self.code
        self.biz_code = biz_code or self.biz_code
        self.detail = detail or self.detail
        self.errors = errors or []

    def to_result(self):
        rv = {"detail": self.detail}
        if self.code:
            rv["code"] = self.code
        if self.biz_code:
            rv["biz_code"] = self.biz_code
        if self.errors:
            rv["errors"] = self.errors
        return ORJSONResponse(rv, status_code=self.status_code)


class NotAuthorized(ApiException):
    status_code = HttpCodeEnum.UNAUTHORIZED.value


class NotFound(ApiException):
    status_code = HttpCodeEnum.NOT_FOUND.value
    detail = error_message[HttpCodeEnum.NOT_FOUND.name]


class InvalidToken(ApiException):
    status_code = HttpCodeEnum.UNAUTHORIZED.value


class AuthExpired(ApiException):
    status_code = HttpCodeEnum.UNAUTHORIZED.value


class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name


def unicorn_exception_handler(request: Request, exc: UnicornException):
    return ORJSONResponse(
        status_code=418,
        content={"detail": f"Oops! {exc.name} did something. There goes a rainbow..."},
    )
