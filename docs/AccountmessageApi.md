# swagger_client.AccountmessageApi

All URIs are relative to *https://api.sendpost.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**message_router_get**](AccountmessageApi.md#message_router_get) | **GET** /account/message/{messageId} | 
[**message_router_get_all_events_for_a_message_id**](AccountmessageApi.md#message_router_get_all_events_for_a_message_id) | **GET** /account/message/{messageId}/events | 
[**message_router_get_all_events_for_a_message_id_from_a_node**](AccountmessageApi.md#message_router_get_all_events_for_a_message_id_from_a_node) | **GET** /account/message/node/{messageId}/events | 
[**message_router_get_message_from_node**](AccountmessageApi.md#message_router_get_message_from_node) | **GET** /account/message/node/{messageId} | 


# **message_router_get**
> ModelsQEmailMessage message_router_get(x_account_api_key, message_id)



Find Message By Id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountmessageApi()
x_account_api_key = 'x_account_api_key_example' # str | Sub-Account API Key
message_id = 'message_id_example' # str | the messageId that you want to retrieve

try:
    api_response = api_instance.message_router_get(x_account_api_key, message_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountmessageApi->message_router_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Sub-Account API Key | 
 **message_id** | **str**| the messageId that you want to retrieve | 

### Return type

[**ModelsQEmailMessage**](ModelsQEmailMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **message_router_get_all_events_for_a_message_id**
> list[ModelsQEvent] message_router_get_all_events_for_a_message_id(x_account_api_key, message_id)



Find all events associated with a message id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountmessageApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key
message_id = 'message_id_example' # str | the messageId that you want to retrieve

try:
    api_response = api_instance.message_router_get_all_events_for_a_message_id(x_account_api_key, message_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountmessageApi->message_router_get_all_events_for_a_message_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 
 **message_id** | **str**| the messageId that you want to retrieve | 

### Return type

[**list[ModelsQEvent]**](ModelsQEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **message_router_get_all_events_for_a_message_id_from_a_node**
> list[ModelsQEvent] message_router_get_all_events_for_a_message_id_from_a_node(x_account_api_key, message_id)



Find all message events associated with a message id from a specific node

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountmessageApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key
message_id = 'message_id_example' # str | the messageId that you want to retrieve

try:
    api_response = api_instance.message_router_get_all_events_for_a_message_id_from_a_node(x_account_api_key, message_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountmessageApi->message_router_get_all_events_for_a_message_id_from_a_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 
 **message_id** | **str**| the messageId that you want to retrieve | 

### Return type

[**list[ModelsQEvent]**](ModelsQEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **message_router_get_message_from_node**
> ModelsQEmailMessage message_router_get_message_from_node(x_account_api_key, message_id)



Find Message from node by specific Id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountmessageApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key
message_id = 'message_id_example' # str | the messageId that you want to retrieve

try:
    api_response = api_instance.message_router_get_message_from_node(x_account_api_key, message_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountmessageApi->message_router_get_message_from_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 
 **message_id** | **str**| the messageId that you want to retrieve | 

### Return type

[**ModelsQEmailMessage**](ModelsQEmailMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

