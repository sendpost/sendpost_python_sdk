# swagger_client.AccountpaymentApi

All URIs are relative to *https://api.sendpost.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**payment_router_create_customer_portal**](AccountpaymentApi.md#payment_router_create_customer_portal) | **POST** /account/payment/portal | 
[**payment_router_create_payment_subscription**](AccountpaymentApi.md#payment_router_create_payment_subscription) | **POST** /account/payment/subscription | 
[**payment_router_handle_payment_webhook**](AccountpaymentApi.md#payment_router_handle_payment_webhook) | **POST** /account/payment/webhook | 


# **payment_router_create_customer_portal**
> ModelsBillingPortalSession payment_router_create_customer_portal(x_account_api_key)



Create Customer Portal for account

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountpaymentApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key

try:
    api_response = api_instance.payment_router_create_customer_portal(x_account_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountpaymentApi->payment_router_create_customer_portal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 

### Return type

[**ModelsBillingPortalSession**](ModelsBillingPortalSession.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_router_create_payment_subscription**
> ModelsPaymentStatus payment_router_create_payment_subscription(x_account_api_key, body)



Create Payment Subscription for Stripe

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountpaymentApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key
body = swagger_client.ModelsPaymentOptions() # ModelsPaymentOptions | PaymentOptions content

try:
    api_response = api_instance.payment_router_create_payment_subscription(x_account_api_key, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountpaymentApi->payment_router_create_payment_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 
 **body** | [**ModelsPaymentOptions**](ModelsPaymentOptions.md)| PaymentOptions content | 

### Return type

[**ModelsPaymentStatus**](ModelsPaymentStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_router_handle_payment_webhook**
> payment_router_handle_payment_webhook()



Handle Payment Related Webhooks

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountpaymentApi()

try:
    api_instance.payment_router_handle_payment_webhook()
except ApiException as e:
    print("Exception when calling AccountpaymentApi->payment_router_handle_payment_webhook: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

