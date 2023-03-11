from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Место")

    def __str__(self):
        return self.name
