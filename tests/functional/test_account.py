from tifa.models.system import SysUser


def test_account(setup_db):
    assert len(SysUser.all()) == 1
