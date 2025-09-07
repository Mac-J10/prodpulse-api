# apps/api/urls.py

from django.urls import path, include

# Simplified for initial setup
from django.http import JsonResponse

def api_health_check(request):
    return JsonResponse({"status": "ok", "message": "ProdPulse API is running"})

urlpatterns = [
    path("analytics/", include("apps.analytics.urls")),
    path("notifications/", include("apps.notifications.urls")),
    path("orders/", include("apps.orders.urls")),
    path("products/", include("apps.products.urls")),
    path("pulses/", include("apps.pulses.urls")),
    path("users/", include("apps.users.urls")),

    path("", api_health_check, name="api_health_check"),
    path("authentication/", include("apps.authentication.urls")),
]
