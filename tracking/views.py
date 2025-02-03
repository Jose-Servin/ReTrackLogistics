from rest_framework.viewsets import ModelViewSet
from .models import Tracker, SensorDataLog
from .serializers import (
    TrackerSerializer,
    SensorDataLogSerializer,
    CreateTrackerSerializer,
)


class TrackerViewSet(ModelViewSet):
    """
    A viewset for viewing and editing tracker instances.
    """

    queryset = Tracker.objects.all()
    serializer_class = TrackerSerializer

    def get_serializer_class(self):
        if self.request.method == "POST":
            return CreateTrackerSerializer
        return TrackerSerializer


class SensorDataLogViewSet(ModelViewSet):
    """
    A viewset for viewing and editing sensor data log instances.
    """

    queryset = SensorDataLog.objects.all()
    serializer_class = SensorDataLogSerializer
