from tifa.globals import Dal, db
from tifa.models.system import Staff


def test_account(setup_db):
    dal = Dal(db.session)
    assert len(dal.all(Staff)) == 1
