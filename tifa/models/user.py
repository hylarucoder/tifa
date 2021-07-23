import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship

from tifa.globals import Model


class User(Model):
    id = sa.Column(sa.Integer, primary_key=True)
    nickname = sa.Column(sa.String(50))


class AccountAddress(Model):
    __tablename__ = "account_address"

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


class AccountUser(Model):
    __tablename__ = "account_user"
    __table_args__ = (
        sa.Index("account_use_email_d707ff_gin", "email", "first_name", "last_name"),
    )

    id = sa.Column(sa.Integer, primary_key=True)
    is_superuser = sa.Column(sa.Boolean, nullable=False)
    email = sa.Column(sa.String(254), nullable=False, unique=True)
    is_staff = sa.Column(sa.Boolean, nullable=False)
    is_active = sa.Column(sa.Boolean, nullable=False)
    password = sa.Column(sa.String(128), nullable=False)
    date_joined = sa.Column(sa.DateTime(True), nullable=False)
    last_login = sa.Column(sa.DateTime(True))
    default_billing_address_id = sa.Column(
        sa.ForeignKey("account_address.id", deferrable=True, initially="DEFERRED"),
        index=True,
    )
    default_shipping_address_id = sa.Column(
        sa.ForeignKey("account_address.id", deferrable=True, initially="DEFERRED"),
        index=True,
    )
    note = sa.Column(sa.Text)
    first_name = sa.Column(sa.String(256), nullable=False)
    last_name = sa.Column(sa.String(256), nullable=False)
    avatar = sa.Column(sa.String(100))
    metadata_private = sa.Column(JSONB, index=True)
    metadata_public = sa.Column(JSONB, index=True)
    jwt_token_key = sa.Column(sa.String(12), nullable=False)
    language_code = sa.Column(sa.String(35), nullable=False)

    default_billing_address = relationship(
        "AccountAddres",
        primaryjoin="AccountUser.default_billing_address_id == AccountAddres.id",
    )
    default_shipping_address = relationship(
        "AccountAddres",
        primaryjoin="AccountUser.default_shipping_address_id == AccountAddres.id",
    )


class AccountCustomernote(Model):
    __tablename__ = "account_customernote"

    id = sa.Column(sa.Integer, primary_key=True)
    date = sa.Column(sa.DateTime(True), nullable=False, index=True)
    content = sa.Column(sa.Text, nullable=False)
    is_public = sa.Column(sa.Boolean, nullable=False)
    customer_id = sa.Column(
        sa.ForeignKey("account_user.id", deferrable=True, initially="DEFERRED"),
        nullable=False,
        index=True,
    )
    user_id = sa.Column(
        sa.ForeignKey("account_user.id", deferrable=True, initially="DEFERRED"),
        index=True,
    )

    customer = relationship(
        "AccountUser", primaryjoin="AccountCustomernote.customer_id == AccountUser.id"
    )
    user = relationship(
        "AccountUser", primaryjoin="AccountCustomernote.user_id == AccountUser.id"
    )


class AccountStaffnotificationrecipient(Model):
    __tablename__ = "account_staffnotificationrecipient"

    id = sa.Column(sa.Integer, primary_key=True)
    staff_email = sa.Column(sa.String(254), unique=True)
    active = sa.Column(sa.Boolean, nullable=False)
    user_id = sa.Column(
        sa.ForeignKey("account_user.id", deferrable=True, initially="DEFERRED"),
        unique=True,
    )

    user = relationship("AccountUser", uselist=False)


class AccountUserAddress(Model):
    __tablename__ = "account_user_addresses"
    __table_args__ = (sa.UniqueConstraint("user_id", "address_id"),)

    id = sa.Column(sa.Integer, primary_key=True)
    user_id = sa.Column(
        sa.ForeignKey("account_user.id", deferrable=True, initially="DEFERRED"),
        nullable=False,
        index=True,
    )
    address_id = sa.Column(
        sa.ForeignKey("account_address.id", deferrable=True, initially="DEFERRED"),
        nullable=False,
        index=True,
    )

    address = relationship("AccountAddres")
    user = relationship("AccountUser")


class AccountCustomerevent(Model):
    __tablename__ = "account_customerevent"

    id = sa.Column(sa.Integer, primary_key=True)
    date = sa.Column(sa.DateTime(True), nullable=False)
    type = sa.Column(sa.String(255), nullable=False)
    parameters = sa.Column(JSONB, nullable=False)
    order_id = sa.Column(
        sa.ForeignKey("order_order.id", deferrable=True, initially="DEFERRED"),
        index=True,
    )
    user_id = sa.Column(
        sa.ForeignKey("account_user.id", deferrable=True, initially="DEFERRED"),
        index=True,
    )
    app_id = sa.Column(
        sa.ForeignKey("app_app.id", deferrable=True, initially="DEFERRED"), index=True
    )

    app = relationship("AppApp")
    order = relationship("OrderOrder")
    user = relationship("AccountUser")
