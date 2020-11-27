# swagger_client.AccounttemplateApi

All URIs are relative to *https://api.sendpost.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_template_router_create**](AccounttemplateApi.md#account_template_router_create) | **POST** /account/template/ | 
[**account_template_router_delete**](AccounttemplateApi.md#account_template_router_delete) | **DELETE** /account/template/{templateid} | 
[**account_template_router_get**](AccounttemplateApi.md#account_template_router_get) | **GET** /account/template/{templateid} | 
[**account_template_router_get_all**](AccounttemplateApi.md#account_template_router_get_all) | **GET** /account/template/ | 
[**account_template_router_update**](AccounttemplateApi.md#account_template_router_update) | **PUT** /account/template/{templateid} | 


# **account_template_router_create**
> ModelsAccountTemplate account_template_router_create(x_account_api_key, body)



Create a new template

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccounttemplateApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key
body = swagger_client.ModelsAccountTemplate() # ModelsAccountTemplate | The AccountTemplate content

try:
    api_response = api_instance.account_template_router_create(x_account_api_key, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccounttemplateApi->account_template_router_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 
 **body** | [**ModelsAccountTemplate**](ModelsAccountTemplate.md)| The AccountTemplate content | 

### Return type

[**ModelsAccountTemplate**](ModelsAccountTemplate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_template_router_delete**
> ModelsDeleteResponse account_template_router_delete(x_account_api_key, templateid)



Delete AccountTemplate

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccounttemplateApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key
templateid = 789 # int | The id of the template you want to delete

try:
    api_response = api_instance.account_template_router_delete(x_account_api_key, templateid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccounttemplateApi->account_template_router_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 
 **templateid** | **int**| The id of the template you want to delete | 

### Return type

[**ModelsDeleteResponse**](ModelsDeleteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_template_router_get**
> ModelsAccountTemplate account_template_router_get(x_account_api_key, templateid)



Get single template

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccounttemplateApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key
templateid = 789 # int | ID of the template required

try:
    api_response = api_instance.account_template_router_get(x_account_api_key, templateid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccounttemplateApi->account_template_router_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 
 **templateid** | **int**| ID of the template required | 

### Return type

[**ModelsAccountTemplate**](ModelsAccountTemplate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_template_router_get_all**
> list[ModelsAccountTemplate] account_template_router_get_all(x_account_api_key)



Get all templates

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccounttemplateApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key

try:
    api_response = api_instance.account_template_router_get_all(x_account_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccounttemplateApi->account_template_router_get_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 

### Return type

[**list[ModelsAccountTemplate]**](ModelsAccountTemplate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_template_router_update**
> ModelsAccountTemplate account_template_router_update(x_account_api_key, templateid, body)



update template

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccounttemplateApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key
templateid = 789 # int | The id of the template you want to update
body = swagger_client.ModelsAccountTemplate() # ModelsAccountTemplate | The template content

try:
    api_response = api_instance.account_template_router_update(x_account_api_key, templateid, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccounttemplateApi->account_template_router_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 
 **templateid** | **int**| The id of the template you want to update | 
 **body** | [**ModelsAccountTemplate**](ModelsAccountTemplate.md)| The template content | 

### Return type

[**ModelsAccountTemplate**](ModelsAccountTemplate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

