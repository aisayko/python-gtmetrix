__all__ = ['YSLOW_RULES']


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
