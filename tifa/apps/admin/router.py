import json
from typing import Optional

from fastapi import Header, Depends, Request
from tifa.apps.admin.local import g

from tifa.auth import decode_jwt
from tifa.contrib.fastapi_plus import create_bp
from tifa.db.adal import AsyncDal
from tifa.globals import db
from tifa.models.system import Staff
from tifa.exceptions import NotAuthorized, NotFound

ALLOW_LIST = (
    "/admin/login",
)


async def before_request(
        request: Request,
        authorization: Optional[str] = Header(...),
):
    adal = AsyncDal(db.async_session)
    g.adal = adal
    if request.url.path not in ALLOW_LIST:
        try:
            token = authorization.split(" ")[1]
            content = decode_jwt(token)
            staff = await adal.get_or_404(Staff, json.loads(content["sub"])["admin"])
            g.staff = staff
        except NotFound as e:
            print("not -found????")
            print("not -found????")
            raise NotAuthorized("no such staff")
        except Exception:
            # TODO: more specific error
            raise NotAuthorized("token not correct")


bp = create_bp(
    [
        Depends(
            before_request
        ),
    ]
)
