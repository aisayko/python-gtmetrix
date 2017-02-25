"""
The following settings should be defined in your global settings
"""
import os

GTMETRIX_REST_API_URL = 'https://gtmetrix.com/api/0.1/test'

# API calls will default to using these if an explicit value is not
# passed to GTmetrixInterface()
GTMETRIX_REST_API_EMAIL = os.getenv('GTMETRIX_REST_API_EMAIL', None)
GTMETRIX_REST_API_KEY = os.getenv('GTMETRIX_REST_API_KEY', None)
