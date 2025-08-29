from rest_framework.routers import DefaultRouter
from .views import PulseViewSet

router = DefaultRouter()
router.register("metrics", PulseViewSet, basename="metric")

urlpatterns = router.urls
