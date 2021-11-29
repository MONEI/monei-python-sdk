# coding: utf-8

"""
    MONEI API v1

    The MONEI API is organized around [REST](https://en.wikipedia.org/wiki/Representational_State_Transfer). Our API has predictable resource-oriented URLs, accepts JSON-encoded request bodies, returns JSON-encoded responses, and uses standard HTTP response codes, authentication, and verbs. <br/><br/> **Base URL:** https://api.monei.com/v1 <br/><br/> **Client libraries:** <ul>   <li><a target=\"_blank\" href=\"https://github.com/MONEI/monei-php-sdk\">PHP SDK</a></li>   <li><a target=\"_blank\" href=\"https://github.com/MONEI/monei-python-sdk\">Python SDK</a></li>   <li><a target=\"_blank\" href=\"https://github.com/MONEI/monei-node-sdk\">Node.js SDK</a></li>   <li><a target=\"_blank\" href=\"https://postman.monei.com/\">Postman Collection</a></li> </ul>  # noqa: E501

    The version of the OpenAPI document: 1.1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import Monei
from Monei.models.subscription_payment_method_card import SubscriptionPaymentMethodCard  # noqa: E501
from Monei.rest import ApiException

class TestSubscriptionPaymentMethodCard(unittest.TestCase):
    """SubscriptionPaymentMethodCard unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SubscriptionPaymentMethodCard
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = Monei.models.subscription_payment_method_card.SubscriptionPaymentMethodCard()  # noqa: E501
        if include_optional :
            return SubscriptionPaymentMethodCard(
                country = 'ES', 
                brand = 'visa', 
                type = 'credit', 
                three_d_secure = False, 
                three_d_secure_version = '2.1.0', 
                expiration = 2048544000, 
                last4 = '0004'
            )
        else :
            return SubscriptionPaymentMethodCard(
        )

    def testSubscriptionPaymentMethodCard(self):
        """Test SubscriptionPaymentMethodCard"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
