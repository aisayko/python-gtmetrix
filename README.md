python-gtmetrix
========================

**python-gtmetrix** is a Python client library for GTmetrix REST API.

Quickstart:
========================

Install package:

    $ pip install python-gtmetrix


Make tests:
-----------

Start test:

    from gtmetrix import *

    gt = GTmetrixInterface('your@email.com', 'api-key')
    my_test = gt.start_test('http://google.com')

Fetch results:

    my_test.fetch_results()

or

    my_test = gt.poll_state_request(test_id)

When test is completed you able to access next data:

    >>> my_test.results
    {...}

    >>> my_test.har_data
    {...}

    >>> my_test.speed_data
    {...}

    >>> my_test.yslow_data
    {...}


List of available params and response attributes you can find at http://gtmetrix.com/api/


Utils
-----------

Get name and weight by YSlow rule id:

    from gtmetrix.utils import YSLOW_RULES

    print YSLOW_RULES


Exceptions:
-----------

Invalid test request

    GTmetrixInvalidTestRequest


The requested test does not exist

    GTmetrixTestNotFound

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
