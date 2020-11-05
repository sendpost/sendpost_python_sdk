# swagger_client.AccountippoolApi

All URIs are relative to *https://api.sendpost.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_ip_pool_router_count**](AccountippoolApi.md#account_ip_pool_router_count) | **GET** /account/ippool/count | 
[**account_ip_pool_router_create**](AccountippoolApi.md#account_ip_pool_router_create) | **POST** /account/ippool/ | 
[**account_ip_pool_router_delete**](AccountippoolApi.md#account_ip_pool_router_delete) | **DELETE** /account/ippool/{ippoolid} | 
[**account_ip_pool_router_get**](AccountippoolApi.md#account_ip_pool_router_get) | **GET** /account/ippool/{ippoolid} | 
[**account_ip_pool_router_get_all**](AccountippoolApi.md#account_ip_pool_router_get_all) | **GET** /account/ippool/ | 
[**account_ip_pool_router_update**](AccountippoolApi.md#account_ip_pool_router_update) | **PUT** /account/ippool/{ippoolid} | 


# **account_ip_pool_router_count**
> ModelsCountStat account_ip_pool_router_count(x_account_api_key)



Count Total AccountIPPools

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountippoolApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key

try:
    api_response = api_instance.account_ip_pool_router_count(x_account_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountippoolApi->account_ip_pool_router_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 

### Return type

[**ModelsCountStat**](ModelsCountStat.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_ip_pool_router_create**
> ModelsAccountIPPool account_ip_pool_router_create(x_account_api_key, body)



Create AccountIPPool

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountippoolApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key
body = swagger_client.ModelsEIPPool() # ModelsEIPPool | The AccountIPPool content

try:
    api_response = api_instance.account_ip_pool_router_create(x_account_api_key, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountippoolApi->account_ip_pool_router_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 
 **body** | [**ModelsEIPPool**](ModelsEIPPool.md)| The AccountIPPool content | 

### Return type

[**ModelsAccountIPPool**](ModelsAccountIPPool.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_ip_pool_router_delete**
> ModelsDeleteResponse account_ip_pool_router_delete(x_account_api_key, ippoolid)



Delete AccountIPPool

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountippoolApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key
ippoolid = 789 # int | The AccountIPPoolId you want to delete

try:
    api_response = api_instance.account_ip_pool_router_delete(x_account_api_key, ippoolid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountippoolApi->account_ip_pool_router_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 
 **ippoolid** | **int**| The AccountIPPoolId you want to delete | 

### Return type

[**ModelsDeleteResponse**](ModelsDeleteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_ip_pool_router_get**
> ModelsAccountIPPool account_ip_pool_router_get(x_account_api_key, ippoolid)



Find AccountIPPool by AccountIPPoolId

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountippoolApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key
ippoolid = 789 # int | the AccountIPPoolId you want to get

try:
    api_response = api_instance.account_ip_pool_router_get(x_account_api_key, ippoolid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountippoolApi->account_ip_pool_router_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 
 **ippoolid** | **int**| the AccountIPPoolId you want to get | 

### Return type

[**ModelsAccountIPPool**](ModelsAccountIPPool.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_ip_pool_router_get_all**
> list[ModelsAccountIPPool] account_ip_pool_router_get_all(x_account_api_key, offset=offset, limit=limit, search=search)



Get All AccountIPPools

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountippoolApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key
offset = 789 # int | offset (optional)
limit = 789 # int | limit (optional)
search = 'search_example' # str | search term (optional)

try:
    api_response = api_instance.account_ip_pool_router_get_all(x_account_api_key, offset=offset, limit=limit, search=search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountippoolApi->account_ip_pool_router_get_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 
 **offset** | **int**| offset | [optional] 
 **limit** | **int**| limit | [optional] 
 **search** | **str**| search term | [optional] 

### Return type

[**list[ModelsAccountIPPool]**](ModelsAccountIPPool.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_ip_pool_router_update**
> ModelsAccountIPPool account_ip_pool_router_update(x_account_api_key, ippoolid, body)



Update AccountIPPool

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountippoolApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key
ippoolid = 789 # int | The AccountIPPoolId you want to update
body = swagger_client.ModelsEIPPool() # ModelsEIPPool | The body

try:
    api_response = api_instance.account_ip_pool_router_update(x_account_api_key, ippoolid, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountippoolApi->account_ip_pool_router_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 
 **ippoolid** | **int**| The AccountIPPoolId you want to update | 
 **body** | [**ModelsEIPPool**](ModelsEIPPool.md)| The body | 

### Return type

[**ModelsAccountIPPool**](ModelsAccountIPPool.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

