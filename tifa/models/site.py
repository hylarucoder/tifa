import sqlalchemy as sa
from sqlalchemy.orm import relationship

from tifa.globals import Model


class SiteSetting(Model):
    __tablename__ = "site_setting"

    id = sa.Column(sa.Integer, primary_key=True)
    header_text = sa.Column(sa.String(200), nullable=False)
    description = sa.Column(sa.String(500), nullable=False)
    bottom_menu_id = sa.Column(sa.ForeignKey("menu.id"), index=True)
    bottom_menu = relationship(
        "Menu", primaryjoin="SiteSetting.bottom_menu_id == Menu.id"
    )
    top_menu_id = sa.Column(sa.ForeignKey("menu.id"), index=True)
    top_menu = relationship("Menu", primaryjoin="SiteSetting.top_menu_id == Menu.id")
    display_gross_prices = sa.Column(sa.Boolean, nullable=False)
    include_taxes_in_prices = sa.Column(sa.Boolean, nullable=False)
    charge_taxes_on_shipping = sa.Column(sa.Boolean, nullable=False)
    track_inventory_by_default = sa.Column(sa.Boolean, nullable=False)
    default_weight_unit = sa.Column(sa.String(30), nullable=False)
    automatic_fulfillment_digital_products = sa.Column(sa.Boolean, nullable=False)
    default_digital_max_downloads = sa.Column(sa.Integer)
    default_digital_url_valid_days = sa.Column(sa.Integer)
    company_address_id = sa.Column(sa.ForeignKey("address.id"))
    company_address = relationship("Address")
    default_mail_sender_address = sa.Column(sa.String(254))
    default_mail_sender_name = sa.Column(sa.String(78), nullable=False)
    customer_set_password_url = sa.Column(sa.String(255))
    automatically_confirm_all_new_orders = sa.Column(sa.Boolean, nullable=False)


class SiteSettingsTranslation(Model):
    __tablename__ = "site_setting_translation"
    __table_args__ = (sa.UniqueConstraint("language_code", "site_settings_id"),)

    id = sa.Column(sa.Integer, primary_key=True)
    language_code = sa.Column(sa.String(10), nullable=False)
    header_text = sa.Column(sa.String(200), nullable=False)
    description = sa.Column(sa.String(500), nullable=False)
    site_settings_id = sa.Column(
        sa.ForeignKey("site_setting.id"),
        nullable=False,
    )

    site_settings = relationship(SiteSetting)
