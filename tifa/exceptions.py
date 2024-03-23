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
    OK = "200"
    FAIL = "500"
    NOT_EXISTS = "404"


error_message = {
    HttpCodeEnum.BAD_REQUEST.name: "错误请求",
    HttpCodeEnum.UNAUTHORIZED.name: "未授权",
    HttpCodeEnum.FORBIDDEN.name: "权限不足",
    HttpCodeEnum.NOT_FOUND.name: "未找到资源",
    HttpCodeEnum.SERVER_ERROR.name: "服务器异常",
    BizCodeEnum.FAIL: "未知错误",
}


class ApiException(Exception):
    status_code: int = 400
    code: Optional[int]
    message: Optional[str] = None

    def __init__(self, message, biz_code=None, status_code=400, errors=None):
        self.status_code = status_code or self.status_code
        self.code = self.status_code or self.code
        self.message = message or self.message
        self.errors = errors or []

    def to_result(self):
        rv = {"message": self.message}
        if self.code:
            rv["code"] = self.code
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


