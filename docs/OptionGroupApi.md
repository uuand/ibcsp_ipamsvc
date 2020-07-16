# ibcsp_ipamsvc.OptionGroupApi

All URIs are relative to *http://localhost/api/ddi/v1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**option_group_create**](OptionGroupApi.md#option_group_create) | **POST** /dhcp/option_group | Create the Option Group object.
[**option_group_delete**](OptionGroupApi.md#option_group_delete) | **DELETE** /dhcp/option_group/{id} | Delete the Option Group object.
[**option_group_list**](OptionGroupApi.md#option_group_list) | **GET** /dhcp/option_group | List Option Group objects.
[**option_group_read**](OptionGroupApi.md#option_group_read) | **GET** /dhcp/option_group/{id} | Read the Option Group object.
[**option_group_update**](OptionGroupApi.md#option_group_update) | **PATCH** /dhcp/option_group/{id} | Update the Option Group object.


# **option_group_create**
> IpamsvcCreateOptionGroupResponse option_group_create(payload_id_application_name, payload_id_resource_type, body)

Create the Option Group object.

Use this method to create an Option Group object. The Option Group object is a named collection of options.

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
api_instance = ibcsp_ipamsvc.OptionGroupApi(ibcsp_ipamsvc.ApiClient(configuration))
payload_id_application_name = 'payload_id_application_name_example' # str | An application identifier that will be used among other infrastructure services to identify the application
payload_id_resource_type = 'payload_id_resource_type_example' # str | An application specific type name of a resource
body = ibcsp_ipamsvc.IpamsvcOptionGroup() # IpamsvcOptionGroup | 

try:
    # Create the Option Group object.
    api_response = api_instance.option_group_create(payload_id_application_name, payload_id_resource_type, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OptionGroupApi->option_group_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload_id_application_name** | **str**| An application identifier that will be used among other infrastructure services to identify the application | 
 **payload_id_resource_type** | **str**| An application specific type name of a resource | 
 **body** | [**IpamsvcOptionGroup**](IpamsvcOptionGroup.md)|  | 

### Return type

[**IpamsvcCreateOptionGroupResponse**](IpamsvcCreateOptionGroupResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **option_group_delete**
> option_group_delete(id_application_name, id_resource_type, id)

Delete the Option Group object.

Use this method to delete an Option Group object. The Option Group object is a named collection of options.

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
api_instance = ibcsp_ipamsvc.OptionGroupApi(ibcsp_ipamsvc.ApiClient(configuration))
id_application_name = 'id_application_name_example' # str | An application identifier that will be used among other infrastructure services to identify the application
id_resource_type = 'id_resource_type_example' # str | An application specific type name of a resource
id = 'id_example' # str | An application specific resource identity of a resource

try:
    # Delete the Option Group object.
    api_instance.option_group_delete(id_application_name, id_resource_type, id)
except ApiException as e:
    print("Exception when calling OptionGroupApi->option_group_delete: %s\n" % e)
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

# **option_group_list**
> IpamsvcListOptionGroupResponse option_group_list(fields=fields, filter=filter, offset=offset, limit=limit, page_token=page_token, order_by=order_by, torder_by=torder_by, tfilter=tfilter)

List Option Group objects.

Use this method to list Option Group objects. The Option Group object is a named collection of options.

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
api_instance = ibcsp_ipamsvc.OptionGroupApi(ibcsp_ipamsvc.ApiClient(configuration))
fields = 'fields_example' # str |   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         (optional)
filter = 'filter_example' # str |   A collection of response resources can be filtered by a logical expression string that includes JSON tag references to values in each resource, literal values, and logical operators. If a resource does not have the specified tag, its value is assumed to be null.  Literal values include numbers (integer and floating-point), and quoted (both single- or double-quoted) literal strings, and 'null'. The following operators are commonly used in filter expressions:  |  Op   |  Description               |  |  --   |  -----------               |  |  ==   |  Equal                     |  |  !=   |  Not Equal                 |  |  >    |  Greater Than              |  |   >=  |  Greater Than or Equal To  |  |  <    |  Less Than                 |  |  <=   |  Less Than or Equal To     |  |  and  |  Logical AND               |  |  ~    |  Matches Regex             |  |  !~   |  Does Not Match Regex      |  |  or   |  Logical OR                |  |  not  |  Logical NOT               |  |  ()   |  Groupping Operators       |         (optional)
offset = 56 # int |   The integer index (zero-origin) of the offset into a collection of resources. If omitted or null the value is assumed to be '0'.          (optional)
limit = 56 # int |   The integer number of resources to be returned in the response. The service may impose maximum value. If omitted the service may impose a default value.          (optional)
page_token = 'page_token_example' # str |   The service-defined string used to identify a page of resources. A null value indicates the first page.          (optional)
order_by = 'order_by_example' # str |   A collection of response resources can be sorted by their JSON tags. For a 'flat' resource, the tag name is straightforward. If sorting is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, its value is assumed to be null.)  Specify this parameter as a comma-separated list of JSON tag names. The sort direction can be specified by a suffix separated by whitespace before the tag name. The suffix 'asc' sorts the data in ascending order. The suffix 'desc' sorts the data in descending order. If no suffix is specified the data is sorted in ascending order.         (optional)
torder_by = 'torder_by_example' # str | This parameter is used for sorting by tags. (optional)
tfilter = 'tfilter_example' # str | This parameter is used for filtering by tags. (optional)

try:
    # List Option Group objects.
    api_response = api_instance.option_group_list(fields=fields, filter=filter, offset=offset, limit=limit, page_token=page_token, order_by=order_by, torder_by=torder_by, tfilter=tfilter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OptionGroupApi->option_group_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         | [optional] 
 **filter** | **str**|   A collection of response resources can be filtered by a logical expression string that includes JSON tag references to values in each resource, literal values, and logical operators. If a resource does not have the specified tag, its value is assumed to be null.  Literal values include numbers (integer and floating-point), and quoted (both single- or double-quoted) literal strings, and &#39;null&#39;. The following operators are commonly used in filter expressions:  |  Op   |  Description               |  |  --   |  -----------               |  |  &#x3D;&#x3D;   |  Equal                     |  |  !&#x3D;   |  Not Equal                 |  |  &gt;    |  Greater Than              |  |   &gt;&#x3D;  |  Greater Than or Equal To  |  |  &lt;    |  Less Than                 |  |  &lt;&#x3D;   |  Less Than or Equal To     |  |  and  |  Logical AND               |  |  ~    |  Matches Regex             |  |  !~   |  Does Not Match Regex      |  |  or   |  Logical OR                |  |  not  |  Logical NOT               |  |  ()   |  Groupping Operators       |         | [optional] 
 **offset** | **int**|   The integer index (zero-origin) of the offset into a collection of resources. If omitted or null the value is assumed to be &#39;0&#39;.          | [optional] 
 **limit** | **int**|   The integer number of resources to be returned in the response. The service may impose maximum value. If omitted the service may impose a default value.          | [optional] 
 **page_token** | **str**|   The service-defined string used to identify a page of resources. A null value indicates the first page.          | [optional] 
 **order_by** | **str**|   A collection of response resources can be sorted by their JSON tags. For a &#39;flat&#39; resource, the tag name is straightforward. If sorting is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, its value is assumed to be null.)  Specify this parameter as a comma-separated list of JSON tag names. The sort direction can be specified by a suffix separated by whitespace before the tag name. The suffix &#39;asc&#39; sorts the data in ascending order. The suffix &#39;desc&#39; sorts the data in descending order. If no suffix is specified the data is sorted in ascending order.         | [optional] 
 **torder_by** | **str**| This parameter is used for sorting by tags. | [optional] 
 **tfilter** | **str**| This parameter is used for filtering by tags. | [optional] 

### Return type

[**IpamsvcListOptionGroupResponse**](IpamsvcListOptionGroupResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **option_group_read**
> IpamsvcReadOptionGroupResponse option_group_read(id_application_name, id_resource_type, id, fields=fields)

Read the Option Group object.

Use this method to read an Option Group object. The Option Group object is a named collection of options.

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
api_instance = ibcsp_ipamsvc.OptionGroupApi(ibcsp_ipamsvc.ApiClient(configuration))
id_application_name = 'id_application_name_example' # str | An application identifier that will be used among other infrastructure services to identify the application
id_resource_type = 'id_resource_type_example' # str | An application specific type name of a resource
id = 'id_example' # str | An application specific resource identity of a resource
fields = 'fields_example' # str |   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         (optional)

try:
    # Read the Option Group object.
    api_response = api_instance.option_group_read(id_application_name, id_resource_type, id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OptionGroupApi->option_group_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_application_name** | **str**| An application identifier that will be used among other infrastructure services to identify the application | 
 **id_resource_type** | **str**| An application specific type name of a resource | 
 **id** | **str**| An application specific resource identity of a resource | 
 **fields** | **str**|   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         | [optional] 

### Return type

[**IpamsvcReadOptionGroupResponse**](IpamsvcReadOptionGroupResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **option_group_update**
> IpamsvcUpdateOptionGroupResponse option_group_update(payload_id_application_name, payload_id_resource_type, id, body)

Update the Option Group object.

Use this method to update an Option Group object. The Option Group object is a named collection of options.

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
api_instance = ibcsp_ipamsvc.OptionGroupApi(ibcsp_ipamsvc.ApiClient(configuration))
payload_id_application_name = 'payload_id_application_name_example' # str | An application identifier that will be used among other infrastructure services to identify the application
payload_id_resource_type = 'payload_id_resource_type_example' # str | An application specific type name of a resource
id = 'id_example' # str | An application specific resource identity of a resource
body = ibcsp_ipamsvc.IpamsvcOptionGroup() # IpamsvcOptionGroup | 

try:
    # Update the Option Group object.
    api_response = api_instance.option_group_update(payload_id_application_name, payload_id_resource_type, id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OptionGroupApi->option_group_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload_id_application_name** | **str**| An application identifier that will be used among other infrastructure services to identify the application | 
 **payload_id_resource_type** | **str**| An application specific type name of a resource | 
 **id** | **str**| An application specific resource identity of a resource | 
 **body** | [**IpamsvcOptionGroup**](IpamsvcOptionGroup.md)|  | 

### Return type

[**IpamsvcUpdateOptionGroupResponse**](IpamsvcUpdateOptionGroupResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

