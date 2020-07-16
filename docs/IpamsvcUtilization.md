# IpamsvcUtilization

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abandon_utilization** | **int** | RO field: Abandon_utilization &#x3D; abandoned / total. Leases in the abandoned state are counted in used. | [optional] 
**abandoned** | **str** | RO field: The number of IP Addresses abandoned in the scope of the object. Abandoned counts the number of addresses that are in the abandoned state (issued by a dhcp server and then declined by the client). | [optional] 
**dynamic** | **str** | RO field: Dynamic is defined as all of the addresses handed out by DHCP.  This includes all leased addresses, fixed addresses that are defined but not currently leased and abandoned leases. | [optional] 
**free** | **str** | RO field: The number of IP Addresses available in the scope of the object. | [optional] 
**static** | **str** | RO field: Static includes any other defined addresses such as reservations or DNS records.  It can be computed as static &#x3D; used - dynamic. | [optional] 
**total** | **str** | RO field: The total number of IP Addresses available in the scope of the object. | [optional] 
**used** | **str** | RO field: The number of IP Addresses used in the scope of the object. | [optional] 
**utilization** | **int** | RO field: The ratio (used / total) rounded to the nearest integer and constrained to the interval [0, 100] (0 representing 0% and 100 representing 100% utilization). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


