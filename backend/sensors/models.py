from django.db import models


class Sensors(models.Model):
    sensor_index = models.IntegerField()
    last_complainer_run = models.DateTimeField(auto_now=False)
    def __str__(self):
        return "Sensor {} --- cron job was last run at {}".format(self.sensor_index, self.last_complainer_run)
