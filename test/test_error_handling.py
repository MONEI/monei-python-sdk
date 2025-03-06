import unittest
from unittest.mock import patch

from Monei.monei_client import MoneiClient
from Monei.exceptions import ApiException


class TestErrorHandling(unittest.TestCase):
    """Error handling test stubs"""

    def setUp(self):
        """Set up test fixtures, if any."""
        self.api_key = "test_api_key_12345"
        self.client = MoneiClient(api_key=self.api_key)

    def tearDown(self):
        """Tear down test fixtures, if any."""
        pass

    @patch("Monei.api.payments_api.PaymentsApi.create")
    def test_api_error_handling(self, mock_create):
        """Test handling API errors."""
        # Setup mock to raise an ApiException
        mock_create.side_effect = ApiException(status=400, reason="Bad Request")

        # Create payment request
        payment_request = {
            "amount": 1000,
            "currency": "EUR",
            # Missing required fields
        }

        # Call the API and expect an exception
        with self.assertRaises(ApiException) as context:
            self.client.payments.create(payment_request)

        # Verify the exception details
        self.assertEqual(context.exception.status, 400)
        self.assertEqual(context.exception.reason, "Bad Request")

    @patch("Monei.api.payments_api.PaymentsApi.get")
    def test_not_found_error(self, mock_get):
        """Test handling 404 Not Found errors."""
        # Setup mock to raise an ApiException with 404 status
        mock_get.side_effect = ApiException(status=404, reason="Not Found")

        # Call the API with a non-existent payment ID
        with self.assertRaises(ApiException) as context:
            self.client.payments.get("non_existent_payment_id")

        # Verify the exception details
        self.assertEqual(context.exception.status, 404)
        self.assertEqual(context.exception.reason, "Not Found")

    @patch("Monei.api.payments_api.PaymentsApi.confirm")
    def test_unauthorized_error(self, mock_confirm):
        """Test handling 401 Unauthorized errors."""
        # Setup mock to raise an ApiException with 401 status
        mock_confirm.side_effect = ApiException(status=401, reason="Unauthorized")

        # Call the API with an invalid API key
        with self.assertRaises(ApiException) as context:
            self.client.payments.confirm("payment_id", {"paymentMethod": {"type": "CARD"}})

        # Verify the exception details
        self.assertEqual(context.exception.status, 401)
        self.assertEqual(context.exception.reason, "Unauthorized")

    def test_invalid_account_id_without_user_agent(self):
        """Test error when setting account ID without user agent."""
        client = MoneiClient(api_key=self.api_key)

        with self.assertRaises(ApiException) as context:
            client.set_account_id("account_id")

        self.assertEqual(context.exception.status, 400)
        self.assertEqual(context.exception.reason, "User-Agent must be set before using Account ID")


if __name__ == "__main__":
    unittest.main()
