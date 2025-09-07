from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static
from django.http import JsonResponse

def api_root(request):
    return JsonResponse({
        "message": "Welcome to ProdPulse API",
        "version": "0.1.0",
        "endpoints": {
            "health": "/prod/",
            "admin": "/admin/",
            "api_auth": "/api/auth/",
            "token_obtain": "/api/token/",
            "token_refresh": "/api/token/refresh/"
        }
    })

urlpatterns = [
    path("prod/", api_root, name="api_root"),
    path("admin/", admin.site.urls),
    path("api/", include("apps.api.urls")),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/auth/", include("rest_framework.urls")),
    path("analytics/", include("apps.analytics.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)