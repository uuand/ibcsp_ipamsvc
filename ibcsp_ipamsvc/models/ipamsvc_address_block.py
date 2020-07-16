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


class IpamsvcAddressBlock(object):
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
        'asm_config': 'IpamsvcASMConfig',
        'asm_scope_flag': 'int',
        'cidr': 'int',
        'comment': 'str',
        'dhcp_config': 'IpamsvcDHCPConfig',
        'dhcp_options': 'list[IpamsvcOptionItem]',
        'dhcp_utilization': 'IpamsvcDHCPUtilization',
        'id': 'str',
        'inheritance_parent': 'str',
        'inheritance_sources': 'IpamsvcDHCPInheritance',
        'name': 'str',
        'parent': 'str',
        'protocol': 'str',
        'space': 'str',
        'tags': 'TypesJSONValue',
        'threshold': 'IpamsvcUtilizationThreshold',
        'utilization': 'IpamsvcUtilization'
    }

    attribute_map = {
        'address': 'address',
        'asm_config': 'asm_config',
        'asm_scope_flag': 'asm_scope_flag',
        'cidr': 'cidr',
        'comment': 'comment',
        'dhcp_config': 'dhcp_config',
        'dhcp_options': 'dhcp_options',
        'dhcp_utilization': 'dhcp_utilization',
        'id': 'id',
        'inheritance_parent': 'inheritance_parent',
        'inheritance_sources': 'inheritance_sources',
        'name': 'name',
        'parent': 'parent',
        'protocol': 'protocol',
        'space': 'space',
        'tags': 'tags',
        'threshold': 'threshold',
        'utilization': 'utilization'
    }

    def __init__(self, address=None, asm_config=None, asm_scope_flag=None, cidr=None, comment=None, dhcp_config=None, dhcp_options=None, dhcp_utilization=None, id=None, inheritance_parent=None, inheritance_sources=None, name=None, parent=None, protocol=None, space=None, tags=None, threshold=None, utilization=None):  # noqa: E501
        """IpamsvcAddressBlock - a model defined in Swagger"""  # noqa: E501

        self._address = None
        self._asm_config = None
        self._asm_scope_flag = None
        self._cidr = None
        self._comment = None
        self._dhcp_config = None
        self._dhcp_options = None
        self._dhcp_utilization = None
        self._id = None
        self._inheritance_parent = None
        self._inheritance_sources = None
        self._name = None
        self._parent = None
        self._protocol = None
        self._space = None
        self._tags = None
        self._threshold = None
        self._utilization = None
        self.discriminator = None

        self.address = address
        if asm_config is not None:
            self.asm_config = asm_config
        if asm_scope_flag is not None:
            self.asm_scope_flag = asm_scope_flag
        if cidr is not None:
            self.cidr = cidr
        if comment is not None:
            self.comment = comment
        if dhcp_config is not None:
            self.dhcp_config = dhcp_config
        if dhcp_options is not None:
            self.dhcp_options = dhcp_options
        if dhcp_utilization is not None:
            self.dhcp_utilization = dhcp_utilization
        if id is not None:
            self.id = id
        if inheritance_parent is not None:
            self.inheritance_parent = inheritance_parent
        if inheritance_sources is not None:
            self.inheritance_sources = inheritance_sources
        if name is not None:
            self.name = name
        if parent is not None:
            self.parent = parent
        if protocol is not None:
            self.protocol = protocol
        self.space = space
        if tags is not None:
            self.tags = tags
        if threshold is not None:
            self.threshold = threshold
        if utilization is not None:
            self.utilization = utilization

    @property
    def address(self):
        """Gets the address of this IpamsvcAddressBlock.  # noqa: E501

        The address field in form “a.b.c.d/n” where the “/n” may be omitted. In this case, the cidr value must be defined in the cidr field. When reading, the address field is always in the form “a.b.c.d”.  # noqa: E501

        :return: The address of this IpamsvcAddressBlock.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this IpamsvcAddressBlock.

        The address field in form “a.b.c.d/n” where the “/n” may be omitted. In this case, the cidr value must be defined in the cidr field. When reading, the address field is always in the form “a.b.c.d”.  # noqa: E501

        :param address: The address of this IpamsvcAddressBlock.  # noqa: E501
        :type: str
        """
        if address is None:
            raise ValueError("Invalid value for `address`, must not be `None`")  # noqa: E501

        self._address = address

    @property
    def asm_config(self):
        """Gets the asm_config of this IpamsvcAddressBlock.  # noqa: E501


        :return: The asm_config of this IpamsvcAddressBlock.  # noqa: E501
        :rtype: IpamsvcASMConfig
        """
        return self._asm_config

    @asm_config.setter
    def asm_config(self, asm_config):
        """Sets the asm_config of this IpamsvcAddressBlock.


        :param asm_config: The asm_config of this IpamsvcAddressBlock.  # noqa: E501
        :type: IpamsvcASMConfig
        """

        self._asm_config = asm_config

    @property
    def asm_scope_flag(self):
        """Gets the asm_scope_flag of this IpamsvcAddressBlock.  # noqa: E501


        :return: The asm_scope_flag of this IpamsvcAddressBlock.  # noqa: E501
        :rtype: int
        """
        return self._asm_scope_flag

    @asm_scope_flag.setter
    def asm_scope_flag(self, asm_scope_flag):
        """Sets the asm_scope_flag of this IpamsvcAddressBlock.


        :param asm_scope_flag: The asm_scope_flag of this IpamsvcAddressBlock.  # noqa: E501
        :type: int
        """

        self._asm_scope_flag = asm_scope_flag

    @property
    def cidr(self):
        """Gets the cidr of this IpamsvcAddressBlock.  # noqa: E501

        The CIDR of the Address Block object. Required, if address does not specify it in its input.  # noqa: E501

        :return: The cidr of this IpamsvcAddressBlock.  # noqa: E501
        :rtype: int
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        """Sets the cidr of this IpamsvcAddressBlock.

        The CIDR of the Address Block object. Required, if address does not specify it in its input.  # noqa: E501

        :param cidr: The cidr of this IpamsvcAddressBlock.  # noqa: E501
        :type: int
        """

        self._cidr = cidr

    @property
    def comment(self):
        """Gets the comment of this IpamsvcAddressBlock.  # noqa: E501

        A comment of the Address Block object.  # noqa: E501

        :return: The comment of this IpamsvcAddressBlock.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this IpamsvcAddressBlock.

        A comment of the Address Block object.  # noqa: E501

        :param comment: The comment of this IpamsvcAddressBlock.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def dhcp_config(self):
        """Gets the dhcp_config of this IpamsvcAddressBlock.  # noqa: E501

        A shared DHCP configuration that controls how leases are issued.  # noqa: E501

        :return: The dhcp_config of this IpamsvcAddressBlock.  # noqa: E501
        :rtype: IpamsvcDHCPConfig
        """
        return self._dhcp_config

    @dhcp_config.setter
    def dhcp_config(self, dhcp_config):
        """Sets the dhcp_config of this IpamsvcAddressBlock.

        A shared DHCP configuration that controls how leases are issued.  # noqa: E501

        :param dhcp_config: The dhcp_config of this IpamsvcAddressBlock.  # noqa: E501
        :type: IpamsvcDHCPConfig
        """

        self._dhcp_config = dhcp_config

    @property
    def dhcp_options(self):
        """Gets the dhcp_options of this IpamsvcAddressBlock.  # noqa: E501

        A list of DHCP options. May be either a specific option or a group of options.  # noqa: E501

        :return: The dhcp_options of this IpamsvcAddressBlock.  # noqa: E501
        :rtype: list[IpamsvcOptionItem]
        """
        return self._dhcp_options

    @dhcp_options.setter
    def dhcp_options(self, dhcp_options):
        """Sets the dhcp_options of this IpamsvcAddressBlock.

        A list of DHCP options. May be either a specific option or a group of options.  # noqa: E501

        :param dhcp_options: The dhcp_options of this IpamsvcAddressBlock.  # noqa: E501
        :type: list[IpamsvcOptionItem]
        """

        self._dhcp_options = dhcp_options

    @property
    def dhcp_utilization(self):
        """Gets the dhcp_utilization of this IpamsvcAddressBlock.  # noqa: E501


        :return: The dhcp_utilization of this IpamsvcAddressBlock.  # noqa: E501
        :rtype: IpamsvcDHCPUtilization
        """
        return self._dhcp_utilization

    @dhcp_utilization.setter
    def dhcp_utilization(self, dhcp_utilization):
        """Sets the dhcp_utilization of this IpamsvcAddressBlock.


        :param dhcp_utilization: The dhcp_utilization of this IpamsvcAddressBlock.  # noqa: E501
        :type: IpamsvcDHCPUtilization
        """

        self._dhcp_utilization = dhcp_utilization

    @property
    def id(self):
        """Gets the id of this IpamsvcAddressBlock.  # noqa: E501

        The resource identifier.  # noqa: E501

        :return: The id of this IpamsvcAddressBlock.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IpamsvcAddressBlock.

        The resource identifier.  # noqa: E501

        :param id: The id of this IpamsvcAddressBlock.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def inheritance_parent(self):
        """Gets the inheritance_parent of this IpamsvcAddressBlock.  # noqa: E501

        The resource identifier.  # noqa: E501

        :return: The inheritance_parent of this IpamsvcAddressBlock.  # noqa: E501
        :rtype: str
        """
        return self._inheritance_parent

    @inheritance_parent.setter
    def inheritance_parent(self, inheritance_parent):
        """Sets the inheritance_parent of this IpamsvcAddressBlock.

        The resource identifier.  # noqa: E501

        :param inheritance_parent: The inheritance_parent of this IpamsvcAddressBlock.  # noqa: E501
        :type: str
        """

        self._inheritance_parent = inheritance_parent

    @property
    def inheritance_sources(self):
        """Gets the inheritance_sources of this IpamsvcAddressBlock.  # noqa: E501

        Optional. Inheritance configuration.  # noqa: E501

        :return: The inheritance_sources of this IpamsvcAddressBlock.  # noqa: E501
        :rtype: IpamsvcDHCPInheritance
        """
        return self._inheritance_sources

    @inheritance_sources.setter
    def inheritance_sources(self, inheritance_sources):
        """Sets the inheritance_sources of this IpamsvcAddressBlock.

        Optional. Inheritance configuration.  # noqa: E501

        :param inheritance_sources: The inheritance_sources of this IpamsvcAddressBlock.  # noqa: E501
        :type: IpamsvcDHCPInheritance
        """

        self._inheritance_sources = inheritance_sources

    @property
    def name(self):
        """Gets the name of this IpamsvcAddressBlock.  # noqa: E501

        The name of the Address Block object.  # noqa: E501

        :return: The name of this IpamsvcAddressBlock.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IpamsvcAddressBlock.

        The name of the Address Block object.  # noqa: E501

        :param name: The name of this IpamsvcAddressBlock.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def parent(self):
        """Gets the parent of this IpamsvcAddressBlock.  # noqa: E501

        The resource identifier.  # noqa: E501

        :return: The parent of this IpamsvcAddressBlock.  # noqa: E501
        :rtype: str
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this IpamsvcAddressBlock.

        The resource identifier.  # noqa: E501

        :param parent: The parent of this IpamsvcAddressBlock.  # noqa: E501
        :type: str
        """

        self._parent = parent

    @property
    def protocol(self):
        """Gets the protocol of this IpamsvcAddressBlock.  # noqa: E501

        RO Field: The type of protocol (ipv4 or ipv6).  # noqa: E501

        :return: The protocol of this IpamsvcAddressBlock.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this IpamsvcAddressBlock.

        RO Field: The type of protocol (ipv4 or ipv6).  # noqa: E501

        :param protocol: The protocol of this IpamsvcAddressBlock.  # noqa: E501
        :type: str
        """

        self._protocol = protocol

    @property
    def space(self):
        """Gets the space of this IpamsvcAddressBlock.  # noqa: E501

        The resource identifier.  # noqa: E501

        :return: The space of this IpamsvcAddressBlock.  # noqa: E501
        :rtype: str
        """
        return self._space

    @space.setter
    def space(self, space):
        """Sets the space of this IpamsvcAddressBlock.

        The resource identifier.  # noqa: E501

        :param space: The space of this IpamsvcAddressBlock.  # noqa: E501
        :type: str
        """
        if space is None:
            raise ValueError("Invalid value for `space`, must not be `None`")  # noqa: E501

        self._space = space

    @property
    def tags(self):
        """Gets the tags of this IpamsvcAddressBlock.  # noqa: E501

        Tagging specifics.  # noqa: E501

        :return: The tags of this IpamsvcAddressBlock.  # noqa: E501
        :rtype: TypesJSONValue
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this IpamsvcAddressBlock.

        Tagging specifics.  # noqa: E501

        :param tags: The tags of this IpamsvcAddressBlock.  # noqa: E501
        :type: TypesJSONValue
        """

        self._tags = tags

    @property
    def threshold(self):
        """Gets the threshold of this IpamsvcAddressBlock.  # noqa: E501

        The Utilization threshold (low and high) values of the utilization.  # noqa: E501

        :return: The threshold of this IpamsvcAddressBlock.  # noqa: E501
        :rtype: IpamsvcUtilizationThreshold
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        """Sets the threshold of this IpamsvcAddressBlock.

        The Utilization threshold (low and high) values of the utilization.  # noqa: E501

        :param threshold: The threshold of this IpamsvcAddressBlock.  # noqa: E501
        :type: IpamsvcUtilizationThreshold
        """

        self._threshold = threshold

    @property
    def utilization(self):
        """Gets the utilization of this IpamsvcAddressBlock.  # noqa: E501

        RO Field: The Utilization of this Address Block object.  # noqa: E501

        :return: The utilization of this IpamsvcAddressBlock.  # noqa: E501
        :rtype: IpamsvcUtilization
        """
        return self._utilization

    @utilization.setter
    def utilization(self, utilization):
        """Sets the utilization of this IpamsvcAddressBlock.

        RO Field: The Utilization of this Address Block object.  # noqa: E501

        :param utilization: The utilization of this IpamsvcAddressBlock.  # noqa: E501
        :type: IpamsvcUtilization
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
        if issubclass(IpamsvcAddressBlock, dict):
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
        if not isinstance(other, IpamsvcAddressBlock):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
