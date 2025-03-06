# coding: utf-8

"""
    MONEI API v1

    <p>The MONEI API is organized around <a href=\"https://en.wikipedia.org/wiki/Representational_State_Transfer\">REST</a> principles. Our API is designed to be intuitive and developer-friendly.</p> <h3>Base URL</h3> <p>All API requests should be made to:</p> <pre><code>https://api.monei.com/v1 </code></pre> <h3>Environment</h3> <p>MONEI provides two environments:</p> <ul> <li><strong>Test Environment</strong>: For development and testing without processing real payments</li> <li><strong>Live Environment</strong>: For processing real transactions in production</li> </ul> <h3>Client Libraries</h3> <p>We provide official SDKs to simplify integration:</p> <ul> <li><a href=\"https://github.com/MONEI/monei-php-sdk\">PHP SDK</a></li> <li><a href=\"https://github.com/MONEI/monei-python-sdk\">Python SDK</a></li> <li><a href=\"https://github.com/MONEI/monei-node-sdk\">Node.js SDK</a></li> <li><a href=\"https://postman.monei.com/\">Postman Collection</a></li> </ul> <p>Our SDKs handle authentication, error handling, and request formatting automatically.</p> <p>You can download the OpenAPI specification from the <a href=\"https://js.monei.com/api/v1/openapi.json\">https://js.monei.com/api/v1/openapi.json</a> and generate your own client library using the <a href=\"https://openapi-generator.tech/\">OpenAPI Generator</a>.</p> <h3>Important Requirements</h3> <ul> <li>All API requests must be made over HTTPS</li> <li>If you are not using our official SDKs, you <strong>must provide a valid <code>User-Agent</code> header</strong> with each request</li> <li>Requests without proper authentication will return a <code>401 Unauthorized</code> error</li> </ul> <h3>Error Handling</h3> <p>The API returns consistent error codes and messages to help you troubleshoot issues. Each response includes a <code>statusCode</code> attribute indicating the outcome of your request.</p> <h3>Rate Limits</h3> <p>The API implements rate limiting to ensure stability. If you exceed the limits, requests will return a <code>429 Too Many Requests</code> status code.</p> 

    The version of the OpenAPI document: 1.5.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from Monei.models.create_payment_request import CreatePaymentRequest

class TestCreatePaymentRequest(unittest.TestCase):
    """CreatePaymentRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreatePaymentRequest:
        """Test CreatePaymentRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreatePaymentRequest`
        """
        model = CreatePaymentRequest()
        if include_optional:
            return CreatePaymentRequest(
                amount = 110,
                currency = 'EUR',
                order_id = '14379133960355',
                callback_url = 'https://example.com/checkout/callback',
                complete_url = 'https://example.com/checkout/complete',
                fail_url = 'https://example.com/checkout/fail',
                cancel_url = 'https://example.com/checkout/cancel',
                payment_token = '7cc38b08ff471ccd313ad62b23b9f362b107560b',
                session_id = '39603551437913',
                generate_payment_token = False,
                payment_method = Monei.models.payment_payment_method_input.Payment-PaymentMethodInput(
                    card = Monei.models.payment_payment_method_card_input.Payment-PaymentMethodCardInput(
                        number = '', 
                        cvc = '', 
                        exp_month = '', 
                        exp_year = '', 
                        cardholder_name = 'John Doe', 
                        cardholder_email = 'john.doe@monei.com', ), 
                    bizum = Monei.models.payment_payment_method_bizum_input.Payment-PaymentMethodBizumInput(
                        phone_number = '', ), ),
                allowed_payment_methods = ["card","bizum","paypal"],
                transaction_type = 'SALE',
                sequence = Monei.models.payment_sequence.Payment-Sequence(
                    type = 'recurring', 
                    recurring = Monei.models.payment_sequence_recurring.Payment-SequenceRecurring(
                        expiry = '*(The payment method or card expiration)*', 
                        frequency = 30, ), ),
                store_id = 'e5f28150d9e8974c58ab5ec9c4a880f8734dcf05',
                point_of_sale_id = 'fb269cccfa0cc021f5d0b8eb1421646c696213e1',
                subscription_id = '575bcd84-09fc-4a6e-8c4c-f88b8eb90bfa',
                auto_recover = False,
                description = 'Test Shop - #84370745531439',
                customer = Monei.models.payment_customer.Payment-Customer(
                    email = 'john.doe@example.com', 
                    name = 'John Doe', 
                    phone = '', ),
                billing_details = Monei.models.payment_billing_details.Payment-BillingDetails(
                    name = 'John Doe', 
                    email = 'john.doe@example.com', 
                    phone = '', 
                    company = '', 
                    tax_id = '', 
                    address = Monei.models.address.Address(
                        country = 'ES', 
                        city = 'Málaga', 
                        line1 = 'Fake Street 123', 
                        line2 = '', 
                        zip = '1234', 
                        state = 'Málaga', ), ),
                shipping_details = Monei.models.payment_shipping_details.Payment-ShippingDetails(
                    name = 'John Doe', 
                    email = 'john.doe@example.com', 
                    phone = '', 
                    company = '', 
                    tax_id = '', 
                    address = Monei.models.address.Address(
                        country = 'ES', 
                        city = 'Málaga', 
                        line1 = 'Fake Street 123', 
                        line2 = '', 
                        zip = '1234', 
                        state = 'Málaga', ), ),
                session_details = Monei.models.payment_session_details.Payment-SessionDetails(
                    ip = '100.100.200.100', 
                    country_code = 'ES', 
                    lang = 'es', 
                    device_type = 'desktop', 
                    device_model = '', 
                    browser = 'Chrome', 
                    browser_version = '83.0.4103.116', 
                    os = 'Mac OS', 
                    os_version = '10.15.4', 
                    source = 'MONEI/PHP', 
                    source_version = '0.1.2', 
                    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ...', 
                    browser_accept = 'text/html,application/xhtml+xml,application/json', 
                    browser_color_depth = 24, 
                    browser_screen_height = 1152, 
                    browser_screen_width = 2048, 
                    browser_timezone_offset = 'string', ),
                expire_at = 1663581391,
                metadata = {"systemId":"12345"}
            )
        else:
            return CreatePaymentRequest(
                amount = 110,
                currency = 'EUR',
                order_id = '14379133960355',
        )
        """

    def testCreatePaymentRequest(self):
        """Test CreatePaymentRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
