import unittest
from unittest.mock import patch, MagicMock

import Monei  # noqa: F401
from Monei.monei_client import MoneiClient
from Monei.exceptions import ApiException


class TestPaymentMethodsApiIntegration(unittest.TestCase):
    """PaymentMethodsApi integration test stubs"""

    def setUp(self):
        """Set up test fixtures, if any."""
        self.api_key = "test_api_key_12345"
        self.client = MoneiClient(api_key=self.api_key)
        self.payment_method_id = "pm_123456789"
        self.customer_id = "cus_123456789"

    def tearDown(self):
        """Tear down test fixtures, if any."""
        pass

    @patch("Monei.api.payment_methods_api.PaymentMethodsApi.get")
    def test_get_payment_method(self, mock_get):
        """Test getting a payment method by ID."""
        # Setup mock response
        mock_payment_method = MagicMock()
        mock_payment_method.id = self.payment_method_id
        mock_payment_method.type = "CARD"
        mock_payment_method.card = MagicMock()
        mock_payment_method.card.last4 = "4242"
        mock_payment_method.card.brand = "VISA"
        mock_payment_method.card.expiryMonth = 12
        mock_payment_method.card.expiryYear = 2025
        mock_payment_method.customerId = self.customer_id
        mock_get.return_value = mock_payment_method

        # Call the API
        result = self.client.payment_methods.get(
            self.customer_id, self.payment_method_id
        )

        # Verify the result
        self.assertEqual(result.id, self.payment_method_id)
        self.assertEqual(result.type, "CARD")
        self.assertEqual(result.card.last4, "4242")
        self.assertEqual(result.card.brand, "VISA")
        self.assertEqual(result.card.expiryMonth, 12)
        self.assertEqual(result.card.expiryYear, 2025)
        self.assertEqual(result.customerId, self.customer_id)

        # Verify the mock was called with the correct arguments
        mock_get.assert_called_once_with(self.customer_id, self.payment_method_id)

    @patch("Monei.api.payment_methods_api.PaymentMethodsApi.get")
    def test_get_payment_method_nonexistent(self, mock_get):
        """Test getting a non-existent payment method."""
        # Setup mock to raise a NotFoundError
        mock_get.side_effect = ApiException(status=404, reason="Not Found")

        # Call the API method and verify it raises an exception
        with self.assertRaises(ApiException) as context:
            self.client.payment_methods.get(self.customer_id, "pm_nonexistent")

        # Verify the exception has the correct status code
        self.assertEqual(context.exception.status, 404)

    @patch("Monei.api.payment_methods_api.PaymentMethodsApi.get")
    def test_get_payment_method_unauthorized(self, mock_get):
        """Test unauthorized access to a payment method."""
        # Setup mock to raise an UnauthorizedError
        mock_get.side_effect = ApiException(status=401, reason="Unauthorized")

        # Create a new client with invalid credentials for testing
        invalid_client = MoneiClient(api_key="invalid_key")

        # Call the API method with an invalid API key and verify it raises an exception
        with self.assertRaises(ApiException) as context:
            invalid_client.payment_methods.get(self.customer_id, self.payment_method_id)

        # Verify the exception has the correct status code
        self.assertEqual(context.exception.status, 401)

    @patch("Monei.api.payment_methods_api.PaymentMethodsApi.get")
    def test_get_payment_method_sepa(self, mock_get):
        """Test getting a SEPA payment method."""
        # Setup mock response for SEPA payment method
        mock_payment_method = MagicMock()
        mock_payment_method.id = "pm_sepa_123456"
        mock_payment_method.type = "SEPA"
        mock_payment_method.sepa = MagicMock()
        mock_payment_method.sepa.last4 = "1234"
        mock_payment_method.sepa.bank = "Test Bank"
        mock_payment_method.sepa.country = "ES"
        mock_payment_method.customerId = self.customer_id
        mock_get.return_value = mock_payment_method

        # Call the API
        result = self.client.payment_methods.get(self.customer_id, "pm_sepa_123456")

        # Verify the result
        self.assertEqual(result.id, "pm_sepa_123456")
        self.assertEqual(result.type, "SEPA")
        self.assertEqual(result.sepa.last4, "1234")
        self.assertEqual(result.sepa.bank, "Test Bank")
        self.assertEqual(result.sepa.country, "ES")
        self.assertEqual(result.customerId, self.customer_id)


if __name__ == "__main__":
    unittest.main()
