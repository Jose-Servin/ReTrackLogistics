from rest_framework.routers import DefaultRouter
from registry.views import ClientViewSet, ContactViewSet
from inventory.views import AssetViewSet
from tracking.views import TrackerViewSet, SensorDataLogViewSet

# Create a DRF DefaultRouter instance
router = DefaultRouter()

# Register routes for all apps
router.register("clients", ClientViewSet, basename="clients")
router.register("contacts", ContactViewSet, basename="contacts")
router.register("assets", AssetViewSet, basename="assets")
router.register("devices", TrackerViewSet, basename="trackers")
router.register("sensor-logs", SensorDataLogViewSet, basename="sensor_logs")

# Export the router's URLs
urlpatterns = router.urls
