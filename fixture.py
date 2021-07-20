from tifa.globals import Dal, db
from tifa.models.merchant import Merchant

# thread local session
dal = Dal(db.session)
dal.add(
    Merchant,
    code="001",
    name="hey tea",
)
dal.commit()
