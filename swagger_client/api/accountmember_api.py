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


class AccountmemberApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def member_router_delete(self, x_account_api_key, member_id, **kwargs):  # noqa: E501
        """member_router_delete  # noqa: E501

        Delete Member  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.member_router_delete(x_account_api_key, member_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_account_api_key: Account API Key (required)
        :param int member_id: The MemberId you want to delete (required)
        :return: ModelsDeleteResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.member_router_delete_with_http_info(x_account_api_key, member_id, **kwargs)  # noqa: E501
        else:
            (data) = self.member_router_delete_with_http_info(x_account_api_key, member_id, **kwargs)  # noqa: E501
            return data

    def member_router_delete_with_http_info(self, x_account_api_key, member_id, **kwargs):  # noqa: E501
        """member_router_delete  # noqa: E501

        Delete Member  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.member_router_delete_with_http_info(x_account_api_key, member_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_account_api_key: Account API Key (required)
        :param int member_id: The MemberId you want to delete (required)
        :return: ModelsDeleteResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_account_api_key', 'member_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method member_router_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_account_api_key' is set
        if ('x_account_api_key' not in params or
                params['x_account_api_key'] is None):
            raise ValueError("Missing the required parameter `x_account_api_key` when calling `member_router_delete`")  # noqa: E501
        # verify the required parameter 'member_id' is set
        if ('member_id' not in params or
                params['member_id'] is None):
            raise ValueError("Missing the required parameter `member_id` when calling `member_router_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'member_id' in params:
            path_params['memberId'] = params['member_id']  # noqa: E501

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
            '/account/member/{memberId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ModelsDeleteResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def member_router_get(self, x_account_api_key, member_id, **kwargs):  # noqa: E501
        """member_router_get  # noqa: E501

        Find Member by MemberId  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.member_router_get(x_account_api_key, member_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_account_api_key: Account API Key (required)
        :param int member_id: the MemberId you want to get (required)
        :return: ModelsMember
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.member_router_get_with_http_info(x_account_api_key, member_id, **kwargs)  # noqa: E501
        else:
            (data) = self.member_router_get_with_http_info(x_account_api_key, member_id, **kwargs)  # noqa: E501
            return data

    def member_router_get_with_http_info(self, x_account_api_key, member_id, **kwargs):  # noqa: E501
        """member_router_get  # noqa: E501

        Find Member by MemberId  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.member_router_get_with_http_info(x_account_api_key, member_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_account_api_key: Account API Key (required)
        :param int member_id: the MemberId you want to get (required)
        :return: ModelsMember
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_account_api_key', 'member_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method member_router_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_account_api_key' is set
        if ('x_account_api_key' not in params or
                params['x_account_api_key'] is None):
            raise ValueError("Missing the required parameter `x_account_api_key` when calling `member_router_get`")  # noqa: E501
        # verify the required parameter 'member_id' is set
        if ('member_id' not in params or
                params['member_id'] is None):
            raise ValueError("Missing the required parameter `member_id` when calling `member_router_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'member_id' in params:
            path_params['memberId'] = params['member_id']  # noqa: E501

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
            '/account/member/{memberId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ModelsMember',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def member_router_get_all(self, x_account_api_key, **kwargs):  # noqa: E501
        """member_router_get_all  # noqa: E501

        Get All Members  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.member_router_get_all(x_account_api_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_account_api_key: Account API Key (required)
        :return: list[ModelsMember]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.member_router_get_all_with_http_info(x_account_api_key, **kwargs)  # noqa: E501
        else:
            (data) = self.member_router_get_all_with_http_info(x_account_api_key, **kwargs)  # noqa: E501
            return data

    def member_router_get_all_with_http_info(self, x_account_api_key, **kwargs):  # noqa: E501
        """member_router_get_all  # noqa: E501

        Get All Members  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.member_router_get_all_with_http_info(x_account_api_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_account_api_key: Account API Key (required)
        :return: list[ModelsMember]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_account_api_key']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method member_router_get_all" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_account_api_key' is set
        if ('x_account_api_key' not in params or
                params['x_account_api_key'] is None):
            raise ValueError("Missing the required parameter `x_account_api_key` when calling `member_router_get_all`")  # noqa: E501

        collection_formats = {}

        path_params = {}

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
            '/account/member/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ModelsMember]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
