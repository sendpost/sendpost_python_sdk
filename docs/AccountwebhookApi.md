# swagger_client.AccountwebhookApi

All URIs are relative to *https://api.sendpost.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_webhook_router_count**](AccountwebhookApi.md#account_webhook_router_count) | **GET** /account/webhook/count | 
[**account_webhook_router_create**](AccountwebhookApi.md#account_webhook_router_create) | **POST** /account/webhook/ | 
[**account_webhook_router_create_account_webhook_in_account_webhook_cache**](AccountwebhookApi.md#account_webhook_router_create_account_webhook_in_account_webhook_cache) | **POST** /account/webhook/cache | 
[**account_webhook_router_delete**](AccountwebhookApi.md#account_webhook_router_delete) | **DELETE** /account/webhook/{webhookId} | 
[**account_webhook_router_delete_account_webhook_in_account_webhook_cache**](AccountwebhookApi.md#account_webhook_router_delete_account_webhook_in_account_webhook_cache) | **DELETE** /account/webhook/cache | 
[**account_webhook_router_get**](AccountwebhookApi.md#account_webhook_router_get) | **GET** /account/webhook/{webhookId} | 
[**account_webhook_router_get_all**](AccountwebhookApi.md#account_webhook_router_get_all) | **GET** /account/webhook/ | 
[**account_webhook_router_update**](AccountwebhookApi.md#account_webhook_router_update) | **PUT** /account/webhook/{webhookId} | 


# **account_webhook_router_count**
> ModelsCountStat account_webhook_router_count(x_account_api_key)



Count Total AccountWebhooks

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountwebhookApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key

try:
    api_response = api_instance.account_webhook_router_count(x_account_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountwebhookApi->account_webhook_router_count: %s\n" % e)
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

# **account_webhook_router_create**
> ModelsAccountWebhook account_webhook_router_create(x_account_api_key, body)



Create AccountWebhook

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountwebhookApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key
body = swagger_client.ModelsEWebhook() # ModelsEWebhook | The AccountWebhook content

try:
    api_response = api_instance.account_webhook_router_create(x_account_api_key, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountwebhookApi->account_webhook_router_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 
 **body** | [**ModelsEWebhook**](ModelsEWebhook.md)| The AccountWebhook content | 

### Return type

[**ModelsAccountWebhook**](ModelsAccountWebhook.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_webhook_router_create_account_webhook_in_account_webhook_cache**
> account_webhook_router_create_account_webhook_in_account_webhook_cache(body)



Add Account Webhook To AccountWebhook Cache

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountwebhookApi()
body = swagger_client.ModelsAccountWebhook() # ModelsAccountWebhook | Add account webhook to cache

try:
    api_instance.account_webhook_router_create_account_webhook_in_account_webhook_cache(body)
except ApiException as e:
    print("Exception when calling AccountwebhookApi->account_webhook_router_create_account_webhook_in_account_webhook_cache: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ModelsAccountWebhook**](ModelsAccountWebhook.md)| Add account webhook to cache | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_webhook_router_delete**
> ModelsDeleteResponse account_webhook_router_delete(x_account_api_key, webhook_id)



Delete AccountWebhook

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountwebhookApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key
webhook_id = 789 # int | The AccountWebhookId you want to delete

try:
    api_response = api_instance.account_webhook_router_delete(x_account_api_key, webhook_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountwebhookApi->account_webhook_router_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 
 **webhook_id** | **int**| The AccountWebhookId you want to delete | 

### Return type

[**ModelsDeleteResponse**](ModelsDeleteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_webhook_router_delete_account_webhook_in_account_webhook_cache**
> account_webhook_router_delete_account_webhook_in_account_webhook_cache(body)



Delete Account Webhook which is in AccountWebhook Cache

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountwebhookApi()
body = swagger_client.ModelsAccountWebhook() # ModelsAccountWebhook | AccountWebhook content

try:
    api_instance.account_webhook_router_delete_account_webhook_in_account_webhook_cache(body)
except ApiException as e:
    print("Exception when calling AccountwebhookApi->account_webhook_router_delete_account_webhook_in_account_webhook_cache: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ModelsAccountWebhook**](ModelsAccountWebhook.md)| AccountWebhook content | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_webhook_router_get**
> ModelsAccountWebhook account_webhook_router_get(x_account_api_key, webhook_id)



Find AccountWebhook by AccountWebhookId

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountwebhookApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key
webhook_id = 789 # int | the AccountWebhookId you want to get

try:
    api_response = api_instance.account_webhook_router_get(x_account_api_key, webhook_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountwebhookApi->account_webhook_router_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 
 **webhook_id** | **int**| the AccountWebhookId you want to get | 

### Return type

[**ModelsAccountWebhook**](ModelsAccountWebhook.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_webhook_router_get_all**
> list[ModelsAccountWebhook] account_webhook_router_get_all(x_account_api_key, offset=offset, limit=limit, search=search)



Get All AccountWebhooks

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountwebhookApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key
offset = 789 # int | offset (optional)
limit = 789 # int | limit (optional)
search = 'search_example' # str | search (optional)

try:
    api_response = api_instance.account_webhook_router_get_all(x_account_api_key, offset=offset, limit=limit, search=search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountwebhookApi->account_webhook_router_get_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 
 **offset** | **int**| offset | [optional] 
 **limit** | **int**| limit | [optional] 
 **search** | **str**| search | [optional] 

### Return type

[**list[ModelsAccountWebhook]**](ModelsAccountWebhook.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_webhook_router_update**
> ModelsAccountWebhook account_webhook_router_update(x_account_api_key, webhook_id, body)



Update AccountWebhook

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountwebhookApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key
webhook_id = 789 # int | The AccountWebhookId you want to update
body = swagger_client.ModelsEWebhook() # ModelsEWebhook | The body

try:
    api_response = api_instance.account_webhook_router_update(x_account_api_key, webhook_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountwebhookApi->account_webhook_router_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 
 **webhook_id** | **int**| The AccountWebhookId you want to update | 
 **body** | [**ModelsEWebhook**](ModelsEWebhook.md)| The body | 

### Return type

[**ModelsAccountWebhook**](ModelsAccountWebhook.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

