from django.contrib import admin
from .models import Transcribe 
    
class TranscribeAdmin(admin.ModelAdmin): 
  list_display = ('id', 'user', 'request_time') 
        
admin.site.register(Transcribe, TranscribeAdmin)
