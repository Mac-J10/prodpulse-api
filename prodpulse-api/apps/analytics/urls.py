from django.urls import path
from .views import (
     stripe_usage,
    product_views,
    sales_estimate,
)

urlpatterns = [
    path('stripe/usage/', stripe_usage),
    path('sales/estimate/', sales_estimate),
    path('product/views/', product_views),  # Assuming you have a view for product views
]