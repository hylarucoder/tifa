from tifa.globals import db
from tifa.db.dal import Dal
from tifa.models.system import Staff


def test_staff_count(staff):
    dal = Dal(db.session)
    assert len(dal.all(Staff)) == 1
