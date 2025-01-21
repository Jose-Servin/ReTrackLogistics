from rest_framework_nested import routers
from . import views


router = routers.DefaultRouter()
router.register("clients", views.ClientViewSet, basename="clients")
router.register("contacts", views.ClientContactViewSet, basename="contacts")
router.register("assets", views.AssetViewSet, basename="assets")
router.register("trackers", views.TrackerViewSet, basename="trackers")

urlpatterns = router.urls
