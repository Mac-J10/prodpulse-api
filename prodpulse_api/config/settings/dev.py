# config/settings/dev.py

from .base import *

DEBUG = True

# Allow all hosts for dev
ALLOWED_HOSTS = ['*']

ROOT_URLCONF = "config.urls"

# Use local email backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Logging for dev
LOGGING = {
    'version': 1,
    'handlers': {'console': {'class': 'logging.StreamHandler'}},
    'root': {'handlers': ['console'], 'level': 'DEBUG'},
}