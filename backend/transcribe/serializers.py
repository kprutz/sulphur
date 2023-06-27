# todo/serializers.py

from rest_framework import serializers
from .models import Transcribe
      
class TranscribeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Transcribe
    fields = ('id', 'request_time', 'file', 'transcription')
