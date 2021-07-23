import sqlalchemy as sa
from sqlalchemy.orm import relationship

from tifa.globals import Model


class GiftCard(Model):
    __tablename__ = "giftcard"

    id = sa.Column(sa.Integer, primary_key=True)
    code = sa.Column(sa.String(16), nullable=False, unique=True)
    created = sa.Column(sa.DateTime(True), nullable=False)
    start_date = sa.Column(sa.Date, nullable=False)
    end_date = sa.Column(sa.Date)
    last_used_on = sa.Column(sa.DateTime(True))
    is_active = sa.Column(sa.Boolean, nullable=False)
    initial_balance_amount = sa.Column(sa.Numeric(12, 3), nullable=False)
    current_balance_amount = sa.Column(sa.Numeric(12, 3), nullable=False)
    user_id = sa.Column(
        sa.ForeignKey("account_user.id", deferrable=True, initially="DEFERRED"),
        index=True,
    )
    currency = sa.Column(sa.String(3), nullable=False)

    user = relationship("AccountUser")
