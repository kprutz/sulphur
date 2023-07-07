from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response

from .serializers import SensorsSerializer
from .models import Sensors
from .purpleutils import PurpleUtils
from .complainer import Complainer

class SensorsViewSet(GenericViewSet):
  serializer_class = SensorsSerializer

  @action(methods=['post'], detail=False)
  def getSensorsData(self, request):
      sensor_indices = request.GET.get('ids').split(',')
      data = {}
      for index in sensor_indices:
          sensor_data = PurpleUtils.getSensorHistory_pastWeek(index)
          sensor_data = sorted(sensor_data)
          data[index] = [{'timestamp': +s[0], 'pm25': s[1]} for s in sensor_data]
      return Response(data, status=status.HTTP_200_OK)

  @action(methods=['get'], detail=False)
  def runCronJob(self):
      Complainer.complain()
      return Response({}, status=status.HTTP_200_OK)
