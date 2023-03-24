import uuid

from django.contrib.auth.models import User
from django.db import models


class Map(models.Model):
    unique_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name="Идентификатор"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Пользователь", related_name="maps"
    )
    is_paid = models.BooleanField(default=False, verbose_name="Оплачено?")

    class Meta:
        verbose_name = "Карта"
        verbose_name_plural = "Карты"

    def __str__(self):
        return f"{self.unique_id}"
