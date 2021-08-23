from fastapi_utils.api_model import APIModel

from tifa.apps.admin.local import g
from tifa.apps.admin.router import bp
from tifa.models.channel import Channel


class TChannel(APIModel):
    id: str
    name: str
    is_active: bool
    slug: str
    currency_code: str


@bp.page("/channels", out=TChannel, summary="Channel", tags=["Channel"])
async def get_channels():
    return await g.adal.page(Channel, per_page=100)


@bp.item("/channel/{id}", out=TChannel, summary="Channel", tags=["Channel"])
async def get_channel(id: str):
    item = await g.adal.get_or_404(Channel, id)
    return {"item": item}


class ParamsChannelCreate(APIModel):
    name: str
    is_active: bool
    slug: str
    currency_code: str


@bp.op("/channel/create", out=TChannel, summary="Channel", tags=["Channel"])
async def channel_create(params: ParamsChannelCreate):
    ins = g.adal.add(
        Channel,
        name=params.name,
        is_active=params.is_active,
        slug=params.slug,
        currency_code=params.currency_code,
    )
    await g.adal.commit()
    return {"item": ins}


class ParamsChannelUpdate(APIModel):
    id: str
    name: str
    is_active: bool
    slug: str
    currency_code: str


@bp.op("/channel/update", out=TChannel, summary="Channel", tags=["Channel"])
async def channel_update(params: ParamsChannelUpdate):
    ins = await g.adal.get_or_404(Channel, params.id)
    ins.name = params.name
    ins.is_active = params.is_active
    ins.slug = params.slug
    ins.currency_code = params.currency_code
    await g.adal.commit()
    return {"item": ins}


class ParamsChannelActivate(APIModel):
    id: str


@bp.op("/channel/activate", out=TChannel, summary="Channel", tags=["Channel"])
async def channel_activate(params: ParamsChannelActivate):
    ins = await g.adal.get_or_404(Channel, params.id)
    ins.is_active = True
    await g.adal.commit()
    return {"item": ins}


class ParamsChannelDeactivate(APIModel):
    id: str


@bp.op("/channel/deactivate", out=TChannel, summary="Channel", tags=["Channel"])
async def channel_deactivate(params: ParamsChannelDeactivate):
    ins = await g.adal.get_or_404(Channel, params.id)
    ins.is_active = True
    await g.adal.commit()
    return {"item": ins}


class ParamsChannelDelete(APIModel):
    id: str


@bp.op("/channel/delete", out=TChannel, summary="Channel", tags=["Channel"])
async def channel_delete(params: ParamsChannelDelete):
    ins = await g.adal.get_or_404(Channel, params.id)
    g.adal.delete(ins)
    await g.adal.commit()
    return {"item": ins}
