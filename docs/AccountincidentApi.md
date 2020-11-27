# swagger_client.AccountincidentApi

All URIs are relative to *https://api.sendpost.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**incident_router_add**](AccountincidentApi.md#incident_router_add) | **POST** /account/incident/{incidentId}/comment | 
[**incident_router_count**](AccountincidentApi.md#incident_router_count) | **GET** /account/incident/count | 
[**incident_router_create**](AccountincidentApi.md#incident_router_create) | **POST** /account/incident/ | 
[**incident_router_get_all**](AccountincidentApi.md#incident_router_get_all) | **GET** /account/incident/ | 
[**incident_router_get_all_comments**](AccountincidentApi.md#incident_router_get_all_comments) | **GET** /account/incident/{incidentId}/comment | 
[**incident_router_get_incident**](AccountincidentApi.md#incident_router_get_incident) | **GET** /account/incident/{incidentId} | 
[**incident_router_update**](AccountincidentApi.md#incident_router_update) | **PUT** /account/incident/{incidentId} | 


# **incident_router_add**
> ModelsComment incident_router_add(x_account_api_key, incident_id, body)



Add comment to Incident

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountincidentApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key
incident_id = 789 # int | the incident id
body = swagger_client.ModelsEComment() # ModelsEComment | The Comment content

try:
    api_response = api_instance.incident_router_add(x_account_api_key, incident_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountincidentApi->incident_router_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 
 **incident_id** | **int**| the incident id | 
 **body** | [**ModelsEComment**](ModelsEComment.md)| The Comment content | 

### Return type

[**ModelsComment**](ModelsComment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **incident_router_count**
> ModelsCountStat incident_router_count(x_account_api_key, status=status, tag=tag, search=search)



Count Total Incidents

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountincidentApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key
status = 789 # int | status (optional)
tag = 789 # int | status (optional)
search = 'search_example' # str | search term (optional)

try:
    api_response = api_instance.incident_router_count(x_account_api_key, status=status, tag=tag, search=search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountincidentApi->incident_router_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 
 **status** | **int**| status | [optional] 
 **tag** | **int**| status | [optional] 
 **search** | **str**| search term | [optional] 

### Return type

[**ModelsCountStat**](ModelsCountStat.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **incident_router_create**
> ModelsIncident incident_router_create(x_account_api_key, body)



Create Incident

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountincidentApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key
body = swagger_client.ModelsEIncident() # ModelsEIncident | The Incident content

try:
    api_response = api_instance.incident_router_create(x_account_api_key, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountincidentApi->incident_router_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 
 **body** | [**ModelsEIncident**](ModelsEIncident.md)| The Incident content | 

### Return type

[**ModelsIncident**](ModelsIncident.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **incident_router_get_all**
> list[ModelsIncident] incident_router_get_all(x_account_api_key, offset=offset, limit=limit, search=search, status=status, tag=tag)



Get All Incidents

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountincidentApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key
offset = 789 # int | offset (optional)
limit = 789 # int | limit (optional)
search = 'search_example' # str | search term (optional)
status = 789 # int | status (optional)
tag = 789 # int | status (optional)

try:
    api_response = api_instance.incident_router_get_all(x_account_api_key, offset=offset, limit=limit, search=search, status=status, tag=tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountincidentApi->incident_router_get_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 
 **offset** | **int**| offset | [optional] 
 **limit** | **int**| limit | [optional] 
 **search** | **str**| search term | [optional] 
 **status** | **int**| status | [optional] 
 **tag** | **int**| status | [optional] 

### Return type

[**list[ModelsIncident]**](ModelsIncident.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **incident_router_get_all_comments**
> list[ModelsComment] incident_router_get_all_comments(x_account_api_key, incident_id)



Get All Comments Associated with Incident

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountincidentApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key
incident_id = 789 # int | the IncidentId you want to get comments for

try:
    api_response = api_instance.incident_router_get_all_comments(x_account_api_key, incident_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountincidentApi->incident_router_get_all_comments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 
 **incident_id** | **int**| the IncidentId you want to get comments for | 

### Return type

[**list[ModelsComment]**](ModelsComment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **incident_router_get_incident**
> ModelsIncident incident_router_get_incident(x_account_api_key, incident_id)



Find Incident by incidentId

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountincidentApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key
incident_id = 789 # int | the IncidentId you want to get

try:
    api_response = api_instance.incident_router_get_incident(x_account_api_key, incident_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountincidentApi->incident_router_get_incident: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 
 **incident_id** | **int**| the IncidentId you want to get | 

### Return type

[**ModelsIncident**](ModelsIncident.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **incident_router_update**
> ModelsIncident incident_router_update(x_account_api_key, incident_id, body)



Update Incident

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountincidentApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key
incident_id = 789 # int | the Incident Id you want to update
body = swagger_client.ModelsEIncident() # ModelsEIncident | The Incident content

try:
    api_response = api_instance.incident_router_update(x_account_api_key, incident_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountincidentApi->incident_router_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 
 **incident_id** | **int**| the Incident Id you want to update | 
 **body** | [**ModelsEIncident**](ModelsEIncident.md)| The Incident content | 

### Return type

[**ModelsIncident**](ModelsIncident.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

