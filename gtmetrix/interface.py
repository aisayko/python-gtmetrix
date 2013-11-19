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
    STATE_QUEUED = 'queued'
    STATE_STARTED = 'started'
    STATE_COMPLETED = 'completed'
    STATE_ERROR = 'error'

    def __init__(self, auth, test_id, poll_state_url=None):
        self.poll_state_url = (poll_state_url or
                               os.path.join(settings.GTMETRIX_REST_API_URL, test_id))
        self.test_id = test_id
        self.state = self.STATE_QUEUED
        self.auth = auth
        self.results = {}
        self.har_data = {}
        self.speed_data = {}
        self.yslow_data = {}

    def _request(self, url):
        response = requests.get(url, auth=self.auth)
        response_data = response.json()

        if response.status_code == 404:
            raise GTmetrixTestNotFound(response_data['error'])

        if response.status_code == 400:
            raise GTmetrixInvalidTestRequest(response_data['error'])

        return response_data

    def fetch_results(self):
        """Get the test state and results/resources (when test complete)."""
        response_data = self._request(self.poll_state_url)

        self.state = response_data['state']

        if self.state == self.STATE_COMPLETED:
            resources = response_data['resources']

            self.results = response_data['results']
            self.har_data = self._request(resources['har'])
            self.speed_data = self._request(resources['pagespeed'])
            self.yslow_data = self._request(resources['yslow'])

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
        test = _TestObject(self.auth, test_id)
        test.fetch_results()
        return test
