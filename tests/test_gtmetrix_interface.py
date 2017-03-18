"""GTmetrix Python API

Interface Initializer Tests

This runs three tests:


    2> TestGTmetrixInterfaceInitializerSuccess

        Runs with forced GOOD values.

    3> TestGTmetrixInterfaceInitializerFailure

        Runs with forced BAD values, test passes if it fails properly.

    1> TestGTmetrixInterfaceInitializer

        Runs with inherited, unmodified environment.  Succeeds if further
        tests will be able to run i.e. email, api key, and URL for GTmetrix
        are all set to values.

"""
from unittest import TestCase

from pytest import raises

from gtmetrix import settings
from gtmetrix.interface import GTmetrixInterface
from gtmetrix.exceptions import (GTmetrixMissingEmailOrAPIKey,
                                 GTmetrixBadAPIUrl,
                                 GTmetrixMissingEmail,
                                 GTmetrixMissingAPIKey)

from .utils import (save_settings,
                    restore_settings,
                    api_url_is_valid,
                    email_is_valid,
                    api_key_is_valid)


def _initialize_using_supplied_values(user_email=None, api_key=None):
    """
    Create GTmetrixInterface with specified values.

    This is meant to be called with values, to call it without values is
    an error.
    """

    # Quick test, URL has to be right and both params must be passed
    if not api_url_is_valid(settings.GTMETRIX_REST_API_URL):
        raise GTmetrixBadAPIUrl
    if not user_email and api_key:
        raise GTmetrixMissingEmailOrAPIKey

    # All we're testing is object creation, it should throw appropriate
    # exceptions which we account for as necessary below.
    gt = GTmetrixInterface(user_email, api_key)


class TestGTmetrixInitializer(TestCase):
    """
    Tests GTMetrixInterface initializer.

    This ensures that the class will accept good values and throw
    correct exceptions on bad.

    Initializer is:
        def __init__(self, user_email=None, api_key=None):

    Default is to use user_email and api_key from settings.py.

    NOTE:   settings.py, as shipped, pulls in user_email and api_key
            from environment vars.  See settings.py or docs for required
            env var names.
    """
    good_email = "example@example.com"
    good_apikey = "abcdef4d91234542222d709124eceaaa"


    def test_initializer_supplying_settings_py_settings_manually(self):
        """Initialize with the values from settings.py."""
        self._initialize_using_supplied_values(
            settings.GTMETRIX_REST_API_EMAIL,
            settings.GTMETRIX_REST_API_KEY)

    def test_initializer_defaulting_from_settings(self):
        # All we're testing is object creation
        gt = GTmetrixInterface()

    def test_initializer_with_bad_emails(self):
        bad_emails = ['email has spaces@example.com',
                      '@example.no.email.address.just.domain.com'
                      'any.other.examples.which.should.fail.find.a.list']
        for bad_email in bad_emails:
            with raises(GTmetrixInvalidEmail):
                gt = GTmetrixInterface(bad_email)

    def test_email_equals_None(self):
        """Ensure that our settings do not contain valid values."""
        save_settings()
        settings.GTMETRIX_REST_API_EMAIL = None
        with raises(GTmetrixMissingEmail):
            gt = GTmetrixInterface()
        restore_settings()


    def test_api_key_is_None(self):
        save_settings()
        settings.GTMETRIX_REST_API_KEY = None
        with raises(GTmetrixMissingAPIKey):
            gt = GTmetrixInterface()
        restore_settings()

     def test_url_is_None(self)
         save_settings()
         settings.GTMETRIX_REST_API_URL = None
         with raises(GTmetrixBadAPIUrl):
             gt = GTmetrixInterface()
         restore_settings()


class TestAPI_Authorization(TestCase):
    pass

if __name__ == '__main__':
    pytest.main()
