
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
DJANGO_ALLOW_ASYNC_UNSAFE = True  # Only for development

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*']

# CORS settings for development
CORS_ALLOWED_ORIGINS += [
    "http://127.0.0.1:3000",
    "http://localhost:3000",
    "http://app-dev.hiretalentt.localhost:3000",
]

# For development, you might want to allow all origins (optional, but not recommended)
# CORS_ALLOW_ALL_ORIGINS = True

# Email backend for development
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Set Redis cache location for development
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'SOCKET_CONNECT_TIMEOUT': 5,
            'SOCKET_TIMEOUT': 5,
            'RETRY_ON_TIMEOUT': True,
            'CONNECTION_POOL_KWARGS': {'max_connections': 100}
        }
    }
}

# Disable some production security settings in development
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False


# Configure DRF to be more permissive in development
REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES'] += [
    'rest_framework.authentication.BasicAuthentication',
]

# Rate limiting settings for development
RATELIMIT_ENABLE = True
RATELIMIT_USE_CACHE = 'default'
RATELIMIT_DEFAULT_LIMIT = '1000/hour'  # More permissive in development

# Django Debug Toolbar settings
# DEBUG_TOOLBAR_CONFIG = {
#     'SHOW_TEMPLATE_CONTEXT': True,
#     'SHOW_TOOLBAR_CALLBACK': lambda request: True,
# }

# if DEBUG:
#     try:
#         import debug_toolbar
#         INSTALLED_APPS += ['debug_toolbar']
#         MIDDLEWARE = [
#                          'debug_toolbar.middleware.DebugToolbarMiddleware',
#                      ] + MIDDLEWARE
#         INTERNAL_IPS = ['127.0.0.1']
#     except ImportError:
#         pass  # debug_toolbar not installed

# File upload settings for development
FILE_UPLOAD_MAX_MEMORY_SIZE = 10 * 1024 * 1024  # 10MB
DATA_UPLOAD_MAX_MEMORY_SIZE = 10 * 1024 * 1024  # 10MB

# Development-specific cache timeouts
CACHE_MIDDLEWARE_SECONDS = 0  # Disable page caching in development

# API Documentation settings
SPECTACULAR_SETTINGS['SERVE_PUBLIC'] = True  # Make API docs accessible without authentication in development

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        '': {  # Root logger
            'handlers': ['console'],
            'level': 'INFO',
        }
    },
}

