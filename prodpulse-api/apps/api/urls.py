# apps/api/urls.py

from django.urls import path, include

urlpatterns = [
    path('auth/', include('apps.authentication.urls')),
    path('products/', include('apps.products.urls')),
    path('metrics/', include('apps.pulses.urls')),
]