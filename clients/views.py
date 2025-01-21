from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import Client, ClientContact
from .serializers import (
    ClientSerializer,
    ClientContactSerializer,
    UpdateClientSerializer,
    UpdateClientContactSerializer,
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
