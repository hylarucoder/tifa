import json
from contextvars import ContextVar
from typing import Optional

from fastapi import HTTPException, Header, Depends, Request

from tifa.apps.deps import get_async_dal
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
    "ctx": None,
    "transactions": None
}
context = ContextVar("_context", default=context_default.copy())


async def pre_request(
        request: Request,
        authorization: Optional[str] = Header(...),
):
    adal = AsyncDal(db.async_session)
    context.get()["adal"] = adal
    if request.url.path not in ALLOW_LIST:
        token = authorization.split(" ")[1]
        content = decode_jwt(token)
        staff = await adal.get_or_404(Staff, json.loads(content["sub"])["admin"])
        context.get()["staff"] = staff


bp = create_bp(
    [
        Depends(
            pre_request
        ),
    ]
)
