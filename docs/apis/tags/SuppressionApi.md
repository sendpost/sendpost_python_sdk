<a id="__pageTop"></a>
# sendpost_python_sdk.apis.tags.suppression_api.SuppressionApi

All URIs are relative to *https://api.sendpost.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count**](#count) | **get** /subaccount/suppression/count | 
[**create_suppressions**](#create_suppressions) | **post** /subaccount/suppression/ | 
[**delete_suppression**](#delete_suppression) | **delete** /subaccount/suppression/ | 
[**get_suppressions**](#get_suppressions) | **get** /subaccount/suppression/ | 

# **count**
<a id="count"></a>
> CountStat count(x_sub_account_api_key)



Count Total Suppressions

### Example

```python
import sendpost_python_sdk
from sendpost_python_sdk.apis.tags import suppression_api
from sendpost_python_sdk.model.count_stat import CountStat
from pprint import pprint
# Defining the host is optional and defaults to https://api.sendpost.io/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = sendpost_python_sdk.Configuration(
    host = "https://api.sendpost.io/api/v1"
)

# Enter a context with an instance of the API client
with sendpost_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = suppression_api.SuppressionApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
    }
    header_params = {
        'X-SubAccount-ApiKey': "X-SubAccount-ApiKey_example",
    }
    try:
        api_response = api_instance.count(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except sendpost_python_sdk.ApiException as e:
        print("Exception when calling SuppressionApi->count: %s\n" % e)

    # example passing only optional values
    query_params = {
        'from': "from_example",
        'to': "to_example",
    }
    header_params = {
        'X-SubAccount-ApiKey': "X-SubAccount-ApiKey_example",
    }
    try:
        api_response = api_instance.count(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except sendpost_python_sdk.ApiException as e:
        print("Exception when calling SuppressionApi->count: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
header_params | RequestHeaderParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
from | ModelFromSchema | | optional
to | ToSchema | | optional


# ModelFromSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ToSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-SubAccount-ApiKey | XSubAccountApiKeySchema | | 

# XSubAccountApiKeySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#count.ApiResponseFor200) | \&quot;Total count of Suppressions for a specific sub-account\&quot;
401 | [ApiResponseFor401](#count.ApiResponseFor401) | Not Authorized
500 | [ApiResponseFor500](#count.ApiResponseFor500) | Internal Server Error

#### count.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CountStat**](../../models/CountStat.md) |  | 


#### count.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### count.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_suppressions**
<a id="create_suppressions"></a>
> [Suppression] create_suppressions(x_sub_account_api_key)



Add Email Addresses To Suppression List

### Example

```python
import sendpost_python_sdk
from sendpost_python_sdk.apis.tags import suppression_api
from sendpost_python_sdk.model.suppression import Suppression
from sendpost_python_sdk.model.r_suppression import RSuppression
from pprint import pprint
# Defining the host is optional and defaults to https://api.sendpost.io/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = sendpost_python_sdk.Configuration(
    host = "https://api.sendpost.io/api/v1"
)

# Enter a context with an instance of the API client
with sendpost_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = suppression_api.SuppressionApi(api_client)

    # example passing only required values which don't have defaults set
    header_params = {
        'X-SubAccount-ApiKey': "X-SubAccount-ApiKey_example",
    }
    try:
        api_response = api_instance.create_suppressions(
            header_params=header_params,
        )
        pprint(api_response)
    except sendpost_python_sdk.ApiException as e:
        print("Exception when calling SuppressionApi->create_suppressions: %s\n" % e)

    # example passing only optional values
    header_params = {
        'X-SubAccount-ApiKey': "X-SubAccount-ApiKey_example",
    }
    body = RSuppression(
        hard_bounce=[
            SuppressionEmail(
                email="email_example",
            )
        ],
,
,
,
    )
    try:
        api_response = api_instance.create_suppressions(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except sendpost_python_sdk.ApiException as e:
        print("Exception when calling SuppressionApi->create_suppressions: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
header_params | RequestHeaderParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RSuppression**](../../models/RSuppression.md) |  | 


### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-SubAccount-ApiKey | XSubAccountApiKeySchema | | 

# XSubAccountApiKeySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_suppressions.ApiResponseFor200) | \&quot;Suppressions created successfully\&quot;
401 | [ApiResponseFor401](#create_suppressions.ApiResponseFor401) | Not Authorized
406 | [ApiResponseFor406](#create_suppressions.ApiResponseFor406) | Suppression list is empty
422 | [ApiResponseFor422](#create_suppressions.ApiResponseFor422) | Request body is not in proper format
500 | [ApiResponseFor500](#create_suppressions.ApiResponseFor500) | Internal Server Error

#### create_suppressions.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Suppression**]({{complexTypePrefix}}Suppression.md) | [**Suppression**]({{complexTypePrefix}}Suppression.md) | [**Suppression**]({{complexTypePrefix}}Suppression.md) |  | 

#### create_suppressions.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_suppressions.ApiResponseFor406
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_suppressions.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_suppressions.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_suppression**
<a id="delete_suppression"></a>
> [DeleteResponse] delete_suppression(x_sub_account_api_key)



Delete specific emails which are in suppression list

### Example

```python
import sendpost_python_sdk
from sendpost_python_sdk.apis.tags import suppression_api
from sendpost_python_sdk.model.rd_suppression import RDSuppression
from sendpost_python_sdk.model.delete_response import DeleteResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.sendpost.io/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = sendpost_python_sdk.Configuration(
    host = "https://api.sendpost.io/api/v1"
)

# Enter a context with an instance of the API client
with sendpost_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = suppression_api.SuppressionApi(api_client)

    # example passing only required values which don't have defaults set
    header_params = {
        'X-SubAccount-ApiKey': "X-SubAccount-ApiKey_example",
    }
    try:
        api_response = api_instance.delete_suppression(
            header_params=header_params,
        )
        pprint(api_response)
    except sendpost_python_sdk.ApiException as e:
        print("Exception when calling SuppressionApi->delete_suppression: %s\n" % e)

    # example passing only optional values
    header_params = {
        'X-SubAccount-ApiKey': "X-SubAccount-ApiKey_example",
    }
    body = RDSuppression(
        suppressions=[
            SuppressionEmail(
                email="email_example",
            )
        ],
    )
    try:
        api_response = api_instance.delete_suppression(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except sendpost_python_sdk.ApiException as e:
        print("Exception when calling SuppressionApi->delete_suppression: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
header_params | RequestHeaderParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RDSuppression**](../../models/RDSuppression.md) |  | 


### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-SubAccount-ApiKey | XSubAccountApiKeySchema | | 

# XSubAccountApiKeySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#delete_suppression.ApiResponseFor200) | \&quot;Emails in suppression list have been deleted successfully\&quot;
401 | [ApiResponseFor401](#delete_suppression.ApiResponseFor401) | Not Authorized
406 | [ApiResponseFor406](#delete_suppression.ApiResponseFor406) | suppression list is empty
422 | [ApiResponseFor422](#delete_suppression.ApiResponseFor422) | Request body is not in proper format
500 | [ApiResponseFor500](#delete_suppression.ApiResponseFor500) | Internal Server Error

#### delete_suppression.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**DeleteResponse**]({{complexTypePrefix}}DeleteResponse.md) | [**DeleteResponse**]({{complexTypePrefix}}DeleteResponse.md) | [**DeleteResponse**]({{complexTypePrefix}}DeleteResponse.md) |  | 

#### delete_suppression.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_suppression.ApiResponseFor406
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_suppression.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_suppression.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_suppressions**
<a id="get_suppressions"></a>
> [Suppression] get_suppressions(x_sub_account_api_key)



Get all suppressions

### Example

```python
import sendpost_python_sdk
from sendpost_python_sdk.apis.tags import suppression_api
from sendpost_python_sdk.model.suppression import Suppression
from pprint import pprint
# Defining the host is optional and defaults to https://api.sendpost.io/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = sendpost_python_sdk.Configuration(
    host = "https://api.sendpost.io/api/v1"
)

# Enter a context with an instance of the API client
with sendpost_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = suppression_api.SuppressionApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
    }
    header_params = {
        'X-SubAccount-ApiKey': "X-SubAccount-ApiKey_example",
    }
    try:
        api_response = api_instance.get_suppressions(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except sendpost_python_sdk.ApiException as e:
        print("Exception when calling SuppressionApi->get_suppressions: %s\n" % e)

    # example passing only optional values
    query_params = {
        'offset': 1,
        'limit': 1,
        'search': "search_example",
        'from': "from_example",
        'to': "to_example",
    }
    header_params = {
        'X-SubAccount-ApiKey': "X-SubAccount-ApiKey_example",
    }
    try:
        api_response = api_instance.get_suppressions(
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except sendpost_python_sdk.ApiException as e:
        print("Exception when calling SuppressionApi->get_suppressions: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
header_params | RequestHeaderParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
offset | OffsetSchema | | optional
limit | LimitSchema | | optional
search | SearchSchema | | optional
from | ModelFromSchema | | optional
to | ToSchema | | optional


# OffsetSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

# SearchSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ModelFromSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ToSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-SubAccount-ApiKey | XSubAccountApiKeySchema | | 

# XSubAccountApiKeySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_suppressions.ApiResponseFor200) | \&quot;Suppressions retrieved successfully\&quot;
401 | [ApiResponseFor401](#get_suppressions.ApiResponseFor401) | Not Authorized
500 | [ApiResponseFor500](#get_suppressions.ApiResponseFor500) | Internal Server Error

#### get_suppressions.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Suppression**]({{complexTypePrefix}}Suppression.md) | [**Suppression**]({{complexTypePrefix}}Suppression.md) | [**Suppression**]({{complexTypePrefix}}Suppression.md) |  | 

#### get_suppressions.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_suppressions.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

