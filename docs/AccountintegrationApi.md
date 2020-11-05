# swagger_client.AccountintegrationApi

All URIs are relative to *https://api.sendpost.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_integration_router_count**](AccountintegrationApi.md#account_integration_router_count) | **GET** /account/integration/count | 
[**account_integration_router_create**](AccountintegrationApi.md#account_integration_router_create) | **POST** /account/integration/{itype} | 
[**account_integration_router_delete**](AccountintegrationApi.md#account_integration_router_delete) | **DELETE** /account/integration/{itype} | 
[**account_integration_router_disable_glockapps_ip_monitoring**](AccountintegrationApi.md#account_integration_router_disable_glockapps_ip_monitoring) | **DELETE** /account/integration/glockapps/monitor/{ipid} | 
[**account_integration_router_enable_glockapps_ip_monitoring**](AccountintegrationApi.md#account_integration_router_enable_glockapps_ip_monitoring) | **POST** /account/integration/glockapps/monitor/{ipid} | 
[**account_integration_router_get_all**](AccountintegrationApi.md#account_integration_router_get_all) | **GET** /account/integration/ | 
[**account_integration_router_get_monitored_ip_stats**](AccountintegrationApi.md#account_integration_router_get_monitored_ip_stats) | **GET** /account/integration/glockapps/monitor/stat/{ipid} | 
[**account_integration_router_update**](AccountintegrationApi.md#account_integration_router_update) | **PUT** /account/integration/{itype} | 


# **account_integration_router_count**
> ModelsCountStat account_integration_router_count(x_account_api_key)



Count Total AccountIntegrations

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountintegrationApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key

try:
    api_response = api_instance.account_integration_router_count(x_account_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountintegrationApi->account_integration_router_count: %s\n" % e)
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

# **account_integration_router_create**
> ModelsIntegration account_integration_router_create(x_account_api_key, itype, body)



Create Integration

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountintegrationApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key
itype = 'itype_example' # str | The integration type you want to create
body = swagger_client.ModelsEIntegration() # ModelsEIntegration | The Integration content

try:
    api_response = api_instance.account_integration_router_create(x_account_api_key, itype, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountintegrationApi->account_integration_router_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 
 **itype** | **str**| The integration type you want to create | 
 **body** | [**ModelsEIntegration**](ModelsEIntegration.md)| The Integration content | 

### Return type

[**ModelsIntegration**](ModelsIntegration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_integration_router_delete**
> ModelsDeleteResponse account_integration_router_delete(x_account_api_key, itype)



Delete Integration

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountintegrationApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key
itype = 'itype_example' # str | The integration type you want to update

try:
    api_response = api_instance.account_integration_router_delete(x_account_api_key, itype)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountintegrationApi->account_integration_router_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 
 **itype** | **str**| The integration type you want to update | 

### Return type

[**ModelsDeleteResponse**](ModelsDeleteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_integration_router_disable_glockapps_ip_monitoring**
> ModelsDeleteResponse account_integration_router_disable_glockapps_ip_monitoring(x_account_api_key, ipid)



Disable IP Monitoring for a single IP

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountintegrationApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key
ipid = 789 # int | the IPId you want to disable monitoring for

try:
    api_response = api_instance.account_integration_router_disable_glockapps_ip_monitoring(x_account_api_key, ipid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountintegrationApi->account_integration_router_disable_glockapps_ip_monitoring: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 
 **ipid** | **int**| the IPId you want to disable monitoring for | 

### Return type

[**ModelsDeleteResponse**](ModelsDeleteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_integration_router_enable_glockapps_ip_monitoring**
> ModelsResponse account_integration_router_enable_glockapps_ip_monitoring(x_account_api_key, ipid)



Enable IP Monitoring for a single IP

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountintegrationApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key
ipid = 789 # int | the IPId you want to enable monitoring for

try:
    api_response = api_instance.account_integration_router_enable_glockapps_ip_monitoring(x_account_api_key, ipid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountintegrationApi->account_integration_router_enable_glockapps_ip_monitoring: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 
 **ipid** | **int**| the IPId you want to enable monitoring for | 

### Return type

[**ModelsResponse**](ModelsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_integration_router_get_all**
> list[ModelsIntegration] account_integration_router_get_all(x_account_api_key)



Get All Integrations

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountintegrationApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key

try:
    api_response = api_instance.account_integration_router_get_all(x_account_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountintegrationApi->account_integration_router_get_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 

### Return type

[**list[ModelsIntegration]**](ModelsIntegration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_integration_router_get_monitored_ip_stats**
> list[ModelsRGlockappsMonitorStat] account_integration_router_get_monitored_ip_stats(x_account_api_key, ipid, _from=_from, to=to)



Get Monitored IP Stats

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountintegrationApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key
ipid = 789 # int | the IPId for which you want monitored stats
_from = '_from_example' # str | from date (optional)
to = 'to_example' # str | to date (optional)

try:
    api_response = api_instance.account_integration_router_get_monitored_ip_stats(x_account_api_key, ipid, _from=_from, to=to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountintegrationApi->account_integration_router_get_monitored_ip_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 
 **ipid** | **int**| the IPId for which you want monitored stats | 
 **_from** | **str**| from date | [optional] 
 **to** | **str**| to date | [optional] 

### Return type

[**list[ModelsRGlockappsMonitorStat]**](ModelsRGlockappsMonitorStat.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_integration_router_update**
> ModelsIntegration account_integration_router_update(x_account_api_key, itype, body)



Update Integration

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountintegrationApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key
itype = 'itype_example' # str | The integration type you want to update
body = swagger_client.ModelsEIntegration() # ModelsEIntegration | The Integration content

try:
    api_response = api_instance.account_integration_router_update(x_account_api_key, itype, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountintegrationApi->account_integration_router_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 
 **itype** | **str**| The integration type you want to update | 
 **body** | [**ModelsEIntegration**](ModelsEIntegration.md)| The Integration content | 

### Return type

[**ModelsIntegration**](ModelsIntegration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

