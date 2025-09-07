from django.apps import AppConfig

class ProductsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.products"

    def ready(self):
        # Optional: preload product metadata or signal handlers
        pass