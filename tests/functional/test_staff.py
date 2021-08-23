import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from tifa.db.adal import AsyncDal
from tifa.globals import db
from tifa.db.dal import Dal
from tifa.models.system import Staff
from tifa.models.user import User


@pytest.mark.asyncio
async def test_staff_count(session: AsyncSession, staff):
    adal = AsyncDal(session)
    assert len(await adal.all(Staff)) == 1


@pytest.mark.asyncio
async def test_user_count(session: AsyncSession, user):
    adal = AsyncDal(session)
    assert len(await adal.all(User)) == 1
