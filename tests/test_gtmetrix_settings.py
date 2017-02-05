"""

GTmetrix Python API

Settings Tests

This runs three tests:

    1> TestGTmetrixSettingsSuccess

        Runs with forced GOOD values.  Quick failure if quickie validations
        are not working properly.

    2> TestGTmetrixSettingsFailure

        Runs with forced BAD values.  Non-failure is a problem.

    3> TestGTmetrixSettings

        Runs with inherited, unmodified environment.  Succeeds if further
        tests will be able to run i.e. email, api key, and URL for GTmetrix
        are all set to some values.

        The success and failure tests just set a good/bad environment
        becalling calling

    TODO: do validation on email format and API key to prevent bogus
          formats e.g. invalid email

"""
import os
from unittest import TestCase

import pytest
from pytest import raises

from gtmetrix import settings
from gtmetrix.interface import GTmetrixInterface
from gtmetrix.exceptions import GTmetrixMissingEmailOrAPIKey
from .utils import save_settings, restore_settings

class TestGTmetrixSettingsSuccess(TestCase):
    """Tests that things succeed when they're supposed to.

    All tests should pass without exception.
    """
    @classmethod
    def setUpClass(cls):
        """Ensure that our settings DO contain valid values."""
        # save 'settings' module's variables
        save_settings()

        # TODO: enforce real valid values e.g. valid email
        settings.GTMETRIX_REST_API_EMAIL = "email, not testing format"
        settings.GTMETRIX_REST_API_KEY = "a fake api key"
        # GTMETRIX_REST_API_URL has to be set in settings.py
        assert(settings.GTMETRIX_REST_API_URL)  # fail if not set!
        cls.testSettings = TestGTmetrixSettings()

    def test_email_OK(self):
        self.testSettings.test_email_has_value()

    def test_api_key_OK(self):
        self.testSettings.test_api_key_has_value()

    def test_url_OK(self):
        self.testSettings.test_check_gtmetrix_url()

    @classmethod
    def tearDownClass(cls):
        """Put settings back as they were before test."""
        # restore 'settings' module's variables
        restore_settings()



class TestGTmetrixSettingsFailure(TestCase):
    """Tests that things fail when they're supposed to.

    Initializer is:
        def __init__(self, user_email=None, api_key=None):

    These tests purposely unset each part of the configuration to ensure
    that the initializer fails fast if required parameters or settings
    are not available.

    This localizes the failure so users aren't confused when their API calls
    fail later due to missing settings being silently ignored.
    """
    @classmethod
    def setUpClass(cls):
        """Ensure that our settings do not contain valid values."""
        save_settings()
        settings.GTMETRIX_REST_API_EMAIL = None
        settings.GTMETRIX_REST_API_KEY = None
        settings.GTMETRIX_REST_API_URL = None
        cls.testSettings = TestGTmetrixSettings()

    def test_email_NOT_OK(self):
        with raises(AssertionError):
            self.testSettings.test_email_has_value()

    def test_api_key_NOT_OK(self):
        with raises(AssertionError):
            self.testSettings.test_api_key_has_value()

    def test_url_NOT_OK(self):
        with raises(AssertionError):
            self.testSettings.test_check_gtmetrix_url()

    @classmethod
    def tearDownClass(cls):
        """Put settings back as they were before test."""
        restore_settings()


class TestGTmetrixSettings(TestCase):
    """Test GTmetrix settings module for valid values.

    Uses settings as they exist in environment, if this won't run by itself
    then tests can't proceed.

    The success/failure tests above just set up the environment, then call
    these tests."""

    def test_api_key_has_value(self):
        # TODO: validate format of the key
        assert (settings.GTMETRIX_REST_API_KEY)

    def test_check_gtmetrix_url(self):
        """Test whether URL is same as when tests were written."""
        assert (settings.GTMETRIX_REST_API_URL == 'https://gtmetrix.com/api/0.1/test')

    def test_email_has_value(self):
        # TODO: validate email format
        assert (settings.GTMETRIX_REST_API_EMAIL)
