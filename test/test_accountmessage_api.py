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
from swagger_client.api.accountmessage_api import AccountmessageApi  # noqa: E501
from swagger_client.rest import ApiException


class TestAccountmessageApi(unittest.TestCase):
    """AccountmessageApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.accountmessage_api.AccountmessageApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_message_router_get(self):
        """Test case for message_router_get

        """
        pass

    def test_message_router_get_all_events_for_a_message_id(self):
        """Test case for message_router_get_all_events_for_a_message_id

        """
        pass

    def test_message_router_get_all_events_for_a_message_id_from_a_node(self):
        """Test case for message_router_get_all_events_for_a_message_id_from_a_node

        """
        pass

    def test_message_router_get_message_from_node(self):
        """Test case for message_router_get_message_from_node

        """
        pass


if __name__ == '__main__':
    unittest.main()
