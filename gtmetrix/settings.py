"""
The following settings should be defined in your global settings
"""

try:
    from django.conf import settings
except ImportError:
    settings = {}


GTMETRIX_REST_API_URL = getattr(settings,
                                'GTMETRIX_REST_API_URL', 'https://gtmetrix.com/api/0.1/test')
