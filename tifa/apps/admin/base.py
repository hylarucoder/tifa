from typing import Optional

from fastapi import HTTPException, Header, Depends, Path

from tifa.contrib.fastapi_plus import create_bp

ALLOW_LIST = (
    "login",
)


async def auth_token(
        authorization: Optional[str] = Header(...),
        # path: str = Path(...),
):
    # print("--->", path)
    if authorization != "fake-super-secret-token":
        raise HTTPException(status_code=401, detail="X-Token header invalid")


bp = create_bp(
    [
        Depends(
            auth_token
        )
    ]
)
