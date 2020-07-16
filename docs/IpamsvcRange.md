# IpamsvcRange

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | A comment of the Range object. | [optional] 
**dhcp_host** | **str** | The resource identifier. | [optional] 
**dhcp_options** | [**list[IpamsvcOptionItem]**](IpamsvcOptionItem.md) | A list of DHCP options. May be either a specific option or a group of options. | [optional] 
**end** | **str** | The end IP Address of the range. | 
**exclusion_ranges** | [**list[IpamsvcExclusionRange]**](IpamsvcExclusionRange.md) | List of all exclusion ranges, applicable only to ranges. | [optional] 
**id** | **str** | The resource identifier. | [optional] 
**inheritance_assigned_hosts** | [**list[InheritanceAssignedHost]**](InheritanceAssignedHost.md) | Read-only. The list of the inheritance assigned hosts of the object. | [optional] 
**inheritance_parent** | **str** | The resource identifier. | [optional] 
**inheritance_sources** | [**IpamsvcDHCPOptionsInheritance**](IpamsvcDHCPOptionsInheritance.md) | Optional. Inheritance configuration. | [optional] 
**name** | **str** | The name of the Range object. | [optional] 
**parent** | **str** | The resource identifier. | [optional] 
**protocol** | **str** | RO Field: The type of protocol (ipv4 or ipv6). | [optional] 
**space** | **str** | The resource identifier. | 
**start** | **str** | The start IP Address of the range. | 
**tags** | [**TypesJSONValue**](TypesJSONValue.md) | Tagging specifics. | [optional] 
**threshold** | [**IpamsvcUtilizationThreshold**](IpamsvcUtilizationThreshold.md) | The Utilization threshold (low and high) values of the utilization. | [optional] 
**utilization** | [**IpamsvcUtilization**](IpamsvcUtilization.md) | RO Field: The Utilization of this Range. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


