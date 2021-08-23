from fastapi_utils.api_model import APIModel

from tifa.apps.admin.local import g
from tifa.apps.admin.router import bp
from tifa.models.gift_card import GiftCard


class TGiftCard(APIModel):
    id: str
    name: str


@bp.list("/gift_cards", out=TGiftCard, summary="GiftCard", tags=["GiftCard"])
async def gift_cards_items():
    ins = await g.adal.first_or_404(GiftCard)
    return {"items": ins}


@bp.item("/gift_card", out=TGiftCard, summary="GiftCard", tags=["GiftCard"])
async def gift_card_item():
    ins = await g.adal.first_or_404(GiftCard)
    return {"items": ins}


@bp.op("/gift_card/create", out=TGiftCard, summary="GiftCard", tags=["GiftCard"])
async def gift_card_create():
    ins = await g.adal.first_or_404(GiftCard)
    return {"items": ins}


@bp.op("/gift_card/update", out=TGiftCard, summary="GiftCard", tags=["GiftCard"])
async def gift_card_update():
    ins = await g.adal.first_or_404(GiftCard)
    return {"items": ins}


@bp.op("/gift_card/delete", out=TGiftCard, summary="GiftCard", tags=["GiftCard"])
async def gift_card_delete():
    ins = await g.adal.first_or_404(GiftCard)
    return {"items": ins}


@bp.op("/gift_card/activate", out=TGiftCard, summary="GiftCard", tags=["GiftCard"])
async def gift_card_activate():
    ins = await g.adal.first_or_404(GiftCard)
    return {"items": ins}


@bp.op("/gift_card/deactivate", out=TGiftCard, summary="GiftCard", tags=["GiftCard"])
async def gift_card_deactivate():
    ins = await g.adal.first_or_404(GiftCard)
    return {"items": ins}
