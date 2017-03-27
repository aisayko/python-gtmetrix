# -*- coding: utf-8 -*-
"""
GTmetrix Python API

Settings Tests

Sets a good/bad value for each configuration validator and ensures that good
values pass and that bad values raise correct exception.

No API calls are actually made.

This runs three tests:

    1> TestGTmetrixSettingsSuccess

        Runs with forced GOOD values.  Will fal if validation methods are 
        not working properly.

    2> TestGTmetrixSettingsFailure

        Runs with forced BAD values. Ensures correct exception is raised.
"""

from unittest import TestCase
from pytest import raises

from gtmetrix.exceptions import (GTmetrixAPIUrlIsNone,
                                 GTmetrixBadAPIUrl,
                                 GTmetrixAPIKeyIsNone,
                                 GTmetrixEmailIsNone,
                                 GTmetrixEmailIsNotStringtype)
from gtmetrix import settings

from gtmetrix.utils import (validate_email,
                            validate_api_key,
                            validate_api_url)

from .utils import (save_settings,
                    restore_settings)


class TestGTmetrixSettingsSuccess(TestCase):
    """
    Tests that things succeed when they're supposed to.

    Set each settings.* to valid values and make sure they pass validation.

    Saves/restores global settings on entry/exit.
    """
    @classmethod
    def setUpClass(cls):
        """Ensure that our settings DO contain valid values."""
        save_settings()
        settings.set_known_good_settings()

    def test_email_OK(self):
        """Ensure known good email passes."""
        validate_email(settings.GTMETRIX_REST_API_EMAIL)

    def test_api_key_OK(self):
        """Ensure known good API key passes."""
        validate_api_key(settings.GTMETRIX_REST_API_KEY)

    def test_url_OK(self):
        """Test whether URL is same as when tests were written."""
        validate_api_url(settings.GTMETRIX_REST_API_URL)

    @classmethod
    def tearDownClass(cls):
        """Put settings back as they were before test."""
        restore_settings()


class TestGTmetrixSettingsFailure(TestCase):
    """
    Tests that things fail when they're supposed to.

    Set each settings.* value to None, then call validators.
    
    TODO: Add any specific values that fail in practice to ensure they're 
    caught.
    
    NOTE: These do not touch the global state and so don't save/restore it.
    """
    def test_api_key_is_None(self):
        """Test failure for key is None."""
        with raises(GTmetrixAPIKeyIsNone):
            validate_api_key(None)

    def test_email_is_None(self):
        """Test failure for email is None."""
        with raises(GTmetrixEmailIsNone):
            validate_email(None)

    def test_email_is_not_stringtype(self):
        """Ensure that we catch non-string emails."""
        with raises(GTmetrixEmailIsNotStringtype):
            validate_email(12345678)

    def test_url_is_None(self):
        """Test failure for api url is None."""
        with raises(GTmetrixAPIUrlIsNone):
            validate_api_url(None)

    def test_url_is_wrong(self):
        """Test failure for api url is not the same as when tests written."""
        with raises(GTmetrixBadAPIUrl):
            validate_api_url("this is not the URL you are looking for...")
