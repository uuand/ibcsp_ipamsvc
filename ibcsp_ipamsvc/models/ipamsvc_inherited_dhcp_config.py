# coding: utf-8

"""
    IP Address Management API

    The IPAM/DHCP Application is a BloxOne DDI service providing IP address management and DHCP protocol features. The IPAM component provides visibility into and provisioning tools to manage networking spaces, monitoring and reporting of entire IP address infrastructures, and integration with DNS and DHCP protocols. The DHCP component provides DHCP protocol configuration service with on-prem host serving DHCP protocol. It is part of the full-featured, DDI cloud solution that enables customers to deploy large numbers of protocol servers to deliver DNS and DHCP throughout their enterprise network.     # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class IpamsvcInheritedDHCPConfig(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'allow_unknown': 'InheritanceInheritedBool',
        'filters': 'InheritedDHCPConfigFilterList',
        'ignore_list': 'InheritedDHCPConfigIgnoreItemList',
        'lease_time': 'InheritanceInheritedUInt32'
    }

    attribute_map = {
        'allow_unknown': 'allow_unknown',
        'filters': 'filters',
        'ignore_list': 'ignore_list',
        'lease_time': 'lease_time'
    }

    def __init__(self, allow_unknown=None, filters=None, ignore_list=None, lease_time=None):  # noqa: E501
        """IpamsvcInheritedDHCPConfig - a model defined in Swagger"""  # noqa: E501

        self._allow_unknown = None
        self._filters = None
        self._ignore_list = None
        self._lease_time = None
        self.discriminator = None

        if allow_unknown is not None:
            self.allow_unknown = allow_unknown
        if filters is not None:
            self.filters = filters
        if ignore_list is not None:
            self.ignore_list = ignore_list
        if lease_time is not None:
            self.lease_time = lease_time

    @property
    def allow_unknown(self):
        """Gets the allow_unknown of this IpamsvcInheritedDHCPConfig.  # noqa: E501

        Optional. Field config for allow_unknown field from [DHCPConfig] object.  # noqa: E501

        :return: The allow_unknown of this IpamsvcInheritedDHCPConfig.  # noqa: E501
        :rtype: InheritanceInheritedBool
        """
        return self._allow_unknown

    @allow_unknown.setter
    def allow_unknown(self, allow_unknown):
        """Sets the allow_unknown of this IpamsvcInheritedDHCPConfig.

        Optional. Field config for allow_unknown field from [DHCPConfig] object.  # noqa: E501

        :param allow_unknown: The allow_unknown of this IpamsvcInheritedDHCPConfig.  # noqa: E501
        :type: InheritanceInheritedBool
        """

        self._allow_unknown = allow_unknown

    @property
    def filters(self):
        """Gets the filters of this IpamsvcInheritedDHCPConfig.  # noqa: E501

        Optional. Field config for filters field from [DHCPConfig] object.  # noqa: E501

        :return: The filters of this IpamsvcInheritedDHCPConfig.  # noqa: E501
        :rtype: InheritedDHCPConfigFilterList
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """Sets the filters of this IpamsvcInheritedDHCPConfig.

        Optional. Field config for filters field from [DHCPConfig] object.  # noqa: E501

        :param filters: The filters of this IpamsvcInheritedDHCPConfig.  # noqa: E501
        :type: InheritedDHCPConfigFilterList
        """

        self._filters = filters

    @property
    def ignore_list(self):
        """Gets the ignore_list of this IpamsvcInheritedDHCPConfig.  # noqa: E501

        Optional. Field config for ignore_list field from [DHCPConfig] object.  # noqa: E501

        :return: The ignore_list of this IpamsvcInheritedDHCPConfig.  # noqa: E501
        :rtype: InheritedDHCPConfigIgnoreItemList
        """
        return self._ignore_list

    @ignore_list.setter
    def ignore_list(self, ignore_list):
        """Sets the ignore_list of this IpamsvcInheritedDHCPConfig.

        Optional. Field config for ignore_list field from [DHCPConfig] object.  # noqa: E501

        :param ignore_list: The ignore_list of this IpamsvcInheritedDHCPConfig.  # noqa: E501
        :type: InheritedDHCPConfigIgnoreItemList
        """

        self._ignore_list = ignore_list

    @property
    def lease_time(self):
        """Gets the lease_time of this IpamsvcInheritedDHCPConfig.  # noqa: E501

        Optional. Field config for lease_time field from [DHCPConfig] object.  # noqa: E501

        :return: The lease_time of this IpamsvcInheritedDHCPConfig.  # noqa: E501
        :rtype: InheritanceInheritedUInt32
        """
        return self._lease_time

    @lease_time.setter
    def lease_time(self, lease_time):
        """Sets the lease_time of this IpamsvcInheritedDHCPConfig.

        Optional. Field config for lease_time field from [DHCPConfig] object.  # noqa: E501

        :param lease_time: The lease_time of this IpamsvcInheritedDHCPConfig.  # noqa: E501
        :type: InheritanceInheritedUInt32
        """

        self._lease_time = lease_time

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(IpamsvcInheritedDHCPConfig, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, IpamsvcInheritedDHCPConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
