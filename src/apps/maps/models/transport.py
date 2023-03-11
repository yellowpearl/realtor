from django.db import models


class TransportType(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Вид транспорта")

    def __str__(self):
        return self.name
