"""
WSGI config for marketing_platform project.
"""

import os

from django.core.wsgi import get_wsgi_application

# Default to development settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings.development')
application = get_wsgi_application()