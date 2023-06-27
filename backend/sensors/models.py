from django.db import models


class Sensors(models.Model):
    sensor_index = models.IntegerField()
    def __str__(self):
        return "it's a sensor"
