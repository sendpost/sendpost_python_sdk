# swagger_client.AccounttagApi

All URIs are relative to *https://api.sendpost.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tag_router_create**](AccounttagApi.md#tag_router_create) | **POST** /account/tag/ | 
[**tag_router_delete**](AccounttagApi.md#tag_router_delete) | **DELETE** /account/tag/{tagid} | 
[**tag_router_get_all**](AccounttagApi.md#tag_router_get_all) | **GET** /account/tag/ | 


# **tag_router_create**
> ModelsTag tag_router_create(x_account_api_key, body)



Create Tag

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccounttagApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key
body = swagger_client.ModelsTag() # ModelsTag | The Tag content

try:
    api_response = api_instance.tag_router_create(x_account_api_key, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccounttagApi->tag_router_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 
 **body** | [**ModelsTag**](ModelsTag.md)| The Tag content | 

### Return type

[**ModelsTag**](ModelsTag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tag_router_delete**
> ModelsDeleteResponse tag_router_delete(x_account_api_key, tagid)



Delete Tag

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccounttagApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key
tagid = 789 # int | The AccountTagId you want to delete

try:
    api_response = api_instance.tag_router_delete(x_account_api_key, tagid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccounttagApi->tag_router_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 
 **tagid** | **int**| The AccountTagId you want to delete | 

### Return type

[**ModelsDeleteResponse**](ModelsDeleteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tag_router_get_all**
> list[ModelsTag] tag_router_get_all(x_account_api_key)



Get All Tags

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccounttagApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key

try:
    api_response = api_instance.tag_router_get_all(x_account_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccounttagApi->tag_router_get_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 

### Return type

[**list[ModelsTag]**](ModelsTag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

