import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship

from tifa.globals import Model


class PluginConfiguration(Model):
    __tablename__ = "plugin_configuration"
    __table_args__ = (sa.UniqueConstraint("identifier", "channel_id"),)

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(128), nullable=False)
    description = sa.Column(sa.Text, nullable=False)
    active = sa.Column(sa.Boolean, nullable=False)
    configuration = sa.Column(JSONB)
    identifier = sa.Column(sa.String(128), nullable=False)
    channel_id = sa.Column(
        sa.ForeignKey("channel_channel.id", deferrable=True, initially="DEFERRED"),
        index=True,
    )

    channel = relationship("ChannelChannel")
