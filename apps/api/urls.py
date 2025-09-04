# apps/api/urls.py

from django.urls import path, include

# Simplified for initial setup
from django.http import JsonResponse
from django.urls import path

def api_health_check(request):
    return JsonResponse({"status": "ok", "message": "ProdPulse API is running"})

urlpatterns = [
    path("", api_health_check, name="api_health_check"),
]
