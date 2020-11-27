# swagger_client.SystemApi

All URIs are relative to *https://api.sendpost.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**system_template_router_get_all_system_templates**](SystemApi.md#system_template_router_get_all_system_templates) | **GET** /system/template | 


# **system_template_router_get_all_system_templates**
> list[ModelsSystemTemplate] system_template_router_get_all_system_templates(x_account_api_key)



Get all System Templates

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SystemApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key

try:
    api_response = api_instance.system_template_router_get_all_system_templates(x_account_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->system_template_router_get_all_system_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 

### Return type

[**list[ModelsSystemTemplate]**](ModelsSystemTemplate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

