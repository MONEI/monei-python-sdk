# coding: utf-8

"""
    MONEI API v1

    <p>The MONEI API is organized around <a href=\"https://en.wikipedia.org/wiki/Representational_State_Transfer\">REST</a> principles. Our API is designed to be intuitive and developer-friendly.</p> <h3>Base URL</h3> <p>All API requests should be made to:</p> <pre><code>https://api.monei.com/v1 </code></pre> <h3>Environment</h3> <p>MONEI provides two environments:</p> <ul> <li><strong>Test Environment</strong>: For development and testing without processing real payments</li> <li><strong>Live Environment</strong>: For processing real transactions in production</li> </ul> <h3>Client Libraries</h3> <p>We provide official SDKs to simplify integration:</p> <ul> <li><a href=\"https://github.com/MONEI/monei-php-sdk\">PHP SDK</a></li> <li><a href=\"https://github.com/MONEI/monei-python-sdk\">Python SDK</a></li> <li><a href=\"https://github.com/MONEI/monei-node-sdk\">Node.js SDK</a></li> <li><a href=\"https://postman.monei.com/\">Postman Collection</a></li> </ul> <p>Our SDKs handle authentication, error handling, and request formatting automatically.</p> <h3>Important Requirements</h3> <ul> <li>All API requests must be made over HTTPS</li> <li>If you are not using our official SDKs, you <strong>must provide a valid <code>User-Agent</code> header</strong> with each request</li> <li>Requests without proper authentication will return a <code>401 Unauthorized</code> error</li> </ul> <h3>Error Handling</h3> <p>The API returns consistent error codes and messages to help you troubleshoot issues. Each response includes a <code>statusCode</code> attribute indicating the outcome of your request.</p> <p><a href=\"https://docs.monei.com/api/errors\">View complete list of status codes →</a></p> <h3>Rate Limits</h3> <p>The API implements rate limiting to ensure stability. If you exceed the limits, requests will return a <code>429 Too Many Requests</code> status code.</p>   # noqa: E501

    The version of the OpenAPI document: 1.4.8
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import Monei
from Monei.models.payment_methods_metadata import PaymentMethodsMetadata  # noqa: E501
from Monei.rest import ApiException

class TestPaymentMethodsMetadata(unittest.TestCase):
    """PaymentMethodsMetadata unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PaymentMethodsMetadata
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = Monei.models.payment_methods_metadata.PaymentMethodsMetadata()  # noqa: E501
        if include_optional :
            return PaymentMethodsMetadata(
                alipay = Monei.models.payment_methods_metadata_alipay.PaymentMethods_Metadata_alipay(
                    countries = ["CN"], ), 
                bancontact = Monei.models.payment_methods_metadata_bancontact.PaymentMethods_Metadata_bancontact(
                    countries = ["BE"], ), 
                bizum = Monei.models.payment_methods_metadata_bizum.PaymentMethods_Metadata_bizum(
                    countries = ["ES"], ), 
                blik = Monei.models.payment_methods_metadata_blik.PaymentMethods_Metadata_blik(
                    countries = ["PL"], ), 
                card = Monei.models.payment_methods_metadata_card.PaymentMethods_Metadata_card(
                    brands = ["visa","mastercard"], ), 
                eps = Monei.models.payment_methods_metadata_eps.PaymentMethods_Metadata_eps(
                    countries = ["AT"], ), 
                i_deal = Monei.models.payment_methods_metadata_i_deal.PaymentMethods_Metadata_iDeal(
                    countries = ["NL"], ), 
                mbway = Monei.models.payment_methods_metadata_mbway.PaymentMethods_Metadata_mbway(
                    countries = ["PT"], ), 
                multibanco = Monei.models.payment_methods_metadata_mbway.PaymentMethods_Metadata_mbway(
                    countries = ["PT"], ), 
                sofort = Monei.models.payment_methods_metadata_sofort.PaymentMethods_Metadata_sofort(
                    countries = ["AT","BE","DE","ES","IT","NL","CH","PL"], ), 
                trustly = Monei.models.payment_methods_metadata_trustly.PaymentMethods_Metadata_trustly(
                    countries = ["DE","DK","EE","ES","FI","GB","LT","LV","NL","NO","PL","SE","SK"], ), 
                sepa = Monei.models.payment_methods_metadata_sepa.PaymentMethods_Metadata_sepa(
                    countries = ["AT","BE","BG","HR","CY","CZ","DK","EE","FI","FR","DE","GR","HU","IE","IT","LV","LT","LU","MT","NL","PL","PT","RO","SK","SI","ES","SE","IS","LI","NO","AD","SM","MC","VA","PF","TF","GI","GG","IM","JE","BL","PM","CH","GB","WF"], ), 
                klarna = Monei.models.payment_methods_metadata_klarna.PaymentMethods_Metadata_klarna(
                    countries = ["AT","BE","CH","DE","DK","ES","FI","FR","GB","IT","NL","NO","SE"], ), 
                giropay = Monei.models.payment_methods_metadata_giropay.PaymentMethods_Metadata_giropay(
                    countries = ["DE"], ), 
                google_pay = Monei.models.payment_methods_metadata_google_pay.PaymentMethods_Metadata_googlePay(
                    merchant_id = '12345678901234567890', 
                    cvc_required = False, ), 
                apple_pay = Monei.models.payment_methods_metadata_apple_pay.PaymentMethods_Metadata_applePay(
                    merchant_id = 'merchant.com.monei', ), 
                click_to_pay = Monei.models.payment_methods_metadata_click_to_pay.PaymentMethods_Metadata_clickToPay(
                    token_support = True, 
                    preselected = False, 
                    visa = Monei.models.payment_methods_metadata_click_to_pay_visa.PaymentMethods_Metadata_clickToPay_visa(
                        srci_dpa_id = 'f47ac10b-58cc-4372-a567-0e02b2c3d479', 
                        src_initiator_id = '550e8400-e29b-41d4-a716-446655440000', ), 
                    mastercard = Monei.models.payment_methods_metadata_click_to_pay_mastercard.PaymentMethods_Metadata_clickToPay_mastercard(
                        srci_dpa_id = '6ba7b810-9dad-11d1-80b4-00c04fd430c8', 
                        src_initiator_id = 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11', ), 
                    discover = Monei.models.payment_methods_metadata_click_to_pay_discover.PaymentMethods_Metadata_clickToPay_discover(
                        srci_dpa_id = '71f0c4d5-9947-4d1c-9cb3-d6a3f7c4e701', 
                        src_initiator_id = 'c2d06c25-9ddb-4a5e-9d5a-3ff1c8d98467', ), )
            )
        else :
            return PaymentMethodsMetadata(
        )

    def testPaymentMethodsMetadata(self):
        """Test PaymentMethodsMetadata"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
