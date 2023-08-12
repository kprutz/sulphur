from django.contrib import admin
from .models import Complaint


class ComplaintAdmin(admin.ModelAdmin):
  list_display = ('id', 'sensor', 'submission_data', 'file_date', 'is_manual_run')

admin.site.register(Complaint, ComplaintAdmin)
