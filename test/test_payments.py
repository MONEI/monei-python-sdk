"""
Unit tests for the payments API.
"""

from unittest.mock import MagicMock


class TestPaymentsApi:
    """Tests for the payments API."""

    def test_create_payment(self, monei_client, mock_payment_response, mock_http_client):
        """Test creating a payment."""
        # Configure the mock to return a successful response
        mock_response = MagicMock()
        mock_response.data = mock_payment_response
        mock_http_client.return_value = mock_response

        # Create a payment
        payment_data = {
            "amount": 1250,
            "orderId": "100200000001",
            "currency": "EUR",
            "description": "Test payment",
            "customer": {"email": "john.doe@monei.com", "name": "John Doe"},
        }
        result = monei_client.payments.create(payment_data)

        # Check that the request was made correctly
        mock_http_client.assert_called_once()
        assert result == mock_payment_response
        assert result["amount"] == 1250
        assert result["currency"] == "EUR"
        assert result["status"] == "COMPLETED" 