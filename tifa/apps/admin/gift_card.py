from fastapi_utils.api_model import APIModel

from tifa.apps.admin import bp
from tifa.globals import db
from tifa.db.adal import AsyncDal
from tifa.models.gift_card import GiftCard


class TGiftCard(APIModel):
    id: str
    name: str


@bp.list("/gift_cards", out=TGiftCard, summary="GiftCard", tags=["GiftCard"])
async def gift_cards_items():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(GiftCard)
    return {"items": ins}


@bp.item("/gift_card", out=TGiftCard, summary="GiftCard", tags=["GiftCard"])
async def gift_card_item():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(GiftCard)
    return {"items": ins}


@bp.op("/gift_card/create", out=TGiftCard, summary="GiftCard", tags=["GiftCard"])
async def gift_card_create():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(GiftCard)
    return {"items": ins}


@bp.op("/gift_card/update", out=TGiftCard, summary="GiftCard", tags=["GiftCard"])
async def gift_card_update():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(GiftCard)
    return {"items": ins}


@bp.op("/gift_card/delete", out=TGiftCard, summary="GiftCard", tags=["GiftCard"])
async def gift_card_delete():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(GiftCard)
    return {"items": ins}


@bp.op("/gift_card/activate", out=TGiftCard, summary="GiftCard", tags=["GiftCard"])
async def gift_card_activate():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(GiftCard)
    return {"items": ins}


@bp.op("/gift_card/deactivate", out=TGiftCard, summary="GiftCard", tags=["GiftCard"])
async def gift_card_deactivate():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(GiftCard)
    return {"items": ins}
