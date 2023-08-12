from django.db import models


class Sensors(models.Model):
    sensor_index = models.IntegerField()
    last_complainer_run = models.DateTimeField(auto_now=False)
