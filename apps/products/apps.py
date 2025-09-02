# products/apps.py
from django.apps import AppConfig

class ProductCatalogConfig(AppConfig):
    name  = "prodpulse_api.apps.products"  # full Python path to the app
    label = "product_catalog"        # must be unique across all apps