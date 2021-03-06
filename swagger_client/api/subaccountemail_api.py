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


class SubaccountemailApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def email_router_send_email(self, x_sub_account_api_key, body, **kwargs):  # noqa: E501
        """email_router_send_email  # noqa: E501

        Send Email To Contacts  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.email_router_send_email(x_sub_account_api_key, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_sub_account_api_key: Sub-Account API Key (required)
        :param ModelsEmailMessage body: The Email Message (required)
        :return: list[ModelsEmailResponse]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.email_router_send_email_with_http_info(x_sub_account_api_key, body, **kwargs)  # noqa: E501
        else:
            (data) = self.email_router_send_email_with_http_info(x_sub_account_api_key, body, **kwargs)  # noqa: E501
            return data

    def email_router_send_email_with_http_info(self, x_sub_account_api_key, body, **kwargs):  # noqa: E501
        """email_router_send_email  # noqa: E501

        Send Email To Contacts  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.email_router_send_email_with_http_info(x_sub_account_api_key, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_sub_account_api_key: Sub-Account API Key (required)
        :param ModelsEmailMessage body: The Email Message (required)
        :return: list[ModelsEmailResponse]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_sub_account_api_key', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method email_router_send_email" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_sub_account_api_key' is set
        if ('x_sub_account_api_key' not in params or
                params['x_sub_account_api_key'] is None):
            raise ValueError("Missing the required parameter `x_sub_account_api_key` when calling `email_router_send_email`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `email_router_send_email`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_sub_account_api_key' in params:
            header_params['X-SubAccount-ApiKey'] = params['x_sub_account_api_key']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/subaccount/email/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ModelsEmailResponse]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def email_router_send_email_with_template(self, x_sub_account_api_key, body, **kwargs):  # noqa: E501
        """email_router_send_email_with_template  # noqa: E501

        Send Email To Contacts With Template  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.email_router_send_email_with_template(x_sub_account_api_key, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_sub_account_api_key: Sub-Account API Key (required)
        :param ModelsEmailMessage body: The Email Message (required)
        :return: list[ModelsEmailResponse]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.email_router_send_email_with_template_with_http_info(x_sub_account_api_key, body, **kwargs)  # noqa: E501
        else:
            (data) = self.email_router_send_email_with_template_with_http_info(x_sub_account_api_key, body, **kwargs)  # noqa: E501
            return data

    def email_router_send_email_with_template_with_http_info(self, x_sub_account_api_key, body, **kwargs):  # noqa: E501
        """email_router_send_email_with_template  # noqa: E501

        Send Email To Contacts With Template  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.email_router_send_email_with_template_with_http_info(x_sub_account_api_key, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_sub_account_api_key: Sub-Account API Key (required)
        :param ModelsEmailMessage body: The Email Message (required)
        :return: list[ModelsEmailResponse]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_sub_account_api_key', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method email_router_send_email_with_template" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_sub_account_api_key' is set
        if ('x_sub_account_api_key' not in params or
                params['x_sub_account_api_key'] is None):
            raise ValueError("Missing the required parameter `x_sub_account_api_key` when calling `email_router_send_email_with_template`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `email_router_send_email_with_template`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_sub_account_api_key' in params:
            header_params['X-SubAccount-ApiKey'] = params['x_sub_account_api_key']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/subaccount/email/template', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ModelsEmailResponse]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
