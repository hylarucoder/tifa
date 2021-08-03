from tifa.globals import db
from tifa.db.dal import Dal
from tifa.models.system import Staff

dal = Dal(db.session)
dal.add(
    Staff,
    name="hey tea",
)
dal.commit()
