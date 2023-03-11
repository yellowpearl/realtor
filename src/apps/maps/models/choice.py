from django.db import models

from apps.maps.models.map import Map
from apps.maps.models.place import Place
from apps.maps.models.transport import TransportType
from apps.maps.models.travel_time import TravelTime


class Choice(models.Model):
    transport = models.ForeignKey(
        TransportType,
        on_delete=models.CASCADE,
        related_name="choices",
        verbose_name="Вид транспорта"
    )
    travel_time = models.ForeignKey(
        TravelTime,
        on_delete=models.CASCADE,
        related_name="choices",
        verbose_name="Время в пути"
    )
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name="choices",
        verbose_name="Место"
    )
    map = models.ForeignKey(
        Map,
        on_delete=models.CASCADE,
        related_name="choices",
        verbose_name="Карта",
        to_field="unique_id"
    )

    class Meta:
        verbose_name = "Выбор"
        verbose_name_plural = "Выборы"

    def __str__(self):
        return f"{self.pk}"
