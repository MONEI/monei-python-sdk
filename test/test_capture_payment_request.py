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
from MONEI PYTHON SDK.models.capture_payment_request import CapturePaymentRequest  # noqa: E501
from MONEI PYTHON SDK.rest import ApiException

class TestCapturePaymentRequest(unittest.TestCase):
    """CapturePaymentRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CapturePaymentRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = MONEI PYTHON SDK.models.capture_payment_request.CapturePaymentRequest()  # noqa: E501
        if include_optional :
            return CapturePaymentRequest(
                amount = null
            )
        else :
            return CapturePaymentRequest(
        )

    def testCapturePaymentRequest(self):
        """Test CapturePaymentRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
