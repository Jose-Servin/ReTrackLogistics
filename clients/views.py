from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Client, ClientContact
from .serializers import ClientSerializer, ClientContactSerializer


class ClientViewSet(ModelViewSet):
    """
    A viewset for viewing and editing client instances.
    """

    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientContactViewSet(ModelViewSet):
    """
    A viewset for viewing and editing client contact instances.
    """

    queryset = ClientContact.objects.all()
    serializer_class = ClientContactSerializer
