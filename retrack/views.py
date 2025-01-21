from rest_framework.viewsets import ModelViewSet
from .models import Client, ClientContact, Asset, Tracker
from .serializers import (
    ClientSerializer,
    ClientContactSerializer,
    UpdateClientSerializer,
    UpdateClientContactSerializer,
    AssetSerializer,
    TrackerSerializer,
)


class ClientViewSet(ModelViewSet):
    """
    A viewset for viewing and editing client instances.
    """

    http_method_names = ["get", "post", "patch", "delete", "head", "options"]

    queryset = Client.objects.all()

    def get_serializer_class(self):
        if self.request.method == "PATCH":
            return UpdateClientSerializer
        return ClientSerializer


class ClientContactViewSet(ModelViewSet):
    """
    A viewset for viewing and editing client contact instances.
    """

    http_method_names = ["get", "post", "patch", "delete", "head", "options"]

    queryset = ClientContact.objects.all()
    serializer_class = ClientContactSerializer

    def get_serializer_class(self):
        if self.request.method == "PATCH":
            return UpdateClientContactSerializer
        return ClientContactSerializer


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
