# swagger_client.AccountvalidateApi

All URIs are relative to *https://api.sendpost.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**validate_router_validate_email_bulk**](AccountvalidateApi.md#validate_router_validate_email_bulk) | **POST** /account/validate/bulk | 
[**validate_router_validate_email_list**](AccountvalidateApi.md#validate_router_validate_email_list) | **POST** /account/validate/ | 


# **validate_router_validate_email_bulk**
> ModelsBulkResponse validate_router_validate_email_bulk(fileinput, x_account_api_key)



Validate Emails In File Asynchronously

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountvalidateApi()
fileinput = '/path/to/file.txt' # file | CSV whose emails need to be validated
x_account_api_key = 'x_account_api_key_example' # str | Account API Key

try:
    api_response = api_instance.validate_router_validate_email_bulk(fileinput, x_account_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountvalidateApi->validate_router_validate_email_bulk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fileinput** | **file**| CSV whose emails need to be validated | 
 **x_account_api_key** | **str**| Account API Key | 

### Return type

[**ModelsBulkResponse**](ModelsBulkResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_router_validate_email_list**
> ModelsCleanedList validate_router_validate_email_list(x_account_api_key, body)



Validate Email List Synchronously

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountvalidateApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key
body = swagger_client.ModelsEmailList() # ModelsEmailList | The email list to be sent for being validated

try:
    api_response = api_instance.validate_router_validate_email_list(x_account_api_key, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountvalidateApi->validate_router_validate_email_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 
 **body** | [**ModelsEmailList**](ModelsEmailList.md)| The email list to be sent for being validated | 

### Return type

[**ModelsCleanedList**](ModelsCleanedList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

