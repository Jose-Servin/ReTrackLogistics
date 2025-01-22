from rest_framework.viewsets import ModelViewSet
from .models import Client, Contact
from .serializers import (
    ClientSerializer,
    ContactSerializer,
    UpdateClientSerializer,
    UpdateContactSerializer,
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


class ContactViewSet(ModelViewSet):
    """
    A viewset for viewing and editing client contact instances.
    """

    http_method_names = ["get", "post", "patch", "delete", "head", "options"]

    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def get_serializer_class(self):
        if self.request.method == "PATCH":
            return UpdateContactSerializer
        return ContactSerializer
