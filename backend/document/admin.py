from django.contrib import admin
from .models import Document

class DocumentAdmin(admin.ModelAdmin):
  list_display = ('id', 'edms_id', 'ai', 'dtype', 'dsubtype', 'datetime', 'entry_datetime', 'description', 'media', 'dfunction', 'num_pages', 'converted_text')

admin.site.register(Document, DocumentAdmin)
