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
from swagger_client.api.cluster_api import ClusterApi  # noqa: E501
from swagger_client.rest import ApiException


class TestClusterApi(unittest.TestCase):
    """ClusterApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.cluster_api.ClusterApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_cluster_router_delete_item_from_cache_of_every_node_in_cluster(self):
        """Test case for cluster_router_delete_item_from_cache_of_every_node_in_cluster

        """
        pass

    def test_cluster_router_delete_item_from_cache_of_specific_node_in_cluster(self):
        """Test case for cluster_router_delete_item_from_cache_of_specific_node_in_cluster

        """
        pass


if __name__ == '__main__':
    unittest.main()