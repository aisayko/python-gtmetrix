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

    results = my_test.get_results()

or

    gt.poll_state_request(test_id)


List of available params and response attributes you can find [here]: http://gtmetrix.com/api/


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
