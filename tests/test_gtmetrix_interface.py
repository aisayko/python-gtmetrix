"""GTmetrix Python API Interface Tests

This runs three tests:


    2> TestGTmetrixInterfaceInitializerSuccess

        Runs with forced GOOD values.

    3> TestGTmetrixInterfaceInitializerFailure

        Runs with forced BAD values, test passes if it fails properly.

    1> TestGTmetrixInterfaceInitializer

        Runs with inherited, unmodified environment.  Succeeds if further
        tests will be able to run i.e. email, api key, and URL for GTmetrix
        are all set to values.

    TODO: do validation on email format and API key to prevent bogus
          formats e.g. invalid email.

"""
import os
from unittest import TestCase

import pytest
from pytest import raises

from gtmetrix import settings
from gtmetrix.interface import GTmetrixInterface
from gtmetrix.exceptions import GTmetrixMissingEmailOrAPIKey
from .utils import save_settings, restore_settings


class TestGTmetrixInitializer(TestCase):
    """Tests that things succeed when they're supposed to.

    All tests should pass without exception.
    """
    def test_initializer_supplying_settings(self):
        self.testInitializer.test_initialize_using_supplied_values(
            settings.GTMETRIX_REST_API_EMAIL,
            settings.GTMETRIX_REST_API_KEY)

    def test_initializer_default_settings(self):
        self.testInitializer.test_api_key_has_value()

    def test_url_OK(self):
        self.testInitializer.test_check_gtmetrix_url()

    @classmethod
    def tearDownClass(cls):
        """Put settings back as they were before test."""
        # restore 'settings' module's variables
        restore_settings()



# class TestGTmetrixInitializerFailure(TestCase):
#     """Tests that things fail when they're supposed to.

#     Initializer is:
#         def __init__(self, user_email=None, api_key=None):

#     These tests purposely unset each part of the configuration to ensure
#     that the initializer fails fast if required parameters or settings
#     are not available.

#     This localizes the failure so users aren't confused when their API calls
#     fail later due to missing settings being silently ignored.
#     """
#     @classmethod
#     def setUpClass(cls):
#         """Ensure that our settings do not contain valid values."""
#         save_settings()
#         settings.GTMETRIX_REST_API_EMAIL = None
#         settings.GTMETRIX_REST_API_KEY = None
#         settings.GTMETRIX_REST_API_URL = None
#         cls.testInitializer = TestGTmetrixInterfaceInitializer()

#     def test_email_NOT_OK(self):
#         with raises(AssertionError):
#             self.testInitializer.test_email_has_value()

#     def test_api_key_NOT_OK(self):
#         with raises(AssertionError):
#             self.testInitializer.test_api_key_has_value()

#     def test_url_NOT_OK(self):
#         with raises(AssertionError):
#             self.testInitializer.test_check_gtmetrix_url()

#     @classmethod
#     def tearDownClass(cls):
#         """Put settings back as they were before test."""
#         restore_settings()


class TestGTmetrixInterfaceInitializer(TestCase):
    """
    Test GTmetrix interface using default and prepared values.
    """

    def check_url():
        """Ensure URL is same as when tests were written."""
        assert (settings.GTMETRIX_REST_API_URL == 'https://gtmetrix.com/api/0.1/test')

    def test_initialize_using_settings(self):
        self.check_url()
        gt = GTmetrixInterface(
            settings.GTMETRIX_REST_API_EMAIL,
            settings.GTMETRIX_REST_API_KEY)

    def test_initialize_using_supplied_values(self, user_email=None, api_key=None):
        self.check_url()
        gt = GTmetrixInterface(user_email, api_key)


# class TestAPI_Authorization(TestCase):
#     pass


# # class TestGTmetrixInterfaceInitializerFailures(TestCase):
# #     # Ensure that email is set for tests.
# #     # Set in gtmetrix/settings.py and set manually or by environment.
# #     # TBD: move to setup on actual login & call tests
# #     def test_email_is_set_in_settings(self):
# #         assert (settings.GTMETRIX_REST_API_EMAIL)

# #     def test_api_key_is_set_in_settings(self):
# #         assert (settings.GTMETRIX_REST_API_KEY)

# #     # Exercise the initializer with bad values to make sure we can't get
# #     # any further
# #     def test_error_on_no_email_or_api_key_on_interface_constructor(self):
# #         """Ensure that initialization fails on missing email or api key."""
# #         with raises(GTmetrixMissingEmailOrAPIKey):
# #             """TBD: kill env vars in test setup"""
# #             """Fail if environment vars aren't set"""
# #             gt = GTmetrixInterface()

# #         with raises(GTmetrixMissingEmailOrAPIKey):
# #             # Missing api_key
# #             gt = GTmetrixInterface(user_email="no@example.com", api_key=None)

# #         with raises(GTmetrixMissingEmailOrAPIKey):
# #              gt = GTmetrixInterface(user_email=None, api_key="whatever")


# if __name__ == '__main__':
#     pytest.main()
