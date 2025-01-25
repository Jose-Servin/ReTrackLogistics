from rest_framework import serializers
from .models import Client, Contact
from core.validators import validate_phone_number


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


class UpdateClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ["phone_number"]

    def validate_phone_number(self, value):
        return validate_phone_number(value)


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = [
            "id",
            "client",
            "first_name",
            "last_name",
            "email",
            "phone_number",
        ]


class UpdateContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = [
            "first_name",
            "last_name",
            "email",
            "phone_number",
        ]

    def validate_phone_number(self, value):
        return validate_phone_number(value)
