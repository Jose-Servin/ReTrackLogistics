from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from inventory.models import Asset
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

    queryset = Client.objects.all().order_by("id")

    def get_serializer_class(self):
        if self.request.method == "PATCH":
            return UpdateClientSerializer
        return ClientSerializer

    def destroy(self, request, *args, **kwargs):
        client_id = self.kwargs["pk"]
        contact_count = Contact.objects.filter(client_id=client_id).count()
        asset_count = Asset.objects.filter(owner_id=client_id).count()

        if contact_count > 0 and asset_count > 0:
            error_message = (
                f"The client cannot be deleted because it has {contact_count} associated contact(s) "
                f"and {asset_count} associated asset(s). Please remove these records before deleting the client."
            )
        elif contact_count > 0:
            error_message = (
                f"The client cannot be deleted because it has {contact_count} associated contact(s). "
                "Please remove them before deleting the client."
            )
        elif asset_count > 0:
            error_message = (
                f"The client cannot be deleted because it has {asset_count} associated asset(s). "
                "Please remove them before deleting the client."
            )

        if contact_count > 0 or asset_count > 0:
            return Response(
                {"error": error_message},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return super().destroy(request, *args, **kwargs)


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
