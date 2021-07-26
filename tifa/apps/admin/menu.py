from fastapi_utils.api_model import APIModel

from . import bp
from ...globals import AsyncDal, db
from ...models.menu import Menu


class TMenu(APIModel):
    id: str
    name: str
    slug: str

    class TItem(APIModel):
        id: str
        name: str

    items: list[TItem]


@bp.list("/menus", out=TMenu, summary="Menu", tags=["Menu"])
async def get_menus():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"items": merchant}


@bp.item("/menu", out=TMenu, summary="Menu", tags=["Menu"])
async def get_menu():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op("/menu/create", out=TMenu, summary="Menu", tags=["Menu"])
async def menu_create():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op("/menu/update", out=TMenu, summary="Menu", tags=["Menu"])
async def menu_create():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op("/menu/delete", out=TMenu, summary="Menu", tags=["Menu"])
async def menu_delete():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op("/menu/bulk_delete", out=TMenu, summary="Menu", tags=["Menu"])
async def menu_delete():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


class TMenuItem(APIModel):
    id: str
    name: str


@bp.page("/menu_items", out=TMenuItem, summary="MenuItem", tags=["Menu"])
async def menu_items():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.item("/menu_item", out=TMenuItem, summary="MenuItem", tags=["Menu"])
async def menu_item():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op("/menu_item/create", out=TMenuItem, summary="MenuItem", tags=["Menu"])
async def menu_item_create():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op("/menu_item/update", out=TMenuItem, summary="MenuItem", tags=["Menu"])
async def menu_item_update():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op("/menu_item/move", out=TMenuItem, summary="MenuItem-Move", tags=["Menu"])
async def menu_item_move():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op("/menu_item/translate", out=TMenuItem, summary="MenuItem", tags=["Menu"])
async def menu_item_translate():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op("/menu_item/delete", out=TMenuItem, summary="MenuItem", tags=["Menu"])
async def menu_item_delete():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}


@bp.op("/menu_item/bulk_delete", out=TMenuItem, summary="MenuItem", tags=["Menu"])
async def menu_item_bulk_delete():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Menu)
    return {"item": merchant}
