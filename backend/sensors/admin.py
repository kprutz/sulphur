from django.contrib import admin
from .models import Sensors


class SensorsAdmin(admin.ModelAdmin):
  list_display = ('id', 'sensor_index', 'last_complainer_run')

admin.site.register(Sensors, SensorsAdmin)
