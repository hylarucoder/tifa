import pytest

from tifa.globals import db
from tifa.models.sys_account import SysUser


@pytest.mark.asyncio
async def test_account(setup_db):
    assert len(await SysUser.all()) == 1
