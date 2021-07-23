import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship

from tifa.globals import Model
from tifa.models.utils import TimestampMixin


class User(TimestampMixin, Model):
    __tablename__ = "user"
    __table_args__ = (
        sa.Index("account_username_email", "email", "first_name", "last_name"),
    )

    id = sa.Column(sa.Integer, primary_key=True)
    email = sa.Column(sa.String(254), nullable=False, unique=True)
    is_active = sa.Column(sa.Boolean, default=False)
    password = sa.Column(sa.String(128), nullable=False)
    last_login_at = sa.Column(sa.DateTime)
    default_billing_address_id = sa.Column(sa.ForeignKey("user_address.id"))
    default_billing_address = relationship(
        "UserAddress",
        primaryjoin="User.default_billing_address_id == UserAddress.id",
    )
    default_shipping_address_id = sa.Column(sa.ForeignKey("account_address.id"), )
    default_shipping_address = relationship(
        "UserAddress",
        primaryjoin="User.default_shipping_address_id == UserAddress.id",
    )
    note = sa.Column(sa.Text)
    first_name = sa.Column(sa.String(256), nullable=False)
    last_name = sa.Column(sa.String(256), nullable=False)
    avatar = sa.Column(sa.String(100))
    metadata_private = sa.Column(JSONB, index=True)
    metadata_public = sa.Column(JSONB, index=True)
    jwt_token_key = sa.Column(sa.String(12), nullable=False)
    language_code = sa.Column(sa.String(35), nullable=False)


class Address(Model):
    __tablename__ = "address"

    id = sa.Column(sa.Integer, primary_key=True)
    first_name = sa.Column(sa.String(256), nullable=False)
    last_name = sa.Column(sa.String(256), nullable=False)
    company_name = sa.Column(sa.String(256), nullable=False)
    street_address_1 = sa.Column(sa.String(256), nullable=False)
    street_address_2 = sa.Column(sa.String(256), nullable=False)
    city = sa.Column(sa.String(256), nullable=False)
    postal_code = sa.Column(sa.String(20), nullable=False)
    country = sa.Column(sa.String(2), nullable=False)
    country_area = sa.Column(sa.String(128), nullable=False)
    phone = sa.Column(sa.String(128), nullable=False)
    city_area = sa.Column(sa.String(128), nullable=False)


class UserAddressMap(Model):
    __tablename__ = "user_address_map"
    __table_args__ = (sa.UniqueConstraint("user_id", "address_id"),)

    id = sa.Column(sa.Integer, primary_key=True)
    user_id = sa.Column(
        sa.ForeignKey("account_user.id"),
        nullable=False,
        index=True,
    )
    address_id = sa.Column(
        sa.ForeignKey("account_address.id"),
        nullable=False,
        index=True,
    )

    address = relationship("AccountAddres")
    user = relationship("AccountUser")


class CustomerEvent(Model):
    __tablename__ = "customer_event"

    id = sa.Column(sa.Integer, primary_key=True)
    date = sa.Column(sa.DateTime, nullable=False)
    type = sa.Column(sa.String(255), nullable=False)
    parameters = sa.Column(JSONB, nullable=False)
    order_id = sa.Column(sa.ForeignKey("order.id"))
    order = relationship("Order")
    user_id = sa.Column(sa.ForeignKey("user.id"))
    user = relationship(User)
    app_id = sa.Column(sa.ForeignKey("app.id"))
    app = relationship("App")


class CustomerNote(Model):
    __tablename__ = "customer_note"

    id = sa.Column(sa.Integer, primary_key=True)
    date = sa.Column(sa.DateTime, nullable=False, index=True)
    content = sa.Column(sa.Text, nullable=False)
    is_public = sa.Column(sa.Boolean, nullable=False)
    user_id = sa.Column(sa.ForeignKey("user.id"), nullable=False)
    user = relationship(User)
    staff_id = sa.Column(sa.ForeignKey("staff.id"), )
    staff = relationship("Staff")
