from __future__ import annotations

from typing import Any, Optional

from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import F, QuerySet
from django.http import Http404
from django.shortcuts import get_object_or_404 as _get_object_or_404
from typing_extensions import Self


def get_object_or_404(queryset, *filter_args, **filter_kwargs) -> Model:
    try:
        return _get_object_or_404(queryset, *filter_args, **filter_kwargs)  # type: ignore
    except (TypeError, ValueError, ValidationError):
        raise Http404()


class BaseManager(models.Manager):
    ...


class Model(models.Model):
    id: Optional[int] | models.AutoField | models.BigAutoField

    class Meta:
        abstract = True

    objects = BaseManager()

    @classmethod
    def filter(cls, *args, **kwargs) -> QuerySet[Model]:
        return cls.objects.filter(*args, **kwargs)

    @classmethod
    def all(cls) -> QuerySet[Self] | list[Self]:
        return cls.objects.all()



    @classmethod
    def get(cls, pk) -> Self:
        return cls.objects.get(pk=pk)

    @classmethod
    def create(cls, **kwargs) -> Self:
        return cls.objects.create(**kwargs)

    @classmethod
    def get_or_404(cls, **kwargs) -> Self:
        return get_object_or_404(cls.objects.filter(**kwargs))

    @classmethod
    def find_or_404(cls, **kwargs) -> Self:
        return get_object_or_404(cls.objects.filter(**kwargs))

    @classmethod
    def find_first(cls, order_by: Optional[list[str]] = None, **kwargs) -> Self | None:
        if not order_by:
            order_by = ["-id"]
        return cls.objects.filter(**kwargs).order_by(*order_by).first()

    @classmethod
    def one_or_404(cls, **kwargs) -> Self:
        return get_object_or_404(cls.objects.filter(**kwargs))

    @classmethod
    def first_or_404(cls, **kwargs) -> Self:
        return get_object_or_404(cls.objects.filter(**kwargs))

    def update_from_dict(self, obj: dict[str, Any], *fields: str):
        if not fields:
            for k, v in obj.items():
                setattr(self, k, v)
        else:
            for field in fields:
                setattr(self, field, obj[field])

    def partial_from_dict(self, obj: dict[str, Any], *fields: str):
        if not fields:
            for k, v in obj.items():
                setattr(self, k, v)
        else:
            for field in fields:
                setattr(self, field, obj[field])

    def incr(self, field, value=1):
        return self.__class__.objects.filter(id=self.id).update(**{field: F(field) + value})

    def decr(self, field, value=1):
        return self.__class__.objects.filter(id=self.id).update(**{field: F(field) - value})
