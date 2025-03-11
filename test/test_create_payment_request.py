"""
MONEI API v1

<p>The MONEI API is organized around <a href=\"https://en.wikipedia.org/wiki/Representational_State_Transfer\">REST</a> principles. Our API is designed to be intuitive and developer-friendly.</p> <h3>Base URL</h3> <p>All API requests should be made to:</p> <pre><code>https://api.monei.com/v1 </code></pre> <h3>Environment</h3> <p>MONEI provides two environments:</p> <ul> <li><strong>Test Environment</strong>: For development and testing without processing real payments</li> <li><strong>Live Environment</strong>: For processing real transactions in production</li> </ul> <h3>Client Libraries</h3> <p>We provide official SDKs to simplify integration:</p> <ul> <li><a href=\"https://github.com/MONEI/monei-php-sdk\">PHP SDK</a></li> <li><a href=\"https://github.com/MONEI/monei-python-sdk\">Python SDK</a></li> <li><a href=\"https://github.com/MONEI/monei-node-sdk\">Node.js SDK</a></li> <li><a href=\"https://postman.monei.com/\">Postman Collection</a></li> </ul> <p>Our SDKs handle authentication, error handling, and request formatting automatically.</p> <p>You can download the OpenAPI specification from the <a href=\"https://js.monei.com/api/v1/openapi.json\">https://js.monei.com/api/v1/openapi.json</a> and generate your own client library using the <a href=\"https://openapi-generator.tech/\">OpenAPI Generator</a>.</p> <h3>Important Requirements</h3> <ul> <li>All API requests must be made over HTTPS</li> <li>If you are not using our official SDKs, you <strong>must provide a valid <code>User-Agent</code> header</strong> with each request</li> <li>Requests without proper authentication will return a <code>401 Unauthorized</code> error</li> </ul> <h3>Error Handling</h3> <p>The API returns consistent error codes and messages to help you troubleshoot issues. Each response includes a <code>statusCode</code> attribute indicating the outcome of your request.</p> <h3>Rate Limits</h3> <p>The API implements rate limiting to ensure stability. If you exceed the limits, requests will return a <code>429 Too Many Requests</code> status code.</p>   # noqa: E501

The version of the OpenAPI document: 1.5.3
Generated by: https://openapi-generator.tech
"""

import sys
import unittest

import Monei
from Monei.model.payment_billing_details import PaymentBillingDetails
from Monei.model.payment_customer import PaymentCustomer
from Monei.model.payment_payment_method_input import PaymentPaymentMethodInput
from Monei.model.payment_payment_methods import PaymentPaymentMethods
from Monei.model.payment_sequence import PaymentSequence
from Monei.model.payment_session_details import PaymentSessionDetails
from Monei.model.payment_shipping_details import PaymentShippingDetails
from Monei.model.payment_transaction_type import PaymentTransactionType

globals()["PaymentBillingDetails"] = PaymentBillingDetails
globals()["PaymentCustomer"] = PaymentCustomer
globals()["PaymentPaymentMethodInput"] = PaymentPaymentMethodInput
globals()["PaymentPaymentMethods"] = PaymentPaymentMethods
globals()["PaymentSequence"] = PaymentSequence
globals()["PaymentSessionDetails"] = PaymentSessionDetails
globals()["PaymentShippingDetails"] = PaymentShippingDetails
globals()["PaymentTransactionType"] = PaymentTransactionType
from Monei.model.create_payment_request import CreatePaymentRequest
from Monei.exceptions import ApiTypeError, ApiValueError


class TestCreatePaymentRequest(unittest.TestCase):
    """CreatePaymentRequest unit test stubs"""

    def setUp(self):
        self.valid_params = {
            "amount": 1000,
            "currency": "EUR",
            "description": "Test payment",
        }

    def tearDown(self):
        pass

    def test_create_payment_request(self):
        """Test CreatePaymentRequest"""
        # Initialize the model with required parameters
        payment_request = CreatePaymentRequest(
            amount=1000, currency="EUR", order_id="order123"
        )

        # Verify required parameters were set correctly
        self.assertEqual(payment_request.amount, 1000)
        self.assertEqual(payment_request.currency, "EUR")
        self.assertEqual(payment_request.order_id, "order123")

    def test_required_field_validation(self):
        """Test validation of required fields."""
        # Test missing amount
        with self.assertRaises(TypeError) as context:
            CreatePaymentRequest(currency="EUR", order_id="order123")
        self.assertIn("amount", str(context.exception))

        # Test missing currency
        with self.assertRaises(TypeError) as context:
            CreatePaymentRequest(amount=1000, order_id="order123")
        self.assertIn("currency", str(context.exception))

        # Test missing order_id
        with self.assertRaises(TypeError) as context:
            CreatePaymentRequest(amount=1000, currency="EUR")
        self.assertIn("order_id", str(context.exception))

    def test_field_type_validation(self):
        """Test validation of field types."""
        # Test invalid amount type
        with self.assertRaises(ApiTypeError) as context:
            CreatePaymentRequest(amount="1000", currency="EUR", order_id="order123")
        self.assertIn("amount", str(context.exception))

        # Test invalid currency type
        with self.assertRaises(ApiTypeError) as context:
            CreatePaymentRequest(amount=1000, currency=123, order_id="order123")
        self.assertIn("currency", str(context.exception))

        # Test invalid order_id type
        with self.assertRaises(ApiTypeError) as context:
            CreatePaymentRequest(amount=1000, currency="EUR", order_id=123)
        self.assertIn("order_id", str(context.exception))

    def test_field_value_validation(self):
        """Test validation of field values."""
        # Test negative amount can be set (no validation)
        payment_request = CreatePaymentRequest(
            amount=-100, currency="EUR", order_id="order123"
        )
        self.assertEqual(payment_request.amount, -100)

        # Test invalid currency code can be set (no validation)
        payment_request = CreatePaymentRequest(
            amount=1000, currency="INVALID", order_id="order123"
        )
        self.assertEqual(payment_request.currency, "INVALID")

    def test_optional_fields(self):
        """Test setting optional fields."""
        payment_request = CreatePaymentRequest(
            amount=1000,
            currency="EUR",
            order_id="order123",
            description="Test payment",
            success_url="https://example.com/success",
            cancel_url="https://example.com/cancel",
            payment_methods=["card", "paypal"],
        )

        # Verify optional fields were set correctly
        self.assertEqual(payment_request.description, "Test payment")
        self.assertEqual(payment_request.order_id, "order123")
        self.assertEqual(payment_request.success_url, "https://example.com/success")
        self.assertEqual(payment_request.cancel_url, "https://example.com/cancel")
        self.assertEqual(payment_request.payment_methods, ["card", "paypal"])


if __name__ == "__main__":
    unittest.main()
