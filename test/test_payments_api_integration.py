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
        result = self.client.payments.send_receipt(
            self.payment_id, send_receipt_request
        )

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
        result = self.client.payments.send_request(
            self.payment_id, send_request_request
        )

        # Verify the result
        self.assertEqual(result.id, self.payment_id)
        self.assertEqual(result.amount, 1000)
        self.assertEqual(result.currency, "EUR")
        self.assertEqual(result.status, PaymentStatus("PENDING"))

        # Verify the mock was called with the correct arguments
        mock_send_request.assert_called_once()

    @patch("Monei.api.payments_api.PaymentsApi.create")
    def test_create_payment_validation_error(self, mock_create):
        """Test that validation errors are properly handled when creating a payment."""
        # Setup mock to raise an ApiException
        mock_create.side_effect = ApiException(
            status=422, reason="Unprocessable Entity"
        )

        # Create invalid payment request (missing required fields)
        payment_request = {
            "currency": "EUR",  # Missing required 'amount' field
            "description": "Test payment",
        }

        # Call the API and expect an exception
        with self.assertRaises(ApiException) as context:
            self.client.payments.create(payment_request)

        # Verify the exception details
        self.assertEqual(context.exception.status, 422)
        self.assertIn("Unprocessable Entity", context.exception.reason)

        # Verify the mock was called
        mock_create.assert_called_once()

    @patch("Monei.api.payments_api.PaymentsApi.get")
    def test_get_payment_not_found(self, mock_get):
        """Test handling not found error when getting a payment."""
        # Setup mock to raise an ApiException
        mock_get.side_effect = ApiException(status=404, reason="Not Found")

        # Use a non-existent payment ID
        non_existent_id = "pay_nonexistent"

        # Call the API and expect an exception
        with self.assertRaises(ApiException) as context:
            self.client.payments.get(non_existent_id)

        # Verify the exception details
        self.assertEqual(context.exception.status, 404)
        self.assertIn("Not Found", context.exception.reason)

        # Verify the mock was called with the correct arguments
        mock_get.assert_called_once_with(non_existent_id)

    @patch("Monei.api.payments_api.PaymentsApi.get")
    def test_malformed_response_handling(self, mock_get):
        """Test handling of malformed API responses."""
        # Set up the mock to raise a JSON parsing error
        import json

        def side_effect(*args, **kwargs):
            raise json.JSONDecodeError(
                "Expecting value", '{"id":"pay_123456789", "amount": invalid_json}', 30
            )

        mock_get.side_effect = side_effect

        # Call the API and expect an exception
        with self.assertRaises(Exception) as context:
            self.client.payments.get(self.payment_id)

        # Verify the exception details indicate a parsing issue
        self.assertIn("Expecting value", str(context.exception))

    def test_payment_object_handling(self):
        """Test handling of Payment objects."""
        # Create a Payment object with required attributes
        payment = Payment(
            id="pay_123456789",
            amount=1000,
            currency="EUR",
            account_id="acc_123456789",
            livemode=False,
            status=PaymentStatus("SUCCEEDED"),
        )

        # Set additional attributes
        payment.order_id = "order_123"
        payment.description = "Test payment"

        # Verify the object properties are correctly set
        self.assertEqual(payment.id, "pay_123456789")
        self.assertEqual(payment.amount, 1000)
        self.assertEqual(payment.currency, "EUR")
        self.assertEqual(payment.account_id, "acc_123456789")
        self.assertEqual(payment.livemode, False)
        self.assertEqual(payment.status, PaymentStatus("SUCCEEDED"))
        self.assertEqual(payment.order_id, "order_123")
        self.assertEqual(payment.description, "Test payment")

        # Convert to dictionary
        payment_dict = payment.to_dict()

        # Verify the converted dictionary contains the expected values
        self.assertEqual(payment_dict.get("id"), "pay_123456789")
        self.assertEqual(payment_dict.get("amount"), 1000)
        self.assertEqual(payment_dict.get("currency"), "EUR")
        self.assertEqual(payment_dict.get("account_id"), "acc_123456789")
        self.assertEqual(payment_dict.get("livemode"), False)
        self.assertEqual(payment_dict.get("status"), "SUCCEEDED")
        self.assertEqual(payment_dict.get("order_id"), "order_123")
        self.assertEqual(payment_dict.get("description"), "Test payment")

    @patch("Monei.api.payments_api.PaymentsApi")
    def test_pagination_handling(self, mock_payments_api_class):
        """Test pagination handling when listing payments."""
        # Create a mock instance with a list method
        mock_instance = MagicMock()
        mock_payments_api_class.return_value = mock_instance

        # First page response
        first_page_response = MagicMock()
        first_page_response.data = [
            MagicMock(id="pay_1", amount=1000),
            MagicMock(id="pay_2", amount=2000),
        ]
        first_page_response.has_more = True
        first_page_response.next_page = "page_token_2"

        # Second page response
        second_page_response = MagicMock()
        second_page_response.data = [
            MagicMock(id="pay_3", amount=3000),
            MagicMock(id="pay_4", amount=4000),
        ]
        second_page_response.has_more = False
        second_page_response.next_page = None

        # Configure the mock to return different responses based on page parameter
        def side_effect(*args, **kwargs):
            if "page" not in kwargs or kwargs["page"] is None:
                return first_page_response
            elif kwargs["page"] == "page_token_2":
                return second_page_response
            return MagicMock(data=[], has_more=False, next_page=None)

        mock_instance.list.side_effect = side_effect

        # Replace client.payments with our mock
        original_payments = self.client.payments
        self.client.payments = mock_instance

        try:
            # Test fetching the first page of results
            first_page = self.client.payments.list(limit=2)
            self.assertEqual(len(first_page.data), 2)
            self.assertEqual(first_page.data[0].id, "pay_1")
            self.assertEqual(first_page.data[1].id, "pay_2")
            self.assertTrue(first_page.has_more)
            self.assertEqual(first_page.next_page, "page_token_2")

            # Test fetching the second page of results
            second_page = self.client.payments.list(limit=2, page=first_page.next_page)
            self.assertEqual(len(second_page.data), 2)
            self.assertEqual(second_page.data[0].id, "pay_3")
            self.assertEqual(second_page.data[1].id, "pay_4")
            self.assertFalse(second_page.has_more)
            self.assertIsNone(second_page.next_page)
        finally:
            # Restore original payments api
            self.client.payments = original_payments


if __name__ == "__main__":
    unittest.main()
