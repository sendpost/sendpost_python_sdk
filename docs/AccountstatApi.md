# swagger_client.AccountstatApi

All URIs are relative to *https://api.sendpost.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_stat_router_get_all_account_stats**](AccountstatApi.md#account_stat_router_get_all_account_stats) | **GET** /account/stat/ | 
[**account_stat_router_get_all_account_stats_by_group**](AccountstatApi.md#account_stat_router_get_all_account_stats_by_group) | **GET** /account/stat/group | 
[**account_stat_router_get_all_aggregate_account_stats**](AccountstatApi.md#account_stat_router_get_all_aggregate_account_stats) | **GET** /account/stat/aggregate | 
[**account_stat_router_get_all_aggregate_account_stats_by_group**](AccountstatApi.md#account_stat_router_get_all_aggregate_account_stats_by_group) | **GET** /account/stat/aggregate/group | 


# **account_stat_router_get_all_account_stats**
> list[ModelsRStat] account_stat_router_get_all_account_stats(x_account_api_key, _from=_from, to=to)



Get All Account Stats

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountstatApi()
x_account_api_key = 'x_account_api_key_example' # str | Sub-Account API Key
_from = '_from_example' # str | from date (optional)
to = 'to_example' # str | to date (optional)

try:
    api_response = api_instance.account_stat_router_get_all_account_stats(x_account_api_key, _from=_from, to=to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountstatApi->account_stat_router_get_all_account_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Sub-Account API Key | 
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

# **account_stat_router_get_all_account_stats_by_group**
> list[ModelsRStat] account_stat_router_get_all_account_stats_by_group(x_account_api_key, group, _from=_from, to=to)



Get All Account Stats by Group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountstatApi()
x_account_api_key = 'x_account_api_key_example' # str | Sub-Account API Key
group = 'group_example' # str | the group whose stats you want
_from = '_from_example' # str | from date (optional)
to = 'to_example' # str | to date (optional)

try:
    api_response = api_instance.account_stat_router_get_all_account_stats_by_group(x_account_api_key, group, _from=_from, to=to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountstatApi->account_stat_router_get_all_account_stats_by_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Sub-Account API Key | 
 **group** | **str**| the group whose stats you want | 
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

# **account_stat_router_get_all_aggregate_account_stats**
> ModelsStat account_stat_router_get_all_aggregate_account_stats(x_account_api_key, _from=_from, to=to)



Get All Aggregate Stats

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountstatApi()
x_account_api_key = 'x_account_api_key_example' # str | Sub-Account API Key
_from = '_from_example' # str | from date (optional)
to = 'to_example' # str | to date (optional)

try:
    api_response = api_instance.account_stat_router_get_all_aggregate_account_stats(x_account_api_key, _from=_from, to=to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountstatApi->account_stat_router_get_all_aggregate_account_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Sub-Account API Key | 
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

# **account_stat_router_get_all_aggregate_account_stats_by_group**
> ModelsStat account_stat_router_get_all_aggregate_account_stats_by_group(x_account_api_key, group, _from=_from, to=to)



Get All Aggregate Stats by Group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountstatApi()
x_account_api_key = 'x_account_api_key_example' # str | Sub-Account API Key
group = 'group_example' # str | the group whose stats you want
_from = '_from_example' # str | from date (optional)
to = 'to_example' # str | to date (optional)

try:
    api_response = api_instance.account_stat_router_get_all_aggregate_account_stats_by_group(x_account_api_key, group, _from=_from, to=to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountstatApi->account_stat_router_get_all_aggregate_account_stats_by_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Sub-Account API Key | 
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

