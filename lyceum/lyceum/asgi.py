"""ASGI config for lyceum project"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lyceum.settings')

application = get_asgi_application()
