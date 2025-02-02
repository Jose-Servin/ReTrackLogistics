from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import Asset
from .serializers import AssetSerializer, UpdateAssetSerializer
from tracking.models import Tracker


class AssetViewSet(ModelViewSet):
    """
    A viewset for viewing and editing asset instances.
    """

    http_method_names = ["get", "post", "patch", "delete", "head", "options"]

    queryset = Asset.objects.all()
    serializer_class = AssetSerializer

    def get_serializer_class(self):
        if self.request.method == "PATCH":
            return UpdateAssetSerializer
        return AssetSerializer

    def destroy(self, request, *args, **kwargs):
        asset_id = self.kwargs["pk"]
        tracker_count = Tracker.objects.filter(asset_id=asset_id).count()
        if tracker_count > 0:
            error_message = (
                f"The asset cannot be deleted because it has {tracker_count} associated tracker(s). "
                "Please remove them before deleting the asset."
            )
            return Response(
                {"error": error_message},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return super().destroy(request, *args, **kwargs)
