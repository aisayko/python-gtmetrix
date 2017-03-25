# -*- coding: utf-8 -*-
"""Utilities to support testing."""
from gtmetrix import settings

G_saved_settings = None

# Change this when the test URL changes
G_test_valid_url = 'https://gtmetrix.com/api/0.1/test'

def save_settings():
    global G_saved_settings
    G_saved_settings = (settings.GTMETRIX_REST_API_EMAIL,
             settings.GTMETRIX_REST_API_KEY,
             settings.GTMETRIX_REST_API_URL)


def restore_settings():
    settings.GTMETRIX_REST_API_EMAIL,   \
    settings.GTMETRIX_REST_API_KEY,     \
    settings.GTMETRIX_REST_API_URL = G_saved_settings


