# ibcsp_ipamsvc.AsmApi

All URIs are relative to *http://localhost/api/ddi/v1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**asm_create**](AsmApi.md#asm_create) | **POST** /ipam/asm | Create the ASM object.
[**asm_list**](AsmApi.md#asm_list) | **GET** /ipam/asm | List ASM objects.
[**asm_read**](AsmApi.md#asm_read) | **GET** /ipam/asm/{id} | Read the ASM object.


# **asm_create**
> ProtobufEmpty asm_create(payload_id_application_name, payload_id_resource_type, body)

Create the ASM object.

Use this method to create an ASM object. The ASM object generates and returns the suggestions from the ASM suggestion engine and allows for updating the subnet and range information. When queried it returns the suggested updates for the subnet, when written it attempts to expand the scope by expanding a range or adding a new range and, if necessary, expanding the subnet.

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
api_instance = ibcsp_ipamsvc.AsmApi(ibcsp_ipamsvc.ApiClient(configuration))
payload_id_application_name = 'payload_id_application_name_example' # str | An application identifier that will be used among other infrastructure services to identify the application
payload_id_resource_type = 'payload_id_resource_type_example' # str | An application specific type name of a resource
body = ibcsp_ipamsvc.IpamsvcASM() # IpamsvcASM | 

try:
    # Create the ASM object.
    api_response = api_instance.asm_create(payload_id_application_name, payload_id_resource_type, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AsmApi->asm_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload_id_application_name** | **str**| An application identifier that will be used among other infrastructure services to identify the application | 
 **payload_id_resource_type** | **str**| An application specific type name of a resource | 
 **body** | [**IpamsvcASM**](IpamsvcASM.md)|  | 

### Return type

[**ProtobufEmpty**](ProtobufEmpty.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asm_list**
> IpamsvcListASMResponse asm_list(fields=fields, subnet_id=subnet_id)

List ASM objects.

Use this method to list ASM objects. The ASM object generates and returns the suggestions from the ASM suggestion engine and allows for updating the subnet and range information. When queried it returns the suggested updates for the subnet, when written it attempts to expand the scope by expanding a range or adding a new range and, if necessary, expanding the subnet.

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
api_instance = ibcsp_ipamsvc.AsmApi(ibcsp_ipamsvc.ApiClient(configuration))
fields = 'fields_example' # str |   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         (optional)
subnet_id = 'subnet_id_example' # str |  (optional)

try:
    # List ASM objects.
    api_response = api_instance.asm_list(fields=fields, subnet_id=subnet_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AsmApi->asm_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         | [optional] 
 **subnet_id** | **str**|  | [optional] 

### Return type

[**IpamsvcListASMResponse**](IpamsvcListASMResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asm_read**
> IpamsvcReadASMResponse asm_read(id_application_name, id_resource_type, id, fields=fields)

Read the ASM object.

Use this method to read an ASM object. The ASM object returns the suggested updates for the subnet.

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
api_instance = ibcsp_ipamsvc.AsmApi(ibcsp_ipamsvc.ApiClient(configuration))
id_application_name = 'id_application_name_example' # str | An application identifier that will be used among other infrastructure services to identify the application
id_resource_type = 'id_resource_type_example' # str | An application specific type name of a resource
id = 'id_example' # str | An application specific resource identity of a resource
fields = 'fields_example' # str |   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         (optional)

try:
    # Read the ASM object.
    api_response = api_instance.asm_read(id_application_name, id_resource_type, id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AsmApi->asm_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_application_name** | **str**| An application identifier that will be used among other infrastructure services to identify the application | 
 **id_resource_type** | **str**| An application specific type name of a resource | 
 **id** | **str**| An application specific resource identity of a resource | 
 **fields** | **str**|   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         | [optional] 

### Return type

[**IpamsvcReadASMResponse**](IpamsvcReadASMResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

