# IpamsvcGlobal

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asm_config** | [**IpamsvcASMConfig**](IpamsvcASMConfig.md) |  | [optional] 
**ddns_client_update** | **str** | Optional. Controls who does the updates.  Allowed values: - &#39;client&#39;, DHCP server updates DNS if requested by client - &#39;server&#39;, DHCP server always updates DNS, unless the client says not to. - &#39;ignore&#39;, DHCP server always updates DNS, even if the client says not to.  Defaults to &#39;client&#39;. | [optional] 
**ddns_domain** | **str** | Optional. Domain suffix for DDNS updates. FQDN, may be empty.  Error if empty while ddns_enabled is true.  Default to empty. | [optional] 
**ddns_enabled** | **bool** | Optional. Enable to perform DNS updates for leases. All other ddns_* configuration is ignored when this flag is unset.  At a minimum, ddns_domain and ddns_zones must be configured to enable DDNS.  Defaults to false. | [optional] 
**ddns_generate_name** | **bool** | Optional. True to generate a hostname when not supplied by client.  Defaults to false. | [optional] 
**ddns_zones** | [**list[IpamsvcDDNSZone]**](IpamsvcDDNSZone.md) | Optional. DNS zones that DDNS updates can be sent to. There is no resolver fallback: the target zone must be explicitly configured for the update to be performed.  Updates are sent to the closest enclosing zone.  Error if ddns_enabled is true and the ddns_domain does not have a corresponding entry in ddns_zones.  Error if there are items with duplicate zone in the list.  Defaults to empty list. | [optional] 
**dhcp_config** | [**IpamsvcDHCPConfig**](IpamsvcDHCPConfig.md) | Optional. DHCP lease configuration. Controls how leases are issued. | [optional] 
**dhcp_options** | [**list[IpamsvcOptionItem]**](IpamsvcOptionItem.md) | Optional. List of DHCP options or group of options. An option list is ordered and may include both option groups and specific options. Multiple occurences of the same option or group is not an error. The last occurence of an option in the list will be used.  Error if the graph of referenced groups contains cycles.  Defaults to empty list. | [optional] 
**hostname_rewrite_char** | **str** | Optional. Character to replace non-matching characters with when hostname rewrite is enabled.  Any single ASCII character  Defaults to \&quot;_\&quot;. | [optional] 
**hostname_rewrite_enabled** | **bool** | Optional. When enabled, client supplied hostnames will be rewritten prior to DDNS update by replacing every character that does not match hostname_rewrite_regex by hostname_rewrite_char.  Defaults to false. | [optional] 
**hostname_rewrite_regex** | **str** | Optional. Regex bracket expression to match valid characters.  Must begin with \&quot;[\&quot; and end with \&quot;]\&quot; and be a compilable POSIX regex.  Defaults to \&quot;[a-zA-Z0-9_.]\&quot;. | [optional] 
**id** | **str** | The resource identifier. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


