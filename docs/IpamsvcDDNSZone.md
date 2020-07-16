# IpamsvcDDNSZone

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fqdn** | **str** | Optional. Zone FQDN.  If zone is defined the fqdn field must be empty. | [optional] 
**nameservers** | **list[str]** | Optional. Zones nameservers IPv4 addresses.  Each IP shoud be unique across the list of nameservers. | [optional] 
**tsig_enabled** | **bool** | Optional. True to use a TSIG key for the update.  Defaults to false. | [optional] 
**tsig_key_algo** | **str** | Optional. TSIG key algorithm.  Allowed values:    hmac_sha256    hmac_md5    hmac_sha1    hmac_sha224    hmac_sha384    hmac_sha512  Defaults to hmac_sha256. | [optional] 
**tsig_key_data** | **str** | Optinal. TSIG key data. Base64, may be empty.  Error if empty and tsig_enable is true.  Defaults to empty. | [optional] 
**tsig_key_name** | **str** | Optional. TSIG key name. FQDN, may be empty.  Error if empty and tsig_enable is true.  Defaults to empty. | [optional] 
**view** | **str** | The resource identifier. | [optional] 
**view_name** | **str** | Read-only. The name of the view. | [optional] 
**zone** | **str** | The resource identifier. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


