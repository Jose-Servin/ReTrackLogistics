from rest_framework_nested import routers
from . import views


router = routers.DefaultRouter()
router.register("clients", views.ClientViewSet, basename="clients")
router.register("client-contacts", views.ClientContactViewSet)

urlpatterns = router.urls
