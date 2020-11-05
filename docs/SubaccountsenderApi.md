# swagger_client.SubaccountsenderApi

All URIs are relative to *https://api.sendpost.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sender_router_count**](SubaccountsenderApi.md#sender_router_count) | **GET** /subaccount/sender/count | 
[**sender_router_create**](SubaccountsenderApi.md#sender_router_create) | **POST** /subaccount/sender/ | 
[**sender_router_delete**](SubaccountsenderApi.md#sender_router_delete) | **DELETE** /subaccount/sender/{senderId} | 
[**sender_router_get**](SubaccountsenderApi.md#sender_router_get) | **GET** /subaccount/sender/{senderId} | 
[**sender_router_get_all**](SubaccountsenderApi.md#sender_router_get_all) | **GET** /subaccount/sender/ | 
[**sender_router_update**](SubaccountsenderApi.md#sender_router_update) | **PUT** /subaccount/sender/{senderId} | 


# **sender_router_count**
> ModelsCountStat sender_router_count(x_sub_account_api_key)



Count Total Senders

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubaccountsenderApi()
x_sub_account_api_key = 'x_sub_account_api_key_example' # str | Sub-Account API Key

try:
    api_response = api_instance.sender_router_count(x_sub_account_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubaccountsenderApi->sender_router_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_sub_account_api_key** | **str**| Sub-Account API Key | 

### Return type

[**ModelsCountStat**](ModelsCountStat.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sender_router_create**
> ModelsSender sender_router_create(x_sub_account_api_key, body)



Create Sender

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubaccountsenderApi()
x_sub_account_api_key = 'x_sub_account_api_key_example' # str | Sub-Account API Key
body = swagger_client.ModelsESender() # ModelsESender | The Sender content

try:
    api_response = api_instance.sender_router_create(x_sub_account_api_key, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubaccountsenderApi->sender_router_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_sub_account_api_key** | **str**| Sub-Account API Key | 
 **body** | [**ModelsESender**](ModelsESender.md)| The Sender content | 

### Return type

[**ModelsSender**](ModelsSender.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sender_router_delete**
> ModelsDeleteResponse sender_router_delete(x_sub_account_api_key, sender_id)



Delete Sender

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubaccountsenderApi()
x_sub_account_api_key = 'x_sub_account_api_key_example' # str | Sub-Account API Key
sender_id = 789 # int | The SenderId you want to delete

try:
    api_response = api_instance.sender_router_delete(x_sub_account_api_key, sender_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubaccountsenderApi->sender_router_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_sub_account_api_key** | **str**| Sub-Account API Key | 
 **sender_id** | **int**| The SenderId you want to delete | 

### Return type

[**ModelsDeleteResponse**](ModelsDeleteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sender_router_get**
> ModelsSender sender_router_get(x_sub_account_api_key, sender_id)



Find Sender by SenderId

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubaccountsenderApi()
x_sub_account_api_key = 'x_sub_account_api_key_example' # str | Sub-Account API Key
sender_id = 789 # int | the SenderId you want to get

try:
    api_response = api_instance.sender_router_get(x_sub_account_api_key, sender_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubaccountsenderApi->sender_router_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_sub_account_api_key** | **str**| Sub-Account API Key | 
 **sender_id** | **int**| the SenderId you want to get | 

### Return type

[**ModelsSender**](ModelsSender.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sender_router_get_all**
> list[ModelsSender] sender_router_get_all(x_sub_account_api_key, offset=offset, limit=limit, search=search)



Get All Senders

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubaccountsenderApi()
x_sub_account_api_key = 'x_sub_account_api_key_example' # str | Sub-Account API Key
offset = 789 # int | offset (optional)
limit = 789 # int | limit (optional)
search = 'search_example' # str | search term (optional)

try:
    api_response = api_instance.sender_router_get_all(x_sub_account_api_key, offset=offset, limit=limit, search=search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubaccountsenderApi->sender_router_get_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_sub_account_api_key** | **str**| Sub-Account API Key | 
 **offset** | **int**| offset | [optional] 
 **limit** | **int**| limit | [optional] 
 **search** | **str**| search term | [optional] 

### Return type

[**list[ModelsSender]**](ModelsSender.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sender_router_update**
> ModelsSender sender_router_update(x_sub_account_api_key, sender_id, body)



Update Sender

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubaccountsenderApi()
x_sub_account_api_key = 'x_sub_account_api_key_example' # str | Sub-Account API Key
sender_id = 789 # int | The SenderId you want to update
body = swagger_client.ModelsESender() # ModelsESender | The body

try:
    api_response = api_instance.sender_router_update(x_sub_account_api_key, sender_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubaccountsenderApi->sender_router_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_sub_account_api_key** | **str**| Sub-Account API Key | 
 **sender_id** | **int**| The SenderId you want to update | 
 **body** | [**ModelsESender**](ModelsESender.md)| The body | 

### Return type

[**ModelsSender**](ModelsSender.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

