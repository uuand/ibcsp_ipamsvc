# coding: utf-8

"""
    IP Address Management API

    The IPAM/DHCP Application is a BloxOne DDI service providing IP address management and DHCP protocol features. The IPAM component provides visibility into and provisioning tools to manage networking spaces, monitoring and reporting of entire IP address infrastructures, and integration with DNS and DHCP protocols. The DHCP component provides DHCP protocol configuration service with on-prem host serving DHCP protocol. It is part of the full-featured, DDI cloud solution that enables customers to deploy large numbers of protocol servers to deliver DNS and DHCP throughout their enterprise network.     # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import ibcsp_ipamsvc
from ibcsp_ipamsvc.api.address_api import AddressApi  # noqa: E501
from ibcsp_ipamsvc.rest import ApiException


class TestAddressApi(unittest.TestCase):
    """AddressApi unit test stubs"""

    def setUp(self):
        self.api = ibcsp_ipamsvc.api.address_api.AddressApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_address_create(self):
        """Test case for address_create

        Create the Address object.  # noqa: E501
        """
        pass

    def test_address_delete(self):
        """Test case for address_delete

        Delete the Address object.  # noqa: E501
        """
        pass

    def test_address_list(self):
        """Test case for address_list

        List Address objects.  # noqa: E501
        """
        pass

    def test_address_read(self):
        """Test case for address_read

        Read the Address object.  # noqa: E501
        """
        pass

    def test_address_update(self):
        """Test case for address_update

        Update the Address object.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
