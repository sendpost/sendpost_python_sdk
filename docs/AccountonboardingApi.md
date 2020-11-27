# swagger_client.AccountonboardingApi

All URIs are relative to *https://api.sendpost.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**onboarding_router_get_onboarding_checklist**](AccountonboardingApi.md#onboarding_router_get_onboarding_checklist) | **GET** /account/onboarding/checklist | 


# **onboarding_router_get_onboarding_checklist**
> ModelsOnboardingChecklist onboarding_router_get_onboarding_checklist(x_account_api_key)



Gets Onboarding Checklist data for account if not present creates a default entry

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountonboardingApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key

try:
    api_response = api_instance.onboarding_router_get_onboarding_checklist(x_account_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountonboardingApi->onboarding_router_get_onboarding_checklist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 

### Return type

[**ModelsOnboardingChecklist**](ModelsOnboardingChecklist.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

