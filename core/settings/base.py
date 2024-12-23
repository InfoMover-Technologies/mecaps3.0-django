import os
from pathlib import Path

import certifi
from mongoengine import connect, disconnect
from pymongo import MongoClient

# Disconnect any existing connections first
disconnect()

# MongoDB Connection Settings
default_mongodb_url = 'mongodb+srv://shakir:mecaps@cluster0.zatib.mongodb.net/?retryWrites=true&w=majority'

# Try to establish connection
try:
    # First verify connection using pymongo
    client = MongoClient(
        os.getenv('MONGODB_URI', default_mongodb_url),
        ssl=True,
        tlsCAFile=certifi.where()
    )

    # Test the connection
    client.server_info()

    # If successful, connect mongoengine
    connect(
        db='training',
        host=os.getenv('MONGODB_URI', default_mongodb_url),
        ssl=True,
        tlsCAFile=certifi.where(),
        alias='default'
    )
    print("MongoDB connection successful!")
except Exception as e:
    print(f"MongoDB connection failed: {str(e)}")
    raise



SECRET_KEY = 'django-insecure-your-secret-key-here'  # Change this in production

DJANGO_APPS = [
    # Removed django.contrib.admin
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

LOCAL_APPS = [
    'apps.customers',
]

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS
# INSTALLED_APPS = DJANGO_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

BASE_DIR = Path(__file__).resolve().parent.parent.parent

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # os.path.join(BASE_DIR, 'apps', 'customers', 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Rest Framework settings
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [],  # No authentication required
    'DEFAULT_AUTHENTICATION_CLASSES': [],  # No authentication required
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}

# API Documentation settings
SPECTACULAR_SETTINGS = {
    'TITLE': 'Marketing Platform API',
    'DESCRIPTION': 'API documentation for Marketing Platform',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
}

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CORS settings
CORS_ALLOW_ALL_ORIGINS = False  # Don't allow all origins
CORS_ALLOWED_ORIGINS = [
    "http://app-dev.hiretalentt.localhost:3000",  # Your NextJS app
    "https://app.hiretalentt.com",  # Your NextJS app
    "https://hiretalentt.com",  # Your NextJS app
    "https://www.hiretalentt.com",  # Your NextJS app
    "http://localhost:3000",
]

CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'X-Campaign-ID',
    'x-campaign-id',
    'x-csrftoken',
    'x-requested-with',
    'ngrok-skip-browser-warning',  # Add this for your ngrok header
]

CORS_EXPOSE_HEADERS = ['Content-Type', 'X-CSRFToken']
CORS_ALLOW_CREDENTIALS = True  # If you're using credentials in requests
