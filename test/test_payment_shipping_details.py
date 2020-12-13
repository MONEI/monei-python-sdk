# coding: utf-8

"""
    MONEI API v1

    The MONEI API is organized around [REST](https://en.wikipedia.org/wiki/Representational_State_Transfer). Our API has predictable resource-oriented URLs, accepts JSON-encoded request bodies, returns JSON-encoded responses, and uses standard HTTP response codes, authentication, and verbs.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import MONEI PYTHON SDK
from MONEI PYTHON SDK.models.payment_shipping_details import PaymentShippingDetails  # noqa: E501
from MONEI PYTHON SDK.rest import ApiException

class TestPaymentShippingDetails(unittest.TestCase):
    """PaymentShippingDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PaymentShippingDetails
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = MONEI PYTHON SDK.models.payment_shipping_details.PaymentShippingDetails()  # noqa: E501
        if include_optional :
            return PaymentShippingDetails(
                name = 'John Doe', 
                email = 'john.doe@microapps.com', 
                phone = '0', 
                company = '0', 
                address = MONEI PYTHON SDK.models.address.Address(
                    country = 'ES', 
                    city = 'Málaga', 
                    line1 = 'Fake Street 123', 
                    line2 = '0', 
                    zip = '1234', 
                    state = 'Málaga', )
            )
        else :
            return PaymentShippingDetails(
        )

    def testPaymentShippingDetails(self):
        """Test PaymentShippingDetails"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
