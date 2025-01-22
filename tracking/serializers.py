from rest_framework import serializers
from .models import Tracker, SensorDataLog
from inventory.models import Asset


class TrackerSerializer(serializers.ModelSerializer):
    # Serializing related Asset model's fields as needed, for example, just the id
    asset_id = serializers.PrimaryKeyRelatedField(
        queryset=Asset.objects.all(), source="asset"
    )

    class Meta:
        model = Tracker
        fields = [
            "id",
            "name",
            "description",
            "tracker_type",
            "asset_id",
            "created_at",
            "updated_at",
            "status",
        ]


class SensorDataLogSerializer(serializers.ModelSerializer):
    tracker_id = serializers.PrimaryKeyRelatedField(
        queryset=Tracker.objects.all(), source="tracker"
    )

    class Meta:
        model = SensorDataLog
        fields = ["id", "tracker_id", "timestamp", "sensor_data"]
