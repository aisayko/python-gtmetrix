"""
Python GTmetrix API Library

Exceptions

TODO: ss -- rearrange __all__ and code to match and alphabetical order
"""
__all__ = ['GTmetrixInvalidTestRequest',
           'GTmetrixAPIUrlIsNone',
           'GTmetrixBadAPIUrl',
           'GTmetrixAPIKeyIsNone',
           'GTmetrixEmailIsNone',
           'GTmetrixInvalidEmail',
           'GTmetrixEmailIsNotStringtype',
           'GTmetrixMissingEmailOrAPIKey',
           'GTmetrixManyConcurrentRequests',
           'GTmetrixMaximumNumberOfApis',
           'GTmetrixTestNotFound',
           ]


class GTmetrixBadAPIUrl(Exception):
    """URL is not the same as what was in settings."""
    pass


class GTmetrixAPIUrlIsNone(Exception):
    """The URL is `None`."""
    pass


class GTmetrixAPIKeyIsNone(Exception):
    """API key is not in settings or passed to initializer."""

    def __init__(self, message=None):
        self.message = (message or
                        "API key must be passed or exist in the settings.")


class GTmetrixEmailIsNone(Exception):
    """Email is not in settings or passed to initializer."""

    def __init__(self, message=None):
        self.message = (message or
                        "Email must be passed or exist in the settings.")


class GTmetrixEmailIsNotStringtype(Exception):
    """Email is not a string type."""

    def __init__(self, message=None):
        self.message = (message or
                        "Email is not a stringtype.")


class GTmetrixInvalidEmail(Exception):
    """Email is invalid."""

    def __init__(self, message=None):
        self.message = (message or
                        "Email is invalid.")


class GTmetrixMissingEmailOrAPIKey(Exception):
    """Email or API key is not in settings or passed to initializer.
    NOTE: this exception isn't used in actual interface due to specific
          exceptions for invalid email/key/url taking precedence.  This is
          used only to validate when invalid test data is produced while
          testing.
    """

    def __init__(self, message=None):
        self.message = (message or
                        "Email and API key must be passed or exist in the settings.")


class GTmetrixInvalidTestRequest(Exception):
    """Invalid test request."""
    pass


class GTmetrixManyConcurrentRequests(Exception):
    """Too many concurrent requests from your IP."""
    pass


class GTmetrixMaximumNumberOfApis(Exception):
    """The maximum number of API calls reached."""
    pass


class GTmetrixTestNotFound(Exception):
    """The requested test does not exist."""
    pass
