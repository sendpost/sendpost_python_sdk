# swagger_client.SubaccountsuppressionApi

All URIs are relative to *https://api.sendpost.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**suppression_router_count**](SubaccountsuppressionApi.md#suppression_router_count) | **GET** /subaccount/suppression/count | 
[**suppression_router_create_suppressions**](SubaccountsuppressionApi.md#suppression_router_create_suppressions) | **POST** /subaccount/suppression/ | 
[**suppression_router_create_suppressions_in_suppression_filter**](SubaccountsuppressionApi.md#suppression_router_create_suppressions_in_suppression_filter) | **POST** /subaccount/suppression/filter | 
[**suppression_router_delete_suppression**](SubaccountsuppressionApi.md#suppression_router_delete_suppression) | **DELETE** /subaccount/suppression/ | 
[**suppression_router_delete_suppressions_in_suppression_filter**](SubaccountsuppressionApi.md#suppression_router_delete_suppressions_in_suppression_filter) | **DELETE** /subaccount/suppression/filter | 
[**suppression_router_get_all_suppressions**](SubaccountsuppressionApi.md#suppression_router_get_all_suppressions) | **GET** /subaccount/suppression/ | 


# **suppression_router_count**
> ModelsCountStat suppression_router_count(x_sub_account_api_key)



Count Total Suppressions

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubaccountsuppressionApi()
x_sub_account_api_key = 'x_sub_account_api_key_example' # str | Sub-Account API Key

try:
    api_response = api_instance.suppression_router_count(x_sub_account_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubaccountsuppressionApi->suppression_router_count: %s\n" % e)
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

# **suppression_router_create_suppressions**
> ModelsSuppression suppression_router_create_suppressions(x_sub_account_api_key, body)



Add Email Addresses To Suppression List

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubaccountsuppressionApi()
x_sub_account_api_key = 'x_sub_account_api_key_example' # str | Sub-Account API Key
body = swagger_client.ModelsRSuppression() # ModelsRSuppression | Suppression content

try:
    api_response = api_instance.suppression_router_create_suppressions(x_sub_account_api_key, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubaccountsuppressionApi->suppression_router_create_suppressions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_sub_account_api_key** | **str**| Sub-Account API Key | 
 **body** | [**ModelsRSuppression**](ModelsRSuppression.md)| Suppression content | 

### Return type

[**ModelsSuppression**](ModelsSuppression.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suppression_router_create_suppressions_in_suppression_filter**
> suppression_router_create_suppressions_in_suppression_filter(body)



Add Email Addresses To Suppression Filter

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubaccountsuppressionApi()
body = swagger_client.ModelsSuppression() # ModelsSuppression | Add suppressions to suppression filter

try:
    api_instance.suppression_router_create_suppressions_in_suppression_filter(body)
except ApiException as e:
    print("Exception when calling SubaccountsuppressionApi->suppression_router_create_suppressions_in_suppression_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ModelsSuppression**](ModelsSuppression.md)| Add suppressions to suppression filter | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suppression_router_delete_suppression**
> ModelsSuppression suppression_router_delete_suppression(x_sub_account_api_key, body)



Delete specific emails which are in suppression list

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubaccountsuppressionApi()
x_sub_account_api_key = 'x_sub_account_api_key_example' # str | Sub-Account API Key
body = swagger_client.ModelsRDSuppression() # ModelsRDSuppression | Suppression content

try:
    api_response = api_instance.suppression_router_delete_suppression(x_sub_account_api_key, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubaccountsuppressionApi->suppression_router_delete_suppression: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_sub_account_api_key** | **str**| Sub-Account API Key | 
 **body** | [**ModelsRDSuppression**](ModelsRDSuppression.md)| Suppression content | 

### Return type

[**ModelsSuppression**](ModelsSuppression.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suppression_router_delete_suppressions_in_suppression_filter**
> suppression_router_delete_suppressions_in_suppression_filter(body)



Delete specific emails which are in suppression list

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubaccountsuppressionApi()
body = swagger_client.ModelsSuppression() # ModelsSuppression | Suppression content

try:
    api_instance.suppression_router_delete_suppressions_in_suppression_filter(body)
except ApiException as e:
    print("Exception when calling SubaccountsuppressionApi->suppression_router_delete_suppressions_in_suppression_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ModelsSuppression**](ModelsSuppression.md)| Suppression content | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suppression_router_get_all_suppressions**
> list[ModelsSuppression] suppression_router_get_all_suppressions(x_sub_account_api_key, offset=offset, limit=limit, search=search)



Get all suppressions

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubaccountsuppressionApi()
x_sub_account_api_key = 'x_sub_account_api_key_example' # str | Sub-Account API Key
offset = 789 # int | offset (optional)
limit = 789 # int | limit (optional)
search = 'search_example' # str | search (optional)

try:
    api_response = api_instance.suppression_router_get_all_suppressions(x_sub_account_api_key, offset=offset, limit=limit, search=search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubaccountsuppressionApi->suppression_router_get_all_suppressions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_sub_account_api_key** | **str**| Sub-Account API Key | 
 **offset** | **int**| offset | [optional] 
 **limit** | **int**| limit | [optional] 
 **search** | **str**| search | [optional] 

### Return type

[**list[ModelsSuppression]**](ModelsSuppression.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

