import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship

from tifa.globals import Model


class PageType(Model):
    __tablename__ = "page_type"
    __table_args__ = (sa.Index("page_type_name_slug", "name", "slug"),)

    id = sa.Column(sa.Integer, primary_key=True)
    metadata_public = sa.Column(JSONB, index=True)
    metadata_private = sa.Column(JSONB, index=True)
    name = sa.Column(sa.String(250), nullable=False)
    slug = sa.Column(sa.String(255), nullable=False, unique=True)


class Page(Model):
    __tablename__ = "page"
    __table_args__ = (sa.Index("page_title_slug", "title", "slug"),)

    id = sa.Column(sa.Integer, primary_key=True)
    slug = sa.Column(sa.String(255), nullable=False, unique=True)
    title = sa.Column(sa.String(250), nullable=False)
    content = sa.Column(JSONB)
    created = sa.Column(sa.DateTime, nullable=False)
    is_published = sa.Column(sa.Boolean, nullable=False)
    publication_date = sa.Column(sa.Date)
    seo_description = sa.Column(sa.String(300))
    seo_title = sa.Column(sa.String(70))
    metadata_public = sa.Column(JSONB, index=True)
    metadata_private = sa.Column(JSONB, index=True)
    page_type_id = sa.Column(sa.ForeignKey("page_type.id"), nullable=False)
    page_type = relationship(PageType)


class PageTranslation(Model):
    __tablename__ = "page_translation"
    __table_args__ = (sa.UniqueConstraint("language_code", "page_id"),)

    id = sa.Column(sa.Integer, primary_key=True)
    seo_title = sa.Column(sa.String(70))
    seo_description = sa.Column(sa.String(300))
    language_code = sa.Column(sa.String(10), nullable=False)
    title = sa.Column(sa.String(255))
    content = sa.Column(JSONB)
    page_id = sa.Column(
        sa.ForeignKey("page.id"),
        nullable=False,
    )
    page = relationship(Page)
