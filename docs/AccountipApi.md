# swagger_client.AccountipApi

All URIs are relative to *https://api.sendpost.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**i_p_router_allocate_ip**](AccountipApi.md#i_p_router_allocate_ip) | **POST** /account/ip/allocate | 
[**i_p_router_count**](AccountipApi.md#i_p_router_count) | **GET** /account/ip/count | 
[**i_p_router_delete**](AccountipApi.md#i_p_router_delete) | **DELETE** /account/ip/{ipid} | 
[**i_p_router_get**](AccountipApi.md#i_p_router_get) | **GET** /account/ip/{ipid} | 
[**i_p_router_get_all**](AccountipApi.md#i_p_router_get_all) | **GET** /account/ip/ | 
[**i_p_router_update**](AccountipApi.md#i_p_router_update) | **PUT** /account/ip/{ipid} | 


# **i_p_router_allocate_ip**
> list[ModelsIP] i_p_router_allocate_ip(x_account_api_key)



Allocate IP To Account

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountipApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key

try:
    api_response = api_instance.i_p_router_allocate_ip(x_account_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountipApi->i_p_router_allocate_ip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 

### Return type

[**list[ModelsIP]**](ModelsIP.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **i_p_router_count**
> ModelsCountStat i_p_router_count(x_account_api_key, search=search)



Count Total AccountIPs

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountipApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key
search = 'search_example' # str | search term (optional)

try:
    api_response = api_instance.i_p_router_count(x_account_api_key, search=search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountipApi->i_p_router_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 
 **search** | **str**| search term | [optional] 

### Return type

[**ModelsCountStat**](ModelsCountStat.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **i_p_router_delete**
> ModelsDeleteResponse i_p_router_delete(x_account_api_key, ipid)



Delete IP

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountipApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key
ipid = 789 # int | The IPId you want to delete

try:
    api_response = api_instance.i_p_router_delete(x_account_api_key, ipid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountipApi->i_p_router_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 
 **ipid** | **int**| The IPId you want to delete | 

### Return type

[**ModelsDeleteResponse**](ModelsDeleteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **i_p_router_get**
> ModelsIP i_p_router_get(x_account_api_key, ipid)



Find IP by IPId

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountipApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key
ipid = 789 # int | the IPId you want to get

try:
    api_response = api_instance.i_p_router_get(x_account_api_key, ipid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountipApi->i_p_router_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 
 **ipid** | **int**| the IPId you want to get | 

### Return type

[**ModelsIP**](ModelsIP.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **i_p_router_get_all**
> list[ModelsIP] i_p_router_get_all(x_account_api_key, offset=offset, limit=limit, search=search)



Get All IPs

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountipApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key
offset = 789 # int | offset (optional)
limit = 789 # int | limit (optional)
search = 'search_example' # str | search term (optional)

try:
    api_response = api_instance.i_p_router_get_all(x_account_api_key, offset=offset, limit=limit, search=search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountipApi->i_p_router_get_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 
 **offset** | **int**| offset | [optional] 
 **limit** | **int**| limit | [optional] 
 **search** | **str**| search term | [optional] 

### Return type

[**list[ModelsIP]**](ModelsIP.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **i_p_router_update**
> ModelsIP i_p_router_update(x_account_api_key, ipid, body)



Update an IP

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountipApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key
ipid = 789 # int | The IP you want to update
body = swagger_client.ModelsIIP() # ModelsIIP | The IP Email Provider Settings

try:
    api_response = api_instance.i_p_router_update(x_account_api_key, ipid, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountipApi->i_p_router_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 
 **ipid** | **int**| The IP you want to update | 
 **body** | [**ModelsIIP**](ModelsIIP.md)| The IP Email Provider Settings | 

### Return type

[**ModelsIP**](ModelsIP.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

