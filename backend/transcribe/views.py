from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import (
    CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
)
from rest_framework.viewsets import GenericViewSet    
from rest_framework.response import Response

from .serializers import TranscribeSerializer     
from .models import Transcribe                   
from .transcribe import transcribeAudioFile


class TranscribeViewSet(GenericViewSet,  # generic view functionality
                     CreateModelMixin,  # handles POSTs
                     RetrieveModelMixin,  # handles GETs
                     UpdateModelMixin,  # handles PUTs and PATCHes
                     ListModelMixin): 
  serializer_class = TranscribeSerializer         
  queryset = Transcribe.objects.all()

  @action(methods=['post'], detail=False)
  def transcribeAudio(self, request):
    data = transcribeAudioFile(self, request.data.get('file'))
    return Response(data, status=status.HTTP_200_OK)
