# apps/authentication/apps.py

from django.apps import AppConfig

class AuthenticationConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.authentication"

    def ready(self):
        # Only here do we import things that rely on Django being fully loaded
        from . import signals