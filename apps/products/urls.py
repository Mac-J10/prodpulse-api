from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet, ProductListView, ProductDetailView
from django.urls import path, include

router = DefaultRouter()
router.register("categories", CategoryViewSet, basename="category")
router.register("products", ProductViewSet, basename="product")

urlpatterns = [
    path("", include(router.urls)),
    
    path("", ProductListView.as_view(), name="product-list"),
    path("<int:pk>/", ProductDetailView.as_view(), name="product-detail"),

]
