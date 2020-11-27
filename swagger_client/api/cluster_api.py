# coding: utf-8

"""
    SendPost API

    SendPost API to send transactional emails reliably  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: hello@sendx.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class ClusterApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def cluster_router_delete_item_from_cache_of_every_node_in_cluster(self, x_system_api_key, **kwargs):  # noqa: E501
        """cluster_router_delete_item_from_cache_of_every_node_in_cluster  # noqa: E501

        Delete item from cache of every node in cluster  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cluster_router_delete_item_from_cache_of_every_node_in_cluster(x_system_api_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_system_api_key: System API Key (required)
        :param str name: cache name
        :param str key: cache item key to delete
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.cluster_router_delete_item_from_cache_of_every_node_in_cluster_with_http_info(x_system_api_key, **kwargs)  # noqa: E501
        else:
            (data) = self.cluster_router_delete_item_from_cache_of_every_node_in_cluster_with_http_info(x_system_api_key, **kwargs)  # noqa: E501
            return data

    def cluster_router_delete_item_from_cache_of_every_node_in_cluster_with_http_info(self, x_system_api_key, **kwargs):  # noqa: E501
        """cluster_router_delete_item_from_cache_of_every_node_in_cluster  # noqa: E501

        Delete item from cache of every node in cluster  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cluster_router_delete_item_from_cache_of_every_node_in_cluster_with_http_info(x_system_api_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_system_api_key: System API Key (required)
        :param str name: cache name
        :param str key: cache item key to delete
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_system_api_key', 'name', 'key']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cluster_router_delete_item_from_cache_of_every_node_in_cluster" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_system_api_key' is set
        if ('x_system_api_key' not in params or
                params['x_system_api_key'] is None):
            raise ValueError("Missing the required parameter `x_system_api_key` when calling `cluster_router_delete_item_from_cache_of_every_node_in_cluster`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501
        if 'key' in params:
            query_params.append(('key', params['key']))  # noqa: E501

        header_params = {}
        if 'x_system_api_key' in params:
            header_params['X-System-ApiKey'] = params['x_system_api_key']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/cluster/cache', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def cluster_router_delete_item_from_cache_of_specific_node_in_cluster(self, x_system_api_key, **kwargs):  # noqa: E501
        """cluster_router_delete_item_from_cache_of_specific_node_in_cluster  # noqa: E501

        Delete item from cache of specific node in cluster  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cluster_router_delete_item_from_cache_of_specific_node_in_cluster(x_system_api_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_system_api_key: System API Key (required)
        :param str name: cache name
        :param str key: cache item key to delete
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.cluster_router_delete_item_from_cache_of_specific_node_in_cluster_with_http_info(x_system_api_key, **kwargs)  # noqa: E501
        else:
            (data) = self.cluster_router_delete_item_from_cache_of_specific_node_in_cluster_with_http_info(x_system_api_key, **kwargs)  # noqa: E501
            return data

    def cluster_router_delete_item_from_cache_of_specific_node_in_cluster_with_http_info(self, x_system_api_key, **kwargs):  # noqa: E501
        """cluster_router_delete_item_from_cache_of_specific_node_in_cluster  # noqa: E501

        Delete item from cache of specific node in cluster  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cluster_router_delete_item_from_cache_of_specific_node_in_cluster_with_http_info(x_system_api_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_system_api_key: System API Key (required)
        :param str name: cache name
        :param str key: cache item key to delete
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_system_api_key', 'name', 'key']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cluster_router_delete_item_from_cache_of_specific_node_in_cluster" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_system_api_key' is set
        if ('x_system_api_key' not in params or
                params['x_system_api_key'] is None):
            raise ValueError("Missing the required parameter `x_system_api_key` when calling `cluster_router_delete_item_from_cache_of_specific_node_in_cluster`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501
        if 'key' in params:
            query_params.append(('key', params['key']))  # noqa: E501

        header_params = {}
        if 'x_system_api_key' in params:
            header_params['X-System-ApiKey'] = params['x_system_api_key']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/cluster/cache/node', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
