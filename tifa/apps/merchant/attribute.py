from fastapi_utils.api_model import APIModel

from . import bp
from ...globals import db, AsyncDal
from ...models.attr import Attribute


class TAttribute(APIModel):
    id: str
    name: str


@bp.list("/attributes", out=TAttribute, summary="Attribute", tags=["Attribute"])
async def addresses_list():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(Attribute)
    return {"items": ins}


@bp.item("/attribute", out=TAttribute, summary="Attribute", tags=["Attribute"])
async def app_item():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(Attribute)
    return {"items": ins}


@bp.op("/attribute/create", out=TAttribute, summary="Attribute", tags=["Attribute"])
async def app_create():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(Attribute)
    return {"items": ins}


@bp.op("/attribute/update", out=TAttribute, summary="Attribute", tags=["Attribute"])
async def app_update():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(Attribute)
    return {"items": ins}


@bp.op("/attribute/delete", out=TAttribute, summary="Attribute", tags=["Attribute"])
async def app_update():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(Attribute)
    return {"items": ins}


@bp.op(
    "/attribute/bulk_delete", out=TAttribute, summary="Attribute", tags=["Attribute"]
)
async def app_update():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(Attribute)
    return {"items": ins}


@bp.op("/attribute/translate", out=TAttribute, summary="Attribute", tags=["Attribute"])
async def app_create():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(Attribute)
    return {"items": ins}


@bp.op(
    "/attribute/reorder_values", out=TAttribute, summary="Attribute", tags=["Attribute"]
)
async def app_create():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(Attribute)
    return {"items": ins}


@bp.op(
    "/attribute_value/create", out=TAttribute, summary="Attribute", tags=["Attribute"]
)
async def app_create():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(Attribute)
    return {"items": ins}


@bp.op(
    "/attribute_value/update", out=TAttribute, summary="Attribute", tags=["Attribute"]
)
async def app_create():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(Attribute)
    return {"items": ins}


@bp.op(
    "/attribute_value/delete", out=TAttribute, summary="Attribute", tags=["Attribute"]
)
async def app_create():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(Attribute)
    return {"items": ins}


@bp.op(
    "/attribute_value/bulk_delete",
    out=TAttribute,
    summary="Attribute",
    tags=["Attribute"],
)
async def app_create():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(Attribute)
    return {"items": ins}


@bp.op(
    "/attribute_value/translate",
    out=TAttribute,
    summary="Attribute",
    tags=["Attribute"],
)
async def app_create():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(Attribute)
    return {"items": ins}
