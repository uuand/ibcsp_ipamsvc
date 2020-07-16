# IpamsvcAddressBlock

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The address field in form “a.b.c.d/n” where the “/n” may be omitted. In this case, the cidr value must be defined in the cidr field. When reading, the address field is always in the form “a.b.c.d”. | 
**asm_config** | [**IpamsvcASMConfig**](IpamsvcASMConfig.md) |  | [optional] 
**asm_scope_flag** | **int** |  | [optional] 
**cidr** | **int** | The CIDR of the Address Block object. Required, if address does not specify it in its input. | [optional] 
**comment** | **str** | A comment of the Address Block object. | [optional] 
**dhcp_config** | [**IpamsvcDHCPConfig**](IpamsvcDHCPConfig.md) | A shared DHCP configuration that controls how leases are issued. | [optional] 
**dhcp_options** | [**list[IpamsvcOptionItem]**](IpamsvcOptionItem.md) | A list of DHCP options. May be either a specific option or a group of options. | [optional] 
**dhcp_utilization** | [**IpamsvcDHCPUtilization**](IpamsvcDHCPUtilization.md) |  | [optional] 
**id** | **str** | The resource identifier. | [optional] 
**inheritance_parent** | **str** | The resource identifier. | [optional] 
**inheritance_sources** | [**IpamsvcDHCPInheritance**](IpamsvcDHCPInheritance.md) | Optional. Inheritance configuration. | [optional] 
**name** | **str** | The name of the Address Block object. | [optional] 
**parent** | **str** | The resource identifier. | [optional] 
**protocol** | **str** | RO Field: The type of protocol (ipv4 or ipv6). | [optional] 
**space** | **str** | The resource identifier. | 
**tags** | [**TypesJSONValue**](TypesJSONValue.md) | Tagging specifics. | [optional] 
**threshold** | [**IpamsvcUtilizationThreshold**](IpamsvcUtilizationThreshold.md) | The Utilization threshold (low and high) values of the utilization. | [optional] 
**utilization** | [**IpamsvcUtilization**](IpamsvcUtilization.md) | RO Field: The Utilization of this Address Block object. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


