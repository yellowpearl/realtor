from django.contrib.auth.models import User
from django.db import models


class Map(models.Model):
    unique_id = models.CharField(max_length=255, verbose_name="Идентификатор")

    class Meta:
        verbose_name = "Карта"
        verbose_name_plural = "Карты"

    def __str__(self):
        return f"{self.unique_id}"


class TravelTime(models.Model):
    time = models.SmallIntegerField(default=10, verbose_name="Время в пути")

    def __str__(self):
        return f"{self.time} минут"


class TransportType(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Вид транспорта")

    def __str__(self):
        return self.name


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
    map = models.ForeignKey(
        Map,
        on_delete=models.CASCADE,
        related_name="choices",
        verbose_name="Карта",
        default=None,
        blank=True
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Пользователь", related_name="choices"
    )

    class Meta:
        verbose_name = "Выбор"
        verbose_name_plural = "Выборы"

    def __str__(self):
        return f"{self.pk}"
