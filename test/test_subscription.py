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
from Monei.models.subscription import Subscription  # noqa: E501
from Monei.rest import ApiException

class TestSubscription(unittest.TestCase):
    """Subscription unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Subscription
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = Monei.models.subscription.Subscription()  # noqa: E501
        if include_optional :
            return Subscription(
                id = '575bcd84-09fc-4a6e-8c4c-f88b8eb90bfa', 
                amount = 110, 
                currency = 'EUR', 
                description = 'MoonMail Monthly Lite', 
                account_id = 'aa9333ba-82de-400c-9ae7-087b9f8d2242', 
                livemode = False, 
                status = 'PENDING', 
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
                interval = 'month', 
                interval_count = 1, 
                pause_interval_count = 1, 
                last_order_id = '14379133960355', 
                last_payment = Monei.models.subscription_last_payment.Subscription-LastPayment(
                    id = 'af6029f80f5fc73a8ad2753eea0b1be0', 
                    status = 'PENDING', 
                    status_code = '0', 
                    status_message = '0', ), 
                payment_method = Monei.models.subscription_payment_method.Subscription-PaymentMethod(
                    method = 'card', 
                    card = Monei.models.payment_payment_method_card.Payment-PaymentMethodCard(
                        country = 'ES', 
                        brand = 'visa', 
                        type = 'credit', 
                        three_d_secure = False, 
                        three_d_secure_version = '2.1.0', 
                        expiration = 2048544000, 
                        last4 = '0004', ), ), 
                current_period_start = 1636366897, 
                current_period_end = 1636366897, 
                trial_period_end = 1636366897, 
                next_payment_at = 1636366897, 
                retry_count = 1, 
                cancel_at_period_end = False, 
                pause_at_period_end = False, 
                trace_details = Monei.models.payment_trace_details.Payment-TraceDetails(
                    ip = '100.100.200.100', 
                    country_code = 'ES', 
                    lang = 'es', 
                    device_type = 'desktop', 
                    device_model = '0', 
                    browser = 'Chrome', 
                    browser_version = '83.0.4103.116', 
                    os = 'Mac OS', 
                    os_version = '10.15.4', 
                    source = 'MONEI/PHP', 
                    source_version = '0.1.2', 
                    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ...', 
                    user_id = '0', 
                    user_email = 'user@example.com', ), 
                sequence_id = '62b23b9f3627cc38b08ff471ccd313ad', 
                callback_url = 'https://example.com/subscriptions/callback', 
                payment_callback_url = 'https://example.com/payments/callback', 
                created_at = 1636366897, 
                updated_at = 1636366897
            )
        else :
            return Subscription(
        )

    def testSubscription(self):
        """Test Subscription"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
