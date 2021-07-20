from tifa.globals import Dal, db
from tifa.models.system import SysUser


def test_account(setup_db):
    dal = Dal(db.session)
    assert len(dal.all(SysUser)) == 1
