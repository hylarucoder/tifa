import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship

from tifa.globals import Model
from tifa.models.app import App
from tifa.models.user import User
from tifa.models.utils import TimestampMixin


class CsvExportFile(TimestampMixin, Model):
    __tablename__ = "csv_export_file"

    id = sa.Column(sa.Integer, primary_key=True)
    status = sa.Column(sa.String(50), nullable=False)
    created_at = sa.Column(sa.DateTime, nullable=False)
    updated_at = sa.Column(sa.DateTime, nullable=False)
    content_file = sa.Column(sa.String(100))
    app_id = sa.Column(sa.ForeignKey("app.id"), index=True)
    app = relationship(App)
    user_id = sa.Column(sa.ForeignKey("user.id"), )
    user = relationship(User)
    message = sa.Column(sa.String(255))


class CsvExportEvent(Model):
    __tablename__ = "csv_export_event"

    id = sa.Column(sa.Integer, primary_key=True)
    date = sa.Column(sa.DateTime, nullable=False)
    type = sa.Column(sa.String(255), nullable=False)
    parameters = sa.Column(JSONB, nullable=False)
    app_id = sa.Column(sa.ForeignKey("app.id"))
    app = relationship(App)
    export_file_id = sa.Column(sa.ForeignKey("csv_export_file.id"), nullable=False, )
    user_id = sa.Column(sa.ForeignKey("user.id"))
    user = relationship(User)
    export_file = relationship(CsvExportFile)
