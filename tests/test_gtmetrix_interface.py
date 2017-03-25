# -*- coding: utf-8 -*-
"""
GTmetrix Python API

Interface Initializer Tests

Tests to make sure the initializer catches bad inputs.  

They still might not work (i.e. inactive API key, etc.), but they'll at least
be valid values. 

    TestGTmetrixInitializerCatchesBadData

        Runs with forced BAD values, test passes if it fails properly.
"""
from unittest import TestCase

from pytest import raises

from gtmetrix import settings
from gtmetrix.exceptions import GTmetrixAPIKeyIsNone, GTmetrixEmailIsNone, \
    GTmetrixInvalidEmail
from gtmetrix.interface import GTmetrixInterface
from gtmetrix.settings import set_known_good_settings
from .utils import restore_settings, save_settings


class TestGTmetrixInitializerCatchesBadData(TestCase):
    """
    Tests GTMetrixInterface initializer with purposely bad data.

    This ensures that the class will throw correct exceptions on bad data.

    NOTE: The initializer throws exceptions in a particular order so we only
          test one bad chunk at a time so as not to care about the order of
          testing within the initializer itself.
    """
    bad_emails = ['email has spaces@example.com',
                  '@example.no.email.address.just.domain.com',
                  'an.email.with.no.domain.or.at.sign',
                  'an.email.with.no.domain.with.at.sign@',
                  'any.other.examples.which.should.fail.find.a.list', ]

    def setup_method(self, method):
        """`setup_method` is invoked for every test method."""
        save_settings()
        set_known_good_settings()

    def teardown_method(self, method):
        """teardown_method is invoked after every test method."""
        restore_settings()

    def test_initializer_with_bad_emails_passed(self):
        """Ensure correct exception is raised when invalid email specified."""
        for bad_email in self.bad_emails:
            with raises(GTmetrixInvalidEmail):
                gt = GTmetrixInterface(bad_email)

    def test_initializer_with_bad_emails_default(self):
        """Ensure correct exception is raised for invalid email via 
        settings."""
        for bad_email in self.bad_emails:
            with raises(GTmetrixInvalidEmail):
                settings.GTMETRIX_REST_API_EMAIL = bad_email
                gt = GTmetrixInterface()

    def test_email_is_None(self):
        """Ensure correct exception is raised when email is None."""
        settings.GTMETRIX_REST_API_EMAIL = None
        with raises(GTmetrixEmailIsNone):
            gt = GTmetrixInterface()

    def test_api_key_is_None(self):
        """Ensure correct exception is raised when API key is None."""
        settings.GTMETRIX_REST_API_KEY = None
        with raises(GTmetrixAPIKeyIsNone):
            gt = GTmetrixInterface()
