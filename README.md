python-gtmetrix
========================

**python-gtmetrix** is a Python client library for GTmetrix REST API.

Quickstart:
========================

Install package:

    $ pip install python-gtmetrix


Make tests:
-----------

Create json with urls:

    {
    "google": "http://google.com",
    }

Start test using json with urls:

    from gtmetrix import *
    import json

    with open('sites.json') as data_file:
    list_sites = json.load(data_file)

    for key, value in list_sites.items():
        print ("Site: %s - Url: %s" % (key, value))
        gt = GTmetrixInterface('your@email.com', 'api-key')
        my_test = gt.start_test(value)


Fetch results:

    my_test.fetch_results(key)

or

    results = gt.poll_state_request(key, my_test.test_id)

When test is completed you able to access next data in the files:

    results-date = pagespeed_score, yslow_score, page_bytes, page_load_time, page_elements
    resources-date= urls to screenshot, har, pagespeed_url, pagespeed_files, yslow_url,  report_pdf, report_pdf_full



List of available params and response attributes you can find at http://gtmetrix.com/api/


Exceptions:
-----------

Invalid test request

    GTmetrixInvalidTestRequest


The requested test does not exist

    GTmetrixTestNotFound

The maximum number of API calls reached

    GTmetrixMaximumNumberOfApis

Too many concurrent requests from your IP

    GTmetrixManyConcurrentRequests

Example:

    from gtmetrix import *

    gt = GTmetrixInterface('your@email.com', 'api-key')

    try:
        my_test = gt.start_test('http://google.com')
    except GTmetrixInvalidTestRequest:
        print 'Something goes wrong'

    try:
        results = gt.poll_state_request(my_test.test_id)
    except GTmetrixTestNotFound:
        raise Http404

Running Tests & Development
---------------------------


