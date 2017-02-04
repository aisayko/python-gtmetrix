"""
python-gtmetrix
-----------------

A Python client library for GTmetrix REST API

"""
import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

class PyTest(TestCommand):
    """Make the tests self-contained within setup.py."""
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = [
            '--strict',
            '--verbose',
            '--tb=long',
            'tests']
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


setup(
    name='python-gtmetrix',
    version='0.2.3',
    url='https://github.com/aisayko/python-gtmetrix',
    license='MIT License',
    author='Alex Isayko',
    author_email='alex.isayko@gmail.com',
    description='A Python client library for GTmetrix REST API.',
    keywords='python gtmetrix performance pagespeed yslow',
    long_description=__doc__,
    packages=['gtmetrix',],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    cmdclass={'test': PyTest},
    tests_require=['pytest', 'pytest-cov'],
    test_suite='tests.test_gtmetrix_api',
    install_requires=['requests>=2.13.0','six>=1.10.0'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
