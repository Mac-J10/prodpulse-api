# config/settings/base.py

import os
import environ
from django.db import models

STRIPE_API_KEY = os.getenv("STRIPE_API_KEY", "")

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Load .env file
env = environ.Env()
environ.Env.read_env(env_file=os.path.join(os.path.dirname(__file__), '../../.env'))

# Set the default Django settings module for the 'django' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

# Core settings
SECRET_KEY = env('SECRET_KEY')
DEBUG = env.bool('DEBUG', default=False)
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=[])

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.analytics',
    'apps.notifications',
    'apps.users',
    'apps.authentication',
    'apps.products',
    'apps.orders',
    'apps.pulses',
    'django_extensions',
    'rest_framework',
    'rest_framework_simplejwt',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {'context_processors': [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
        ]},
    },
]

WSGI_APPLICATION = 'config.wsgi.application'
ASGI_APPLICATION = 'config.asgi.application'

# Default database; override in dev.py or prod.py
DATABASES = {'default': env.db_url('DATABASE_URL', default='sqlite:///db.sqlite3')}

# Static and media
STATIC_URL = '/static/'
MEDIA_URL = '/media/'