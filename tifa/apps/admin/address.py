"""
addressSetDefault(...): AddressSetDefault

accountAddressCreate(...): AccountAddressCreate
accountAddressDelete(...): AccountAddressDelete
accountAddressUpdate(...): AccountAddressUpdate
"""
from fastapi_utils.api_model import APIModel

from . import bp
from ...globals import db, AsyncDal
from ...models.address import Address


class TAddress(APIModel):
    id: str
    name: str


@bp.list("/addresses", out=TAddress, summary="Address", tags=["Address"])
async def addresses_list():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(Address)
    return {"items": ins}


@bp.item("/address", out=TAddress, summary="Address", tags=["Address"])
async def address_item():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(Address)
    return {"items": ins}


@bp.op("/address/create", out=TAddress, summary="Address", tags=["Address"])
async def address_create():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(Address)
    return {"items": ins}


@bp.op("/address/update", out=TAddress, summary="Address", tags=["Address"])
async def address_update():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(Address)
    return {"items": ins}


@bp.op("/address/set_default", out=TAddress, summary="Address", tags=["Address"])
async def address_set_default():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(Address)
    return {"items": ins}


@bp.op("/address/delete", out=TAddress, summary="Address", tags=["Address"])
async def address_delete():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(Address)
    return {"items": ins}


@bp.op("/address/validation_rules", out=TAddress, summary="Address", tags=["Address"])
async def address_validation_rule():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(Address)
    return {"items": ins}
