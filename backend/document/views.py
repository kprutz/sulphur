from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import (
    CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
)
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response

from .serializers import DocumentSerializer
from .models import Document


class DocumentViewSet(GenericViewSet,  # generic view functionality
                     CreateModelMixin,  # handles POSTs
                     RetrieveModelMixin,  # handles GETs
                     UpdateModelMixin,  # handles PUTs and PATCHes
                     ListModelMixin):
  serializer_class = DocumentSerializer
  queryset = Document.objects.all()
