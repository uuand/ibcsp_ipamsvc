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
from ibcsp_ipamsvc.api.global_api import GlobalApi  # noqa: E501
from ibcsp_ipamsvc.rest import ApiException


class TestGlobalApi(unittest.TestCase):
    """GlobalApi unit test stubs"""

    def setUp(self):
        self.api = ibcsp_ipamsvc.api.global_api.GlobalApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_global_read(self):
        """Test case for global_read

        Read the Global configuration object.  # noqa: E501
        """
        pass

    def test_global_read2(self):
        """Test case for global_read2

        Read the Global configuration object.  # noqa: E501
        """
        pass

    def test_global_update(self):
        """Test case for global_update

        Update the Global configuration object.  # noqa: E501
        """
        pass

    def test_global_update2(self):
        """Test case for global_update2

        Update the Global configuration object.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
