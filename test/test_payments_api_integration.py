import unittest
from unittest.mock import patch, MagicMock

import Monei
from Monei.monei_client import MoneiClient
from Monei.exceptions import ApiException
from Monei.model.create_payment_request import CreatePaymentRequest
from Monei.model.confirm_payment_request import ConfirmPaymentRequest
from Monei.model.capture_payment_request import CapturePaymentRequest
from Monei.model.cancel_payment_request import CancelPaymentRequest
from Monei.model.refund_payment_request import RefundPaymentRequest
from Monei.model.recurring_payment_request import RecurringPaymentRequest
from Monei.model.send_payment_link_request import SendPaymentLinkRequest
from Monei.model.send_payment_receipt_request import SendPaymentReceiptRequest
from Monei.model.send_payment_request_request import SendPaymentRequestRequest
from Monei.model.payment import Payment
from Monei.model.payment_status import PaymentStatus


class TestPaymentsApiIntegration(unittest.TestCase):
    """PaymentsApi integration test stubs"""

    def setUp(self):
        """Set up test fixtures, if any."""
        self.api_key = "test_api_key_12345"
        self.client = MoneiClient(api_key=self.api_key)
        self.payment_id = "pay_123456789"

    def tearDown(self):
        """Tear down test fixtures, if any."""
        pass

    @patch("Monei.api.payments_api.PaymentsApi.create")
    def test_create_payment(self, mock_create):
        """Test creating a payment."""
        # Setup mock response
        mock_payment = MagicMock()
        mock_payment.id = self.payment_id
        mock_payment.amount = 1000
        mock_payment.currency = "EUR"
        mock_payment.status = PaymentStatus("PENDING")
        mock_create.return_value = mock_payment

        # Create payment request
        payment_request = {
            "amount": 1000,
            "currency": "EUR",
            "orderId": "order_123",
            "description": "Test payment",
            "customer": {"email": "customer@example.com", "name": "John Doe"},
        }

        # Call the API
        result = self.client.payments.create(payment_request)

        # Verify the result
        self.assertEqual(result.id, self.payment_id)
        self.assertEqual(result.amount, 1000)
        self.assertEqual(result.currency, "EUR")
        self.assertEqual(result.status, PaymentStatus("PENDING"))

        # Verify the mock was called with the correct arguments
        mock_create.assert_called_once()

    @patch("Monei.api.payments_api.PaymentsApi.get")
    def test_get_payment(self, mock_get):
        """Test getting a payment by ID."""
        # Setup mock response
        mock_payment = MagicMock()
        mock_payment.id = self.payment_id
        mock_payment.amount = 1000
        mock_payment.currency = "EUR"
        mock_payment.status = PaymentStatus("SUCCEEDED")
        mock_get.return_value = mock_payment

        # Call the API
        result = self.client.payments.get(self.payment_id)

        # Verify the result
        self.assertEqual(result.id, self.payment_id)
        self.assertEqual(result.amount, 1000)
        self.assertEqual(result.currency, "EUR")
        self.assertEqual(result.status, PaymentStatus("SUCCEEDED"))

        # Verify the mock was called with the correct arguments
        mock_get.assert_called_once_with(self.payment_id)

    @patch("Monei.api.payments_api.PaymentsApi.confirm")
    def test_confirm_payment(self, mock_confirm):
        """Test confirming a payment."""
        # Setup mock response
        mock_payment = MagicMock()
        mock_payment.id = self.payment_id
        mock_payment.amount = 1000
        mock_payment.currency = "EUR"
        mock_payment.status = PaymentStatus("SUCCEEDED")
        mock_confirm.return_value = mock_payment

        # Create confirm request
        confirm_request = {
            "paymentMethod": {
                "type": "CARD",
                "card": {
                    "number": "4242424242424242",
                    "expiryMonth": 12,
                    "expiryYear": 2025,
                    "cvc": "123",
                },
            }
        }

        # Call the API
        result = self.client.payments.confirm(self.payment_id, confirm_request)

        # Verify the result
        self.assertEqual(result.id, self.payment_id)
        self.assertEqual(result.amount, 1000)
        self.assertEqual(result.currency, "EUR")
        self.assertEqual(result.status, PaymentStatus("SUCCEEDED"))

        # Verify the mock was called with the correct arguments
        mock_confirm.assert_called_once()

    @patch("Monei.api.payments_api.PaymentsApi.capture")
    def test_capture_payment(self, mock_capture):
        """Test capturing a payment."""
        # Setup mock response
        mock_payment = MagicMock()
        mock_payment.id = self.payment_id
        mock_payment.amount = 1000
        mock_payment.currency = "EUR"
        mock_payment.status = PaymentStatus("SUCCEEDED")
        mock_capture.return_value = mock_payment

        # Create capture request
        capture_request = {"amount": 1000}

        # Call the API
        result = self.client.payments.capture(self.payment_id, capture_request)

        # Verify the result
        self.assertEqual(result.id, self.payment_id)
        self.assertEqual(result.amount, 1000)
        self.assertEqual(result.currency, "EUR")
        self.assertEqual(result.status, PaymentStatus("SUCCEEDED"))

        # Verify the mock was called with the correct arguments
        mock_capture.assert_called_once()

    @patch("Monei.api.payments_api.PaymentsApi.cancel")
    def test_cancel_payment(self, mock_cancel):
        """Test cancelling a payment."""
        # Setup mock response
        mock_payment = MagicMock()
        mock_payment.id = self.payment_id
        mock_payment.amount = 1000
        mock_payment.currency = "EUR"
        mock_payment.status = PaymentStatus("CANCELED")
        mock_cancel.return_value = mock_payment

        # Create cancel request
        cancel_request = {"reason": "CUSTOMER_CANCEL"}

        # Call the API
        result = self.client.payments.cancel(self.payment_id, cancel_request)

        # Verify the result
        self.assertEqual(result.id, self.payment_id)
        self.assertEqual(result.amount, 1000)
        self.assertEqual(result.currency, "EUR")
        self.assertEqual(result.status, PaymentStatus("CANCELED"))

        # Verify the mock was called with the correct arguments
        mock_cancel.assert_called_once()

    @patch("Monei.api.payments_api.PaymentsApi.refund")
    def test_refund_payment(self, mock_refund):
        """Test refunding a payment."""
        # Setup mock response
        mock_payment = MagicMock()
        mock_payment.id = self.payment_id
        mock_payment.amount = 1000
        mock_payment.currency = "EUR"
        mock_payment.status = PaymentStatus("SUCCEEDED")
        mock_refund.return_value = mock_payment

        # Create refund request
        refund_request = {"amount": 500, "reason": "CUSTOMER_REQUEST"}

        # Call the API
        result = self.client.payments.refund(self.payment_id, refund_request)

        # Verify the result
        self.assertEqual(result.id, self.payment_id)
        self.assertEqual(result.amount, 1000)
        self.assertEqual(result.currency, "EUR")
        self.assertEqual(result.status, PaymentStatus("SUCCEEDED"))

        # Verify the mock was called with the correct arguments
        mock_refund.assert_called_once()

    @patch("Monei.api.payments_api.PaymentsApi.recurring")
    def test_recurring_payment(self, mock_recurring):
        """Test creating a recurring payment."""
        # Setup mock response
        mock_payment = MagicMock()
        mock_payment.id = self.payment_id
        mock_payment.amount = 1000
        mock_payment.currency = "EUR"
        mock_payment.status = PaymentStatus("SUCCEEDED")
        mock_recurring.return_value = mock_payment

        # Create recurring request
        recurring_request = {
            "amount": 1000,
            "currency": "EUR",
            "orderId": "order_123",
            "description": "Recurring payment",
            "paymentMethodId": "pm_123456789",
        }

        # Call the API
        sequence_id = "seq_123456789"
        result = self.client.payments.recurring(sequence_id, recurring_request)

        # Verify the result
        self.assertEqual(result.id, self.payment_id)
        self.assertEqual(result.amount, 1000)
        self.assertEqual(result.currency, "EUR")
        self.assertEqual(result.status, PaymentStatus("SUCCEEDED"))

        # Verify the mock was called with the correct arguments
        mock_recurring.assert_called_once()

    @patch("Monei.api.payments_api.PaymentsApi.send_link")
    def test_send_payment_link(self, mock_send_link):
        """Test sending a payment link."""
        # Setup mock response
        mock_response = MagicMock()
        mock_response.success = True
        mock_send_link.return_value = mock_response

        # Create send link request
        send_link_request = {
            "customerEmail": "customer@example.com",
            "customerPhone": "+34600000000",
        }

        # Call the API
        result = self.client.payments.send_link(self.payment_id, send_link_request)

        # Verify the result
        self.assertTrue(result.success)

        # Verify the mock was called with the correct arguments
        mock_send_link.assert_called_once()

    @patch("Monei.api.payments_api.PaymentsApi.send_receipt")
    def test_send_payment_receipt(self, mock_send_receipt):
        """Test sending a payment receipt."""
        # Setup mock response
        mock_response = MagicMock()
        mock_response.success = True
        mock_send_receipt.return_value = mock_response

        # Create send receipt request
        send_receipt_request = {"customerEmail": "customer@example.com"}

        # Call the API
        result = self.client.payments.send_receipt(self.payment_id, send_receipt_request)

        # Verify the result
        self.assertTrue(result.success)

        # Verify the mock was called with the correct arguments
        mock_send_receipt.assert_called_once()

    @patch("Monei.api.payments_api.PaymentsApi.send_request")
    def test_send_payment_request(self, mock_send_request):
        """Test sending a payment request."""
        # Setup mock response
        mock_payment = MagicMock()
        mock_payment.id = self.payment_id
        mock_payment.amount = 1000
        mock_payment.currency = "EUR"
        mock_payment.status = PaymentStatus("PENDING")
        mock_send_request.return_value = mock_payment

        # Create send request request
        send_request_request = {"phoneNumber": "+34600000000"}

        # Call the API
        result = self.client.payments.send_request(self.payment_id, send_request_request)

        # Verify the result
        self.assertEqual(result.id, self.payment_id)
        self.assertEqual(result.amount, 1000)
        self.assertEqual(result.currency, "EUR")
        self.assertEqual(result.status, PaymentStatus("PENDING"))

        # Verify the mock was called with the correct arguments
        mock_send_request.assert_called_once()


if __name__ == "__main__":
    unittest.main()
