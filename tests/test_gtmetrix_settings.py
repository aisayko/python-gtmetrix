"""

GTmetrix Python API

Settings Tests

The success and failure tests just set a good/bad environment, the default
just tests what it got from importing the settings module.

No API calls are actually made.

This runs three tests:

    1> TestGTmetrixSettingsSuccess

        Runs with forced GOOD values.  Will fal if util.* validation
        methods are not working properly.

    2> TestGTmetrixSettingsFailure

        Runs with forced BAD values.  Non-failure is a problem.

    3> TestGTmetrixSettings

        Runs with inherited, unmodified environment.  Succeeds if further
        tests will be able to run i.e. email, api key, and URL for GTmetrix
        are all set to some values.

"""

from unittest import TestCase
from pytest import raises

from gtmetrix import settings

from .utils import (save_settings,
                    restore_settings,
                    email_is_valid,
                    api_key_is_valid,
                    api_url_is_valid,)


class TestGTmetrixSettingsSuccess(TestCase):
    """
    Tests that things succeed when they're supposed to.

    Set each settings.* to valid values and make sure they pass validation.

    Saves/restores global settings on entry/exit
    """
    @classmethod
    def setUpClass(cls):
        """Ensure that our settings DO contain valid values."""
        save_settings()
        settings.GTMETRIX_REST_API_EMAIL = "email, not testing format"
        settings.GTMETRIX_REST_API_KEY = "a fake api key"
        cls.settingsTester = TestGTmetrixSettings()

    def test_email_OK(self):
        self.settingsTester.test_email_is_valid()

    def test_api_key_OK(self):
        self.settingsTester.test_api_key_is_valid()

    def test_url_OK(self):
        self.settingsTester.test_check_gtmetrix_url()

    @classmethod
    def tearDownClass(cls):
        """Put settings back as they were before test."""
        # restore 'settings' module's variables
        restore_settings()



class TestGTmetrixSettingsFailure(TestCase):
    """
    Tests that things fail when they're supposed to.

    Set each settings.* value to invalid values, then call validators.

    Saves/restores global settings on entry/exit
    """
    @classmethod
    def setUpClass(cls):
        """Ensure that our settings do not contain valid values."""
        save_settings()
        settings.GTMETRIX_REST_API_EMAIL = None
        settings.GTMETRIX_REST_API_KEY = None
        settings.GTMETRIX_REST_API_URL = None
        cls.settingsTester = TestGTmetrixSettings()

    def test_email_NOT_OK(self):
        with raises(AssertionError):
            self.value = self.settingsTester.test_email_is_valid()

    def test_api_key_NOT_OK(self):
        with raises(AssertionError):
            self.settingsTester.test_api_key_is_valid()

    def test_url_NOT_OK(self):
        with raises(AssertionError):
            self.settingsTester.test_check_gtmetrix_url()

    @classmethod
    def tearDownClass(cls):
        """Put settings back as they were before test."""
        restore_settings()



class TestGTmetrixSettings(TestCase):
    """
    Test global settings from settings module for valid values.

    Uses settings as they exist in environment, if this won't run by itself
    then API calls can't be made.

    The success/failure tests above just set up the environment, then call
    these tests.

    NOTE:   there is no initializer here, the settings are available by virtue
            of the import of the settings and are saved/restored by any
            tests that modify them.
    """

    def test_api_key_is_valid(self):
        assert api_key_is_valid(settings.GTMETRIX_REST_API_KEY)

    def api_url_is_valid(self):
        """Test whether URL is same as when tests were written."""
        assert api_url_is_valid(settings.GTMETRIX_REST_API_URL)

    def test_email_is_valid(self):
        # TODO: validate email format
        assert email_is_valid(settings.GTMETRIX_REST_API_EMAIL)
