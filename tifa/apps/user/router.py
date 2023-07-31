import json

from fastapi import Depends
from starlette.requests import Request

from tifa.auth import decode_jwt
from tifa.contrib.fastapi_plus import create_bp
from tifa.exceptions import NotFound, NotAuthorized

ALLOW_LIST = ("/user/login",)


async def before_request(
    request: Request,
):
    if request.url.path not in ALLOW_LIST:
        try:
            authorization = request.headers.get("Authorization", None)
            if not authorization:
                raise NotAuthorized("Authorization Headers Required")
            token = authorization.split(" ")[1]
            content = decode_jwt(token)
            # staff = await adal.get_or_404(User, json.loads(content["sub"])["user"])
            # g.staff = staff
        except NotAuthorized as e:
            raise e
        except NotFound as e:
            raise NotAuthorized("no such staff")
        except Exception:
            # TODO: more specific error
            raise NotAuthorized("token not correct")


bp = create_bp(
    [
        Depends(before_request),
    ]
)
