"""
Python GTmetrix API Library

Exceptions
"""

__all__ = [
            'GTmetrixInvalidTestRequest',
            'GTmetrixMissingAPIKey',
            'GTmetrixMissingEmail',
            'GTmetrixMissingEmailOrAPIKey',
            'GTmetrixManyConcurrentRequests',
            'GTmetrixMaximumNumberOfApis',
            'GTmetrixTestNotFound',
          ]


class GTmetrixMissingAPIKey(Exception):
   """API key is not in settings or passed to initializer."""
   def __init__(self, message=None):
       self.message = (message or
           "API key must be passed or exist in the settings.")


class GTmetrixMissingEmail(Exception):
    """Email is not in settings or passed to initializer."""
    def __init__(self, message=None):
        self.message = (message or
            "Email must be passed or exist in the settings.")

class GTmetrixInvalidEmail(Exception):
    """Email is invalid."""
    def __init__(self, message=None):
        self.message = (message or
            "Email is invalid.")

class GTmetrixMissingEmailOrAPIKey(Exception):
    """Email or API key is not in settings or passed to initializer."""
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

