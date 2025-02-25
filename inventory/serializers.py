from rest_framework import serializers
from .models import Asset


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


class UpdateAssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = ["name", "description", "industry", "owner"]
