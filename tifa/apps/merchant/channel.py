from fastapi_utils.api_model import APIModel

from . import bp
from ...globals import db, AsyncDal
from ...models.channel import Channel


class TChannel(APIModel):
    id: str
    name: str


@bp.list("/channels", out=TChannel, summary="Channel", tags=["Channel"])
async def addresses_list():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(Channel)
    return {"items": ins}


@bp.item("/channel", out=TChannel, summary="Channel", tags=["Channel"])
async def app_item():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(Channel)
    return {"items": ins}


@bp.op("/channel/create", out=TChannel, summary="Channel", tags=["Channel"])
async def app_create():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(Channel)
    return {"items": ins}


@bp.op("/channel/update", out=TChannel, summary="Channel", tags=["Channel"])
async def app_update():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(Channel)
    return {"items": ins}


@bp.op("/channel/activate", out=TChannel, summary="Channel", tags=["Channel"])
async def app_update():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(Channel)
    return {"items": ins}


@bp.op("/channel/deactivate", out=TChannel, summary="Channel", tags=["Channel"])
async def app_update():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(Channel)
    return {"items": ins}


@bp.op("/channel/delete", out=TChannel, summary="Channel", tags=["Channel"])
async def app_update():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(Channel)
    return {"items": ins}
