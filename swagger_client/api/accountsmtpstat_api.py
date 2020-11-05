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


class AccountsmtpstatApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def s_mtp_stat_router_get_all_aggregate_ip_provider_smtp_stats(self, x_account_api_key, ipid, pname, **kwargs):  # noqa: E501
        """s_mtp_stat_router_get_all_aggregate_ip_provider_smtp_stats  # noqa: E501

        Get All Aggregate IP Provider SMTP Stats  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.s_mtp_stat_router_get_all_aggregate_ip_provider_smtp_stats(x_account_api_key, ipid, pname, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_account_api_key: Account API Key (required)
        :param int ipid: the IP ID you want to get (required)
        :param str pname: the provider name (required)
        :param str _from: from date
        :param str to: to date
        :return: list[ModelsSMTPStat]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.s_mtp_stat_router_get_all_aggregate_ip_provider_smtp_stats_with_http_info(x_account_api_key, ipid, pname, **kwargs)  # noqa: E501
        else:
            (data) = self.s_mtp_stat_router_get_all_aggregate_ip_provider_smtp_stats_with_http_info(x_account_api_key, ipid, pname, **kwargs)  # noqa: E501
            return data

    def s_mtp_stat_router_get_all_aggregate_ip_provider_smtp_stats_with_http_info(self, x_account_api_key, ipid, pname, **kwargs):  # noqa: E501
        """s_mtp_stat_router_get_all_aggregate_ip_provider_smtp_stats  # noqa: E501

        Get All Aggregate IP Provider SMTP Stats  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.s_mtp_stat_router_get_all_aggregate_ip_provider_smtp_stats_with_http_info(x_account_api_key, ipid, pname, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_account_api_key: Account API Key (required)
        :param int ipid: the IP ID you want to get (required)
        :param str pname: the provider name (required)
        :param str _from: from date
        :param str to: to date
        :return: list[ModelsSMTPStat]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_account_api_key', 'ipid', 'pname', '_from', 'to']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method s_mtp_stat_router_get_all_aggregate_ip_provider_smtp_stats" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_account_api_key' is set
        if ('x_account_api_key' not in params or
                params['x_account_api_key'] is None):
            raise ValueError("Missing the required parameter `x_account_api_key` when calling `s_mtp_stat_router_get_all_aggregate_ip_provider_smtp_stats`")  # noqa: E501
        # verify the required parameter 'ipid' is set
        if ('ipid' not in params or
                params['ipid'] is None):
            raise ValueError("Missing the required parameter `ipid` when calling `s_mtp_stat_router_get_all_aggregate_ip_provider_smtp_stats`")  # noqa: E501
        # verify the required parameter 'pname' is set
        if ('pname' not in params or
                params['pname'] is None):
            raise ValueError("Missing the required parameter `pname` when calling `s_mtp_stat_router_get_all_aggregate_ip_provider_smtp_stats`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'ipid' in params:
            path_params['ipid'] = params['ipid']  # noqa: E501
        if 'pname' in params:
            path_params['pname'] = params['pname']  # noqa: E501

        query_params = []
        if '_from' in params:
            query_params.append(('from', params['_from']))  # noqa: E501
        if 'to' in params:
            query_params.append(('to', params['to']))  # noqa: E501

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
            '/account/smtp/stat/ip/{ipid}/provider/{pname}/aggregate', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ModelsSMTPStat]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def s_mtp_stat_router_get_all_aggregate_ip_smtp_stats(self, x_account_api_key, ipid, **kwargs):  # noqa: E501
        """s_mtp_stat_router_get_all_aggregate_ip_smtp_stats  # noqa: E501

        Get All Aggregate IP SMTP Stats  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.s_mtp_stat_router_get_all_aggregate_ip_smtp_stats(x_account_api_key, ipid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_account_api_key: Account API Key (required)
        :param int ipid: the IPId you want to get (required)
        :param str _from: from date
        :param str to: to date
        :return: list[ModelsSMTPStat]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.s_mtp_stat_router_get_all_aggregate_ip_smtp_stats_with_http_info(x_account_api_key, ipid, **kwargs)  # noqa: E501
        else:
            (data) = self.s_mtp_stat_router_get_all_aggregate_ip_smtp_stats_with_http_info(x_account_api_key, ipid, **kwargs)  # noqa: E501
            return data

    def s_mtp_stat_router_get_all_aggregate_ip_smtp_stats_with_http_info(self, x_account_api_key, ipid, **kwargs):  # noqa: E501
        """s_mtp_stat_router_get_all_aggregate_ip_smtp_stats  # noqa: E501

        Get All Aggregate IP SMTP Stats  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.s_mtp_stat_router_get_all_aggregate_ip_smtp_stats_with_http_info(x_account_api_key, ipid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_account_api_key: Account API Key (required)
        :param int ipid: the IPId you want to get (required)
        :param str _from: from date
        :param str to: to date
        :return: list[ModelsSMTPStat]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_account_api_key', 'ipid', '_from', 'to']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method s_mtp_stat_router_get_all_aggregate_ip_smtp_stats" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_account_api_key' is set
        if ('x_account_api_key' not in params or
                params['x_account_api_key'] is None):
            raise ValueError("Missing the required parameter `x_account_api_key` when calling `s_mtp_stat_router_get_all_aggregate_ip_smtp_stats`")  # noqa: E501
        # verify the required parameter 'ipid' is set
        if ('ipid' not in params or
                params['ipid'] is None):
            raise ValueError("Missing the required parameter `ipid` when calling `s_mtp_stat_router_get_all_aggregate_ip_smtp_stats`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'ipid' in params:
            path_params['ipid'] = params['ipid']  # noqa: E501

        query_params = []
        if '_from' in params:
            query_params.append(('from', params['_from']))  # noqa: E501
        if 'to' in params:
            query_params.append(('to', params['to']))  # noqa: E501

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
            '/account/smtp/stat/ip/{ipid}/aggregate', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ModelsSMTPStat]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def s_mtp_stat_router_get_all_aggregate_ip_smtp_stats_for_sub_account(self, x_account_api_key, ipid, sid, **kwargs):  # noqa: E501
        """s_mtp_stat_router_get_all_aggregate_ip_smtp_stats_for_sub_account  # noqa: E501

        Get All Aggregate IP SMTP Stats For SubAccount  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.s_mtp_stat_router_get_all_aggregate_ip_smtp_stats_for_sub_account(x_account_api_key, ipid, sid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_account_api_key: Account API Key (required)
        :param int ipid: the IP ID you want to get (required)
        :param int sid: the SubAccount ID you want to get (required)
        :param str _from: from date
        :param str to: to date
        :return: list[ModelsSMTPStat]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.s_mtp_stat_router_get_all_aggregate_ip_smtp_stats_for_sub_account_with_http_info(x_account_api_key, ipid, sid, **kwargs)  # noqa: E501
        else:
            (data) = self.s_mtp_stat_router_get_all_aggregate_ip_smtp_stats_for_sub_account_with_http_info(x_account_api_key, ipid, sid, **kwargs)  # noqa: E501
            return data

    def s_mtp_stat_router_get_all_aggregate_ip_smtp_stats_for_sub_account_with_http_info(self, x_account_api_key, ipid, sid, **kwargs):  # noqa: E501
        """s_mtp_stat_router_get_all_aggregate_ip_smtp_stats_for_sub_account  # noqa: E501

        Get All Aggregate IP SMTP Stats For SubAccount  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.s_mtp_stat_router_get_all_aggregate_ip_smtp_stats_for_sub_account_with_http_info(x_account_api_key, ipid, sid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_account_api_key: Account API Key (required)
        :param int ipid: the IP ID you want to get (required)
        :param int sid: the SubAccount ID you want to get (required)
        :param str _from: from date
        :param str to: to date
        :return: list[ModelsSMTPStat]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_account_api_key', 'ipid', 'sid', '_from', 'to']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method s_mtp_stat_router_get_all_aggregate_ip_smtp_stats_for_sub_account" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_account_api_key' is set
        if ('x_account_api_key' not in params or
                params['x_account_api_key'] is None):
            raise ValueError("Missing the required parameter `x_account_api_key` when calling `s_mtp_stat_router_get_all_aggregate_ip_smtp_stats_for_sub_account`")  # noqa: E501
        # verify the required parameter 'ipid' is set
        if ('ipid' not in params or
                params['ipid'] is None):
            raise ValueError("Missing the required parameter `ipid` when calling `s_mtp_stat_router_get_all_aggregate_ip_smtp_stats_for_sub_account`")  # noqa: E501
        # verify the required parameter 'sid' is set
        if ('sid' not in params or
                params['sid'] is None):
            raise ValueError("Missing the required parameter `sid` when calling `s_mtp_stat_router_get_all_aggregate_ip_smtp_stats_for_sub_account`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'ipid' in params:
            path_params['ipid'] = params['ipid']  # noqa: E501
        if 'sid' in params:
            path_params['sid'] = params['sid']  # noqa: E501

        query_params = []
        if '_from' in params:
            query_params.append(('from', params['_from']))  # noqa: E501
        if 'to' in params:
            query_params.append(('to', params['to']))  # noqa: E501

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
            '/account/smtp/stat/ip/{ipid}/subaccount/{sid}/aggregate', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ModelsSMTPStat]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def s_mtp_stat_router_get_all_aggregate_sub_account_provider_smtp_stats(self, x_account_api_key, sid, pname, **kwargs):  # noqa: E501
        """s_mtp_stat_router_get_all_aggregate_sub_account_provider_smtp_stats  # noqa: E501

        Get All Aggregate SubAccount Provider SMTP Stats  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.s_mtp_stat_router_get_all_aggregate_sub_account_provider_smtp_stats(x_account_api_key, sid, pname, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_account_api_key: Account API Key (required)
        :param int sid: the SubAccount ID you want to get (required)
        :param str pname: the provider name (required)
        :param str _from: from date
        :param str to: to date
        :return: list[ModelsSMTPStat]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.s_mtp_stat_router_get_all_aggregate_sub_account_provider_smtp_stats_with_http_info(x_account_api_key, sid, pname, **kwargs)  # noqa: E501
        else:
            (data) = self.s_mtp_stat_router_get_all_aggregate_sub_account_provider_smtp_stats_with_http_info(x_account_api_key, sid, pname, **kwargs)  # noqa: E501
            return data

    def s_mtp_stat_router_get_all_aggregate_sub_account_provider_smtp_stats_with_http_info(self, x_account_api_key, sid, pname, **kwargs):  # noqa: E501
        """s_mtp_stat_router_get_all_aggregate_sub_account_provider_smtp_stats  # noqa: E501

        Get All Aggregate SubAccount Provider SMTP Stats  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.s_mtp_stat_router_get_all_aggregate_sub_account_provider_smtp_stats_with_http_info(x_account_api_key, sid, pname, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_account_api_key: Account API Key (required)
        :param int sid: the SubAccount ID you want to get (required)
        :param str pname: the provider name (required)
        :param str _from: from date
        :param str to: to date
        :return: list[ModelsSMTPStat]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_account_api_key', 'sid', 'pname', '_from', 'to']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method s_mtp_stat_router_get_all_aggregate_sub_account_provider_smtp_stats" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_account_api_key' is set
        if ('x_account_api_key' not in params or
                params['x_account_api_key'] is None):
            raise ValueError("Missing the required parameter `x_account_api_key` when calling `s_mtp_stat_router_get_all_aggregate_sub_account_provider_smtp_stats`")  # noqa: E501
        # verify the required parameter 'sid' is set
        if ('sid' not in params or
                params['sid'] is None):
            raise ValueError("Missing the required parameter `sid` when calling `s_mtp_stat_router_get_all_aggregate_sub_account_provider_smtp_stats`")  # noqa: E501
        # verify the required parameter 'pname' is set
        if ('pname' not in params or
                params['pname'] is None):
            raise ValueError("Missing the required parameter `pname` when calling `s_mtp_stat_router_get_all_aggregate_sub_account_provider_smtp_stats`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'sid' in params:
            path_params['sid'] = params['sid']  # noqa: E501
        if 'pname' in params:
            path_params['pname'] = params['pname']  # noqa: E501

        query_params = []
        if '_from' in params:
            query_params.append(('from', params['_from']))  # noqa: E501
        if 'to' in params:
            query_params.append(('to', params['to']))  # noqa: E501

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
            '/account/smtp/stat/subaccount/{sid}/provider/{pname}/aggregate', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ModelsSMTPStat]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def s_mtp_stat_router_get_all_aggregate_sub_account_smtp_stats(self, x_account_api_key, sid, **kwargs):  # noqa: E501
        """s_mtp_stat_router_get_all_aggregate_sub_account_smtp_stats  # noqa: E501

        Get All Aggregate SubAccount SMTP Stats  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.s_mtp_stat_router_get_all_aggregate_sub_account_smtp_stats(x_account_api_key, sid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_account_api_key: Account API Key (required)
        :param int sid: the Sub-Account ID you want to get (required)
        :param str _from: from date
        :param str to: to date
        :return: list[ModelsSMTPStat]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.s_mtp_stat_router_get_all_aggregate_sub_account_smtp_stats_with_http_info(x_account_api_key, sid, **kwargs)  # noqa: E501
        else:
            (data) = self.s_mtp_stat_router_get_all_aggregate_sub_account_smtp_stats_with_http_info(x_account_api_key, sid, **kwargs)  # noqa: E501
            return data

    def s_mtp_stat_router_get_all_aggregate_sub_account_smtp_stats_with_http_info(self, x_account_api_key, sid, **kwargs):  # noqa: E501
        """s_mtp_stat_router_get_all_aggregate_sub_account_smtp_stats  # noqa: E501

        Get All Aggregate SubAccount SMTP Stats  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.s_mtp_stat_router_get_all_aggregate_sub_account_smtp_stats_with_http_info(x_account_api_key, sid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_account_api_key: Account API Key (required)
        :param int sid: the Sub-Account ID you want to get (required)
        :param str _from: from date
        :param str to: to date
        :return: list[ModelsSMTPStat]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_account_api_key', 'sid', '_from', 'to']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method s_mtp_stat_router_get_all_aggregate_sub_account_smtp_stats" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_account_api_key' is set
        if ('x_account_api_key' not in params or
                params['x_account_api_key'] is None):
            raise ValueError("Missing the required parameter `x_account_api_key` when calling `s_mtp_stat_router_get_all_aggregate_sub_account_smtp_stats`")  # noqa: E501
        # verify the required parameter 'sid' is set
        if ('sid' not in params or
                params['sid'] is None):
            raise ValueError("Missing the required parameter `sid` when calling `s_mtp_stat_router_get_all_aggregate_sub_account_smtp_stats`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'sid' in params:
            path_params['sid'] = params['sid']  # noqa: E501

        query_params = []
        if '_from' in params:
            query_params.append(('from', params['_from']))  # noqa: E501
        if 'to' in params:
            query_params.append(('to', params['to']))  # noqa: E501

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
            '/account/smtp/stat/subaccount/{sid}/aggregate', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ModelsSMTPStat]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def s_mtp_stat_router_get_all_aggregate_sub_account_smtp_stats_for_ip(self, x_account_api_key, sid, ipid, **kwargs):  # noqa: E501
        """s_mtp_stat_router_get_all_aggregate_sub_account_smtp_stats_for_ip  # noqa: E501

        Get All Aggregate SubAccount SMTP Stats For IP  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.s_mtp_stat_router_get_all_aggregate_sub_account_smtp_stats_for_ip(x_account_api_key, sid, ipid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_account_api_key: Account API Key (required)
        :param int sid: the Sub-Account ID you want to get (required)
        :param int ipid: the IP  ID you want to get (required)
        :param str _from: from date
        :param str to: to date
        :return: list[ModelsSMTPStat]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.s_mtp_stat_router_get_all_aggregate_sub_account_smtp_stats_for_ip_with_http_info(x_account_api_key, sid, ipid, **kwargs)  # noqa: E501
        else:
            (data) = self.s_mtp_stat_router_get_all_aggregate_sub_account_smtp_stats_for_ip_with_http_info(x_account_api_key, sid, ipid, **kwargs)  # noqa: E501
            return data

    def s_mtp_stat_router_get_all_aggregate_sub_account_smtp_stats_for_ip_with_http_info(self, x_account_api_key, sid, ipid, **kwargs):  # noqa: E501
        """s_mtp_stat_router_get_all_aggregate_sub_account_smtp_stats_for_ip  # noqa: E501

        Get All Aggregate SubAccount SMTP Stats For IP  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.s_mtp_stat_router_get_all_aggregate_sub_account_smtp_stats_for_ip_with_http_info(x_account_api_key, sid, ipid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_account_api_key: Account API Key (required)
        :param int sid: the Sub-Account ID you want to get (required)
        :param int ipid: the IP  ID you want to get (required)
        :param str _from: from date
        :param str to: to date
        :return: list[ModelsSMTPStat]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_account_api_key', 'sid', 'ipid', '_from', 'to']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method s_mtp_stat_router_get_all_aggregate_sub_account_smtp_stats_for_ip" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_account_api_key' is set
        if ('x_account_api_key' not in params or
                params['x_account_api_key'] is None):
            raise ValueError("Missing the required parameter `x_account_api_key` when calling `s_mtp_stat_router_get_all_aggregate_sub_account_smtp_stats_for_ip`")  # noqa: E501
        # verify the required parameter 'sid' is set
        if ('sid' not in params or
                params['sid'] is None):
            raise ValueError("Missing the required parameter `sid` when calling `s_mtp_stat_router_get_all_aggregate_sub_account_smtp_stats_for_ip`")  # noqa: E501
        # verify the required parameter 'ipid' is set
        if ('ipid' not in params or
                params['ipid'] is None):
            raise ValueError("Missing the required parameter `ipid` when calling `s_mtp_stat_router_get_all_aggregate_sub_account_smtp_stats_for_ip`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'sid' in params:
            path_params['sid'] = params['sid']  # noqa: E501
        if 'ipid' in params:
            path_params['ipid'] = params['ipid']  # noqa: E501

        query_params = []
        if '_from' in params:
            query_params.append(('from', params['_from']))  # noqa: E501
        if 'to' in params:
            query_params.append(('to', params['to']))  # noqa: E501

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
            '/account/smtp/stat/subaccount/{sid}/ip/{ipid}/aggregate', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ModelsSMTPStat]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
