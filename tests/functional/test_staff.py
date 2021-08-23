import pytest

from tifa.globals import db
from tifa.db.dal import Dal
from tifa.models.system import Staff
from tifa.models.user import User


@pytest.mark.asyncio
async def test_staff_count(adal, staff):
    assert len(await adal.all(Staff)) == 1

@pytest.mark.asyncio
async def test_user_count(adal, user):
    assert len(await adal.all(User)) == 1
