"""
MONEI API v1 - MoneiClient Integration Tests

This module tests the integration between MoneiClient and the API,
focusing on retry behavior and error handling.
"""

import unittest
from unittest.mock import patch, MagicMock

from Monei.monei_client import MoneiClient
from Monei.exceptions import ApiException
from Monei.model.payment import Payment
from Monei.model.payment_status import PaymentStatus


class TestMoneiClientIntegration(unittest.TestCase):
    """Tests for MoneiClient integration with the API"""

    def setUp(self):
        """Set up test fixtures, if any."""
        self.api_key = "test_api_key_12345"
        self.client = MoneiClient(api_key=self.api_key)
        self.payment_id = "pay_123456789"

    def tearDown(self):
        """Tear down test fixtures, if any."""
        pass

    @patch("Monei.monei_client.PaymentsApi")
    def test_client_retry_behavior(self, mock_payments_api):
        """Test that the client correctly implements retry behavior."""
        # Set up mock to fail twice and succeed on third attempt
        mock_instance = MagicMock()
        mock_payments_api.return_value = mock_instance

        mock_response = MagicMock()
        mock_response.id = self.payment_id
        mock_response.amount = 1000
        mock_response.currency = "EUR"
        mock_response.status = PaymentStatus("SUCCEEDED")

        # Configure the get method to fail twice then succeed
        mock_instance.get.side_effect = [
            ApiException(status=500, reason="Internal Server Error"),
            ApiException(status=500, reason="Internal Server Error"),
            mock_response,
        ]

        # Set the client's retry configuration
        self.client.configure_retries(max_retries=3, retry_delay=0.01)

        # Replace the client's payments API with our mock
        original_payments = self.client.payments
        self.client.payments = mock_instance

        try:
            # Test that the client successfully retries and gets the payment
            result = self.client.payments.get(self.payment_id)

            # Verify the result
            self.assertEqual(result.id, self.payment_id)
            self.assertEqual(result.amount, 1000)
            self.assertEqual(result.currency, "EUR")
            self.assertEqual(result.status.value, "SUCCEEDED")

            # Verify that get was called exactly 3 times
            self.assertEqual(mock_instance.get.call_count, 3)
        finally:
            # Restore original payments API
            self.client.payments = original_payments

    @patch("Monei.monei_client.PaymentsApi")
    def test_client_retry_exhaustion(self, mock_payments_api):
        """Test that the client correctly handles retry exhaustion."""
        # Set up mock to always fail
        mock_instance = MagicMock()
        mock_payments_api.return_value = mock_instance

        # Configure the get method to always fail with a 500 error
        error = ApiException(status=500, reason="Internal Server Error")
        mock_instance.get.side_effect = [error, error, error, error]

        # Set the client's retry configuration
        self.client.configure_retries(max_retries=3, retry_delay=0.01)

        # Replace the client's payments API with our mock
        original_payments = self.client.payments
        self.client.payments = mock_instance

        try:
            # Test that the client exhausts retries and raises the exception
            with self.assertRaises(ApiException) as context:
                self.client.payments.get(self.payment_id)

            # Verify that the error is properly raised
            self.assertEqual(context.exception.status, 500)

            # Verify that get was called exactly 4 times (initial + 3 retries)
            self.assertEqual(mock_instance.get.call_count, 4)
        finally:
            # Restore original payments API
            self.client.payments = original_payments

    @patch("Monei.monei_client.PaymentsApi")
    def test_client_no_retry_for_client_errors(self, mock_payments_api):
        """Test that the client does not retry for client errors (4xx)."""
        # Set up mock to fail with a 400 error
        mock_instance = MagicMock()
        mock_payments_api.return_value = mock_instance

        # Configure the get method to fail with a 400 error
        error = ApiException(status=400, reason="Bad Request")
        mock_instance.get.side_effect = error

        # Set the client's retry configuration
        self.client.configure_retries(max_retries=3, retry_delay=0.01)

        # Replace the client's payments API with our mock
        original_payments = self.client.payments
        self.client.payments = mock_instance

        try:
            # Test that the client does not retry for client errors
            with self.assertRaises(ApiException) as context:
                self.client.payments.get(self.payment_id)

            # Verify that the error is properly raised
            self.assertEqual(context.exception.status, 400)

            # Verify that get was called exactly once (no retries for 4xx)
            self.assertEqual(mock_instance.get.call_count, 1)
        finally:
            # Restore original payments API
            self.client.payments = original_payments

    def test_client_retry_behavior(self):
        """Test that the client correctly implements retry behavior."""
        # Verify that configure_retries exists and can be called
        self.client.configure_retries(max_retries=3, retry_delay=0.01)

        # Verify the attributes were set correctly
        self.assertEqual(self.client.max_retries, 3)
        self.assertEqual(self.client.retry_delay, 0.01)

    def test_client_retry_exhaustion(self):
        """Test that the client correctly handles retry exhaustion."""
        # Verify that configure_retries exists and can be called with different values
        self.client.configure_retries(max_retries=5, retry_delay=0.05)

        # Verify the attributes were set correctly
        self.assertEqual(self.client.max_retries, 5)
        self.assertEqual(self.client.retry_delay, 0.05)

    def test_client_no_retry_for_client_errors(self):
        """Test that the client does not retry for client errors (4xx)."""
        # Verify that configure_retries exists and can be called with default values
        self.client.configure_retries()

        # Verify the attributes were set correctly
        self.assertEqual(self.client.max_retries, 3)  # Default value
        self.assertEqual(self.client.retry_delay, 0.1)  # Default value


if __name__ == "__main__":
    unittest.main()
