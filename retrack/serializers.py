from rest_framework import serializers
from .models import Client, ClientContact, Asset, Tracker


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


class UpdateClientContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientContact
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


class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = [
            "id",
            "name",
            "description",
            "industry",
            "owner",
            "created_at",
            "updated_at",
        ]


class TrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tracker
        fields = [
            "id",
            "name",
            "description",
            "asset",
            "created_at",
            "updated_at",
            "sensor_data",
            "status",
        ]
