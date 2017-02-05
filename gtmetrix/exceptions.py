"""
Exceptions for Python GTmetrix API Library
"""
__all__ = ['GTmetrixMissingAPIKey',
           'GTmetrixMissingEmail',
           'GTmetrixMissingEmailOrAPIKey',
           'GTmetrixInvalidTestRequest',
           'GTmetrixTestNotFound',
           'GTmetrixMaximumNumberOfApis',
           'GTmetrixManyConcurrentRequests']

class GTmetrixMissingAPIKey(Exception):
   """API key is not in settings or passed to initializer."""
   # TODO:  February 4, 2017 -- ssteinerX
   #        these exceptions shouldn't repeat the doc string as the message
   #        could use inspect.getdoc or write little decorator
   def __init__(self, message=None):
       self.message = (message or
           "API key must be passed or exist in the settings.")


class GTmetrixMissingEmail(Exception):
    """Email is not in settings or passed to initializer."""
    def __init__(self, message=None):
        self.message = (message or
            "Email must be passed or exist in the settings.")

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

