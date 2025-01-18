from rest_framework_nested import routers
from . import views


router = routers.DefaultRouter()
router.register("clients", views.ClientViewSet)
router.register("clients-contacts", views.ClientContactViewSet)

urlpatterns = router.urls
