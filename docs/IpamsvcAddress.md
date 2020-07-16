# IpamsvcAddress

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The address in form \&quot;a.b.c.d\&quot;. | 
**comment** | **str** | A comment of the address object. | [optional] 
**dhcp_info** | [**IpamsvcDHCPInfo**](IpamsvcDHCPInfo.md) | RO field: DHCP information associated with this object. | [optional] 
**host** | **str** | The resource identifier. | [optional] 
**hwaddr** | **str** | A Hardware Address associated with this IP address. | [optional] 
**id** | **str** | The resource identifier. | [optional] 
**interface** | **str** | Name of the network interface card (NIC) associated with the address, if any. | [optional] 
**names** | [**list[IpamsvcName]**](IpamsvcName.md) | List of all names associated with this address. | [optional] 
**parent** | **str** | The resource identifier. | [optional] 
**protocol** | **str** | RO field: The type of protocol (ipv4 or ipv6). | [optional] 
**range** | **str** | The resource identifier. | [optional] 
**space** | **str** | The resource identifier. | 
**state** | **str** | RO field: Indicates if address is used or free. | [optional] 
**tags** | [**TypesJSONValue**](TypesJSONValue.md) | Tagging specifics. | [optional] 
**usage** | **list[str]** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


