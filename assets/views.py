from rest_framework.viewsets import ModelViewSet
from .models import Asset, Tracker
from .serializers import AssetSerializer, TrackerSerializer


class AssetViewSet(ModelViewSet):
    """
    A viewset for viewing and editing asset instances.
    """

    http_method_names = ["get", "post", "patch", "delete", "head", "options"]

    queryset = Asset.objects.all()
    serializer_class = AssetSerializer


class TrackerViewSet(ModelViewSet):
    """
    A viewset for viewing and editing tracker instances.
    """

    http_method_names = ["get", "post", "patch", "delete", "head", "options"]

    queryset = Tracker.objects.all()
    serializer_class = TrackerSerializer
