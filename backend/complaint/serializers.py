from rest_framework import serializers
from .models import Complaint

class ComplaintSerializer(serializers.ModelSerializer):
  class Meta:
    model = Complaint
    fields = ('id', 'sensor', 'submission_data', 'file_date', 'is_manual_run')
