# swagger_client.AccountipstatApi

All URIs are relative to *https://api.sendpost.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**i_p_stat_router_get_all_aggregate_ip_stats**](AccountipstatApi.md#i_p_stat_router_get_all_aggregate_ip_stats) | **GET** /account/ip/stat/{ipid}/aggregate | 
[**i_p_stat_router_get_all_aggregate_ip_stats_by_group**](AccountipstatApi.md#i_p_stat_router_get_all_aggregate_ip_stats_by_group) | **GET** /account/ip/stat/{ipid}/aggregate/provider | 
[**i_p_stat_router_get_all_aggregated_provider_stats_for_a_ip**](AccountipstatApi.md#i_p_stat_router_get_all_aggregated_provider_stats_for_a_ip) | **GET** /account/ip/stat/{ipid}/aggregate/providers | 
[**i_p_stat_router_get_all_aggregated_provider_stats_for_a_specific_sub_account_of_a_ip**](AccountipstatApi.md#i_p_stat_router_get_all_aggregated_provider_stats_for_a_specific_sub_account_of_a_ip) | **GET** /account/ip/stat/{ipid}/aggregate/sid/{sid}/providers | 
[**i_p_stat_router_get_all_aggregated_sub_account_stats_for_an_ip**](AccountipstatApi.md#i_p_stat_router_get_all_aggregated_sub_account_stats_for_an_ip) | **GET** /account/ip/stat/{ipid}/aggregate/subaccounts | 
[**i_p_stat_router_get_all_ip_stats**](AccountipstatApi.md#i_p_stat_router_get_all_ip_stats) | **GET** /account/ip/stat/{ipid} | 
[**i_p_stat_router_get_all_ip_stats_by_group**](AccountipstatApi.md#i_p_stat_router_get_all_ip_stats_by_group) | **GET** /account/ip/stat/{ipid}/provider | 


# **i_p_stat_router_get_all_aggregate_ip_stats**
> ModelsStat i_p_stat_router_get_all_aggregate_ip_stats(x_account_api_key, ipid, _from=_from, to=to)



Get All Aggregate Stats

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountipstatApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key
ipid = 789 # int | the IPId you want to get
_from = '_from_example' # str | from date (optional)
to = 'to_example' # str | to date (optional)

try:
    api_response = api_instance.i_p_stat_router_get_all_aggregate_ip_stats(x_account_api_key, ipid, _from=_from, to=to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountipstatApi->i_p_stat_router_get_all_aggregate_ip_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 
 **ipid** | **int**| the IPId you want to get | 
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

# **i_p_stat_router_get_all_aggregate_ip_stats_by_group**
> ModelsStat i_p_stat_router_get_all_aggregate_ip_stats_by_group(x_account_api_key, ipid, provider, _from=_from, to=to)



Get All Aggregate Stats by Group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountipstatApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key
ipid = 789 # int | the IPId you want to get
provider = 'provider_example' # str | the group whose stats you want
_from = '_from_example' # str | from date (optional)
to = 'to_example' # str | to date (optional)

try:
    api_response = api_instance.i_p_stat_router_get_all_aggregate_ip_stats_by_group(x_account_api_key, ipid, provider, _from=_from, to=to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountipstatApi->i_p_stat_router_get_all_aggregate_ip_stats_by_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 
 **ipid** | **int**| the IPId you want to get | 
 **provider** | **str**| the group whose stats you want | 
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

# **i_p_stat_router_get_all_aggregated_provider_stats_for_a_ip**
> list[ModelsPIPStat] i_p_stat_router_get_all_aggregated_provider_stats_for_a_ip(x_account_api_key, ipid, _from=_from, to=to)



Get All Aggregated Provider Stats for a IP

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountipstatApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key
ipid = 789 # int | the IPId you want to get
_from = '_from_example' # str | from date (optional)
to = 'to_example' # str | to date (optional)

try:
    api_response = api_instance.i_p_stat_router_get_all_aggregated_provider_stats_for_a_ip(x_account_api_key, ipid, _from=_from, to=to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountipstatApi->i_p_stat_router_get_all_aggregated_provider_stats_for_a_ip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 
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

# **i_p_stat_router_get_all_aggregated_provider_stats_for_a_specific_sub_account_of_a_ip**
> list[ModelsPIPStat] i_p_stat_router_get_all_aggregated_provider_stats_for_a_specific_sub_account_of_a_ip(x_account_api_key, ipid, sid, _from=_from, to=to)



Get All Aggregated Provider Stats for a Specific Sub-Account of a IP

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountipstatApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key
ipid = 789 # int | the IPId you want to get
sid = 789 # int | the Sub Account Id you want to get
_from = '_from_example' # str | from date (optional)
to = 'to_example' # str | to date (optional)

try:
    api_response = api_instance.i_p_stat_router_get_all_aggregated_provider_stats_for_a_specific_sub_account_of_a_ip(x_account_api_key, ipid, sid, _from=_from, to=to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountipstatApi->i_p_stat_router_get_all_aggregated_provider_stats_for_a_specific_sub_account_of_a_ip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 
 **ipid** | **int**| the IPId you want to get | 
 **sid** | **int**| the Sub Account Id you want to get | 
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

# **i_p_stat_router_get_all_aggregated_sub_account_stats_for_an_ip**
> list[ModelsSIPStat] i_p_stat_router_get_all_aggregated_sub_account_stats_for_an_ip(x_account_api_key, ipid, _from=_from, to=to)



Get All Aggregated Sub-Account Stats for an IP

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountipstatApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key
ipid = 789 # int | the IPId you want to get
_from = '_from_example' # str | from date (optional)
to = 'to_example' # str | to date (optional)

try:
    api_response = api_instance.i_p_stat_router_get_all_aggregated_sub_account_stats_for_an_ip(x_account_api_key, ipid, _from=_from, to=to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountipstatApi->i_p_stat_router_get_all_aggregated_sub_account_stats_for_an_ip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 
 **ipid** | **int**| the IPId you want to get | 
 **_from** | **str**| from date | [optional] 
 **to** | **str**| to date | [optional] 

### Return type

[**list[ModelsSIPStat]**](ModelsSIPStat.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **i_p_stat_router_get_all_ip_stats**
> list[ModelsRIPStat] i_p_stat_router_get_all_ip_stats(x_account_api_key, ipid, _from=_from, to=to)



Get All IP Stats

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountipstatApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key
ipid = 789 # int | the IPId you want to get
_from = '_from_example' # str | from date (optional)
to = 'to_example' # str | to date (optional)

try:
    api_response = api_instance.i_p_stat_router_get_all_ip_stats(x_account_api_key, ipid, _from=_from, to=to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountipstatApi->i_p_stat_router_get_all_ip_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 
 **ipid** | **int**| the IPId you want to get | 
 **_from** | **str**| from date | [optional] 
 **to** | **str**| to date | [optional] 

### Return type

[**list[ModelsRIPStat]**](ModelsRIPStat.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **i_p_stat_router_get_all_ip_stats_by_group**
> list[ModelsRIPStat] i_p_stat_router_get_all_ip_stats_by_group(ipid, x_account_api_key, provider, _from=_from, to=to)



Get All IP Stats by Group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountipstatApi()
ipid = 789 # int | the IPId you want to get
x_account_api_key = 'x_account_api_key_example' # str | Account API Key
provider = 'provider_example' # str | the provider whose stats you want
_from = '_from_example' # str | from date (optional)
to = 'to_example' # str | to date (optional)

try:
    api_response = api_instance.i_p_stat_router_get_all_ip_stats_by_group(ipid, x_account_api_key, provider, _from=_from, to=to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountipstatApi->i_p_stat_router_get_all_ip_stats_by_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ipid** | **int**| the IPId you want to get | 
 **x_account_api_key** | **str**| Account API Key | 
 **provider** | **str**| the provider whose stats you want | 
 **_from** | **str**| from date | [optional] 
 **to** | **str**| to date | [optional] 

### Return type

[**list[ModelsRIPStat]**](ModelsRIPStat.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

