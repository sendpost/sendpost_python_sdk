# swagger_client.AccountrecipientApi

All URIs are relative to *https://api.sendpost.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**recipient_router_get_all_messages_for_a_recipient**](AccountrecipientApi.md#recipient_router_get_all_messages_for_a_recipient) | **GET** /account/recipient/{recipient}/messages | 
[**recipient_router_get_all_messages_for_a_recipient_from_a_node**](AccountrecipientApi.md#recipient_router_get_all_messages_for_a_recipient_from_a_node) | **GET** /account/recipient/node/{recipient}/messages | 


# **recipient_router_get_all_messages_for_a_recipient**
> list[ModelsQEmailMessage] recipient_router_get_all_messages_for_a_recipient(x_account_api_key, recipient)



Find all messages sent to a specific recipient

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountrecipientApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key
recipient = 'recipient_example' # str | email of the recipient

try:
    api_response = api_instance.recipient_router_get_all_messages_for_a_recipient(x_account_api_key, recipient)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountrecipientApi->recipient_router_get_all_messages_for_a_recipient: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 
 **recipient** | **str**| email of the recipient | 

### Return type

[**list[ModelsQEmailMessage]**](ModelsQEmailMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recipient_router_get_all_messages_for_a_recipient_from_a_node**
> list[ModelsQEmailMessage] recipient_router_get_all_messages_for_a_recipient_from_a_node(x_account_api_key, recipient)



Find all message sent to a recipient from a specific node

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountrecipientApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key
recipient = 'recipient_example' # str | email of the recipient

try:
    api_response = api_instance.recipient_router_get_all_messages_for_a_recipient_from_a_node(x_account_api_key, recipient)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountrecipientApi->recipient_router_get_all_messages_for_a_recipient_from_a_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 
 **recipient** | **str**| email of the recipient | 

### Return type

[**list[ModelsQEmailMessage]**](ModelsQEmailMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

