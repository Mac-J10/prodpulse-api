# config/__init__.py
import os
from .celery_app import app as celery_app

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.dev")

__all__ = ("celery_app",)