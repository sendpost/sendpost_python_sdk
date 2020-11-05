# swagger_client.AccountsubaccountApi

All URIs are relative to *https://api.sendpost.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sub_account_router_count**](AccountsubaccountApi.md#sub_account_router_count) | **GET** /account/subaccount/count | 
[**sub_account_router_create**](AccountsubaccountApi.md#sub_account_router_create) | **POST** /account/subaccount/ | 
[**sub_account_router_delete**](AccountsubaccountApi.md#sub_account_router_delete) | **DELETE** /account/subaccount/{subAccountId} | 
[**sub_account_router_get**](AccountsubaccountApi.md#sub_account_router_get) | **GET** /account/subaccount/{subAccountId} | 
[**sub_account_router_get_all**](AccountsubaccountApi.md#sub_account_router_get_all) | **GET** /account/subaccount/ | 
[**sub_account_router_update**](AccountsubaccountApi.md#sub_account_router_update) | **PUT** /account/subaccount/{subAccountId} | 


# **sub_account_router_count**
> ModelsCountStat sub_account_router_count(x_account_api_key, filter_by=filter_by, filter_value=filter_value, search=search)



Count Total Subaccounts

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountsubaccountApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key
filter_by = 'filter_by_example' # str | filterBy (optional)
filter_value = 789 # int | filterValue (optional)
search = 'search_example' # str | search term (optional)

try:
    api_response = api_instance.sub_account_router_count(x_account_api_key, filter_by=filter_by, filter_value=filter_value, search=search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsubaccountApi->sub_account_router_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 
 **filter_by** | **str**| filterBy | [optional] 
 **filter_value** | **int**| filterValue | [optional] 
 **search** | **str**| search term | [optional] 

### Return type

[**ModelsCountStat**](ModelsCountStat.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sub_account_router_create**
> ModelsSubAccount sub_account_router_create(x_account_api_key, body)



Create SubAccount

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountsubaccountApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key
body = swagger_client.ModelsESubAccount() # ModelsESubAccount | The SubAccount content

try:
    api_response = api_instance.sub_account_router_create(x_account_api_key, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsubaccountApi->sub_account_router_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 
 **body** | [**ModelsESubAccount**](ModelsESubAccount.md)| The SubAccount content | 

### Return type

[**ModelsSubAccount**](ModelsSubAccount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sub_account_router_delete**
> ModelsDeleteResponse sub_account_router_delete(x_account_api_key, sub_account_id)



Delete SubAccount

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountsubaccountApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key
sub_account_id = 789 # int | The SubAccountId you want to delete

try:
    api_response = api_instance.sub_account_router_delete(x_account_api_key, sub_account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsubaccountApi->sub_account_router_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 
 **sub_account_id** | **int**| The SubAccountId you want to delete | 

### Return type

[**ModelsDeleteResponse**](ModelsDeleteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sub_account_router_get**
> ModelsSubAccount sub_account_router_get(x_account_api_key, sub_account_id)



Find SubAccount by SubAccountId

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountsubaccountApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key
sub_account_id = 789 # int | the SubAccountId you want to get

try:
    api_response = api_instance.sub_account_router_get(x_account_api_key, sub_account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsubaccountApi->sub_account_router_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 
 **sub_account_id** | **int**| the SubAccountId you want to get | 

### Return type

[**ModelsSubAccount**](ModelsSubAccount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sub_account_router_get_all**
> list[ModelsSubAccount] sub_account_router_get_all(x_account_api_key, offset=offset, limit=limit, filter_by=filter_by, filter_value=filter_value, search=search)



Get All SubAccounts

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountsubaccountApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key
offset = 789 # int | offset (optional)
limit = 789 # int | limit (optional)
filter_by = 'filter_by_example' # str | filterBy (optional)
filter_value = 789 # int | filterValue (optional)
search = 'search_example' # str | search term (optional)

try:
    api_response = api_instance.sub_account_router_get_all(x_account_api_key, offset=offset, limit=limit, filter_by=filter_by, filter_value=filter_value, search=search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsubaccountApi->sub_account_router_get_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 
 **offset** | **int**| offset | [optional] 
 **limit** | **int**| limit | [optional] 
 **filter_by** | **str**| filterBy | [optional] 
 **filter_value** | **int**| filterValue | [optional] 
 **search** | **str**| search term | [optional] 

### Return type

[**list[ModelsSubAccount]**](ModelsSubAccount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sub_account_router_update**
> ModelsSubAccount sub_account_router_update(x_account_api_key, sub_account_id, body)



Update SubAccount

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountsubaccountApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key
sub_account_id = 789 # int | The SubAccountId you want to update
body = swagger_client.ModelsESubAccount() # ModelsESubAccount | The body

try:
    api_response = api_instance.sub_account_router_update(x_account_api_key, sub_account_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsubaccountApi->sub_account_router_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 
 **sub_account_id** | **int**| The SubAccountId you want to update | 
 **body** | [**ModelsESubAccount**](ModelsESubAccount.md)| The body | 

### Return type

[**ModelsSubAccount**](ModelsSubAccount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

