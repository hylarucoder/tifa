from fastapi_utils.api_model import APIModel

from tifa.apps.admin.router import bp
from tifa.apps.admin.local import g
from tifa.models.attr import Attribute, AttributeValue


class TAttribute(APIModel):
    id: str
    name: str


@bp.list("/attributes", out=TAttribute, summary="Attribute", tags=["Attribute"])
def get_attributes():
    items = g.adal.all(Attribute)
    return {"items": items}


@bp.item("/attribute/{id}", out=TAttribute, summary="Attribute", tags=["Attribute"])
def get_attribute(id: str):
    ins = g.adal.get_or_404(Attribute, id)
    return {"items": ins}


class ParamsAttributeCreate(APIModel):
    name: str


@bp.op("/attribute/create", out=TAttribute, summary="Attribute", tags=["Attribute"])
def attribute_create(params: ParamsAttributeCreate):
    ins = g.adal.add(Attribute, **params.dict())
    return {"items": ins}


class ParamsAttributeUpdate(APIModel):
    id: str
    name: str


@bp.op("/attribute/update", out=TAttribute, summary="Attribute", tags=["Attribute"])
def attribute_update(params: ParamsAttributeUpdate):
    ins = g.adal.get_or_404(Attribute, params.id)
    return {"items": ins}


class ParamsAttributeDelete(APIModel):
    id: str


@bp.op("/attribute/delete", out=TAttribute, summary="Attribute", tags=["Attribute"])
def attribute_delete(params: ParamsAttributeDelete):
    ins = g.adal.get_or_404(Attribute, params.id)
    g.adal.delete(ins)
    g.adal.commit()
    return {"item": ins}


class ParamsAttributeBulkDelete(APIModel):
    ids: list[str]


@bp.op(
    "/attribute/bulk_delete", out=TAttribute, summary="Attribute", tags=["Attribute"]
)
def attribute_bulk_delete(params: ParamsAttributeBulkDelete):
    items = g.adal.bulk_get(Attribute, params.ids)
    for item in items:
        g.adal.delete(item)
    g.adal.commit()
    return {"items": items}


class ParamsAttributeTranslate(APIModel):
    id: str


@bp.op("/attribute/translate", out=TAttribute, summary="Attribute", tags=["Attribute"])
def attribute_translate(params: ParamsAttributeTranslate):
    ins = g.adal.get_or_404(Attribute, params.id)
    return {"item": ins}


class ParamsAttributeReorderValues(APIModel):
    id: str
    value_ids: list[str]


@bp.op(
    "/attribute/reorder_values", out=TAttribute, summary="Attribute", tags=["Attribute"]
)
def attribute_reorder_values(params: ParamsAttributeReorderValues):
    ins = g.adal.get_or_404(Attribute, params.id)
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
    ins = g.adal.add(AttributeValue)
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
    ins = g.adal.get_or_404(AttributeValue, params.id)
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
    ins = g.adal.get_or_404(AttributeValue, params.id)
    g.adal.delete(ins)
    g.adal.commit()
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
    items = g.adal.bulk_get(AttributeValue, params.ids)
    for item in items:
        g.adal.delete(item)
    g.adal.commit()
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
    ins = g.adal.get_or_404(AttributeValue, params.id)
    return {"item": ins}
