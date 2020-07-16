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


class IpamsvcOptionSpace(object):
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
        'comment': 'str',
        'id': 'str',
        'name': 'str',
        'protocol': 'str',
        'tags': 'TypesJSONValue'
    }

    attribute_map = {
        'comment': 'comment',
        'id': 'id',
        'name': 'name',
        'protocol': 'protocol',
        'tags': 'tags'
    }

    def __init__(self, comment=None, id=None, name=None, protocol=None, tags=None):  # noqa: E501
        """IpamsvcOptionSpace - a model defined in Swagger"""  # noqa: E501

        self._comment = None
        self._id = None
        self._name = None
        self._protocol = None
        self._tags = None
        self.discriminator = None

        if comment is not None:
            self.comment = comment
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if protocol is not None:
            self.protocol = protocol
        if tags is not None:
            self.tags = tags

    @property
    def comment(self):
        """Gets the comment of this IpamsvcOptionSpace.  # noqa: E501

        A comment of Option Space object.  # noqa: E501

        :return: The comment of this IpamsvcOptionSpace.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this IpamsvcOptionSpace.

        A comment of Option Space object.  # noqa: E501

        :param comment: The comment of this IpamsvcOptionSpace.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def id(self):
        """Gets the id of this IpamsvcOptionSpace.  # noqa: E501

        The resource identifier.  # noqa: E501

        :return: The id of this IpamsvcOptionSpace.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IpamsvcOptionSpace.

        The resource identifier.  # noqa: E501

        :param id: The id of this IpamsvcOptionSpace.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this IpamsvcOptionSpace.  # noqa: E501

        The name of Option Space object.  # noqa: E501

        :return: The name of this IpamsvcOptionSpace.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IpamsvcOptionSpace.

        The name of Option Space object.  # noqa: E501

        :param name: The name of this IpamsvcOptionSpace.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def protocol(self):
        """Gets the protocol of this IpamsvcOptionSpace.  # noqa: E501

        RO Field: The type of protocol (ipv4 or ipv6).  # noqa: E501

        :return: The protocol of this IpamsvcOptionSpace.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this IpamsvcOptionSpace.

        RO Field: The type of protocol (ipv4 or ipv6).  # noqa: E501

        :param protocol: The protocol of this IpamsvcOptionSpace.  # noqa: E501
        :type: str
        """

        self._protocol = protocol

    @property
    def tags(self):
        """Gets the tags of this IpamsvcOptionSpace.  # noqa: E501

        Tagging specifics.  # noqa: E501

        :return: The tags of this IpamsvcOptionSpace.  # noqa: E501
        :rtype: TypesJSONValue
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this IpamsvcOptionSpace.

        Tagging specifics.  # noqa: E501

        :param tags: The tags of this IpamsvcOptionSpace.  # noqa: E501
        :type: TypesJSONValue
        """

        self._tags = tags

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
        if issubclass(IpamsvcOptionSpace, dict):
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
        if not isinstance(other, IpamsvcOptionSpace):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
