# coding: utf-8

"""
    MONEI API v1

    The MONEI API is organized around [REST](https://en.wikipedia.org/wiki/Representational_State_Transfer). Our API has predictable resource-oriented URLs, accepts JSON-encoded request bodies, returns JSON-encoded responses, and uses standard HTTP response codes, authentication, and verbs. <br/><br/> **Base URL:** https://api.monei.com/v1 <br/><br/> **Client libraries:** <ul>   <li><a target=\"_blank\" href=\"https://github.com/MONEI/monei-php-sdk\">PHP SDK</a></li>   <li><a target=\"_blank\" href=\"https://github.com/MONEI/monei-python-sdk\">Python SDK</a></li>   <li><a target=\"_blank\" href=\"https://github.com/MONEI/monei-node-sdk\">Node.js SDK</a></li>   <li><a target=\"_blank\" href=\"https://postman.monei.com/\">Postman Collection</a></li> </ul>  # noqa: E501

    The version of the OpenAPI document: 1.1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import Monei
from Monei.api.apple_pay_domain_api import ApplePayDomainApi  # noqa: E501
from Monei.rest import ApiException


class TestApplePayDomainApi(unittest.TestCase):
    """ApplePayDomainApi unit test stubs"""

    def setUp(self):
        self.api = Monei.api.apple_pay_domain_api.ApplePayDomainApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_register(self):
        """Test case for register

        Register  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
