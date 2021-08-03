from fastapi_utils.api_model import APIModel

from tifa.apps.admin import bp
from tifa.globals import db
from tifa.db.dal import Dal
from tifa.models.attr import Attribute, AttributeValue


class TAttribute(APIModel):
    id: str
    name: str


@bp.list("/attributes", out=TAttribute, summary="Attribute", tags=["Attribute"])
def get_attributes():
    adal = Dal(db.session)
    items = adal.all(Attribute)
    return {"items": items}


@bp.item("/attribute/{id}", out=TAttribute, summary="Attribute", tags=["Attribute"])
def get_attribute(id: str):
    adal = Dal(db.session)
    ins = adal.get_or_404(Attribute, id)
    return {"items": ins}


class ParamsAttributeCreate(APIModel):
    name: str


@bp.op("/attribute/create", out=TAttribute, summary="Attribute", tags=["Attribute"])
def attribute_create(params: ParamsAttributeCreate):
    adal = Dal(db.session)
    ins = adal.add(Attribute, **params.dict())
    return {"items": ins}


class ParamsAttributeUpdate(APIModel):
    id: str
    name: str


@bp.op("/attribute/update", out=TAttribute, summary="Attribute", tags=["Attribute"])
def attribute_update(params: ParamsAttributeUpdate):
    adal = Dal(db.session)
    ins = adal.get_or_404(Attribute, params.id)
    return {"items": ins}


class ParamsAttributeDelete(APIModel):
    id: str


@bp.op("/attribute/delete", out=TAttribute, summary="Attribute", tags=["Attribute"])
def attribute_delete(params: ParamsAttributeDelete):
    adal = Dal(db.session)
    ins = adal.get_or_404(Attribute, params.id)
    adal.delete(ins)
    adal.commit()
    return {"item": ins}


class ParamsAttributeBulkDelete(APIModel):
    ids: list[str]


@bp.op(
    "/attribute/bulk_delete", out=TAttribute, summary="Attribute", tags=["Attribute"]
)
def attribute_bulk_delete(params: ParamsAttributeBulkDelete):
    adal = Dal(db.session)
    items = adal.bulk_get(Attribute, params.ids)
    for item in items:
        adal.delete(item)
    adal.commit()
    return {"items": items}


class ParamsAttributeTranslate(APIModel):
    id: str


@bp.op("/attribute/translate", out=TAttribute, summary="Attribute", tags=["Attribute"])
def attribute_translate(params: ParamsAttributeTranslate):
    adal = Dal(db.session)
    ins = adal.get_or_404(Attribute, params.id)
    return {"item": ins}


class ParamsAttributeReorderValues(APIModel):
    id: str
    value_ids: list[str]


@bp.op(
    "/attribute/reorder_values", out=TAttribute, summary="Attribute", tags=["Attribute"]
)
def attribute_reorder_values(params: ParamsAttributeReorderValues):
    adal = Dal(db.session)
    ins = adal.get_or_404(Attribute, params.id)
    return {"items": ins}


class TAttributeValue(APIModel):
    id: str
    name: str


class ParamsAttributeValueCreate(APIModel):
    name: str


@bp.op(
    "/attribute_value/create",
    out=TAttributeValue,
    summary="AttributeValue",
    tags=["Attribute"],
)
def attribute_value_create(params: ParamsAttributeValueCreate):
    adal = Dal(db.session)
    ins = adal.add(AttributeValue)
    return {"item": ins}


class ParamsAttributeValueUpdate(APIModel):
    id: str
    name: str


@bp.op(
    "/attribute_value/update",
    out=TAttributeValue,
    summary="AttributeValue",
    tags=["Attribute"],
)
def attribute_value_update(params: ParamsAttributeValueUpdate):
    adal = Dal(db.session)
    ins = adal.get_or_404(AttributeValue, params.id)
    return {"item": ins}


class ParamsAttributeValueDelete(APIModel):
    id: str


@bp.op(
    "/attribute_value/delete",
    out=TAttributeValue,
    summary="AttributeValue",
    tags=["Attribute"],
)
def attribute_value_delete(params: ParamsAttributeValueDelete):
    adal = Dal(db.session)
    ins = adal.get_or_404(AttributeValue, params.id)
    adal.delete(ins)
    adal.commit()
    return {"item": ins}


class ParamsAttributeValueBulkDelete(APIModel):
    ids: list[str]


@bp.op(
    "/attribute_value/bulk_delete",
    out=TAttributeValue,
    summary="AttributeValue",
    tags=["Attribute"],
)
def attribute_value_bulk_delete(params: ParamsAttributeBulkDelete):
    adal = Dal(db.session)
    items = adal.bulk_get(AttributeValue, params.ids)
    for item in items:
        adal.delete(item)
    adal.commit()
    return {"items": items}


class ParamsAttributeValueTranslate(APIModel):
    id: str


@bp.op(
    "/attribute_value/translate",
    out=TAttributeValue,
    summary="AttributeValue",
    tags=["Attribute"],
)
def attribute_value_translate(params: ParamsAttributeValueTranslate):
    adal = Dal(db.session)
    ins = adal.get_or_404(AttributeValue, params.id)
    return {"item": ins}
