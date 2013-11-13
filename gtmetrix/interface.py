import settings

import requests

import os.path


__all__ = ['GTmetrixInterface',
           'GTmetrixInvalidTestRequest',
           'GTmetrixTestNotFound']


class GTmetrixInvalidTestRequest(Exception):
    """Invalid test request."""
    pass


class GTmetrixTestNotFound(Exception):
    """The requested test does not exist."""
    pass


class _TestObject(object):
    """GTmetrix Test representation."""
    def __init__(self, auth, test_id, poll_state_url=None):
        self.poll_state_url = poll_state_url
        self.test_id = test_id
        self.auth = auth

    def get_results(self):
        """Get the test state and results/resources (when test complete)."""
        response = requests.get(self.poll_state_url, auth=self.auth)
        response_data = response.json()

        if response.status_code == 404:
            raise GTmetrixTestNotFound(response_data['error'])

        if response.status_code == 400:
            raise GTmetrixInvalidTestRequest(response_data['error'])

        return response_data


class GTmetrixInterface(object):
    """Provides an interface to access GTmetrix REST API."""
    def __init__(self, user_email, api_key):
        self.auth = (user_email, api_key)

    def start_test(self, url, **data):
        """ Start a Test """
        data.update({'url': url})
        response = requests.post(settings.GTMETRIX_REST_API_URL, data=data, auth=self.auth)
        response_data = response.json()

        if response.status_code != 200:
            raise GTmetrixInvalidTestRequest(response_data['error'])

        return _TestObject(self.auth, **response_data)

    def poll_state_request(self, test_id):
        request_url = os.path.join(settings.GTMETRIX_REST_API_URL, test_id)
        return _TestObject(self.auth, test_id, request_url).get_results()
