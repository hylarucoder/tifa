import sqlalchemy as sa
from sqlalchemy.orm import relationship

from tifa.globals import Model


class SiteSitesettingstranslation(Model):
    __tablename__ = "site_sitesettingstranslation"
    __table_args__ = (sa.UniqueConstraint("language_code", "site_settings_id"),)

    id = sa.Column(sa.Integer, primary_key=True)
    language_code = sa.Column(sa.String(10), nullable=False)
    header_text = sa.Column(sa.String(200), nullable=False)
    description = sa.Column(sa.String(500), nullable=False)
    site_settings_id = sa.Column(
        sa.ForeignKey("site_sitesettings.id", deferrable=True, initially="DEFERRED"),
        nullable=False,
        index=True,
    )

    site_settings = relationship("SiteSitesetting")


class SiteSitesetting(Model):
    __tablename__ = "site_sitesettings"

    id = sa.Column(sa.Integer, primary_key=True)
    header_text = sa.Column(sa.String(200), nullable=False)
    description = sa.Column(sa.String(500), nullable=False)
    site_id = sa.Column(
        sa.ForeignKey("django_site.id", deferrable=True, initially="DEFERRED"),
        nullable=False,
        unique=True,
    )
    bottom_menu_id = sa.Column(
        sa.ForeignKey("menu_menu.id", deferrable=True, initially="DEFERRED"), index=True
    )
    top_menu_id = sa.Column(
        sa.ForeignKey("menu_menu.id", deferrable=True, initially="DEFERRED"), index=True
    )
    display_gross_prices = sa.Column(sa.Boolean, nullable=False)
    include_taxes_in_prices = sa.Column(sa.Boolean, nullable=False)
    charge_taxes_on_shipping = sa.Column(sa.Boolean, nullable=False)
    track_inventory_by_default = sa.Column(sa.Boolean, nullable=False)
    default_weight_unit = sa.Column(sa.String(30), nullable=False)
    automatic_fulfillment_digital_products = sa.Column(sa.Boolean, nullable=False)
    default_digital_max_downloads = sa.Column(sa.Integer)
    default_digital_url_valid_days = sa.Column(sa.Integer)
    company_address_id = sa.Column(
        sa.ForeignKey("account_address.id", deferrable=True, initially="DEFERRED"),
        index=True,
    )
    default_mail_sender_address = sa.Column(sa.String(254))
    default_mail_sender_name = sa.Column(sa.String(78), nullable=False)
    customer_set_password_url = sa.Column(sa.String(255))
    automatically_confirm_all_new_orders = sa.Column(sa.Boolean, nullable=False)

    bottom_menu = relationship(
        "MenuMenu", primaryjoin="SiteSitesetting.bottom_menu_id == MenuMenu.id"
    )
    company_address = relationship("AccountAddres")
    site = relationship("DjangoSite", uselist=False)
    top_menu = relationship(
        "MenuMenu", primaryjoin="SiteSitesetting.top_menu_id == MenuMenu.id"
    )
