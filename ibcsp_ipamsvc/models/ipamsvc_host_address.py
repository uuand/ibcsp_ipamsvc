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


class IpamsvcHostAddress(object):
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
        'ref': 'str',
        'space': 'str'
    }

    attribute_map = {
        'address': 'address',
        'ref': 'ref',
        'space': 'space'
    }

    def __init__(self, address=None, ref=None, space=None):  # noqa: E501
        """IpamsvcHostAddress - a model defined in Swagger"""  # noqa: E501

        self._address = None
        self._ref = None
        self._space = None
        self.discriminator = None

        self.address = address
        self.ref = ref
        self.space = space

    @property
    def address(self):
        """Gets the address of this IpamsvcHostAddress.  # noqa: E501

        Field usage depends on the operation: - For read operation, address of the Address corresponding to the ref resource. - For write operation, address to be created if the Address does not exist. Required if ref is not set on write: . If the address already exists and is already pointing to the right host, the operation proceeds. . If the address already exists and is pointing to a different host, the operation must abort. . If the address already exists and is not pointing to any host, it is linked to the host.  # noqa: E501

        :return: The address of this IpamsvcHostAddress.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this IpamsvcHostAddress.

        Field usage depends on the operation: - For read operation, address of the Address corresponding to the ref resource. - For write operation, address to be created if the Address does not exist. Required if ref is not set on write: . If the address already exists and is already pointing to the right host, the operation proceeds. . If the address already exists and is pointing to a different host, the operation must abort. . If the address already exists and is not pointing to any host, it is linked to the host.  # noqa: E501

        :param address: The address of this IpamsvcHostAddress.  # noqa: E501
        :type: str
        """
        if address is None:
            raise ValueError("Invalid value for `address`, must not be `None`")  # noqa: E501

        self._address = address

    @property
    def ref(self):
        """Gets the ref of this IpamsvcHostAddress.  # noqa: E501

        The resource identifier.  # noqa: E501

        :return: The ref of this IpamsvcHostAddress.  # noqa: E501
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        """Sets the ref of this IpamsvcHostAddress.

        The resource identifier.  # noqa: E501

        :param ref: The ref of this IpamsvcHostAddress.  # noqa: E501
        :type: str
        """
        if ref is None:
            raise ValueError("Invalid value for `ref`, must not be `None`")  # noqa: E501

        self._ref = ref

    @property
    def space(self):
        """Gets the space of this IpamsvcHostAddress.  # noqa: E501

        The resource identifier.  # noqa: E501

        :return: The space of this IpamsvcHostAddress.  # noqa: E501
        :rtype: str
        """
        return self._space

    @space.setter
    def space(self, space):
        """Sets the space of this IpamsvcHostAddress.

        The resource identifier.  # noqa: E501

        :param space: The space of this IpamsvcHostAddress.  # noqa: E501
        :type: str
        """
        if space is None:
            raise ValueError("Invalid value for `space`, must not be `None`")  # noqa: E501

        self._space = space

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
        if issubclass(IpamsvcHostAddress, dict):
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
        if not isinstance(other, IpamsvcHostAddress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
