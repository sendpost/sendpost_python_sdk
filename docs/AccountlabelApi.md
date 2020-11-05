# swagger_client.AccountlabelApi

All URIs are relative to *https://api.sendpost.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**label_router_count**](AccountlabelApi.md#label_router_count) | **GET** /account/label/count | 
[**label_router_create**](AccountlabelApi.md#label_router_create) | **POST** /account/label/ | 
[**label_router_delete**](AccountlabelApi.md#label_router_delete) | **DELETE** /account/label/{labelId} | 
[**label_router_get**](AccountlabelApi.md#label_router_get) | **GET** /account/label/{labelId} | 
[**label_router_get_all**](AccountlabelApi.md#label_router_get_all) | **GET** /account/label/ | 
[**label_router_update**](AccountlabelApi.md#label_router_update) | **PUT** /account/label/{labelId} | 


# **label_router_count**
> ModelsCountStat label_router_count(x_account_api_key)



Count Total Labels

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountlabelApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key

try:
    api_response = api_instance.label_router_count(x_account_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountlabelApi->label_router_count: %s\n" % e)
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

# **label_router_create**
> ModelsLabel label_router_create(x_account_api_key, body)



Create Label

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountlabelApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key
body = swagger_client.ModelsLabel() # ModelsLabel | The Label content

try:
    api_response = api_instance.label_router_create(x_account_api_key, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountlabelApi->label_router_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 
 **body** | [**ModelsLabel**](ModelsLabel.md)| The Label content | 

### Return type

[**ModelsLabel**](ModelsLabel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **label_router_delete**
> ModelsDeleteResponse label_router_delete(x_account_api_key, label_id)



Delete Label

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountlabelApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key
label_id = 789 # int | The LabelId you want to delete

try:
    api_response = api_instance.label_router_delete(x_account_api_key, label_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountlabelApi->label_router_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 
 **label_id** | **int**| The LabelId you want to delete | 

### Return type

[**ModelsDeleteResponse**](ModelsDeleteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **label_router_get**
> ModelsLabel label_router_get(x_account_api_key, label_id)



Find Label by LabelId

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountlabelApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key
label_id = 789 # int | the LabelId you want to get

try:
    api_response = api_instance.label_router_get(x_account_api_key, label_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountlabelApi->label_router_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 
 **label_id** | **int**| the LabelId you want to get | 

### Return type

[**ModelsLabel**](ModelsLabel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **label_router_get_all**
> list[ModelsLabel] label_router_get_all(x_account_api_key)



Get All Labels

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountlabelApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key

try:
    api_response = api_instance.label_router_get_all(x_account_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountlabelApi->label_router_get_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 

### Return type

[**list[ModelsLabel]**](ModelsLabel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **label_router_update**
> ModelsLabel label_router_update(x_account_api_key, label_id, body)



Update Label

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountlabelApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key
label_id = 789 # int | The LabelId you want to update
body = swagger_client.ModelsLabel() # ModelsLabel | The body

try:
    api_response = api_instance.label_router_update(x_account_api_key, label_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountlabelApi->label_router_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 
 **label_id** | **int**| The LabelId you want to update | 
 **body** | [**ModelsLabel**](ModelsLabel.md)| The body | 

### Return type

[**ModelsLabel**](ModelsLabel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

