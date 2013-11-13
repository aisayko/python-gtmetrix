"""
python-gtmetrix
-----------------

A Python client library for GTmetrix REST API

"""
from setuptools import setup, find_packages


setup(
    name='python-gtmetrix',
    version='0.1',
    url='https://github.com/aisayko/python-gtmetrix',
    license='MIT License',
    author='Alex Isayko',
    author_email='alex.isayko@gmail.com',
    description='A Python client library for GTmetrix REST API.',
    keywords='python gtmetrix performance pagespeed yslow',
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=['requests'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
