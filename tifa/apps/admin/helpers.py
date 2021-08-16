from tifa.apps.admin.base import context
from tifa.db.adal import AsyncDal
from tifa.models.system import Staff


async def use_adal() -> AsyncDal:
    return context.get()["adal"]


async def use_staff() -> Staff:
    return context.get()["staff"]
