# apps/api/urls.py

from django.urls import path, include

# Simplified for initial setup
from django.http import JsonResponse
from django.urls import path

def api_health_check(request):
    return JsonResponse({"status": "ok", "message": "ProdPulse API is running"})

urlpatterns = [
    path("auth/", include("authentication.urls")),
    path("notifications/", include("notifications.urls")),
    path("orders/", include("orders.urls")),
    path("products/", include("products.urls")),
    path("pulses/", include("pulses.urls")),
    path("users/", include("users.urls")),

    path("", api_health_check, name="api_health_check"),
]
