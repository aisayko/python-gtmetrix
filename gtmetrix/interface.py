import requests
import os.path
import time
import datetime

from gtmetrix import settings
from gtmetrix.exceptions import *
from gtmetrix.utils import  (validate_email,
                             validate_api_key)

__all__ = ['GTmetrixInterface',]


class _TestObject(object):
    """GTmetrix Test representation."""
    STATE_QUEUED = 'queued'
    STATE_STARTED = 'started'
    STATE_COMPLETED = 'completed'
    STATE_ERROR = 'error'

    def __init__(self, auth, test_id, poll_state_url=None, credits_left=None):
        self.poll_state_url = (poll_state_url or
                               os.path.join(settings.GTMETRIX_REST_API_URL, test_id))
        self.test_id = test_id
        self.credits_left = credits_left
        self.state = self.STATE_QUEUED
        self.credits_left = 0
        self.auth = auth
        self.results = {}
        self.resources = {}
        self.pagespeed_score = {}
        self.yslow_score = {}
        self.html_bytes = {}
        self.html_load_time = {}
        self.page_bytes = {}
        self.page_load_time = {}
        self.page_elements ={}
        self.redirect_duration = {}
        self.connect_duration = {}
        self.backend_duration = {}
        self.first_paint_time = {}
        self.first_contentful_paint_time = {}
        self.dom_interactive_time = {}
        self.dom_content_loaded_time = {}
        self.dom_content_loaded_duration = {}
        self.onload_time = {}
        self.onload_duration = {}
        self.fully_loaded_time = {}
        self.rum_speed_index = {}
        self.screenshot ={}
        self.har = {}
        self.pagespeed_url ={}
        self.pagespeed_files = {}
        self.yslow_url = {}
        self.report_pdf = {}
        self.report_pdf_full = {}

    def _request(self, url):
        response = requests.get(url, auth=self.auth)
        response_data = response.json()

        if response.status_code == 404:
            raise GTmetrixTestNotFound(response_data['error'])

        if response.status_code == 400:
            raise GTmetrixInvalidTestRequest(response_data['error'])

        if response.status_code == 402:
            raise GTmetrixMaximumNumberOfApis(response_data['error'])

        if response.status_code == 429:
            raise GTmetrixManyConcurrentRequests(response_data['error'])

        return response_data

    def fetch_results(self, key):
        """Get the test state and results/resources (when test complete)."""
        response_data = self._request(self.poll_state_url)

        self.state = response_data['state']

        number_executions = 0
        while not self.state == self.STATE_COMPLETED and (number_executions < 30):
            number_executions += 1
            time.sleep(30)
            response_data = self._request(self.poll_state_url)
            self.state = response_data['state']

        self._extract_results(response_data, key)

        return response_data

    def _get_result( self, key, dflt='' ):
      return self.results[ key ] if key in self.results else dflt
    
    def _get_resource( self, key, dflt='' ):
      return self.resources[ key ] if key in self.resources else dflt

    def _extract_results(self, response_data, key):
      today = datetime.datetime.now()
      day = today.day
      month = today.month
      year = today.year
      if 'results' in response_data:
        self.results = response_data['results']
        self.pagespeed_score = self._get_result( 'pagespeed_score' )
        self.yslow_score = self._get_result( 'yslow_score' )
        self.html_bytes = self._get_result( 'html_bytes' )
        self.html_load_time = self._get_result( 'html_load_time' )
        self.page_bytes = self._get_result( 'page_bytes' )
        self.page_load_time = self._get_result( 'page_load_time' )
        self.page_elements = self._get_result( 'page_elements' )
        self.redirect_duration = self._get_result( 'redirect_duration' )
        self.connect_duration = self._get_result( 'connect_duration' )
        self.backend_duration = self._get_result( 'backend_duration' )
        self.first_paint_time = self._get_result( 'first_paint_time' )
        self.first_contentful_paint_time = self._get_result( 'first_contentful_paint_time' )
        self.dom_interactive_time = self._get_result( 'dom_interactive_time' )
        self.dom_content_loaded_time = self._get_result( 'dom_content_loaded_time' )
        self.dom_content_loaded_duration = self._get_result( 'dom_content_loaded_duration' )
        self.onload_time = self._get_result( 'onload_time' )
        self.onload_duration = self._get_result( 'onload_duration' )
        self.fully_loaded_time = self._get_result( 'fully_loaded_time' )
        self.rum_speed_index = self._get_result( 'rum_speed_index' )
        #name_of_file_results = "results-%d-%d-%d" % (day,month, year)
        #file = open(name_of_file_results, "a")
        #file.write("site:%s pagespeed_score:%s yslow_score:%s page_load_time:%s page_bytes:%s page_elements:%s \n" % (key, self.pagespeed_score, self.yslow_score, self.page_load_time, self.page_bytes, self.page_elements))
        #file.close()

      if 'resources' in response_data:
        self.resources = response_data['resources']
        self.screenshot = self._get_resource( 'screenshot' )
        self.har = self._get_resource( 'har' )
        self.pagespeed_url = self._get_resource( 'pagespeed' )
        self.pagespeed_files = self._get_resource( 'pagespeed_files' )
        self.yslow_url = self._get_resource( 'yslow' )
        self.report_pdf = self._get_resource( 'report_pdf' )
        self.report_pdf_full = self._get_resource( 'report_pdf_full' )
        #name_of_file_resources = "resources-%d-%d-%d" % (day,month, year)
        #file = open(name_of_file_resources, "a")
        #file.write("site:%s screenshot:%s har:%s pagespeed_url:%s pagespeed_files:%s yslow_url:%s  report_pdf:%s report_pdf_full:%s  \n" % (key, self.screenshot, self.har, self.pagespeed_url, self.pagespeed_files, self.yslow_url, self.report_pdf, self.report_pdf_full))
        #file.close()



class GTmetrixInterface(object):
    """Provides an interface to access GTmetrix REST API."""
    def __init__(self, user_email=None, api_key=None):
        # Validate and set instance variables
        self.set_auth_email_and_key(user_email, api_key)
        self.auth = (self.user_email, self.api_key)

    def set_auth_email_and_key(self, user_email=None, api_key=None):
        # Get from params or default to values from settings
        self.user_email = user_email or settings.GTMETRIX_REST_API_EMAIL
        self.api_key = api_key or settings.GTMETRIX_REST_API_KEY

        # Make sure they're valid
        self.validate_user_email()
        self.validate_api_key()

    def validate_user_email(self):
        """Hook for user email validation."""
        return validate_email(self.user_email)

    def validate_api_key(self):
        """Hook for api key validation."""
        return validate_api_key(self.api_key)

    def start_test(self, url, **data):
        """ Start a Test """
        data.update({'url': url})
        response = requests.post(settings.GTMETRIX_REST_API_URL, data=data, auth=self.auth)
        response_data = response.json()

        if response.status_code != 200:
            raise GTmetrixInvalidTestRequest(response_data['error'])

        return _TestObject(self.auth, **response_data)

    def poll_state_request(self, key, test_id):
        test = _TestObject(self.auth, test_id)
        test.fetch_results(key)
        return test
