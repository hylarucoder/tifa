from fastapi_utils.api_model import APIModel

from . import bp
from ...globals import db, AsyncDal
from ...models.discount import DiscountVoucher


class TVoucher(APIModel):
    id: str
    name: str


@bp.list("/vouchers", out=TVoucher, summary="Voucher", tags=["Voucher"])
async def addresses_list():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(DiscountVoucher)
    return {"items": ins}


@bp.item("/voucher", out=TVoucher, summary="Voucher", tags=["Voucher"])
async def app_item():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(DiscountVoucher)
    return {"items": ins}


@bp.op("/voucher/translate", out=TVoucher, summary="Voucher", tags=["Voucher"])
async def app_item():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(DiscountVoucher)
    return {"items": ins}


@bp.op("/voucher/create", out=TVoucher, summary="Voucher", tags=["Voucher"])
async def app_create():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(DiscountVoucher)
    return {"items": ins}


@bp.op("/voucher/update", out=TVoucher, summary="Voucher", tags=["Voucher"])
async def app_update():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(DiscountVoucher)
    return {"items": ins}


@bp.op("/voucher/delete", out=TVoucher, summary="Voucher", tags=["Voucher"])
async def app_update():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(DiscountVoucher)
    return {"items": ins}


@bp.op("/voucher/bulk_delete", out=TVoucher, summary="Voucher", tags=["Voucher"])
async def app_update():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(DiscountVoucher)
    return {"items": ins}


@bp.op("/voucher_catalog/add", out=TVoucher, summary="Voucher", tags=["Voucher"])
async def app_update():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(DiscountVoucher)
    return {"items": ins}


@bp.op("/voucher_catalog/remove", out=TVoucher, summary="Voucher", tags=["Voucher"])
async def app_update():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(DiscountVoucher)
    return {"items": ins}


"""
voucherVoucherListingUpdate(...): VoucherVoucherListingUpdate
"""
