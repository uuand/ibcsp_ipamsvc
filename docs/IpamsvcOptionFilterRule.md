# IpamsvcOptionFilterRule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compare** | **str** | How to compare the option_value to the client option.  Success by comparison: - equals: value and client option are the same - not_equals: value and client option are not the same - exists: client option exists - not_exists: client option does not exist - substring: value is the specified substring of the option - not_substring: value is not the specified substring of the option | 
**option_code** | **str** | The resource identifier. | 
**option_value** | **str** | Value to match against. | [optional] 
**substring_offset** | **int** | Offset where substring match starts, used only if compare is one of the substring modes. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


