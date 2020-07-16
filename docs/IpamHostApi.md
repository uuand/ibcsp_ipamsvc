# ibcsp_ipamsvc.IpamHostApi

All URIs are relative to *http://localhost/api/ddi/v1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ipam_host_create**](IpamHostApi.md#ipam_host_create) | **POST** /ipam/host | Create the IPAM Host object.
[**ipam_host_delete**](IpamHostApi.md#ipam_host_delete) | **DELETE** /ipam/host/{id} | Delete the IPAM Host object.
[**ipam_host_list**](IpamHostApi.md#ipam_host_list) | **GET** /ipam/host | List IPAM Host objects.
[**ipam_host_read**](IpamHostApi.md#ipam_host_read) | **GET** /ipam/host/{id} | Read the IPAM Host object.
[**ipam_host_update**](IpamHostApi.md#ipam_host_update) | **PATCH** /ipam/host/{id} | Update the IPAM Host object.


# **ipam_host_create**
> IpamsvcCreateIpamHostResponse ipam_host_create(payload_id_application_name, payload_id_resource_type, body)

Create the IPAM Host object.

Use this method to create an IPAM Host object. This object (ipam/host) represents any network connected equipment that is assigned one or more IP Addresses.

### Example
```python
from __future__ import print_function
import time
import ibcsp_ipamsvc
from ibcsp_ipamsvc.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = ibcsp_ipamsvc.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = ibcsp_ipamsvc.IpamHostApi(ibcsp_ipamsvc.ApiClient(configuration))
payload_id_application_name = 'payload_id_application_name_example' # str | An application identifier that will be used among other infrastructure services to identify the application
payload_id_resource_type = 'payload_id_resource_type_example' # str | An application specific type name of a resource
body = ibcsp_ipamsvc.IpamsvcIpamHost() # IpamsvcIpamHost | 

try:
    # Create the IPAM Host object.
    api_response = api_instance.ipam_host_create(payload_id_application_name, payload_id_resource_type, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamHostApi->ipam_host_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload_id_application_name** | **str**| An application identifier that will be used among other infrastructure services to identify the application | 
 **payload_id_resource_type** | **str**| An application specific type name of a resource | 
 **body** | [**IpamsvcIpamHost**](IpamsvcIpamHost.md)|  | 

### Return type

[**IpamsvcCreateIpamHostResponse**](IpamsvcCreateIpamHostResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_host_delete**
> ipam_host_delete(id_application_name, id_resource_type, id)

Delete the IPAM Host object.

Use this method to delete an IPAM Host object. This object (ipam/host) represents any network connected equipment that is assigned one or more IP Addresses.

### Example
```python
from __future__ import print_function
import time
import ibcsp_ipamsvc
from ibcsp_ipamsvc.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = ibcsp_ipamsvc.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = ibcsp_ipamsvc.IpamHostApi(ibcsp_ipamsvc.ApiClient(configuration))
id_application_name = 'id_application_name_example' # str | An application identifier that will be used among other infrastructure services to identify the application
id_resource_type = 'id_resource_type_example' # str | An application specific type name of a resource
id = 'id_example' # str | An application specific resource identity of a resource

try:
    # Delete the IPAM Host object.
    api_instance.ipam_host_delete(id_application_name, id_resource_type, id)
except ApiException as e:
    print("Exception when calling IpamHostApi->ipam_host_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_application_name** | **str**| An application identifier that will be used among other infrastructure services to identify the application | 
 **id_resource_type** | **str**| An application specific type name of a resource | 
 **id** | **str**| An application specific resource identity of a resource | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_host_list**
> IpamsvcListIpamHostResponse ipam_host_list(fields=fields, order_by=order_by, filter=filter, offset=offset, limit=limit, page_token=page_token, torder_by=torder_by, tfilter=tfilter)

List IPAM Host objects.

Use this method to list IPAM Host objects. This object (ipam/host) represents any network connected equipment that is assigned one or more IP Addresses.

### Example
```python
from __future__ import print_function
import time
import ibcsp_ipamsvc
from ibcsp_ipamsvc.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = ibcsp_ipamsvc.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = ibcsp_ipamsvc.IpamHostApi(ibcsp_ipamsvc.ApiClient(configuration))
fields = 'fields_example' # str |   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         (optional)
order_by = 'order_by_example' # str |   A collection of response resources can be sorted by their JSON tags. For a 'flat' resource, the tag name is straightforward. If sorting is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, its value is assumed to be null.)  Specify this parameter as a comma-separated list of JSON tag names. The sort direction can be specified by a suffix separated by whitespace before the tag name. The suffix 'asc' sorts the data in ascending order. The suffix 'desc' sorts the data in descending order. If no suffix is specified the data is sorted in ascending order.         (optional)
filter = 'filter_example' # str |   A collection of response resources can be filtered by a logical expression string that includes JSON tag references to values in each resource, literal values, and logical operators. If a resource does not have the specified tag, its value is assumed to be null.  Literal values include numbers (integer and floating-point), and quoted (both single- or double-quoted) literal strings, and 'null'. The following operators are commonly used in filter expressions:  |  Op   |  Description               |  |  --   |  -----------               |  |  ==   |  Equal                     |  |  !=   |  Not Equal                 |  |  >    |  Greater Than              |  |   >=  |  Greater Than or Equal To  |  |  <    |  Less Than                 |  |  <=   |  Less Than or Equal To     |  |  and  |  Logical AND               |  |  ~    |  Matches Regex             |  |  !~   |  Does Not Match Regex      |  |  or   |  Logical OR                |  |  not  |  Logical NOT               |  |  ()   |  Groupping Operators       |         (optional)
offset = 56 # int |   The integer index (zero-origin) of the offset into a collection of resources. If omitted or null the value is assumed to be '0'.          (optional)
limit = 56 # int |   The integer number of resources to be returned in the response. The service may impose maximum value. If omitted the service may impose a default value.          (optional)
page_token = 'page_token_example' # str |   The service-defined string used to identify a page of resources. A null value indicates the first page.          (optional)
torder_by = 'torder_by_example' # str | This parameter is used for sorting by tags. (optional)
tfilter = 'tfilter_example' # str | This parameter is used for filtering by tags. (optional)

try:
    # List IPAM Host objects.
    api_response = api_instance.ipam_host_list(fields=fields, order_by=order_by, filter=filter, offset=offset, limit=limit, page_token=page_token, torder_by=torder_by, tfilter=tfilter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamHostApi->ipam_host_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         | [optional] 
 **order_by** | **str**|   A collection of response resources can be sorted by their JSON tags. For a &#39;flat&#39; resource, the tag name is straightforward. If sorting is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, its value is assumed to be null.)  Specify this parameter as a comma-separated list of JSON tag names. The sort direction can be specified by a suffix separated by whitespace before the tag name. The suffix &#39;asc&#39; sorts the data in ascending order. The suffix &#39;desc&#39; sorts the data in descending order. If no suffix is specified the data is sorted in ascending order.         | [optional] 
 **filter** | **str**|   A collection of response resources can be filtered by a logical expression string that includes JSON tag references to values in each resource, literal values, and logical operators. If a resource does not have the specified tag, its value is assumed to be null.  Literal values include numbers (integer and floating-point), and quoted (both single- or double-quoted) literal strings, and &#39;null&#39;. The following operators are commonly used in filter expressions:  |  Op   |  Description               |  |  --   |  -----------               |  |  &#x3D;&#x3D;   |  Equal                     |  |  !&#x3D;   |  Not Equal                 |  |  &gt;    |  Greater Than              |  |   &gt;&#x3D;  |  Greater Than or Equal To  |  |  &lt;    |  Less Than                 |  |  &lt;&#x3D;   |  Less Than or Equal To     |  |  and  |  Logical AND               |  |  ~    |  Matches Regex             |  |  !~   |  Does Not Match Regex      |  |  or   |  Logical OR                |  |  not  |  Logical NOT               |  |  ()   |  Groupping Operators       |         | [optional] 
 **offset** | **int**|   The integer index (zero-origin) of the offset into a collection of resources. If omitted or null the value is assumed to be &#39;0&#39;.          | [optional] 
 **limit** | **int**|   The integer number of resources to be returned in the response. The service may impose maximum value. If omitted the service may impose a default value.          | [optional] 
 **page_token** | **str**|   The service-defined string used to identify a page of resources. A null value indicates the first page.          | [optional] 
 **torder_by** | **str**| This parameter is used for sorting by tags. | [optional] 
 **tfilter** | **str**| This parameter is used for filtering by tags. | [optional] 

### Return type

[**IpamsvcListIpamHostResponse**](IpamsvcListIpamHostResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_host_read**
> IpamsvcReadIpamHostResponse ipam_host_read(id_application_name, id_resource_type, id, order_by=order_by, fields=fields)

Read the IPAM Host object.

Use this method to read an IPAM Host object. This object (ipam/host) represents any network connected equipment that is assigned one or more IP Addresses.

### Example
```python
from __future__ import print_function
import time
import ibcsp_ipamsvc
from ibcsp_ipamsvc.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = ibcsp_ipamsvc.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = ibcsp_ipamsvc.IpamHostApi(ibcsp_ipamsvc.ApiClient(configuration))
id_application_name = 'id_application_name_example' # str | An application identifier that will be used among other infrastructure services to identify the application
id_resource_type = 'id_resource_type_example' # str | An application specific type name of a resource
id = 'id_example' # str | An application specific resource identity of a resource
order_by = 'order_by_example' # str |   A collection of response resources can be sorted by their JSON tags. For a 'flat' resource, the tag name is straightforward. If sorting is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, its value is assumed to be null.)  Specify this parameter as a comma-separated list of JSON tag names. The sort direction can be specified by a suffix separated by whitespace before the tag name. The suffix 'asc' sorts the data in ascending order. The suffix 'desc' sorts the data in descending order. If no suffix is specified the data is sorted in ascending order.         (optional)
fields = 'fields_example' # str |   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         (optional)

try:
    # Read the IPAM Host object.
    api_response = api_instance.ipam_host_read(id_application_name, id_resource_type, id, order_by=order_by, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamHostApi->ipam_host_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_application_name** | **str**| An application identifier that will be used among other infrastructure services to identify the application | 
 **id_resource_type** | **str**| An application specific type name of a resource | 
 **id** | **str**| An application specific resource identity of a resource | 
 **order_by** | **str**|   A collection of response resources can be sorted by their JSON tags. For a &#39;flat&#39; resource, the tag name is straightforward. If sorting is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, its value is assumed to be null.)  Specify this parameter as a comma-separated list of JSON tag names. The sort direction can be specified by a suffix separated by whitespace before the tag name. The suffix &#39;asc&#39; sorts the data in ascending order. The suffix &#39;desc&#39; sorts the data in descending order. If no suffix is specified the data is sorted in ascending order.         | [optional] 
 **fields** | **str**|   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         | [optional] 

### Return type

[**IpamsvcReadIpamHostResponse**](IpamsvcReadIpamHostResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_host_update**
> IpamsvcUpdateIpamHostResponse ipam_host_update(payload_id_application_name, payload_id_resource_type, id, body)

Update the IPAM Host object.

Use this method to update an IPAM Host object. This object (ipam/host) represents any network connected equipment that is assigned one or more IP Addresses.

### Example
```python
from __future__ import print_function
import time
import ibcsp_ipamsvc
from ibcsp_ipamsvc.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = ibcsp_ipamsvc.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = ibcsp_ipamsvc.IpamHostApi(ibcsp_ipamsvc.ApiClient(configuration))
payload_id_application_name = 'payload_id_application_name_example' # str | An application identifier that will be used among other infrastructure services to identify the application
payload_id_resource_type = 'payload_id_resource_type_example' # str | An application specific type name of a resource
id = 'id_example' # str | An application specific resource identity of a resource
body = ibcsp_ipamsvc.IpamsvcIpamHost() # IpamsvcIpamHost | 

try:
    # Update the IPAM Host object.
    api_response = api_instance.ipam_host_update(payload_id_application_name, payload_id_resource_type, id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamHostApi->ipam_host_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload_id_application_name** | **str**| An application identifier that will be used among other infrastructure services to identify the application | 
 **payload_id_resource_type** | **str**| An application specific type name of a resource | 
 **id** | **str**| An application specific resource identity of a resource | 
 **body** | [**IpamsvcIpamHost**](IpamsvcIpamHost.md)|  | 

### Return type

[**IpamsvcUpdateIpamHostResponse**](IpamsvcUpdateIpamHostResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

