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


class IpamsvcUtilization(object):
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
        'abandon_utilization': 'int',
        'abandoned': 'str',
        'dynamic': 'str',
        'free': 'str',
        'static': 'str',
        'total': 'str',
        'used': 'str',
        'utilization': 'int'
    }

    attribute_map = {
        'abandon_utilization': 'abandon_utilization',
        'abandoned': 'abandoned',
        'dynamic': 'dynamic',
        'free': 'free',
        'static': 'static',
        'total': 'total',
        'used': 'used',
        'utilization': 'utilization'
    }

    def __init__(self, abandon_utilization=None, abandoned=None, dynamic=None, free=None, static=None, total=None, used=None, utilization=None):  # noqa: E501
        """IpamsvcUtilization - a model defined in Swagger"""  # noqa: E501

        self._abandon_utilization = None
        self._abandoned = None
        self._dynamic = None
        self._free = None
        self._static = None
        self._total = None
        self._used = None
        self._utilization = None
        self.discriminator = None

        if abandon_utilization is not None:
            self.abandon_utilization = abandon_utilization
        if abandoned is not None:
            self.abandoned = abandoned
        if dynamic is not None:
            self.dynamic = dynamic
        if free is not None:
            self.free = free
        if static is not None:
            self.static = static
        if total is not None:
            self.total = total
        if used is not None:
            self.used = used
        if utilization is not None:
            self.utilization = utilization

    @property
    def abandon_utilization(self):
        """Gets the abandon_utilization of this IpamsvcUtilization.  # noqa: E501

        RO field: Abandon_utilization = abandoned / total. Leases in the abandoned state are counted in used.  # noqa: E501

        :return: The abandon_utilization of this IpamsvcUtilization.  # noqa: E501
        :rtype: int
        """
        return self._abandon_utilization

    @abandon_utilization.setter
    def abandon_utilization(self, abandon_utilization):
        """Sets the abandon_utilization of this IpamsvcUtilization.

        RO field: Abandon_utilization = abandoned / total. Leases in the abandoned state are counted in used.  # noqa: E501

        :param abandon_utilization: The abandon_utilization of this IpamsvcUtilization.  # noqa: E501
        :type: int
        """

        self._abandon_utilization = abandon_utilization

    @property
    def abandoned(self):
        """Gets the abandoned of this IpamsvcUtilization.  # noqa: E501

        RO field: The number of IP Addresses abandoned in the scope of the object. Abandoned counts the number of addresses that are in the abandoned state (issued by a dhcp server and then declined by the client).  # noqa: E501

        :return: The abandoned of this IpamsvcUtilization.  # noqa: E501
        :rtype: str
        """
        return self._abandoned

    @abandoned.setter
    def abandoned(self, abandoned):
        """Sets the abandoned of this IpamsvcUtilization.

        RO field: The number of IP Addresses abandoned in the scope of the object. Abandoned counts the number of addresses that are in the abandoned state (issued by a dhcp server and then declined by the client).  # noqa: E501

        :param abandoned: The abandoned of this IpamsvcUtilization.  # noqa: E501
        :type: str
        """

        self._abandoned = abandoned

    @property
    def dynamic(self):
        """Gets the dynamic of this IpamsvcUtilization.  # noqa: E501

        RO field: Dynamic is defined as all of the addresses handed out by DHCP.  This includes all leased addresses, fixed addresses that are defined but not currently leased and abandoned leases.  # noqa: E501

        :return: The dynamic of this IpamsvcUtilization.  # noqa: E501
        :rtype: str
        """
        return self._dynamic

    @dynamic.setter
    def dynamic(self, dynamic):
        """Sets the dynamic of this IpamsvcUtilization.

        RO field: Dynamic is defined as all of the addresses handed out by DHCP.  This includes all leased addresses, fixed addresses that are defined but not currently leased and abandoned leases.  # noqa: E501

        :param dynamic: The dynamic of this IpamsvcUtilization.  # noqa: E501
        :type: str
        """

        self._dynamic = dynamic

    @property
    def free(self):
        """Gets the free of this IpamsvcUtilization.  # noqa: E501

        RO field: The number of IP Addresses available in the scope of the object.  # noqa: E501

        :return: The free of this IpamsvcUtilization.  # noqa: E501
        :rtype: str
        """
        return self._free

    @free.setter
    def free(self, free):
        """Sets the free of this IpamsvcUtilization.

        RO field: The number of IP Addresses available in the scope of the object.  # noqa: E501

        :param free: The free of this IpamsvcUtilization.  # noqa: E501
        :type: str
        """

        self._free = free

    @property
    def static(self):
        """Gets the static of this IpamsvcUtilization.  # noqa: E501

        RO field: Static includes any other defined addresses such as reservations or DNS records.  It can be computed as static = used - dynamic.  # noqa: E501

        :return: The static of this IpamsvcUtilization.  # noqa: E501
        :rtype: str
        """
        return self._static

    @static.setter
    def static(self, static):
        """Sets the static of this IpamsvcUtilization.

        RO field: Static includes any other defined addresses such as reservations or DNS records.  It can be computed as static = used - dynamic.  # noqa: E501

        :param static: The static of this IpamsvcUtilization.  # noqa: E501
        :type: str
        """

        self._static = static

    @property
    def total(self):
        """Gets the total of this IpamsvcUtilization.  # noqa: E501

        RO field: The total number of IP Addresses available in the scope of the object.  # noqa: E501

        :return: The total of this IpamsvcUtilization.  # noqa: E501
        :rtype: str
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this IpamsvcUtilization.

        RO field: The total number of IP Addresses available in the scope of the object.  # noqa: E501

        :param total: The total of this IpamsvcUtilization.  # noqa: E501
        :type: str
        """

        self._total = total

    @property
    def used(self):
        """Gets the used of this IpamsvcUtilization.  # noqa: E501

        RO field: The number of IP Addresses used in the scope of the object.  # noqa: E501

        :return: The used of this IpamsvcUtilization.  # noqa: E501
        :rtype: str
        """
        return self._used

    @used.setter
    def used(self, used):
        """Sets the used of this IpamsvcUtilization.

        RO field: The number of IP Addresses used in the scope of the object.  # noqa: E501

        :param used: The used of this IpamsvcUtilization.  # noqa: E501
        :type: str
        """

        self._used = used

    @property
    def utilization(self):
        """Gets the utilization of this IpamsvcUtilization.  # noqa: E501

        RO field: The ratio (used / total) rounded to the nearest integer and constrained to the interval [0, 100] (0 representing 0% and 100 representing 100% utilization).  # noqa: E501

        :return: The utilization of this IpamsvcUtilization.  # noqa: E501
        :rtype: int
        """
        return self._utilization

    @utilization.setter
    def utilization(self, utilization):
        """Sets the utilization of this IpamsvcUtilization.

        RO field: The ratio (used / total) rounded to the nearest integer and constrained to the interval [0, 100] (0 representing 0% and 100 representing 100% utilization).  # noqa: E501

        :param utilization: The utilization of this IpamsvcUtilization.  # noqa: E501
        :type: int
        """

        self._utilization = utilization

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
        if issubclass(IpamsvcUtilization, dict):
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
        if not isinstance(other, IpamsvcUtilization):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other