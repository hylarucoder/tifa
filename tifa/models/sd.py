from django.db import models

from tifa.models.base import Model


class SdTopic(Model):
    class Meta:
        db_table = "sd_topic"

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    position = models.IntegerField(db_index=True, default=999)

    def __str__(self):
        return f"<#{self.id}> - {self.name}"


class SdActivity(Model):
    class Meta:
        db_table = "sd_activity"

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    topic = models.ForeignKey(SdTopic, on_delete=models.PROTECT, null=True)
    position = models.IntegerField(db_index=True, default=999)

    def __str__(self):
        return f"<#{self.id}> - {self.name}"
