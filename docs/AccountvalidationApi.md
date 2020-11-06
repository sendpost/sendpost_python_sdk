# swagger_client.AccountvalidationApi

All URIs are relative to *https://api.sendpost.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**validate_router_validate_email_bulk**](AccountvalidationApi.md#validate_router_validate_email_bulk) | **POST** /account/validation/bulk | 
[**validation_router_count**](AccountvalidationApi.md#validation_router_count) | **GET** /account/validation/count | 
[**validation_router_delete_validation**](AccountvalidationApi.md#validation_router_delete_validation) | **DELETE** /account/validation/ | 
[**validation_router_get_all**](AccountvalidationApi.md#validation_router_get_all) | **GET** /account/validation/ | 
[**validation_router_validate_email_list**](AccountvalidationApi.md#validation_router_validate_email_list) | **POST** /account/validation/ | 


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
api_instance = swagger_client.AccountvalidationApi()
fileinput = '/path/to/file.txt' # file | CSV whose emails need to be validated
x_account_api_key = 'x_account_api_key_example' # str | Account API Key

try:
    api_response = api_instance.validate_router_validate_email_bulk(fileinput, x_account_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountvalidationApi->validate_router_validate_email_bulk: %s\n" % e)
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

# **validation_router_count**
> ModelsCountStat validation_router_count(x_account_api_key)



Count Total Validations

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountvalidationApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key

try:
    api_response = api_instance.validation_router_count(x_account_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountvalidationApi->validation_router_count: %s\n" % e)
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

# **validation_router_delete_validation**
> ModelsValidation validation_router_delete_validation(x_account_api_key, body)



Delete a specific validation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountvalidationApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key
body = swagger_client.ModelsEValidation() # ModelsEValidation | List of emails to be deleted from validation

try:
    api_response = api_instance.validation_router_delete_validation(x_account_api_key, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountvalidationApi->validation_router_delete_validation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 
 **body** | [**ModelsEValidation**](ModelsEValidation.md)| List of emails to be deleted from validation | 

### Return type

[**ModelsValidation**](ModelsValidation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validation_router_get_all**
> list[ModelsValidation] validation_router_get_all(x_account_api_key, offset=offset, limit=limit, search=search)



Get all validation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountvalidationApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key
offset = 789 # int | offset (optional)
limit = 789 # int | limit (optional)
search = 'search_example' # str | search (optional)

try:
    api_response = api_instance.validation_router_get_all(x_account_api_key, offset=offset, limit=limit, search=search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountvalidationApi->validation_router_get_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 
 **offset** | **int**| offset | [optional] 
 **limit** | **int**| limit | [optional] 
 **search** | **str**| search | [optional] 

### Return type

[**list[ModelsValidation]**](ModelsValidation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validation_router_validate_email_list**
> ModelsCleanedList validation_router_validate_email_list(x_account_api_key, body)



Validate Email List Synchronously

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountvalidationApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key
body = swagger_client.ModelsEmailList() # ModelsEmailList | The email list to be sent for being validated

try:
    api_response = api_instance.validation_router_validate_email_list(x_account_api_key, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountvalidationApi->validation_router_validate_email_list: %s\n" % e)
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

