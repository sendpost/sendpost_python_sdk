# coding: utf-8

"""
    SendPost API

    Email API and SMTP relay to not just send and measure email sending, but also alert and optimise. We provide you with tools, expertise and support needed to reliably deliver emails to your customers inboxes on time, every time.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: hello@sendpost.io
    Generated by: https://openapi-generator.tech
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "sendpost_python_sdk"
VERSION = "1.1.1"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "certifi >= 14.5.14",
    "frozendict ~= 2.3.4",
    "python-dateutil ~= 2.7.0",
    "setuptools >= 21.0.0",
    "typing_extensions ~= 4.3.0",
    "urllib3 ~= 1.26.7",
]

setup(
    name=NAME,
    version=VERSION,
    description="SendPost API",
    url = 'https://github.com/sendpost/sendpost_python_sdk',
    download_url = 'https://github.com/sendpost/sendpost_python_sdk/archive/refs/tags/1.1.1.tar.gz',
    author="Sendpost",
    author_email="dev@sendpost.io",
    keywords=["OpenAPI", "OpenAPI-Generator", "SendPost API"],
    python_requires=">=3.7",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description="""\
    Email API and SMTP relay to not just send and measure email sending, but also alert and optimise. We provide you with tools, expertise and support needed to reliably deliver emails to your customers inboxes on time, every time.  # noqa: E501
    """
)
