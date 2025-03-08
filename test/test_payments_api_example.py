import unittest
from unittest.mock import patch, MagicMock
import json
import datetime

from Monei.api.payments_api import PaymentsApi
from Monei.model.payment import Payment
from Monei.model.create_payment_request import CreatePaymentRequest
from Monei.model.confirm_payment_request import ConfirmPaymentRequest
from Monei.model.capture_payment_request import CapturePaymentRequest
from Monei.model.cancel_payment_request import CancelPaymentRequest
from Monei.model.refund_payment_request import RefundPaymentRequest
from Monei.api_client import ApiClient
from Monei.configuration import Configuration
from Monei.exceptions import ApiException, NotFoundException, UnauthorizedException


class TestPaymentsApi(unittest.TestCase):
    """Test case for PaymentsApi"""

    def setUp(self):
        """Set up test fixtures, if any."""
        self.config = Configuration()
        self.config.api_key["ApiKey"] = "test_api_key"
        self.config.host = "https://api.monei.com/v1"

        self.api_client = ApiClient(self.config)
        self.api = PaymentsApi(self.api_client)

        # Sample payment data
        self.payment_data = {
            "id": "pay_123456789",
            "amount": 1000,
            "currency": "EUR",
            "status": "succeeded",
            "description": "Test payment",
            "created": "2023-01-01T12:00:00Z",
            "updated": "2023-01-01T12:05:00Z",
            "metadata": {"order_id": "order_123"},
        }

        # Sample payment object
        self.payment = Payment.from_dict(self.payment_data)

    @patch.object(ApiClient, "call_api")
    def test_create_payment(self, mock_call_api):
        """Test create_payment method."""
        # Mock the API response
        mock_call_api.return_value = self.payment_data

        # Create a payment request
        create_payment_request = CreatePaymentRequest(
            amount=1000,
            currency="EUR",
            description="Test payment",
            metadata={"order_id": "order_123"},
        )

        # Call the API method
        payment = self.api.create_payment(create_payment_request)

        # Verify the response
        self.assertEqual(payment.id, "pay_123456789")
        self.assertEqual(payment.amount, 1000)
        self.assertEqual(payment.currency, "EUR")
        self.assertEqual(payment.status, "succeeded")

        # Verify the API call
        mock_call_api.assert_called_once()
        args, kwargs = mock_call_api.call_args
        self.assertEqual(args[0], "/payments")
        self.assertEqual(args[1], "POST")
        self.assertEqual(kwargs["body"], create_payment_request)

    @patch.object(ApiClient, "call_api")
    def test_get_payment(self, mock_call_api):
        """Test get_payment method."""
        # Mock the API response
        mock_call_api.return_value = self.payment_data

        # Call the API method
        payment = self.api.get_payment("pay_123456789")

        # Verify the response
        self.assertEqual(payment.id, "pay_123456789")
        self.assertEqual(payment.amount, 1000)
        self.assertEqual(payment.currency, "EUR")
        self.assertEqual(payment.status, "succeeded")

        # Verify the API call
        mock_call_api.assert_called_once()
        args, kwargs = mock_call_api.call_args
        self.assertEqual(args[0], "/payments/pay_123456789")
        self.assertEqual(args[1], "GET")

    @patch.object(ApiClient, "call_api")
    def test_get_payment_not_found(self, mock_call_api):
        """Test get_payment method with not found error."""
        # Mock the API response to raise a NotFoundException
        mock_call_api.side_effect = NotFoundException(
            status=404, reason="Not Found", http_resp=MagicMock()
        )

        # Call the API method and expect an exception
        with self.assertRaises(NotFoundException):
            self.api.get_payment("pay_nonexistent")

        # Verify the API call
        mock_call_api.assert_called_once()

    @patch.object(ApiClient, "call_api")
    def test_list_payments(self, mock_call_api):
        """Test list_payments method."""
        # Mock the API response
        mock_call_api.return_value = {
            "data": [self.payment_data],
            "has_more": False,
            "total_count": 1,
        }

        # Call the API method
        response = self.api.list_payments(limit=10, starting_after="pay_previous")

        # Verify the response
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0].id, "pay_123456789")
        self.assertEqual(response.has_more, False)
        self.assertEqual(response.total_count, 1)

        # Verify the API call
        mock_call_api.assert_called_once()
        args, kwargs = mock_call_api.call_args
        self.assertEqual(args[0], "/payments")
        self.assertEqual(args[1], "GET")
        self.assertEqual(kwargs["query_params"]["limit"], 10)
        self.assertEqual(kwargs["query_params"]["starting_after"], "pay_previous")

    @patch.object(ApiClient, "call_api")
    def test_confirm_payment(self, mock_call_api):
        """Test confirm_payment method."""
        # Mock the API response
        confirmed_payment_data = self.payment_data.copy()
        confirmed_payment_data["status"] = "processing"
        mock_call_api.return_value = confirmed_payment_data

        # Create a confirm payment request
        confirm_payment_request = ConfirmPaymentRequest(
            payment_method={
                "type": "card",
                "card": {
                    "number": "4242424242424242",
                    "exp_month": 12,
                    "exp_year": 2025,
                    "cvc": "123",
                },
            }
        )

        # Call the API method
        payment = self.api.confirm_payment("pay_123456789", confirm_payment_request)

        # Verify the response
        self.assertEqual(payment.id, "pay_123456789")
        self.assertEqual(payment.status, "processing")

        # Verify the API call
        mock_call_api.assert_called_once()
        args, kwargs = mock_call_api.call_args
        self.assertEqual(args[0], "/payments/pay_123456789/confirm")
        self.assertEqual(args[1], "POST")
        self.assertEqual(kwargs["body"], confirm_payment_request)

    @patch.object(ApiClient, "call_api")
    def test_capture_payment(self, mock_call_api):
        """Test capture_payment method."""
        # Mock the API response
        captured_payment_data = self.payment_data.copy()
        captured_payment_data["status"] = "succeeded"
        mock_call_api.return_value = captured_payment_data

        # Create a capture payment request
        capture_payment_request = CapturePaymentRequest(amount=1000)

        # Call the API method
        payment = self.api.capture_payment("pay_123456789", capture_payment_request)

        # Verify the response
        self.assertEqual(payment.id, "pay_123456789")
        self.assertEqual(payment.status, "succeeded")

        # Verify the API call
        mock_call_api.assert_called_once()
        args, kwargs = mock_call_api.call_args
        self.assertEqual(args[0], "/payments/pay_123456789/capture")
        self.assertEqual(args[1], "POST")
        self.assertEqual(kwargs["body"], capture_payment_request)

    @patch.object(ApiClient, "call_api")
    def test_cancel_payment(self, mock_call_api):
        """Test cancel_payment method."""
        # Mock the API response
        canceled_payment_data = self.payment_data.copy()
        canceled_payment_data["status"] = "canceled"
        mock_call_api.return_value = canceled_payment_data

        # Create a cancel payment request
        cancel_payment_request = CancelPaymentRequest(reason="requested_by_customer")

        # Call the API method
        payment = self.api.cancel_payment("pay_123456789", cancel_payment_request)

        # Verify the response
        self.assertEqual(payment.id, "pay_123456789")
        self.assertEqual(payment.status, "canceled")

        # Verify the API call
        mock_call_api.assert_called_once()
        args, kwargs = mock_call_api.call_args
        self.assertEqual(args[0], "/payments/pay_123456789/cancel")
        self.assertEqual(args[1], "POST")
        self.assertEqual(kwargs["body"], cancel_payment_request)

    @patch.object(ApiClient, "call_api")
    def test_refund_payment(self, mock_call_api):
        """Test refund_payment method."""
        # Mock the API response
        refunded_payment_data = self.payment_data.copy()
        refunded_payment_data["status"] = "refunded"
        mock_call_api.return_value = refunded_payment_data

        # Create a refund payment request
        refund_payment_request = RefundPaymentRequest(
            amount=1000, reason="requested_by_customer"
        )

        # Call the API method
        payment = self.api.refund_payment("pay_123456789", refund_payment_request)

        # Verify the response
        self.assertEqual(payment.id, "pay_123456789")
        self.assertEqual(payment.status, "refunded")

        # Verify the API call
        mock_call_api.assert_called_once()
        args, kwargs = mock_call_api.call_args
        self.assertEqual(args[0], "/payments/pay_123456789/refund")
        self.assertEqual(args[1], "POST")
        self.assertEqual(kwargs["body"], refund_payment_request)

    @patch.object(ApiClient, "call_api")
    def test_unauthorized_error(self, mock_call_api):
        """Test API call with unauthorized error."""
        # Mock the API response to raise an UnauthorizedException
        mock_call_api.side_effect = UnauthorizedException(
            status=401, reason="Unauthorized", http_resp=MagicMock()
        )

        # Call the API method and expect an exception
        with self.assertRaises(UnauthorizedException):
            self.api.get_payment("pay_123456789")

        # Verify the API call
        mock_call_api.assert_called_once()

    @patch.object(ApiClient, "call_api")
    def test_api_exception(self, mock_call_api):
        """Test API call with generic API exception."""
        # Mock the API response to raise an ApiException
        mock_call_api.side_effect = ApiException(
            status=500, reason="Internal Server Error", http_resp=MagicMock()
        )

        # Call the API method and expect an exception
        with self.assertRaises(ApiException):
            self.api.get_payment("pay_123456789")

        # Verify the API call
        mock_call_api.assert_called_once()


if __name__ == "__main__":
    unittest.main()
