from tifa.globals import Dal, db
from tifa.models.system import Staff

dal = Dal(db.session)
dal.add(
    Staff,
    name="hey tea",
)
dal.commit()
