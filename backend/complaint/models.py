from django.db import models

from sensors.models import Sensors


class Complaint(models.Model):
    sensor = Sensors()
    file_date = models.DateTimeField(auto_now=True)
    submission_data = models.JSONField()
    is_manual_run = models.BooleanField()
