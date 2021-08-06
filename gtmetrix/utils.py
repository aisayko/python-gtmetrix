import re

import six
from gtmetrix import settings
from gtmetrix.exceptions import (GTmetrixAPIKeyIsNone,
                                 GTmetrixEmailIsNone,
                                 GTmetrixEmailIsNotStringtype,
                                 GTmetrixInvalidEmail,
                                 GTmetrixAPIUrlIsNone,
                                 GTmetrixBadAPIUrl)

__all__ = ['YSLOW_RULES',
           'validate_email',
           'validate_api_key',
           'validate_api_url']


YSLOW_RULES = {
    'ynumreq': {
        'name': 'Make fewer HTTP requests',
        'weight': 8
    },
    'ycdn': {
        'name': 'Use a CDN',
        'weight': 6
    },
    'yemptysrc': {
        'name': 'Avoid empty src or href',
        'weight': 30
    },
    'yexpires': {
        'name': 'Add an Expires header',
        'weight': 10
    },
    'ycompress': {
        'name': 'Compress components',
        'weight': 8
    },
    'ycsstop': {
        'name': 'Put CSS at top',
        'weight': 4
    },
    'yjsbottom': {
        'name': 'Put Javascript at the bottom',
        'weight': 4
    },
    'yexpressions': {
        'name': 'Avoid CSS expression',
        'weight': 3
    },
    'yexternal': {
        'name': 'Make JS and CSS external',
        'weight': 4
    },
    'ydns': {
        'name': 'Reduce DNS lookups',
        'weight': 3
    },
    'yminify': {
        'name': 'Minify JS and CSS',
        'weight': 4
    },
    'yredirects': {
        'name': 'Avoid redirects',
        'weight': 4
    },
    'ydupes': {
        'name': 'Remove duplicate JS and CSS',
        'weight': 4
    },
    'yetags': {
        'name': 'Configure ETags',
        'weight': 2
    },
    'yxhr': {
        'name': 'Make Ajax cacheable',
        'weight': 4
    },
    'yxhrmethod': {
        'name': 'Use GET for AJAX requests',
        'weight': 3
    },
    'ymindom': {
        'name': 'Reduce the Number of DOM elements',
        'weight': 3
    },
    'yno404': {
        'name': 'No 404s',
        'weight': 4
    },
    'ymincookie': {
        'name': 'Reduce Cookie Size',
        'weight': 3
    },
    'ycookiefree': {
        'name': 'Use Cookie-free Domains',
        'weight': 3
    },
    'ynofilter': {
        'name': 'Avoid filters',
        'weight': 4
    },
    'yimgnoscale': {
        'name': 'Don\'t Scale Images in HTML',
        'weight': 3
    },
    'yfavicon': {
        'name': 'Make favicon Small and Cacheable',
        'weight': 2
    }
}

# Snagged from: https://www.scottbrady91.com/Email-Verification/Python-Email-Verification-Script
email_re = re.compile(
    '^[_a-z0-9+-]+(\.[_a-z0-9+-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(''\.[a-z]{2,''4})$')


def validate_email(email):
    """Check for valid email address, raise correct exception if not."""
    if email is None:
        raise GTmetrixEmailIsNone

    if not isinstance(email, six.string_types):
        raise GTmetrixEmailIsNotStringtype

    if email_re.match(email) is None:
        raise GTmetrixInvalidEmail

    return True


def validate_api_key(key):
    """Check for valid API key.  Stubbed out for now."""
    if key is None:
        raise GTmetrixAPIKeyIsNone
    return True


def validate_api_url(url):
    """Ensure that it's set to what it was when settings.py was written.

    Prevents e.g. testing api/0.1 calls against api/1.0 if it ever comes
    out."""
    if url is None:
        raise GTmetrixAPIUrlIsNone

    if url != settings.good_url:
        raise GTmetrixBadAPIUrl

    return True
