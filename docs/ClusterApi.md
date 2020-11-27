# swagger_client.ClusterApi

All URIs are relative to *https://api.sendpost.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cluster_router_delete_item_from_cache_of_every_node_in_cluster**](ClusterApi.md#cluster_router_delete_item_from_cache_of_every_node_in_cluster) | **DELETE** /cluster/cache | 
[**cluster_router_delete_item_from_cache_of_specific_node_in_cluster**](ClusterApi.md#cluster_router_delete_item_from_cache_of_specific_node_in_cluster) | **DELETE** /cluster/cache/node | 


# **cluster_router_delete_item_from_cache_of_every_node_in_cluster**
> cluster_router_delete_item_from_cache_of_every_node_in_cluster(x_system_api_key, name=name, key=key)



Delete item from cache of every node in cluster

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClusterApi()
x_system_api_key = 'x_system_api_key_example' # str | System API Key
name = 'name_example' # str | cache name (optional)
key = 'key_example' # str | cache item key to delete (optional)

try:
    api_instance.cluster_router_delete_item_from_cache_of_every_node_in_cluster(x_system_api_key, name=name, key=key)
except ApiException as e:
    print("Exception when calling ClusterApi->cluster_router_delete_item_from_cache_of_every_node_in_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_system_api_key** | **str**| System API Key | 
 **name** | **str**| cache name | [optional] 
 **key** | **str**| cache item key to delete | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cluster_router_delete_item_from_cache_of_specific_node_in_cluster**
> cluster_router_delete_item_from_cache_of_specific_node_in_cluster(x_system_api_key, name=name, key=key)



Delete item from cache of specific node in cluster

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClusterApi()
x_system_api_key = 'x_system_api_key_example' # str | System API Key
name = 'name_example' # str | cache name (optional)
key = 'key_example' # str | cache item key to delete (optional)

try:
    api_instance.cluster_router_delete_item_from_cache_of_specific_node_in_cluster(x_system_api_key, name=name, key=key)
except ApiException as e:
    print("Exception when calling ClusterApi->cluster_router_delete_item_from_cache_of_specific_node_in_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_system_api_key** | **str**| System API Key | 
 **name** | **str**| cache name | [optional] 
 **key** | **str**| cache item key to delete | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

