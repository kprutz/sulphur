from rest_framework import viewsets

from .serializers import ComplaintSerializer
from .models import Complaint

class ComplaintView(viewsets.ModelViewSet):
  queryset = Complaint.objects.all()
  serializer_class = ComplaintSerializer
