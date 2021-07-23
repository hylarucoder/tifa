import sqlalchemy as sa

from tifa.globals import Model


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