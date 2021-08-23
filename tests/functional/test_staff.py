import pytest

from tifa.globals import db
from tifa.db.dal import Dal
from tifa.models.system import Staff


@pytest.mark.asyncio
async def test_staff_count(adal, staff):
    assert len(await adal.all(Staff)) == 1
