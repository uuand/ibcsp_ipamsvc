# IpamsvcHostAddress

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Field usage depends on the operation: - For read operation, address of the Address corresponding to the ref resource. - For write operation, address to be created if the Address does not exist. Required if ref is not set on write: . If the address already exists and is already pointing to the right host, the operation proceeds. . If the address already exists and is pointing to a different host, the operation must abort. . If the address already exists and is not pointing to any host, it is linked to the host. | 
**ref** | **str** | The resource identifier. | 
**space** | **str** | The resource identifier. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


