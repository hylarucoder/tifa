from fastapi_utils.api_model import APIModel

from tifa.contrib.fastapi_plus import create_bp
from tifa.globals import db, AsyncDal, Dal
from tifa.models.merchant import Merchant

bp = create_bp()


@bp.post("/login")
async def login():
    pass


class TProfile(APIModel):
    id: str
    name: str


@bp.item("/profile", out=TProfile)
async def profile():
    adal = AsyncDal(db.async_session)
    merchant = await adal.first_or_404(Merchant)
    return {"item": merchant}


class TMerchant(APIModel):
    id: str
    name: str


@bp.item("/merchant", out=TMerchant)
def get_merchant():
    dal = Dal(db.session)
    merchant = dal.first_or_404(Merchant)
    return {"item": merchant}
