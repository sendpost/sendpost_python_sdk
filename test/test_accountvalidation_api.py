# coding: utf-8

"""
    SendPost API

    SendPost API to send transactional emails reliably  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: hello@sendx.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.accountvalidation_api import AccountvalidationApi  # noqa: E501
from swagger_client.rest import ApiException


class TestAccountvalidationApi(unittest.TestCase):
    """AccountvalidationApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.accountvalidation_api.AccountvalidationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_validate_router_validate_email_bulk(self):
        """Test case for validate_router_validate_email_bulk

        """
        pass

    def test_validation_router_count(self):
        """Test case for validation_router_count

        """
        pass

    def test_validation_router_delete_validation(self):
        """Test case for validation_router_delete_validation

        """
        pass

    def test_validation_router_get_all(self):
        """Test case for validation_router_get_all

        """
        pass

    def test_validation_router_validate_email_list(self):
        """Test case for validation_router_validate_email_list

        """
        pass


if __name__ == '__main__':
    unittest.main()
