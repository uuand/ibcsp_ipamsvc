# IpamsvcFixedAddress

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | 
**comment** | **str** | A comment of the Fixed Address object. | [optional] 
**dhcp_options** | [**list[IpamsvcOptionItem]**](IpamsvcOptionItem.md) | A list of DHCP options. May be either a specific option or a group of options. | [optional] 
**id** | **str** | The resource identifier. | [optional] 
**inheritance_assigned_hosts** | [**list[InheritanceAssignedHost]**](InheritanceAssignedHost.md) | Read-only. The list of the inheritance assigned hosts of the object. | [optional] 
**inheritance_parent** | **str** | The resource identifier. | [optional] 
**inheritance_sources** | [**IpamsvcDHCPOptionsInheritance**](IpamsvcDHCPOptionsInheritance.md) | Optional. Inheritance configuration. | [optional] 
**ip_space** | **str** | The resource identifier. | [optional] 
**match_type** | **str** |  | 
**match_value** | **str** | Value to match. | 
**name** | **str** | The name of Fixed Address object. | [optional] 
**parent** | **str** | The resource identifier. | [optional] 
**tags** | [**TypesJSONValue**](TypesJSONValue.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


