import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship

from tifa.globals import Model
from tifa.models.utils import TimestampMixin


class CsvExportFile(TimestampMixin, Model):
    __tablename__ = "csv_export_file"

    id = sa.Column(sa.Integer, primary_key=True)
    status = sa.Column(sa.String(50), nullable=False)
    created_at = sa.Column(sa.DateTime, nullable=False)
    updated_at = sa.Column(sa.DateTime, nullable=False)
    content_file = sa.Column(sa.String(100))
    app_id = sa.Column(
        sa.ForeignKey("app_app.id", deferrable=True, initially="DEFERRED"), index=True
    )
    user_id = sa.Column(
        sa.ForeignKey("account_user.id", deferrable=True, initially="DEFERRED"),
        index=True,
    )
    message = sa.Column(sa.String(255))

    app = relationship("AppApp")
    user = relationship("AccountUser")


class CsvExportEvent(Model):
    __tablename__ = "csv_export_event"

    id = sa.Column(sa.Integer, primary_key=True)
    date = sa.Column(sa.DateTime(True), nullable=False)
    type = sa.Column(sa.String(255), nullable=False)
    parameters = sa.Column(JSONB, nullable=False)
    app_id = sa.Column(
        sa.ForeignKey("app_app.id", deferrable=True, initially="DEFERRED"), index=True
    )
    export_file_id = sa.Column(
        sa.ForeignKey("csv_exportfile.id", deferrable=True, initially="DEFERRED"),
        nullable=False,
        index=True,
    )
    user_id = sa.Column(
        sa.ForeignKey("account_user.id", deferrable=True, initially="DEFERRED"),
        index=True,
    )

    app = relationship("AppApp")
    export_file = relationship("CsvExportfile")
    user = relationship("AccountUser")
