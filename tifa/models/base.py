from datetime import datetime
from functools import wraps

from sqlalchemy import Boolean, Column, DateTime
from sqlalchemy.exc import IntegrityError

from tifa.globals import db


class Model(db.Model):
    __abstract__ = True

    @classmethod
    def get(cls, id, exclude_deleted=True):
        query = db.session.query(cls)
        if hasattr(cls, "deleted") and exclude_deleted:
            query = query.filter_by(deleted=False)
        return query.filter_by(id=id).first()

    @classmethod
    def paginate(cls, page, per_page, order=None):
        return cls.query.order_by(order).paginate(page, per_page)

    @classmethod
    def all(cls):
        return cls.query.all()

    @classmethod
    def create(cls, _commit=True, **kwargs):
        obj = cls(**kwargs)
        obj.save(_commit)
        return obj

    def update(self, _commit=True, **kwargs):
        for k, v in kwargs.items():
            if hasattr(self, k):
                setattr(self, k, v)
        self.save(_commit)
        return self

    def delete(self, _hard=False, _commit=True):
        if hasattr(self, "deleted") and _hard is False:
            self.deleted = True  # noqa
            db.session.add(self)
        else:
            db.session.delete(self)
        if _commit:
            db.session.commit()

    def save(self, _commit=True):
        try:
            db.session.add(self)
            if _commit:
                db.session.commit()
        except IntegrityError:
            db.session.rollback()
            raise


class TimestampMixin(object):
    created_at = Column(DateTime(), default=datetime.now, comment="创建时间")
    updated_at = Column(
        DateTime(),
        default=datetime.now,
        onupdate=datetime.now,
        nullable=False,
        comment="更新时间",
    )

    deleted = Column(Boolean(), default=False, nullable=False, comment="是否删除")
