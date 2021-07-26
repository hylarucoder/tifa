from fastapi_utils.api_model import APIModel

from . import bp
from ...globals import db, AsyncDal
from ...models.gift_card import GiftCard


class TGiftCard(APIModel):
    id: str
    name: str


@bp.list("/gift_cards", out=TGiftCard, summary="GiftCard", tags=["GiftCard"])
async def addresses_list():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(GiftCard)
    return {"items": ins}


@bp.item("/gift_card", out=TGiftCard, summary="GiftCard", tags=["GiftCard"])
async def app_item():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(GiftCard)
    return {"items": ins}


@bp.op("/gift_card/create", out=TGiftCard, summary="GiftCard", tags=["GiftCard"])
async def app_create():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(GiftCard)
    return {"items": ins}


@bp.op("/gift_card/update", out=TGiftCard, summary="GiftCard", tags=["GiftCard"])
async def app_update():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(GiftCard)
    return {"items": ins}


@bp.op("/gift_card/delete", out=TGiftCard, summary="GiftCard", tags=["GiftCard"])
async def app_update():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(GiftCard)
    return {"items": ins}


@bp.op("/gift_card/activate", out=TGiftCard, summary="GiftCard", tags=["GiftCard"])
async def app_update():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(GiftCard)
    return {"items": ins}


@bp.op("/gift_card/deactivate", out=TGiftCard, summary="GiftCard", tags=["GiftCard"])
async def app_update():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(GiftCard)
    return {"items": ins}
