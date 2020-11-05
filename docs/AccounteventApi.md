# swagger_client.AccounteventApi

All URIs are relative to *https://api.sendpost.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**event_router_count_all_events_from_a_account_for_a_given_time_range**](AccounteventApi.md#event_router_count_all_events_from_a_account_for_a_given_time_range) | **GET** /account/event/count | 
[**event_router_count_all_events_from_a_node_of_a_sub_account_for_a_given_time_range**](AccounteventApi.md#event_router_count_all_events_from_a_node_of_a_sub_account_for_a_given_time_range) | **GET** /account/event/node/count | 
[**event_router_get**](AccounteventApi.md#event_router_get) | **GET** /account/event/{eventId} | 
[**event_router_get_all_event_timestamp_keys_of_a_sub_account_from_a_specific_node_for_a_given_time_range**](AccounteventApi.md#event_router_get_all_event_timestamp_keys_of_a_sub_account_from_a_specific_node_for_a_given_time_range) | **GET** /account/event/node/timestampkeys | 
[**event_router_get_all_events_of_a_account_from_a_specific_node**](AccounteventApi.md#event_router_get_all_events_of_a_account_from_a_specific_node) | **POST** /account/event/node | 
[**event_router_get_event_in_node**](AccounteventApi.md#event_router_get_event_in_node) | **GET** /account/event/node/{eventId} | 


# **event_router_count_all_events_from_a_account_for_a_given_time_range**
> ModelsCountStat event_router_count_all_events_from_a_account_for_a_given_time_range(x_account_api_key, search=search, type=type, _from=_from, to=to, source=source, source_id=source_id)



Count all events from a account for a given time-range

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccounteventApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key
search = 'search_example' # str | search term (optional)
type = 'type_example' # str | search type (optional)
_from = '_from_example' # str | from date (optional)
to = 'to_example' # str | to date (optional)
source = 'source_example' # str | data source from which to get timestamp keys subaccount or ip (optional)
source_id = 'source_id_example' # str | source id from which to get timestamp keys subaccount or ip (optional)

try:
    api_response = api_instance.event_router_count_all_events_from_a_account_for_a_given_time_range(x_account_api_key, search=search, type=type, _from=_from, to=to, source=source, source_id=source_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccounteventApi->event_router_count_all_events_from_a_account_for_a_given_time_range: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 
 **search** | **str**| search term | [optional] 
 **type** | **str**| search type | [optional] 
 **_from** | **str**| from date | [optional] 
 **to** | **str**| to date | [optional] 
 **source** | **str**| data source from which to get timestamp keys subaccount or ip | [optional] 
 **source_id** | **str**| source id from which to get timestamp keys subaccount or ip | [optional] 

### Return type

[**ModelsCountStat**](ModelsCountStat.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_router_count_all_events_from_a_node_of_a_sub_account_for_a_given_time_range**
> ModelsCountStat event_router_count_all_events_from_a_node_of_a_sub_account_for_a_given_time_range(x_account_api_key, search=search, type=type, _from=_from, to=to, source=source, source_id=source_id)



Count all events from a node of a sub-account for a given time-range

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccounteventApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key
search = 'search_example' # str | search term (optional)
type = 'type_example' # str | search type (optional)
_from = '_from_example' # str | from date (optional)
to = 'to_example' # str | to date (optional)
source = 'source_example' # str | data source from which to get timestamp keys subaccount or ip (optional)
source_id = 'source_id_example' # str | source id from which to get timestamp keys subaccount or ip (optional)

try:
    api_response = api_instance.event_router_count_all_events_from_a_node_of_a_sub_account_for_a_given_time_range(x_account_api_key, search=search, type=type, _from=_from, to=to, source=source, source_id=source_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccounteventApi->event_router_count_all_events_from_a_node_of_a_sub_account_for_a_given_time_range: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 
 **search** | **str**| search term | [optional] 
 **type** | **str**| search type | [optional] 
 **_from** | **str**| from date | [optional] 
 **to** | **str**| to date | [optional] 
 **source** | **str**| data source from which to get timestamp keys subaccount or ip | [optional] 
 **source_id** | **str**| source id from which to get timestamp keys subaccount or ip | [optional] 

### Return type

[**ModelsCountStat**](ModelsCountStat.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_router_get**
> ModelsQEvent event_router_get(x_account_api_key, event_id)



Find Event By Id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccounteventApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key
event_id = 'event_id_example' # str | the eventId that you want to retrieve

try:
    api_response = api_instance.event_router_get(x_account_api_key, event_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccounteventApi->event_router_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 
 **event_id** | **str**| the eventId that you want to retrieve | 

### Return type

[**ModelsQEvent**](ModelsQEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_router_get_all_event_timestamp_keys_of_a_sub_account_from_a_specific_node_for_a_given_time_range**
> list[ModelsQEvent] event_router_get_all_event_timestamp_keys_of_a_sub_account_from_a_specific_node_for_a_given_time_range(x_account_api_key, search=search, type=type, _from=_from, to=to, source=source, source_id=source_id)



Find all events of a sub-account from a specific node for a give time-range

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccounteventApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key
search = 'search_example' # str | search term (optional)
type = 'type_example' # str | search type (optional)
_from = '_from_example' # str | from date (optional)
to = 'to_example' # str | to date (optional)
source = 'source_example' # str | data source from which to get timestamp keys subaccount or ip (optional)
source_id = 'source_id_example' # str | source id from which to get timestamp keys subaccount or ip (optional)

try:
    api_response = api_instance.event_router_get_all_event_timestamp_keys_of_a_sub_account_from_a_specific_node_for_a_given_time_range(x_account_api_key, search=search, type=type, _from=_from, to=to, source=source, source_id=source_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccounteventApi->event_router_get_all_event_timestamp_keys_of_a_sub_account_from_a_specific_node_for_a_given_time_range: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 
 **search** | **str**| search term | [optional] 
 **type** | **str**| search type | [optional] 
 **_from** | **str**| from date | [optional] 
 **to** | **str**| to date | [optional] 
 **source** | **str**| data source from which to get timestamp keys subaccount or ip | [optional] 
 **source_id** | **str**| source id from which to get timestamp keys subaccount or ip | [optional] 

### Return type

[**list[ModelsQEvent]**](ModelsQEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_router_get_all_events_of_a_account_from_a_specific_node**
> list[ModelsQEvent] event_router_get_all_events_of_a_account_from_a_specific_node(x_account_api_key)



Find all events of a account from a specific node

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccounteventApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key

try:
    api_response = api_instance.event_router_get_all_events_of_a_account_from_a_specific_node(x_account_api_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccounteventApi->event_router_get_all_events_of_a_account_from_a_specific_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 

### Return type

[**list[ModelsQEvent]**](ModelsQEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **event_router_get_event_in_node**
> ModelsQEvent event_router_get_event_in_node(x_account_api_key, event_id)



Find Event From Node by id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccounteventApi()
x_account_api_key = 'x_account_api_key_example' # str | Account API Key
event_id = 'event_id_example' # str | the eventId that you want to retrieve

try:
    api_response = api_instance.event_router_get_event_in_node(x_account_api_key, event_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccounteventApi->event_router_get_event_in_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_api_key** | **str**| Account API Key | 
 **event_id** | **str**| the eventId that you want to retrieve | 

### Return type

[**ModelsQEvent**](ModelsQEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

