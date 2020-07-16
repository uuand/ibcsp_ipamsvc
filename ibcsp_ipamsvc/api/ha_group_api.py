# coding: utf-8

"""
    IP Address Management API

    The IPAM/DHCP Application is a BloxOne DDI service providing IP address management and DHCP protocol features. The IPAM component provides visibility into and provisioning tools to manage networking spaces, monitoring and reporting of entire IP address infrastructures, and integration with DNS and DHCP protocols. The DHCP component provides DHCP protocol configuration service with on-prem host serving DHCP protocol. It is part of the full-featured, DDI cloud solution that enables customers to deploy large numbers of protocol servers to deliver DNS and DHCP throughout their enterprise network.     # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from ibcsp_ipamsvc.api_client import ApiClient


class HaGroupApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def ha_group_create(self, payload_id_application_name, payload_id_resource_type, body, **kwargs):  # noqa: E501
        """Create the HA Group object.  # noqa: E501

        Use this method to create an HA Group object. The HA Group object represents Hosts that can serve the same leases for HA.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.ha_group_create(payload_id_application_name, payload_id_resource_type, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str payload_id_application_name: An application identifier that will be used among other infrastructure services to identify the application (required)
        :param str payload_id_resource_type: An application specific type name of a resource (required)
        :param IpamsvcHAGroup body: (required)
        :return: IpamsvcCreateHAGroupResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.ha_group_create_with_http_info(payload_id_application_name, payload_id_resource_type, body, **kwargs)  # noqa: E501
        else:
            (data) = self.ha_group_create_with_http_info(payload_id_application_name, payload_id_resource_type, body, **kwargs)  # noqa: E501
            return data

    def ha_group_create_with_http_info(self, payload_id_application_name, payload_id_resource_type, body, **kwargs):  # noqa: E501
        """Create the HA Group object.  # noqa: E501

        Use this method to create an HA Group object. The HA Group object represents Hosts that can serve the same leases for HA.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.ha_group_create_with_http_info(payload_id_application_name, payload_id_resource_type, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str payload_id_application_name: An application identifier that will be used among other infrastructure services to identify the application (required)
        :param str payload_id_resource_type: An application specific type name of a resource (required)
        :param IpamsvcHAGroup body: (required)
        :return: IpamsvcCreateHAGroupResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['payload_id_application_name', 'payload_id_resource_type', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method ha_group_create" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'payload_id_application_name' is set
        if ('payload_id_application_name' not in params or
                params['payload_id_application_name'] is None):
            raise ValueError("Missing the required parameter `payload_id_application_name` when calling `ha_group_create`")  # noqa: E501
        # verify the required parameter 'payload_id_resource_type' is set
        if ('payload_id_resource_type' not in params or
                params['payload_id_resource_type'] is None):
            raise ValueError("Missing the required parameter `payload_id_resource_type` when calling `ha_group_create`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `ha_group_create`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'payload_id_application_name' in params:
            path_params['payload.id.application_name'] = params['payload_id_application_name']  # noqa: E501
        if 'payload_id_resource_type' in params:
            path_params['payload.id.resource_type'] = params['payload_id_resource_type']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/dhcp/ha_group', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IpamsvcCreateHAGroupResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def ha_group_delete(self, id_application_name, id_resource_type, id, **kwargs):  # noqa: E501
        """Delete the HA Group object.  # noqa: E501

        Use this method to delete an HA Group object. The HA Group object represents Hosts that can serve the same leases for HA.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.ha_group_delete(id_application_name, id_resource_type, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id_application_name: An application identifier that will be used among other infrastructure services to identify the application (required)
        :param str id_resource_type: An application specific type name of a resource (required)
        :param str id: An application specific resource identity of a resource (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.ha_group_delete_with_http_info(id_application_name, id_resource_type, id, **kwargs)  # noqa: E501
        else:
            (data) = self.ha_group_delete_with_http_info(id_application_name, id_resource_type, id, **kwargs)  # noqa: E501
            return data

    def ha_group_delete_with_http_info(self, id_application_name, id_resource_type, id, **kwargs):  # noqa: E501
        """Delete the HA Group object.  # noqa: E501

        Use this method to delete an HA Group object. The HA Group object represents Hosts that can serve the same leases for HA.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.ha_group_delete_with_http_info(id_application_name, id_resource_type, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id_application_name: An application identifier that will be used among other infrastructure services to identify the application (required)
        :param str id_resource_type: An application specific type name of a resource (required)
        :param str id: An application specific resource identity of a resource (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id_application_name', 'id_resource_type', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method ha_group_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id_application_name' is set
        if ('id_application_name' not in params or
                params['id_application_name'] is None):
            raise ValueError("Missing the required parameter `id_application_name` when calling `ha_group_delete`")  # noqa: E501
        # verify the required parameter 'id_resource_type' is set
        if ('id_resource_type' not in params or
                params['id_resource_type'] is None):
            raise ValueError("Missing the required parameter `id_resource_type` when calling `ha_group_delete`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `ha_group_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id_application_name' in params:
            path_params['id.application_name'] = params['id_application_name']  # noqa: E501
        if 'id_resource_type' in params:
            path_params['id.resource_type'] = params['id_resource_type']  # noqa: E501
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/dhcp/ha_group/{id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def ha_group_list(self, **kwargs):  # noqa: E501
        """List HA Group objects.  # noqa: E501

        Use this method to list HA Group objects. The HA Group object represents Hosts that can serve the same leases for HA.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.ha_group_list(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str filter:   A collection of response resources can be filtered by a logical expression string that includes JSON tag references to values in each resource, literal values, and logical operators. If a resource does not have the specified tag, its value is assumed to be null.  Literal values include numbers (integer and floating-point), and quoted (both single- or double-quoted) literal strings, and 'null'. The following operators are commonly used in filter expressions:  |  Op   |  Description               |  |  --   |  -----------               |  |  ==   |  Equal                     |  |  !=   |  Not Equal                 |  |  >    |  Greater Than              |  |   >=  |  Greater Than or Equal To  |  |  <    |  Less Than                 |  |  <=   |  Less Than or Equal To     |  |  and  |  Logical AND               |  |  ~    |  Matches Regex             |  |  !~   |  Does Not Match Regex      |  |  or   |  Logical OR                |  |  not  |  Logical NOT               |  |  ()   |  Groupping Operators       |        
        :param str order_by:   A collection of response resources can be sorted by their JSON tags. For a 'flat' resource, the tag name is straightforward. If sorting is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, its value is assumed to be null.)  Specify this parameter as a comma-separated list of JSON tag names. The sort direction can be specified by a suffix separated by whitespace before the tag name. The suffix 'asc' sorts the data in ascending order. The suffix 'desc' sorts the data in descending order. If no suffix is specified the data is sorted in ascending order.        
        :param str fields:   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.        
        :param int offset:   The integer index (zero-origin) of the offset into a collection of resources. If omitted or null the value is assumed to be '0'.         
        :param int limit:   The integer number of resources to be returned in the response. The service may impose maximum value. If omitted the service may impose a default value.         
        :param str page_token:   The service-defined string used to identify a page of resources. A null value indicates the first page.         
        :param str torder_by: This parameter is used for sorting by tags.
        :param str tfilter: This parameter is used for filtering by tags.
        :return: IpamsvcListHAGroupResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.ha_group_list_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.ha_group_list_with_http_info(**kwargs)  # noqa: E501
            return data

    def ha_group_list_with_http_info(self, **kwargs):  # noqa: E501
        """List HA Group objects.  # noqa: E501

        Use this method to list HA Group objects. The HA Group object represents Hosts that can serve the same leases for HA.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.ha_group_list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str filter:   A collection of response resources can be filtered by a logical expression string that includes JSON tag references to values in each resource, literal values, and logical operators. If a resource does not have the specified tag, its value is assumed to be null.  Literal values include numbers (integer and floating-point), and quoted (both single- or double-quoted) literal strings, and 'null'. The following operators are commonly used in filter expressions:  |  Op   |  Description               |  |  --   |  -----------               |  |  ==   |  Equal                     |  |  !=   |  Not Equal                 |  |  >    |  Greater Than              |  |   >=  |  Greater Than or Equal To  |  |  <    |  Less Than                 |  |  <=   |  Less Than or Equal To     |  |  and  |  Logical AND               |  |  ~    |  Matches Regex             |  |  !~   |  Does Not Match Regex      |  |  or   |  Logical OR                |  |  not  |  Logical NOT               |  |  ()   |  Groupping Operators       |        
        :param str order_by:   A collection of response resources can be sorted by their JSON tags. For a 'flat' resource, the tag name is straightforward. If sorting is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, its value is assumed to be null.)  Specify this parameter as a comma-separated list of JSON tag names. The sort direction can be specified by a suffix separated by whitespace before the tag name. The suffix 'asc' sorts the data in ascending order. The suffix 'desc' sorts the data in descending order. If no suffix is specified the data is sorted in ascending order.        
        :param str fields:   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.        
        :param int offset:   The integer index (zero-origin) of the offset into a collection of resources. If omitted or null the value is assumed to be '0'.         
        :param int limit:   The integer number of resources to be returned in the response. The service may impose maximum value. If omitted the service may impose a default value.         
        :param str page_token:   The service-defined string used to identify a page of resources. A null value indicates the first page.         
        :param str torder_by: This parameter is used for sorting by tags.
        :param str tfilter: This parameter is used for filtering by tags.
        :return: IpamsvcListHAGroupResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['filter', 'order_by', 'fields', 'offset', 'limit', 'page_token', 'torder_by', 'tfilter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method ha_group_list" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'filter' in params:
            query_params.append(('_filter', params['filter']))  # noqa: E501
        if 'order_by' in params:
            query_params.append(('_order_by', params['order_by']))  # noqa: E501
        if 'fields' in params:
            query_params.append(('_fields', params['fields']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('_offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('_limit', params['limit']))  # noqa: E501
        if 'page_token' in params:
            query_params.append(('_page_token', params['page_token']))  # noqa: E501
        if 'torder_by' in params:
            query_params.append(('_torder_by', params['torder_by']))  # noqa: E501
        if 'tfilter' in params:
            query_params.append(('_tfilter', params['tfilter']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/dhcp/ha_group', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IpamsvcListHAGroupResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def ha_group_read(self, id_application_name, id_resource_type, id, **kwargs):  # noqa: E501
        """Read the HA Group object.  # noqa: E501

        Use this method to read an HA Group object. The HA Group object represents Hosts that can serve the same leases for HA.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.ha_group_read(id_application_name, id_resource_type, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id_application_name: An application identifier that will be used among other infrastructure services to identify the application (required)
        :param str id_resource_type: An application specific type name of a resource (required)
        :param str id: An application specific resource identity of a resource (required)
        :param str fields:   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.        
        :return: IpamsvcReadHAGroupResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.ha_group_read_with_http_info(id_application_name, id_resource_type, id, **kwargs)  # noqa: E501
        else:
            (data) = self.ha_group_read_with_http_info(id_application_name, id_resource_type, id, **kwargs)  # noqa: E501
            return data

    def ha_group_read_with_http_info(self, id_application_name, id_resource_type, id, **kwargs):  # noqa: E501
        """Read the HA Group object.  # noqa: E501

        Use this method to read an HA Group object. The HA Group object represents Hosts that can serve the same leases for HA.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.ha_group_read_with_http_info(id_application_name, id_resource_type, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id_application_name: An application identifier that will be used among other infrastructure services to identify the application (required)
        :param str id_resource_type: An application specific type name of a resource (required)
        :param str id: An application specific resource identity of a resource (required)
        :param str fields:   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.        
        :return: IpamsvcReadHAGroupResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id_application_name', 'id_resource_type', 'id', 'fields']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method ha_group_read" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id_application_name' is set
        if ('id_application_name' not in params or
                params['id_application_name'] is None):
            raise ValueError("Missing the required parameter `id_application_name` when calling `ha_group_read`")  # noqa: E501
        # verify the required parameter 'id_resource_type' is set
        if ('id_resource_type' not in params or
                params['id_resource_type'] is None):
            raise ValueError("Missing the required parameter `id_resource_type` when calling `ha_group_read`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `ha_group_read`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id_application_name' in params:
            path_params['id.application_name'] = params['id_application_name']  # noqa: E501
        if 'id_resource_type' in params:
            path_params['id.resource_type'] = params['id_resource_type']  # noqa: E501
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'fields' in params:
            query_params.append(('_fields', params['fields']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/dhcp/ha_group/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IpamsvcReadHAGroupResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def ha_group_update(self, payload_id_application_name, payload_id_resource_type, id, body, **kwargs):  # noqa: E501
        """Update the HA Group object.  # noqa: E501

        Use this method to update an HA Group object. The HA Group object represents Hosts that can serve the same leases for HA.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.ha_group_update(payload_id_application_name, payload_id_resource_type, id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str payload_id_application_name: An application identifier that will be used among other infrastructure services to identify the application (required)
        :param str payload_id_resource_type: An application specific type name of a resource (required)
        :param str id: An application specific resource identity of a resource (required)
        :param IpamsvcHAGroup body: (required)
        :return: IpamsvcUpdateHAGroupResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.ha_group_update_with_http_info(payload_id_application_name, payload_id_resource_type, id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.ha_group_update_with_http_info(payload_id_application_name, payload_id_resource_type, id, body, **kwargs)  # noqa: E501
            return data

    def ha_group_update_with_http_info(self, payload_id_application_name, payload_id_resource_type, id, body, **kwargs):  # noqa: E501
        """Update the HA Group object.  # noqa: E501

        Use this method to update an HA Group object. The HA Group object represents Hosts that can serve the same leases for HA.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.ha_group_update_with_http_info(payload_id_application_name, payload_id_resource_type, id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str payload_id_application_name: An application identifier that will be used among other infrastructure services to identify the application (required)
        :param str payload_id_resource_type: An application specific type name of a resource (required)
        :param str id: An application specific resource identity of a resource (required)
        :param IpamsvcHAGroup body: (required)
        :return: IpamsvcUpdateHAGroupResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['payload_id_application_name', 'payload_id_resource_type', 'id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method ha_group_update" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'payload_id_application_name' is set
        if ('payload_id_application_name' not in params or
                params['payload_id_application_name'] is None):
            raise ValueError("Missing the required parameter `payload_id_application_name` when calling `ha_group_update`")  # noqa: E501
        # verify the required parameter 'payload_id_resource_type' is set
        if ('payload_id_resource_type' not in params or
                params['payload_id_resource_type'] is None):
            raise ValueError("Missing the required parameter `payload_id_resource_type` when calling `ha_group_update`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `ha_group_update`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `ha_group_update`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'payload_id_application_name' in params:
            path_params['payload.id.application_name'] = params['payload_id_application_name']  # noqa: E501
        if 'payload_id_resource_type' in params:
            path_params['payload.id.resource_type'] = params['payload_id_resource_type']  # noqa: E501
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/dhcp/ha_group/{id}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IpamsvcUpdateHAGroupResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)