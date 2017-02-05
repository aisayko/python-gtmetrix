"""Utilities to support testing."""
from gtmetrix import settings

G_saved_settings = None

def save_settings():
    global G_saved_settings
    G_saved_settings = (settings.GTMETRIX_REST_API_EMAIL,
             settings.GTMETRIX_REST_API_KEY,
             settings.GTMETRIX_REST_API_URL)


def restore_settings():
    settings.GTMETRIX_REST_API_EMAIL,   \
    settings.GTMETRIX_REST_API_KEY,     \
    settings.GTMETRIX_REST_API_URL = G_saved_settings


def email_is_valid(email):
    """Check for valid email address.  Stubbed out for now"""
    return email != None


def api_key_is_valid(key):
    """Check for valid API key.  Stubbed out for now."""
    return key != None


def api_url_is_valid(url):
    """Ensure that it's set to what it was when settings.py was written.

    Prevents e.g. testing api/0.1 calls against api/1.0 if it ever comes
    out."""
    return (settings.GTMETRIX_REST_API_URL ==
            'https://gtmetrix.com/api/0.1/test')
