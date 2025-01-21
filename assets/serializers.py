from rest_framework import serializers
from .models import Asset, Tracker


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
