from tifa.globals import Model
import sqlalchemy as sa


class DjangoPricesOpenexchangeratesConversionrate(Model):
    __tablename__ = "django_prices_openexchangerates_conversionrate"

    id = sa.Column(sa.Integer, primary_key=True)
    to_currency = sa.Column(sa.String(3), nullable=False, unique=True)
    rate = sa.Column(sa.Numeric(20, 12), nullable=False)
    modified_at = sa.Column(sa.DateTime, nullable=False)


class DjangoPricesVatlayerRatetype(Model):
    __tablename__ = "django_prices_vatlayer_ratetypes"

    id = sa.Column(sa.Integer, primary_key=True)
    types = sa.Column(sa.Text, nullable=False)


class DjangoPricesVatlayerVat(Model):
    __tablename__ = "django_prices_vatlayer_vat"

    id = sa.Column(sa.Integer, primary_key=True)
    country_code = sa.Column(sa.String(2), nullable=False, index=True)
    data = sa.Column(sa.Text, nullable=False)
