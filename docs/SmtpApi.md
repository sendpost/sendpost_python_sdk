# swagger_client.SmtpApi

All URIs are relative to *https://api.sendpost.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**s_mtp_router_receive_webhooks_raised_from_smtp_servers**](SmtpApi.md#s_mtp_router_receive_webhooks_raised_from_smtp_servers) | **POST** /smtp/webhook | 


# **s_mtp_router_receive_webhooks_raised_from_smtp_servers**
> s_mtp_router_receive_webhooks_raised_from_smtp_servers(body)



Receive webhooks raised from SMTP servers

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SmtpApi()
body = swagger_client.ModelsWMessage() # ModelsWMessage | The Webhook content

try:
    api_instance.s_mtp_router_receive_webhooks_raised_from_smtp_servers(body)
except ApiException as e:
    print("Exception when calling SmtpApi->s_mtp_router_receive_webhooks_raised_from_smtp_servers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ModelsWMessage**](ModelsWMessage.md)| The Webhook content | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

