# IpamsvcIPSpace

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asm_config** | [**IpamsvcASMConfig**](IpamsvcASMConfig.md) |  | [optional] 
**asm_scope_flag** | **int** |  | [optional] 
**comment** | **str** | A comment of the IP Space object. | [optional] 
**dhcp_config** | [**IpamsvcDHCPConfig**](IpamsvcDHCPConfig.md) | A shared DHCP configuration that controls how leases are issued. | [optional] 
**dhcp_options** | [**list[IpamsvcOptionItem]**](IpamsvcOptionItem.md) | A list of DHCP options. May be either a specific option or a group of options. | [optional] 
**id** | **str** | The resource identifier. | [optional] 
**inheritance_sources** | [**IpamsvcDHCPInheritance**](IpamsvcDHCPInheritance.md) | Optional. Inheritance configuration. | [optional] 
**name** | **str** | The name of the IP Space object. | 
**tags** | [**TypesJSONValue**](TypesJSONValue.md) | Tagging specifics. | [optional] 
**threshold** | [**IpamsvcUtilizationThreshold**](IpamsvcUtilizationThreshold.md) | The Utilization threshold (low and high) values of the utilization. | [optional] 
**utilization** | [**IpamsvcUtilization**](IpamsvcUtilization.md) | RO Field: The Total Utilization of all the children of this IP Space. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


