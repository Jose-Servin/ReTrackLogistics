from rest_framework import serializers
from .models import Client, Contact


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
        """
        Check that the phone number is exactly 10 digits.
        """
        if not value.isdigit() or len(value) != 10:
            raise serializers.ValidationError(
                "The phone number must be exactly 10 digits."
            )
        return value


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
        """
        Check that the phone number is exactly 10 digits.
        """
        if not value.isdigit() or len(value) != 10:
            raise serializers.ValidationError(
                "The phone number must be exactly 10 digits."
            )
        return value
