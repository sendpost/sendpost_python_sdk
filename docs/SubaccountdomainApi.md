# swagger_client.SubaccountdomainApi

All URIs are relative to *https://api.sendpost.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**domain_router_count**](SubaccountdomainApi.md#domain_router_count) | **GET** /subaccount/domain/count | 
[**domain_router_create**](SubaccountdomainApi.md#domain_router_create) | **POST** /subaccount/domain/ | 
[**domain_router_delete**](SubaccountdomainApi.md#domain_router_delete) | **DELETE** /subaccount/domain/{domainId} | 
[**domain_router_get**](SubaccountdomainApi.md#domain_router_get) | **GET** /subaccount/domain/{domainId} | 
[**domain_router_get_all**](SubaccountdomainApi.md#domain_router_get_all) | **GET** /subaccount/domain/ | 
[**domain_router_update**](SubaccountdomainApi.md#domain_router_update) | **PUT** /subaccount/domain/{domainId} | 
[**domain_router_verify**](SubaccountdomainApi.md#domain_router_verify) | **POST** /subaccount/domain/{domainId}/verify | 


# **domain_router_count**
> ModelsCountStat domain_router_count(x_sub_account_api_key)



Count Total Domains

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubaccountdomainApi()
x_sub_account_api_key = 'x_sub_account_api_key_example' # str | Sub-Account API Key

try:
    api_response = api_instance.domain_router_count(x_sub_account_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubaccountdomainApi->domain_router_count: %s\n" % e)
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

# **domain_router_create**
> ModelsDomain domain_router_create(x_sub_account_api_key, body)



Create Domain

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubaccountdomainApi()
x_sub_account_api_key = 'x_sub_account_api_key_example' # str | Sub-Account API Key
body = swagger_client.ModelsEDomain() # ModelsEDomain | The Domain content

try:
    api_response = api_instance.domain_router_create(x_sub_account_api_key, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubaccountdomainApi->domain_router_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_sub_account_api_key** | **str**| Sub-Account API Key | 
 **body** | [**ModelsEDomain**](ModelsEDomain.md)| The Domain content | 

### Return type

[**ModelsDomain**](ModelsDomain.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **domain_router_delete**
> ModelsDeleteResponse domain_router_delete(x_sub_account_api_key, domain_id)



Delete Domain

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubaccountdomainApi()
x_sub_account_api_key = 'x_sub_account_api_key_example' # str | Sub-Account API Key
domain_id = 789 # int | The DomainId you want to delete

try:
    api_response = api_instance.domain_router_delete(x_sub_account_api_key, domain_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubaccountdomainApi->domain_router_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_sub_account_api_key** | **str**| Sub-Account API Key | 
 **domain_id** | **int**| The DomainId you want to delete | 

### Return type

[**ModelsDeleteResponse**](ModelsDeleteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **domain_router_get**
> ModelsDomain domain_router_get(x_sub_account_api_key, domain_id)



Find Domain by DomainId

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubaccountdomainApi()
x_sub_account_api_key = 'x_sub_account_api_key_example' # str | Sub-Account API Key
domain_id = 789 # int | the DomainId you want to get

try:
    api_response = api_instance.domain_router_get(x_sub_account_api_key, domain_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubaccountdomainApi->domain_router_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_sub_account_api_key** | **str**| Sub-Account API Key | 
 **domain_id** | **int**| the DomainId you want to get | 

### Return type

[**ModelsDomain**](ModelsDomain.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **domain_router_get_all**
> list[ModelsDomain] domain_router_get_all(x_sub_account_api_key, offset=offset, limit=limit, search=search)



Get All Domains

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubaccountdomainApi()
x_sub_account_api_key = 'x_sub_account_api_key_example' # str | Sub-Account API Key
offset = 789 # int | offset (optional)
limit = 789 # int | limit (optional)
search = 'search_example' # str | search term (optional)

try:
    api_response = api_instance.domain_router_get_all(x_sub_account_api_key, offset=offset, limit=limit, search=search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubaccountdomainApi->domain_router_get_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_sub_account_api_key** | **str**| Sub-Account API Key | 
 **offset** | **int**| offset | [optional] 
 **limit** | **int**| limit | [optional] 
 **search** | **str**| search term | [optional] 

### Return type

[**list[ModelsDomain]**](ModelsDomain.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **domain_router_update**
> ModelsDomain domain_router_update(x_sub_account_api_key, domain_id, body)



Update Domain

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubaccountdomainApi()
x_sub_account_api_key = 'x_sub_account_api_key_example' # str | Sub-Account API Key
domain_id = 789 # int | The DomainId you want to update
body = swagger_client.ModelsEDomain() # ModelsEDomain | The body

try:
    api_response = api_instance.domain_router_update(x_sub_account_api_key, domain_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubaccountdomainApi->domain_router_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_sub_account_api_key** | **str**| Sub-Account API Key | 
 **domain_id** | **int**| The DomainId you want to update | 
 **body** | [**ModelsEDomain**](ModelsEDomain.md)| The body | 

### Return type

[**ModelsDomain**](ModelsDomain.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **domain_router_verify**
> ModelsDomain domain_router_verify(x_sub_account_api_key, domain_id)



Verify Domain By Domain Id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubaccountdomainApi()
x_sub_account_api_key = 'x_sub_account_api_key_example' # str | Sub-Account API Key
domain_id = 789 # int | the DomainId you want to get

try:
    api_response = api_instance.domain_router_verify(x_sub_account_api_key, domain_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubaccountdomainApi->domain_router_verify: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_sub_account_api_key** | **str**| Sub-Account API Key | 
 **domain_id** | **int**| the DomainId you want to get | 

### Return type

[**ModelsDomain**](ModelsDomain.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

