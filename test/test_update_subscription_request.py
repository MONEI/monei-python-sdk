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
from Monei.models.update_subscription_request import UpdateSubscriptionRequest  # noqa: E501
from Monei.rest import ApiException

class TestUpdateSubscriptionRequest(unittest.TestCase):
    """UpdateSubscriptionRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UpdateSubscriptionRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = Monei.models.update_subscription_request.UpdateSubscriptionRequest()  # noqa: E501
        if include_optional :
            return UpdateSubscriptionRequest(
                amount = 110, 
                interval = 'month', 
                interval_count = 1, 
                description = 'MoonMail Monthly Lite', 
                customer = Monei.models.payment_customer.Payment-Customer(
                    email = 'john.doe@example.com', 
                    name = 'John Doe', 
                    phone = '0', ), 
                billing_details = Monei.models.payment_billing_details.Payment-BillingDetails(
                    name = 'John Doe', 
                    email = 'john.doe@example.com', 
                    phone = '0', 
                    company = '0', 
                    address = Monei.models.address.Address(
                        country = 'ES', 
                        city = 'Málaga', 
                        line1 = 'Fake Street 123', 
                        line2 = '0', 
                        zip = '1234', 
                        state = 'Málaga', ), ), 
                shipping_details = Monei.models.payment_shipping_details.Payment-ShippingDetails(
                    name = 'John Doe', 
                    email = 'john.doe@example.com', 
                    phone = '0', 
                    company = '0', 
                    address = Monei.models.address.Address(
                        country = 'ES', 
                        city = 'Málaga', 
                        line1 = 'Fake Street 123', 
                        line2 = '0', 
                        zip = '1234', 
                        state = 'Málaga', ), ), 
                trial_period_end = 1636366897, 
                callback_url = 'https://example.com/subscriptions/callback', 
                payment_callback_url = 'https://example.com/payments/callback', 
                pause_at_period_end = False, 
                cancel_at_period_end = False, 
                pause_interval_count = 1
            )
        else :
            return UpdateSubscriptionRequest(
        )

    def testUpdateSubscriptionRequest(self):
        """Test UpdateSubscriptionRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
