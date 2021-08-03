from fastapi_utils.api_model import APIModel

from tifa.apps.admin import bp
from tifa.globals import db
from tifa.db.adal import AsyncDal
from tifa.models.discount import DiscountVoucher


class TVoucher(APIModel):
    id: str
    name: str


@bp.list("/vouchers", out=TVoucher, summary="Voucher", tags=["Voucher"])
async def vouchers_page():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(DiscountVoucher)
    return {"items": ins}


@bp.item("/voucher", out=TVoucher, summary="Voucher", tags=["Voucher"])
async def voucher_item():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(DiscountVoucher)
    return {"items": ins}


@bp.op("/voucher/translate", out=TVoucher, summary="Voucher", tags=["Voucher"])
async def voucher_translate():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(DiscountVoucher)
    return {"items": ins}


@bp.op("/voucher/create", out=TVoucher, summary="Voucher", tags=["Voucher"])
async def voucher_create():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(DiscountVoucher)
    return {"items": ins}


@bp.op("/voucher/update", out=TVoucher, summary="Voucher", tags=["Voucher"])
async def voucher_update():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(DiscountVoucher)
    return {"items": ins}


@bp.op("/voucher/delete", out=TVoucher, summary="Voucher", tags=["Voucher"])
async def voucher_delete():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(DiscountVoucher)
    return {"items": ins}


@bp.op("/voucher/bulk_delete", out=TVoucher, summary="Voucher", tags=["Voucher"])
async def voucher_bulk_delete():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(DiscountVoucher)
    return {"items": ins}


@bp.op("/voucher_catalog/add", out=TVoucher, summary="Voucher", tags=["Voucher"])
async def voucher_catalog_add():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(DiscountVoucher)
    return {"items": ins}


@bp.op("/voucher_catalog/remove", out=TVoucher, summary="Voucher", tags=["Voucher"])
async def voucher_catalog_remove():
    adal = AsyncDal(db.async_session)
    ins = await adal.first_or_404(DiscountVoucher)
    return {"items": ins}


"""
voucherVoucherListingUpdate(...): VoucherVoucherListingUpdate
"""
