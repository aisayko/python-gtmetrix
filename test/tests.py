__author__ = 'samycici'
import unittest

import mock

from gtmetrix import GTmetrixInterface


class GTmetrixTest(unittest.TestCase):

    def setUp(self):
        self.gtmetrix = GTmetrixInterface(user_email='user', api_key='123')

    @mock.patch('gtmetrix.requests.get')
    def test_get_ok(self, mock_get):
        mock_response = mock.Mock()
        expected_dict= {
            "results":{
                "page_load_time":"522",
                "html_bytes":"3395",
                "page_elements":"16",
                "report_url":"https://gtmetrix.com/reports/gtmetrix.com/Cz0AQOjf",
                "html_load_time":"87",
                "page_bytes":"89229",
                "pagespeed_score":"95",
                "yslow_score":"98"
            },
            "state":"completed"
        }

        mock_response.json.return_value = expected_dict
        mock_get.return_value = mock_response

        url = 'http://api.corgidata.com/breeds/'
        response_dict = self.gtmetrix.poll_state_request(url=url)

        mock_get.assert_called_once_with(url=url)
        self.assertEqual(1, mock_response.json.call_count)




if __name__ == '__main__':
    unittest.main()