from tifa.globals import Dal, db
from tifa.models.system import Staff


def test_staff_count(staff):
    dal = Dal(db.session)
    assert len(dal.all(Staff)) == 1
