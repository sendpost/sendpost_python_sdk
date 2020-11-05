# swagger_client.AccountmemberApi

All URIs are relative to *https://api.sendpost.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**member_router_delete**](AccountmemberApi.md#member_router_delete) | **DELETE** /account/member/{memberId} | 
[**member_router_get**](AccountmemberApi.md#member_router_get) | **GET** /account/member/{memberId} | 
[**member_router_get_all**](AccountmemberApi.md#member_router_get_all) | **GET** /account/member/ | 


# **member_router_delete**
> ModelsDeleteResponse member_router_delete(x_account_api_key, member_id)



Delete Member

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountmemberApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key
member_id = 789 # int | The MemberId you want to delete

try:
    api_response = api_instance.member_router_delete(x_account_api_key, member_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountmemberApi->member_router_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 
 **member_id** | **int**| The MemberId you want to delete | 

### Return type

[**ModelsDeleteResponse**](ModelsDeleteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **member_router_get**
> ModelsMember member_router_get(x_account_api_key, member_id)



Find Member by MemberId

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountmemberApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key
member_id = 789 # int | the MemberId you want to get

try:
    api_response = api_instance.member_router_get(x_account_api_key, member_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountmemberApi->member_router_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 
 **member_id** | **int**| the MemberId you want to get | 

### Return type

[**ModelsMember**](ModelsMember.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **member_router_get_all**
> list[ModelsMember] member_router_get_all(x_account_api_key)



Get All Members

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountmemberApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key

try:
    api_response = api_instance.member_router_get_all(x_account_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountmemberApi->member_router_get_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 

### Return type

[**list[ModelsMember]**](ModelsMember.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

