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


Exceptions:

    GTmetrixInvalidTestRequest - Invalid test request
    GTmetrixTestNotFound - The requested test does not exist.
