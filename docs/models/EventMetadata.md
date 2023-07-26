# sendpost_python_sdk.model.event_metadata.EventMetadata

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**clickedURL** | str,  | str,  |  | [optional] 
**device** | [**Device**](Device.md) | [**Device**](Device.md) |  | [optional] 
**geo** | [**City**](City.md) | [**City**](City.md) |  | [optional] 
**os** | [**Os**](Os.md) | [**Os**](Os.md) |  | [optional] 
**smtpCode** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**smtpDescription** | str,  | str,  |  | [optional] 
**userAgent** | [**UserAgent**](UserAgent.md) | [**UserAgent**](UserAgent.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

