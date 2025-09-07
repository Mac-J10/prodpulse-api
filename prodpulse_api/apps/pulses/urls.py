from rest_framework.routers import DefaultRouter
from .views import PulseViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r"", PulseViewSet, basename="pulse")

urlpatterns = [
    path("", include(router.urls)),
]