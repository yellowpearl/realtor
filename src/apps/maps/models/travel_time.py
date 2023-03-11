from django.db import models


class TravelTime(models.Model):
    time = models.SmallIntegerField(default=10, verbose_name="Время в пути")

    def __str__(self):
        return f"{self.time} минут"
