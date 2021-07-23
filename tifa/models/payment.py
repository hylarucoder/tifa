import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import INET, JSONB
from sqlalchemy.orm import relationship

from tifa.globals import Model


class Payment(Model):
    __tablename__ = "payment"
    __table_args__ = (
        sa.CheckConstraint("cc_exp_month >= 0"),
        sa.CheckConstraint("cc_exp_year >= 0"),
        sa.Index(
            "payment_pay_order_i_f22aa2_gin", "order_id", "is_active", "charge_status"
        ),
    )

    id = sa.Column(sa.Integer, primary_key=True)
    gateway = sa.Column(sa.String(255), nullable=False)
    is_active = sa.Column(sa.Boolean, nullable=False)
    created = sa.Column(sa.DateTime(True), nullable=False)
    modified = sa.Column(sa.DateTime(True), nullable=False)
    charge_status = sa.Column(sa.String(20), nullable=False)
    billing_first_name = sa.Column(sa.String(256), nullable=False)
    billing_last_name = sa.Column(sa.String(256), nullable=False)
    billing_company_name = sa.Column(sa.String(256), nullable=False)
    billing_address_1 = sa.Column(sa.String(256), nullable=False)
    billing_address_2 = sa.Column(sa.String(256), nullable=False)
    billing_city = sa.Column(sa.String(256), nullable=False)
    billing_city_area = sa.Column(sa.String(128), nullable=False)
    billing_postal_code = sa.Column(sa.String(256), nullable=False)
    billing_country_code = sa.Column(sa.String(2), nullable=False)
    billing_country_area = sa.Column(sa.String(256), nullable=False)
    billing_email = sa.Column(sa.String(254), nullable=False)
    customer_ip_address = sa.Column(INET)
    cc_brand = sa.Column(sa.String(40), nullable=False)
    cc_exp_month = sa.Column(sa.Integer)
    cc_exp_year = sa.Column(sa.Integer)
    cc_first_digits = sa.Column(sa.String(6), nullable=False)
    cc_last_digits = sa.Column(sa.String(4), nullable=False)
    extra_data = sa.Column(sa.Text, nullable=False)
    token = sa.Column(sa.String(512), nullable=False)
    currency = sa.Column(sa.String(3), nullable=False)
    total = sa.Column(sa.Numeric(12, 3), nullable=False)
    captured_amount = sa.Column(sa.Numeric(12, 3), nullable=False)
    checkout_id = sa.Column(
        sa.ForeignKey("checkout_checkout.token", deferrable=True, initially="DEFERRED"),
        index=True,
    )
    order_id = sa.Column(
        sa.ForeignKey("order_order.id", deferrable=True, initially="DEFERRED"),
        index=True,
    )
    to_confirm = sa.Column(sa.Boolean, nullable=False)
    payment_method_type = sa.Column(sa.String(256), nullable=False)
    return_url = sa.Column(sa.String(200))
    psp_reference = sa.Column(sa.String(512), index=True)

    checkout = relationship("CheckoutCheckout")
    order = relationship("OrderOrder")


class PaymentTransaction(Model):
    __tablename__ = "payment_transaction"

    id = sa.Column(sa.Integer, primary_key=True)
    created = sa.Column(sa.DateTime(True), nullable=False)
    token = sa.Column(sa.String(512), nullable=False)
    kind = sa.Column(sa.String(25), nullable=False)
    is_success = sa.Column(sa.Boolean, nullable=False)
    error = sa.Column(sa.String(256))
    currency = sa.Column(sa.String(3), nullable=False)
    amount = sa.Column(sa.Numeric(12, 3), nullable=False)
    gateway_response = sa.Column(JSONB, nullable=False)
    payment_id = sa.Column(
        sa.ForeignKey("payment_payment.id", deferrable=True, initially="DEFERRED"),
        nullable=False,
        index=True,
    )
    customer_id = sa.Column(sa.String(256))
    action_required = sa.Column(sa.Boolean, nullable=False)
    action_required_data = sa.Column(JSONB, nullable=False)
    already_processed = sa.Column(sa.Boolean, nullable=False)

    payment = relationship("PaymentPayment")
