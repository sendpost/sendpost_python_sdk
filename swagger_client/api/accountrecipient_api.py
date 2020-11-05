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


class AccountrecipientApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def recipient_router_get_all_messages_for_a_recipient(self, x_account_api_key, recipient, **kwargs):  # noqa: E501
        """recipient_router_get_all_messages_for_a_recipient  # noqa: E501

        Find all messages sent to a specific recipient  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.recipient_router_get_all_messages_for_a_recipient(x_account_api_key, recipient, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_account_api_key: Account API Key (required)
        :param str recipient: email of the recipient (required)
        :return: list[ModelsQEmailMessage]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.recipient_router_get_all_messages_for_a_recipient_with_http_info(x_account_api_key, recipient, **kwargs)  # noqa: E501
        else:
            (data) = self.recipient_router_get_all_messages_for_a_recipient_with_http_info(x_account_api_key, recipient, **kwargs)  # noqa: E501
            return data

    def recipient_router_get_all_messages_for_a_recipient_with_http_info(self, x_account_api_key, recipient, **kwargs):  # noqa: E501
        """recipient_router_get_all_messages_for_a_recipient  # noqa: E501

        Find all messages sent to a specific recipient  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.recipient_router_get_all_messages_for_a_recipient_with_http_info(x_account_api_key, recipient, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_account_api_key: Account API Key (required)
        :param str recipient: email of the recipient (required)
        :return: list[ModelsQEmailMessage]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_account_api_key', 'recipient']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method recipient_router_get_all_messages_for_a_recipient" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_account_api_key' is set
        if ('x_account_api_key' not in params or
                params['x_account_api_key'] is None):
            raise ValueError("Missing the required parameter `x_account_api_key` when calling `recipient_router_get_all_messages_for_a_recipient`")  # noqa: E501
        # verify the required parameter 'recipient' is set
        if ('recipient' not in params or
                params['recipient'] is None):
            raise ValueError("Missing the required parameter `recipient` when calling `recipient_router_get_all_messages_for_a_recipient`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'recipient' in params:
            path_params['recipient'] = params['recipient']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_account_api_key' in params:
            header_params['X-Account-ApiKey'] = params['x_account_api_key']  # noqa: E501

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
            '/account/recipient/{recipient}/messages', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ModelsQEmailMessage]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def recipient_router_get_all_messages_for_a_recipient_from_a_node(self, x_account_api_key, recipient, **kwargs):  # noqa: E501
        """recipient_router_get_all_messages_for_a_recipient_from_a_node  # noqa: E501

        Find all message sent to a recipient from a specific node  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.recipient_router_get_all_messages_for_a_recipient_from_a_node(x_account_api_key, recipient, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_account_api_key: Account API Key (required)
        :param str recipient: email of the recipient (required)
        :return: list[ModelsQEmailMessage]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.recipient_router_get_all_messages_for_a_recipient_from_a_node_with_http_info(x_account_api_key, recipient, **kwargs)  # noqa: E501
        else:
            (data) = self.recipient_router_get_all_messages_for_a_recipient_from_a_node_with_http_info(x_account_api_key, recipient, **kwargs)  # noqa: E501
            return data

    def recipient_router_get_all_messages_for_a_recipient_from_a_node_with_http_info(self, x_account_api_key, recipient, **kwargs):  # noqa: E501
        """recipient_router_get_all_messages_for_a_recipient_from_a_node  # noqa: E501

        Find all message sent to a recipient from a specific node  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.recipient_router_get_all_messages_for_a_recipient_from_a_node_with_http_info(x_account_api_key, recipient, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_account_api_key: Account API Key (required)
        :param str recipient: email of the recipient (required)
        :return: list[ModelsQEmailMessage]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_account_api_key', 'recipient']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method recipient_router_get_all_messages_for_a_recipient_from_a_node" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_account_api_key' is set
        if ('x_account_api_key' not in params or
                params['x_account_api_key'] is None):
            raise ValueError("Missing the required parameter `x_account_api_key` when calling `recipient_router_get_all_messages_for_a_recipient_from_a_node`")  # noqa: E501
        # verify the required parameter 'recipient' is set
        if ('recipient' not in params or
                params['recipient'] is None):
            raise ValueError("Missing the required parameter `recipient` when calling `recipient_router_get_all_messages_for_a_recipient_from_a_node`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'recipient' in params:
            path_params['recipient'] = params['recipient']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_account_api_key' in params:
            header_params['X-Account-ApiKey'] = params['x_account_api_key']  # noqa: E501

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
            '/account/recipient/node/{recipient}/messages', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ModelsQEmailMessage]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
