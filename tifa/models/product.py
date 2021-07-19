import datetime
import enum

from fastapi_utils.enums import StrEnum
from sqlalchemy.orm import relationship

from tifa.globals import Model
import sqlalchemy as sa

from tifa.models.merchant import Merchant


class ProductBrand(Model):
    id = sa.Column(sa.Integer, primary_key=True)
    merchant_id = sa.Column(sa.Integer, sa.ForeignKey('merchant.id'))
    merchant = relationship(Merchant)

    name = sa.Column(sa.String(50))
    desc = sa.Column(sa.String(255))
    logo_url = sa.Column(sa.String(255))

    class Status(StrEnum):
        ENABLE = enum.auto()
        DISABLE = enum.auto()

    status = sa.Column(sa.Enum(Status), default=Status.ENABLE)
    deleted = sa.Column(sa.Boolean, default=False)


class ProductCategory(Model):
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(255))
    desc = sa.Column(sa.String(255))
    merchant_id = sa.Column(sa.Integer, sa.ForeignKey('merchant.id'))
    merchant = relationship(Merchant)
    deleted = sa.Column(sa.Boolean, default=False)


class ProductSpu(Model):
    """
    -- spu: standard product unit 标准产品单位
    """
    id = sa.Column(sa.Integer, primary_key=True)
    category_id = sa.Column(sa.Integer, sa.ForeignKey('product_brand.id'))
    category = relationship(ProductCategory)
    merchant_id = sa.Column(sa.Integer, sa.ForeignKey('merchant.id'))
    merchant = relationship(Merchant)
    name = sa.Column(sa.String(255))
    desc = sa.Column(sa.String(255))
    price = sa.Column(sa.DECIMAL(10, 2))
    market_price = sa.Column(sa.DECIMAL(10, 2))
    deleted = sa.Column(sa.Boolean, default=False)


class ProductSku(Model):
    """
    -- sku: stock keeping unit 库存量单位
    """
    id = sa.Column(sa.Integer, primary_key=True)
    merchant_id = sa.Column(sa.Integer, sa.ForeignKey('merchant.id'))
    merchant = relationship(Merchant)
    product_id = sa.Column(sa.Integer, sa.ForeignKey('product_spu.id'))
    product = relationship(ProductSpu)
    price = sa.Column(sa.DECIMAL(10, 2))
    market_price = sa.Column(sa.DECIMAL(10, 2))
    deleted = sa.Column(sa.Boolean, default=False)
    # attrs 属性可以丢缓存


class ProductAttr(Model):
    # -- 销售属性表 product_attr
    id = sa.Column(sa.BigInteger, primary_key=True)
    merchant_id = sa.Column(sa.Integer, sa.ForeignKey('merchant.id'))
    merchant = relationship(Merchant)
    name = sa.Column(sa.String(255))
    desc = sa.Column(sa.String(255))


class ProductAttrValue(Model):
    # -- 销售属性值 product_attr_value
    id = sa.Column(sa.BigInteger, primary_key=True)
    merchant_id = sa.Column(sa.Integer, sa.ForeignKey('merchant.id'))
    merchant = relationship(Merchant)
    attr_id = sa.Column(sa.BigInteger, sa.ForeignKey('product_attr.id'))
    attr = relationship(ProductAttr)
    value = sa.Column(sa.String(255))
    desc = sa.Column(sa.String(255))


class ProductSpuSkuAttrMap(Model):
    # -- 关联关系冗余表
    # product_spu_sku_attr_map
    # -- 1. # spu下 # 有哪些sku
    # -- 2. # spu下 # 有那些销售属性
    # -- 3. # spu下 # 每个销售属性对应的销售属性值(一对多)
    # -- 4. # spu下 # 每个销售属性值对应的sku(一对多)
    id = sa.Column(sa.BigInteger, primary_key=True)
    merchant_id = sa.Column(sa.Integer, sa.ForeignKey('merchant.id'))
    merchant = relationship(Merchant)
    spu_id = sa.Column(sa.BigInteger, sa.ForeignKey('product_spu.id'))
    spu = relationship(ProductSpu)
    sku_id = sa.Column(sa.BigInteger, sa.ForeignKey('product_sku.id'))
    sku = relationship(ProductSku)
    attr_id = sa.Column(sa.BigInteger, sa.ForeignKey('product_attr.id'))
    attr = relationship(ProductAttr)
    attr_value_id = sa.Column(sa.BigInteger, sa.ForeignKey('product_attr_value.id'))
    attr_value = relationship(ProductAttrValue)


class ProductSkuStock(Model):
    id = sa.Column(sa.BigInteger, primary_key=True)
    sku_id = sa.Column(sa.BigInteger, sa.ForeignKey('product_sku.id'))
    sku = relationship(ProductSku)
    qty = sa.Column(sa.Integer, default=99999)
