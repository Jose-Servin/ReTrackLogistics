from rest_framework import serializers
from .models import Client, ClientContact


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = [
            "id",
            "name",
            "email",
            "phone_number",
            "address",
            "city",
            "state",
            "zipcode",
            "country",
        ]


class ClientContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientContact
        fields = [
            "id",
            "client",
            "first_name",
            "last_name",
            "email",
            "phone_number",
        ]
