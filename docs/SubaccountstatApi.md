# swagger_client.SubaccountstatApi

All URIs are relative to *https://api.sendpost.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sub_account_stat_router_get_all_aggregate_sub_account_stats**](SubaccountstatApi.md#sub_account_stat_router_get_all_aggregate_sub_account_stats) | **GET** /subaccount/stat/aggregate | 
[**sub_account_stat_router_get_all_aggregate_sub_account_stats_by_group**](SubaccountstatApi.md#sub_account_stat_router_get_all_aggregate_sub_account_stats_by_group) | **GET** /subaccount/stat/aggregate/group | 
[**sub_account_stat_router_get_all_aggregated_group_stats_for_a_sub_account**](SubaccountstatApi.md#sub_account_stat_router_get_all_aggregated_group_stats_for_a_sub_account) | **GET** /subaccount/stat/aggregate/groups | 
[**sub_account_stat_router_get_all_aggregated_ip_stats_for_a_sub_account**](SubaccountstatApi.md#sub_account_stat_router_get_all_aggregated_ip_stats_for_a_sub_account) | **GET** /subaccount/stat/aggregate/ips | 
[**sub_account_stat_router_get_all_aggregated_provider_stats_for_a_specific_ip_of_a_sub_account**](SubaccountstatApi.md#sub_account_stat_router_get_all_aggregated_provider_stats_for_a_specific_ip_of_a_sub_account) | **GET** /subaccount/stat/aggregate/ip/{ipid}/providers | 
[**sub_account_stat_router_get_all_aggregated_provider_stats_for_a_sub_account**](SubaccountstatApi.md#sub_account_stat_router_get_all_aggregated_provider_stats_for_a_sub_account) | **GET** /subaccount/stat/aggregate/providers | 
[**sub_account_stat_router_get_all_sub_account_stats**](SubaccountstatApi.md#sub_account_stat_router_get_all_sub_account_stats) | **GET** /subaccount/stat/ | 
[**sub_account_stat_router_get_all_sub_account_stats_by_group**](SubaccountstatApi.md#sub_account_stat_router_get_all_sub_account_stats_by_group) | **GET** /subaccount/stat/group | 


# **sub_account_stat_router_get_all_aggregate_sub_account_stats**
> ModelsStat sub_account_stat_router_get_all_aggregate_sub_account_stats(x_sub_account_api_key, _from=_from, to=to)



Get All Aggregate Sub-Account Stats

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubaccountstatApi()
x_sub_account_api_key = 'x_sub_account_api_key_example' # str | Sub-Account API Key
_from = '_from_example' # str | from date (optional)
to = 'to_example' # str | to date (optional)

try:
    api_response = api_instance.sub_account_stat_router_get_all_aggregate_sub_account_stats(x_sub_account_api_key, _from=_from, to=to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubaccountstatApi->sub_account_stat_router_get_all_aggregate_sub_account_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_sub_account_api_key** | **str**| Sub-Account API Key | 
 **_from** | **str**| from date | [optional] 
 **to** | **str**| to date | [optional] 

### Return type

[**ModelsStat**](ModelsStat.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sub_account_stat_router_get_all_aggregate_sub_account_stats_by_group**
> ModelsStat sub_account_stat_router_get_all_aggregate_sub_account_stats_by_group(x_sub_account_api_key, group, _from=_from, to=to)



Get All Aggregate Sub-Account Stats by Group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubaccountstatApi()
x_sub_account_api_key = 'x_sub_account_api_key_example' # str | Sub-Account API Key
group = 'group_example' # str | the group whose stats you want
_from = '_from_example' # str | from date (optional)
to = 'to_example' # str | to date (optional)

try:
    api_response = api_instance.sub_account_stat_router_get_all_aggregate_sub_account_stats_by_group(x_sub_account_api_key, group, _from=_from, to=to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubaccountstatApi->sub_account_stat_router_get_all_aggregate_sub_account_stats_by_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_sub_account_api_key** | **str**| Sub-Account API Key | 
 **group** | **str**| the group whose stats you want | 
 **_from** | **str**| from date | [optional] 
 **to** | **str**| to date | [optional] 

### Return type

[**ModelsStat**](ModelsStat.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sub_account_stat_router_get_all_aggregated_group_stats_for_a_sub_account**
> list[ModelsAGStat] sub_account_stat_router_get_all_aggregated_group_stats_for_a_sub_account(x_sub_account_api_key, _from=_from, to=to)



Get All Aggregated Group Stats for a Sub-Account

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubaccountstatApi()
x_sub_account_api_key = 'x_sub_account_api_key_example' # str | Sub-Account API Key
_from = '_from_example' # str | from date (optional)
to = 'to_example' # str | to date (optional)

try:
    api_response = api_instance.sub_account_stat_router_get_all_aggregated_group_stats_for_a_sub_account(x_sub_account_api_key, _from=_from, to=to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubaccountstatApi->sub_account_stat_router_get_all_aggregated_group_stats_for_a_sub_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_sub_account_api_key** | **str**| Sub-Account API Key | 
 **_from** | **str**| from date | [optional] 
 **to** | **str**| to date | [optional] 

### Return type

[**list[ModelsAGStat]**](ModelsAGStat.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sub_account_stat_router_get_all_aggregated_ip_stats_for_a_sub_account**
> list[ModelsAIPStat] sub_account_stat_router_get_all_aggregated_ip_stats_for_a_sub_account(x_sub_account_api_key, _from=_from, to=to)



Get All Aggregated IP Stats for a Sub-Account

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubaccountstatApi()
x_sub_account_api_key = 'x_sub_account_api_key_example' # str | Sub-Account API Key
_from = '_from_example' # str | from date (optional)
to = 'to_example' # str | to date (optional)

try:
    api_response = api_instance.sub_account_stat_router_get_all_aggregated_ip_stats_for_a_sub_account(x_sub_account_api_key, _from=_from, to=to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubaccountstatApi->sub_account_stat_router_get_all_aggregated_ip_stats_for_a_sub_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_sub_account_api_key** | **str**| Sub-Account API Key | 
 **_from** | **str**| from date | [optional] 
 **to** | **str**| to date | [optional] 

### Return type

[**list[ModelsAIPStat]**](ModelsAIPStat.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sub_account_stat_router_get_all_aggregated_provider_stats_for_a_specific_ip_of_a_sub_account**
> list[ModelsPIPStat] sub_account_stat_router_get_all_aggregated_provider_stats_for_a_specific_ip_of_a_sub_account(x_sub_account_api_key, ipid, _from=_from, to=to)



Get All Aggregated Provider Stats for a Specific IP of a Sub-Account

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubaccountstatApi()
x_sub_account_api_key = 'x_sub_account_api_key_example' # str | Sub-Account API Key
ipid = 789 # int | the IPId you want to get
_from = '_from_example' # str | from date (optional)
to = 'to_example' # str | to date (optional)

try:
    api_response = api_instance.sub_account_stat_router_get_all_aggregated_provider_stats_for_a_specific_ip_of_a_sub_account(x_sub_account_api_key, ipid, _from=_from, to=to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubaccountstatApi->sub_account_stat_router_get_all_aggregated_provider_stats_for_a_specific_ip_of_a_sub_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_sub_account_api_key** | **str**| Sub-Account API Key | 
 **ipid** | **int**| the IPId you want to get | 
 **_from** | **str**| from date | [optional] 
 **to** | **str**| to date | [optional] 

### Return type

[**list[ModelsPIPStat]**](ModelsPIPStat.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sub_account_stat_router_get_all_aggregated_provider_stats_for_a_sub_account**
> list[ModelsPIPStat] sub_account_stat_router_get_all_aggregated_provider_stats_for_a_sub_account(x_sub_account_api_key, _from=_from, to=to)



Get All Aggregated Provider Stats for a Sub-Account

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubaccountstatApi()
x_sub_account_api_key = 'x_sub_account_api_key_example' # str | Sub-Account API Key
_from = '_from_example' # str | from date (optional)
to = 'to_example' # str | to date (optional)

try:
    api_response = api_instance.sub_account_stat_router_get_all_aggregated_provider_stats_for_a_sub_account(x_sub_account_api_key, _from=_from, to=to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubaccountstatApi->sub_account_stat_router_get_all_aggregated_provider_stats_for_a_sub_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_sub_account_api_key** | **str**| Sub-Account API Key | 
 **_from** | **str**| from date | [optional] 
 **to** | **str**| to date | [optional] 

### Return type

[**list[ModelsPIPStat]**](ModelsPIPStat.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sub_account_stat_router_get_all_sub_account_stats**
> list[ModelsRStat] sub_account_stat_router_get_all_sub_account_stats(x_sub_account_api_key, _from=_from, to=to)



Get All Sub-Account Stats

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubaccountstatApi()
x_sub_account_api_key = 'x_sub_account_api_key_example' # str | Sub-Account API Key
_from = '_from_example' # str | from date (optional)
to = 'to_example' # str | to date (optional)

try:
    api_response = api_instance.sub_account_stat_router_get_all_sub_account_stats(x_sub_account_api_key, _from=_from, to=to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubaccountstatApi->sub_account_stat_router_get_all_sub_account_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_sub_account_api_key** | **str**| Sub-Account API Key | 
 **_from** | **str**| from date | [optional] 
 **to** | **str**| to date | [optional] 

### Return type

[**list[ModelsRStat]**](ModelsRStat.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sub_account_stat_router_get_all_sub_account_stats_by_group**
> list[ModelsRStat] sub_account_stat_router_get_all_sub_account_stats_by_group(x_sub_account_api_key, group, _from=_from, to=to)



Get All Sub-Account Stats by Group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubaccountstatApi()
x_sub_account_api_key = 'x_sub_account_api_key_example' # str | Sub-Account API Key
group = 'group_example' # str | the tag whose stats you want
_from = '_from_example' # str | from date (optional)
to = 'to_example' # str | to date (optional)

try:
    api_response = api_instance.sub_account_stat_router_get_all_sub_account_stats_by_group(x_sub_account_api_key, group, _from=_from, to=to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubaccountstatApi->sub_account_stat_router_get_all_sub_account_stats_by_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_sub_account_api_key** | **str**| Sub-Account API Key | 
 **group** | **str**| the tag whose stats you want | 
 **_from** | **str**| from date | [optional] 
 **to** | **str**| to date | [optional] 

### Return type

[**list[ModelsRStat]**](ModelsRStat.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

