# IpamsvcDHCPInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_hostname** | **str** | RO field: A DHCP host name associated with this client. | [optional] 
**client_hwaddr** | **str** | RO field: A Hardware Address associated with this client. | [optional] 
**client_id** | **str** | RO field: ID associated with this client. | [optional] 
**end** | **datetime** | RO field: The time at which the state, when set to leased, will changed to free. | [optional] 
**fingerprint** | **str** |  | [optional] 
**remain** | **int** | RO field: The remaining time, in seconds, until which the state, when set to leased, will remain in that state. | [optional] 
**start** | **datetime** |  | [optional] 
**state** | **str** | RO Field: Indicates the status of this IP address from a DHCP protocol standpoint as: -   none: Address is not under DHCP control -   free: Address is under DHCP control but has no lease currently assigned. -   leased: Address is under DHCP control and has a lease currently assigned. The lease details are contained in the matching dhcp/lease resource. | [optional] 
**state_ts** | **datetime** | RO field: The time at which the state was last reported. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


