from rest_framework.viewsets import ModelViewSet
from .models import Tracker, SensorDataLog
from .serializers import TrackerSerializer, SensorDataLogSerializer


class TrackerViewSet(ModelViewSet):
    """
    A viewset for viewing and editing tracker instances.
    """

    queryset = Tracker.objects.all()
    serializer_class = TrackerSerializer


class SensorDataLogViewSet(ModelViewSet):
    """
    A viewset for viewing and editing sensor data log instances.
    """

    queryset = SensorDataLog.objects.all()
    serializer_class = SensorDataLogSerializer
