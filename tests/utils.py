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
