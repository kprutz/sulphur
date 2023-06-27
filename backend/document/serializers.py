# todo/serializers.py

from rest_framework import serializers
from .models import Document

class DocumentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Document
    fields = ('id', 'edms_id', 'ai', 'dtype', 'dsubtype', 'datetime', 'entry_datetime', 'description', 'media', 'dfunction', 'num_pages', 'converted_text')
