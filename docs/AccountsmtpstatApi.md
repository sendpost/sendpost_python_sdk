# swagger_client.AccountsmtpstatApi

All URIs are relative to *https://api.sendpost.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**s_mtp_stat_router_get_all_aggregate_ip_provider_smtp_stats**](AccountsmtpstatApi.md#s_mtp_stat_router_get_all_aggregate_ip_provider_smtp_stats) | **GET** /account/smtp/stat/ip/{ipid}/provider/{pname}/aggregate | 
[**s_mtp_stat_router_get_all_aggregate_ip_smtp_stats**](AccountsmtpstatApi.md#s_mtp_stat_router_get_all_aggregate_ip_smtp_stats) | **GET** /account/smtp/stat/ip/{ipid}/aggregate | 
[**s_mtp_stat_router_get_all_aggregate_ip_smtp_stats_for_sub_account**](AccountsmtpstatApi.md#s_mtp_stat_router_get_all_aggregate_ip_smtp_stats_for_sub_account) | **GET** /account/smtp/stat/ip/{ipid}/subaccount/{sid}/aggregate | 
[**s_mtp_stat_router_get_all_aggregate_sub_account_provider_smtp_stats**](AccountsmtpstatApi.md#s_mtp_stat_router_get_all_aggregate_sub_account_provider_smtp_stats) | **GET** /account/smtp/stat/subaccount/{sid}/provider/{pname}/aggregate | 
[**s_mtp_stat_router_get_all_aggregate_sub_account_smtp_stats**](AccountsmtpstatApi.md#s_mtp_stat_router_get_all_aggregate_sub_account_smtp_stats) | **GET** /account/smtp/stat/subaccount/{sid}/aggregate | 
[**s_mtp_stat_router_get_all_aggregate_sub_account_smtp_stats_for_ip**](AccountsmtpstatApi.md#s_mtp_stat_router_get_all_aggregate_sub_account_smtp_stats_for_ip) | **GET** /account/smtp/stat/subaccount/{sid}/ip/{ipid}/aggregate | 


# **s_mtp_stat_router_get_all_aggregate_ip_provider_smtp_stats**
> list[ModelsSMTPStat] s_mtp_stat_router_get_all_aggregate_ip_provider_smtp_stats(x_account_api_key, ipid, pname, _from=_from, to=to)



Get All Aggregate IP Provider SMTP Stats

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountsmtpstatApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key
ipid = 789 # int | the IP ID you want to get
pname = 'pname_example' # str | the provider name
_from = '_from_example' # str | from date (optional)
to = 'to_example' # str | to date (optional)

try:
    api_response = api_instance.s_mtp_stat_router_get_all_aggregate_ip_provider_smtp_stats(x_account_api_key, ipid, pname, _from=_from, to=to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsmtpstatApi->s_mtp_stat_router_get_all_aggregate_ip_provider_smtp_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 
 **ipid** | **int**| the IP ID you want to get | 
 **pname** | **str**| the provider name | 
 **_from** | **str**| from date | [optional] 
 **to** | **str**| to date | [optional] 

### Return type

[**list[ModelsSMTPStat]**](ModelsSMTPStat.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **s_mtp_stat_router_get_all_aggregate_ip_smtp_stats**
> list[ModelsSMTPStat] s_mtp_stat_router_get_all_aggregate_ip_smtp_stats(x_account_api_key, ipid, _from=_from, to=to)



Get All Aggregate IP SMTP Stats

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountsmtpstatApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key
ipid = 789 # int | the IPId you want to get
_from = '_from_example' # str | from date (optional)
to = 'to_example' # str | to date (optional)

try:
    api_response = api_instance.s_mtp_stat_router_get_all_aggregate_ip_smtp_stats(x_account_api_key, ipid, _from=_from, to=to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsmtpstatApi->s_mtp_stat_router_get_all_aggregate_ip_smtp_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 
 **ipid** | **int**| the IPId you want to get | 
 **_from** | **str**| from date | [optional] 
 **to** | **str**| to date | [optional] 

### Return type

[**list[ModelsSMTPStat]**](ModelsSMTPStat.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **s_mtp_stat_router_get_all_aggregate_ip_smtp_stats_for_sub_account**
> list[ModelsSMTPStat] s_mtp_stat_router_get_all_aggregate_ip_smtp_stats_for_sub_account(x_account_api_key, ipid, sid, _from=_from, to=to)



Get All Aggregate IP SMTP Stats For SubAccount

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountsmtpstatApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key
ipid = 789 # int | the IP ID you want to get
sid = 789 # int | the SubAccount ID you want to get
_from = '_from_example' # str | from date (optional)
to = 'to_example' # str | to date (optional)

try:
    api_response = api_instance.s_mtp_stat_router_get_all_aggregate_ip_smtp_stats_for_sub_account(x_account_api_key, ipid, sid, _from=_from, to=to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsmtpstatApi->s_mtp_stat_router_get_all_aggregate_ip_smtp_stats_for_sub_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 
 **ipid** | **int**| the IP ID you want to get | 
 **sid** | **int**| the SubAccount ID you want to get | 
 **_from** | **str**| from date | [optional] 
 **to** | **str**| to date | [optional] 

### Return type

[**list[ModelsSMTPStat]**](ModelsSMTPStat.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **s_mtp_stat_router_get_all_aggregate_sub_account_provider_smtp_stats**
> list[ModelsSMTPStat] s_mtp_stat_router_get_all_aggregate_sub_account_provider_smtp_stats(x_account_api_key, sid, pname, _from=_from, to=to)



Get All Aggregate SubAccount Provider SMTP Stats

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountsmtpstatApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key
sid = 789 # int | the SubAccount ID you want to get
pname = 'pname_example' # str | the provider name
_from = '_from_example' # str | from date (optional)
to = 'to_example' # str | to date (optional)

try:
    api_response = api_instance.s_mtp_stat_router_get_all_aggregate_sub_account_provider_smtp_stats(x_account_api_key, sid, pname, _from=_from, to=to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsmtpstatApi->s_mtp_stat_router_get_all_aggregate_sub_account_provider_smtp_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 
 **sid** | **int**| the SubAccount ID you want to get | 
 **pname** | **str**| the provider name | 
 **_from** | **str**| from date | [optional] 
 **to** | **str**| to date | [optional] 

### Return type

[**list[ModelsSMTPStat]**](ModelsSMTPStat.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **s_mtp_stat_router_get_all_aggregate_sub_account_smtp_stats**
> list[ModelsSMTPStat] s_mtp_stat_router_get_all_aggregate_sub_account_smtp_stats(x_account_api_key, sid, _from=_from, to=to)



Get All Aggregate SubAccount SMTP Stats

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountsmtpstatApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key
sid = 789 # int | the Sub-Account ID you want to get
_from = '_from_example' # str | from date (optional)
to = 'to_example' # str | to date (optional)

try:
    api_response = api_instance.s_mtp_stat_router_get_all_aggregate_sub_account_smtp_stats(x_account_api_key, sid, _from=_from, to=to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsmtpstatApi->s_mtp_stat_router_get_all_aggregate_sub_account_smtp_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 
 **sid** | **int**| the Sub-Account ID you want to get | 
 **_from** | **str**| from date | [optional] 
 **to** | **str**| to date | [optional] 

### Return type

[**list[ModelsSMTPStat]**](ModelsSMTPStat.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **s_mtp_stat_router_get_all_aggregate_sub_account_smtp_stats_for_ip**
> list[ModelsSMTPStat] s_mtp_stat_router_get_all_aggregate_sub_account_smtp_stats_for_ip(x_account_api_key, sid, ipid, _from=_from, to=to)



Get All Aggregate SubAccount SMTP Stats For IP

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountsmtpstatApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key
sid = 789 # int | the Sub-Account ID you want to get
ipid = 789 # int | the IP  ID you want to get
_from = '_from_example' # str | from date (optional)
to = 'to_example' # str | to date (optional)

try:
    api_response = api_instance.s_mtp_stat_router_get_all_aggregate_sub_account_smtp_stats_for_ip(x_account_api_key, sid, ipid, _from=_from, to=to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsmtpstatApi->s_mtp_stat_router_get_all_aggregate_sub_account_smtp_stats_for_ip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 
 **sid** | **int**| the Sub-Account ID you want to get | 
 **ipid** | **int**| the IP  ID you want to get | 
 **_from** | **str**| from date | [optional] 
 **to** | **str**| to date | [optional] 

### Return type

[**list[ModelsSMTPStat]**](ModelsSMTPStat.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

