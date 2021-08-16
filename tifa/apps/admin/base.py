import json
from contextvars import ContextVar
from typing import Optional

from fastapi import Header, Depends, Request

from tifa.auth import decode_jwt
from tifa.contrib.fastapi_plus import create_bp
from tifa.db.adal import AsyncDal
from tifa.globals import db
from tifa.models.system import Staff

ALLOW_LIST = (
    "/admin/login",
)

context_default = {
    "staff": None,
    "adal": None,
}
_context = ContextVar("_context", default=context_default.copy())


class Context:
    _context: ContextVar

    def __init__(self):
        self._context = _context

    @property
    def adal(self):
        return self._context.get()["adal"]

    @adal.setter
    def adal(self, v: AsyncDal):
        self._context.get()["adal"] = v

    @property
    def staff(self):
        return self._context.get()["staff"]

    @staff.setter
    def staff(self, v: Staff):
        self._context.get()["staff"] = v


context = Context()


async def pre_request(
        request: Request,
        authorization: Optional[str] = Header(...),
):
    adal = AsyncDal(db.async_session)
    context.adal = adal
    if request.url.path not in ALLOW_LIST:
        token = authorization.split(" ")[1]
        content = decode_jwt(token)
        staff = await adal.get_or_404(Staff, json.loads(content["sub"])["admin"])
        context.staff = staff


bp = create_bp(
    [
        Depends(
            pre_request
        ),
    ]
)
