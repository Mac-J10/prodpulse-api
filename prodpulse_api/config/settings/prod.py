# config/settings/prod.py

from .base import *

DEBUG = False

# Restrict allowed hosts via .env
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

ROOT_URLCONF = "config.urls"

# Security
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = env.int('SECURE_HSTS_SECONDS', default=3600)
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Email via SMTP
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_PORT = env.int('EMAIL_PORT')
EMAIL_USE_TLS = env.bool('EMAIL_USE_TLS', default=True)
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')

# Structured logging
LOGGING = {
    'version': 1,
    'formatters': {
        'json': {'()': 'pythonjsonlogger.jsonlogger.JsonFormatter'},
    },
    'handlers': {
        'stdout': {
            'class': 'logging.StreamHandler',
            'formatter': 'json',
        },
    },
    'root': {'handlers': ['stdout'], 'level': env('LOG_LEVEL', default='INFO')},
}