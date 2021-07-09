import pytest

from tifa.globals import db
from tifa.models.sys_account import SysUser


def test_account(setup_db):
    assert len(SysUser.all()) == 1
