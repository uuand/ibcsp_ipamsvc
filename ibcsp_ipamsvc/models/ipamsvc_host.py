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


class IpamsvcHost(object):
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
        'address': 'str',
        'id': 'str',
        'ip_space': 'str',
        'name': 'str',
        'ophid': 'str',
        'server': 'str'
    }

    attribute_map = {
        'address': 'address',
        'id': 'id',
        'ip_space': 'ip_space',
        'name': 'name',
        'ophid': 'ophid',
        'server': 'server'
    }

    def __init__(self, address=None, id=None, ip_space=None, name=None, ophid=None, server=None):  # noqa: E501
        """IpamsvcHost - a model defined in Swagger"""  # noqa: E501

        self._address = None
        self._id = None
        self._ip_space = None
        self._name = None
        self._ophid = None
        self._server = None
        self.discriminator = None

        if address is not None:
            self.address = address
        if id is not None:
            self.id = id
        if ip_space is not None:
            self.ip_space = ip_space
        if name is not None:
            self.name = name
        self.ophid = ophid
        if server is not None:
            self.server = server

    @property
    def address(self):
        """Gets the address of this IpamsvcHost.  # noqa: E501

        RO field: Host's primary IP Address.  # noqa: E501

        :return: The address of this IpamsvcHost.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this IpamsvcHost.

        RO field: Host's primary IP Address.  # noqa: E501

        :param address: The address of this IpamsvcHost.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def id(self):
        """Gets the id of this IpamsvcHost.  # noqa: E501

        The resource identifier.  # noqa: E501

        :return: The id of this IpamsvcHost.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IpamsvcHost.

        The resource identifier.  # noqa: E501

        :param id: The id of this IpamsvcHost.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def ip_space(self):
        """Gets the ip_space of this IpamsvcHost.  # noqa: E501

        The resource identifier.  # noqa: E501

        :return: The ip_space of this IpamsvcHost.  # noqa: E501
        :rtype: str
        """
        return self._ip_space

    @ip_space.setter
    def ip_space(self, ip_space):
        """Sets the ip_space of this IpamsvcHost.

        The resource identifier.  # noqa: E501

        :param ip_space: The ip_space of this IpamsvcHost.  # noqa: E501
        :type: str
        """

        self._ip_space = ip_space

    @property
    def name(self):
        """Gets the name of this IpamsvcHost.  # noqa: E501

        RO field: Host's display name.  # noqa: E501

        :return: The name of this IpamsvcHost.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IpamsvcHost.

        RO field: Host's display name.  # noqa: E501

        :param name: The name of this IpamsvcHost.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def ophid(self):
        """Gets the ophid of this IpamsvcHost.  # noqa: E501

        On-Prem HostID.  # noqa: E501

        :return: The ophid of this IpamsvcHost.  # noqa: E501
        :rtype: str
        """
        return self._ophid

    @ophid.setter
    def ophid(self, ophid):
        """Sets the ophid of this IpamsvcHost.

        On-Prem HostID.  # noqa: E501

        :param ophid: The ophid of this IpamsvcHost.  # noqa: E501
        :type: str
        """
        if ophid is None:
            raise ValueError("Invalid value for `ophid`, must not be `None`")  # noqa: E501

        self._ophid = ophid

    @property
    def server(self):
        """Gets the server of this IpamsvcHost.  # noqa: E501

        The resource identifier.  # noqa: E501

        :return: The server of this IpamsvcHost.  # noqa: E501
        :rtype: str
        """
        return self._server

    @server.setter
    def server(self, server):
        """Sets the server of this IpamsvcHost.

        The resource identifier.  # noqa: E501

        :param server: The server of this IpamsvcHost.  # noqa: E501
        :type: str
        """

        self._server = server

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
        if issubclass(IpamsvcHost, dict):
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
        if not isinstance(other, IpamsvcHost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
