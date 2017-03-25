"""
The following settings should be defined in your global settings
"""
import os

GTMETRIX_REST_API_URL = 'https://gtmetrix.com/api/0.1/test'

# API calls will default to using these if an explicit value is not
# passed to GTmetrixInterface()
GTMETRIX_REST_API_EMAIL = os.getenv('GTMETRIX_REST_API_EMAIL', None)
GTMETRIX_REST_API_KEY = os.getenv('GTMETRIX_REST_API_KEY', None)

# TODO: when validation is tighter, these might not pass.  The tests
#       will fail then, just like they're supposed to.
good_email = "example@example.com"
good_apikey = "abcdef4d91234542222d709124eceaaa"
good_url = GTMETRIX_REST_API_URL

def set_known_good_settings():
    """Get known good settings so we have a valid starting point for tests"""
    global  GTMETRIX_REST_API_KEY, \
            GTMETRIX_REST_API_EMAIL, \
            GTMETRIX_REST_API_URL

    GTMETRIX_REST_API_EMAIL = good_email
    GTMETRIX_REST_API_KEY = good_apikey
    GTMETRIX_REST_API_URL = good_url
