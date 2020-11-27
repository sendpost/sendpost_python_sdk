# swagger_client.EditorApi

All URIs are relative to *https://api.sendpost.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**editor_api_router_get_token**](EditorApi.md#editor_api_router_get_token) | **GET** /editor/ | 


# **editor_api_router_get_token**
> ModelsEditorTokenResponse editor_api_router_get_token(x_account_api_key)



fetch Bee editor token

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EditorApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key

try:
    api_response = api_instance.editor_api_router_get_token(x_account_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorApi->editor_api_router_get_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 

### Return type

[**ModelsEditorTokenResponse**](ModelsEditorTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

