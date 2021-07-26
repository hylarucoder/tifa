from fastapi_utils.api_model import APIModel

from . import bp
from ...globals import db, AsyncDal, Dal
from ...models.channel import Channel


class TChannel(APIModel):
    id: str
    name: str
    is_active: bool
    slug: str
    currency_code: str


@bp.page("/channels", out=TChannel, summary="Channel", tags=["Channel"])
def get_channels():
    dal = Dal(db.session)
    items = dal.all(Channel)
    return {"items": items}


@bp.item("/channel/{id}", out=TChannel, summary="Channel", tags=["Channel"])
def get_channel(id: str):
    dal = Dal(db.session)
    item = dal.get_or_404(Channel, id)
    return {"item": item}


class PChannelCreate(APIModel):
    name: str
    is_active: bool
    slug: str
    currency_code: str


@bp.op("/channel/create", out=TChannel, summary="Channel", tags=["Channel"])
def channel_create(params: PChannelCreate):
    dal = Dal(db.session)
    ins = dal.add(
        Channel,
        name=params.name,
        is_active=params.is_active,
        slug=params.slug,
        currency_code=params.currency_code,
    )
    dal.commit()
    return {"item": ins}


class PChannelUpdate(APIModel):
    id: str
    name: str
    is_active: bool
    slug: str
    currency_code: str


@bp.op("/channel/update", out=TChannel, summary="Channel", tags=["Channel"])
def channel_update(params: PChannelUpdate):
    dal = Dal(db.session)
    ins = dal.get_or_404(Channel, params.id)
    ins.name = params.name
    ins.is_active = params.is_active
    ins.slug = params.slug
    ins.currency_code = params.currency_code
    dal.commit()
    return {"item": ins}


class PChannelActivate(APIModel):
    id: str


@bp.op("/channel/activate", out=TChannel, summary="Channel", tags=["Channel"])
def channel_activate(params: PChannelActivate):
    dal = Dal(db.session)
    ins = dal.get_or_404(Channel, params.id)
    ins.is_active = True
    dal.commit()
    return {"item": ins}


class PChannelDeactivate(APIModel):
    id: str


@bp.op("/channel/deactivate", out=TChannel, summary="Channel", tags=["Channel"])
def channel_deactivate(params: PChannelDeactivate):
    dal = Dal(db.session)
    ins = dal.get_or_404(Channel, params.id)
    ins.is_active = False
    dal.commit()
    return {"item": ins}


class PChannelDelete(APIModel):
    id: str


@bp.op("/channel/delete", out=TChannel, summary="Channel", tags=["Channel"])
def channel_delete(params: PChannelDelete):
    dal = Dal(db.session)
    ins = dal.get_or_404(Channel, params.id)
    dal.delete(ins)
    dal.commit()
    return {"item": ins}