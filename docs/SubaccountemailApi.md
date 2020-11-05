# swagger_client.SubaccountemailApi

All URIs are relative to *https://api.sendpost.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**email_router_send_email**](SubaccountemailApi.md#email_router_send_email) | **POST** /subaccount/email/ | 


# **email_router_send_email**
> list[ModelsEmailResponse] email_router_send_email(x_sub_account_api_key, body)



Send Email To Contacts

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubaccountemailApi()
x_sub_account_api_key = 'x_sub_account_api_key_example' # str | Sub-Account API Key
body = swagger_client.ModelsEmailMessage() # ModelsEmailMessage | The Email Message

try:
    api_response = api_instance.email_router_send_email(x_sub_account_api_key, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubaccountemailApi->email_router_send_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_sub_account_api_key** | **str**| Sub-Account API Key | 
 **body** | [**ModelsEmailMessage**](ModelsEmailMessage.md)| The Email Message | 

### Return type

[**list[ModelsEmailResponse]**](ModelsEmailResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

