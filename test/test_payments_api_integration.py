import pytest
from unittest.mock import patch, MagicMock

from Monei.monei_client import MoneiClient
from Monei.api.payments_api import PaymentsApi
from Monei.model.create_payment_request import CreatePaymentRequest
from Monei.model.confirm_payment_request import ConfirmPaymentRequest
from Monei.model.capture_payment_request import CapturePaymentRequest
from Monei.model.refund_payment_request import RefundPaymentRequest
from Monei.model.cancel_payment_request import CancelPaymentRequest
from Monei.model.recurring_payment_request import RecurringPaymentRequest
from Monei.model.send_payment_link_request import SendPaymentLinkRequest
from Monei.model.send_payment_receipt_request import SendPaymentReceiptRequest
from Monei.model.send_payment_request_request import SendPaymentRequestRequest
from Monei.model.payment_status import PaymentStatus
from Monei.model.payment import Payment


@pytest.mark.unit
class TestPaymentsApiIntegration:
    """Integration tests for the Payments API with mocked responses"""

    @pytest.fixture
    def mock_payment_response(self):
        """Fixture for a mock payment response"""
        return {
            "id": "pay_123456789",
            "amount": 1000,
            "currency": "EUR",
            "status": PaymentStatus("PENDING"),
            "description": "Test payment",
            "created": "2023-01-01T12:00:00Z",
            "updated": "2023-01-01T12:00:00Z",
        }

    @pytest.fixture
    def mock_client(self):
        """Fixture for creating a mock client"""
        return MoneiClient(api_key="test_api_key")

    @patch.object(PaymentsApi, "create")
    def test_create_payment(self, mock_create, mock_client, mock_payment_response):
        """Test creating a payment"""
        mock_create.return_value = mock_payment_response

        payment_request = CreatePaymentRequest(
            amount=1000, currency="EUR", description="Test payment"  # 10.00 in cents
        )

        result = mock_client.Payments.create(create_payment_request=payment_request)

        assert result["id"] == "pay_123456789"
        assert result["amount"] == 1000
        assert result["currency"] == "EUR"
        assert result["status"] == PaymentStatus("PENDING")
        mock_create.assert_called_once_with(create_payment_request=payment_request)

    @patch.object(PaymentsApi, "get")
    def test_get_payment(self, mock_get, mock_client, mock_payment_response):
        """Test retrieving a payment"""
        mock_get.return_value = mock_payment_response

        result = mock_client.Payments.get(payment_id="pay_123456789")

        assert result["id"] == "pay_123456789"
        assert result["status"] == PaymentStatus("PENDING")
        mock_get.assert_called_once_with(payment_id="pay_123456789")

    @patch.object(PaymentsApi, "confirm")
    def test_confirm_payment(self, mock_confirm, mock_client):
        """Test confirming a payment"""
        confirmed_payment = {
            "id": "pay_123456789",
            "amount": 1000,
            "currency": "EUR",
            "status": PaymentStatus("CONFIRMED"),
            "description": "Test payment",
            "created": "2023-01-01T12:00:00Z",
            "updated": "2023-01-01T12:01:00Z",
        }
        mock_confirm.return_value = confirmed_payment

        confirm_request = ConfirmPaymentRequest()
        result = mock_client.Payments.confirm(
            payment_id="pay_123456789", confirm_payment_request=confirm_request
        )

        assert result["id"] == "pay_123456789"
        assert result["status"] == PaymentStatus("CONFIRMED")
        mock_confirm.assert_called_once_with(
            payment_id="pay_123456789", confirm_payment_request=confirm_request
        )

    @patch.object(PaymentsApi, "capture")
    def test_capture_payment(self, mock_capture, mock_client):
        """Test capturing a payment"""
        captured_payment = {
            "id": "pay_123456789",
            "amount": 1000,
            "currency": "EUR",
            "status": PaymentStatus("COMPLETED"),
            "description": "Test payment",
            "created": "2023-01-01T12:00:00Z",
            "updated": "2023-01-01T12:02:00Z",
        }
        mock_capture.return_value = captured_payment

        capture_request = CapturePaymentRequest(amount=1000)
        result = mock_client.Payments.capture(
            payment_id="pay_123456789", capture_payment_request=capture_request
        )

        assert result["id"] == "pay_123456789"
        assert result["status"] == PaymentStatus("COMPLETED")
        mock_capture.assert_called_once_with(
            payment_id="pay_123456789", capture_payment_request=capture_request
        )

    @patch.object(PaymentsApi, "refund")
    def test_refund_payment(self, mock_refund, mock_client):
        """Test refunding a payment"""
        refunded_payment = {
            "id": "pay_123456789",
            "amount": 1000,
            "currency": "EUR",
            "status": PaymentStatus("REFUNDED"),
            "description": "Test payment",
            "created": "2023-01-01T12:00:00Z",
            "updated": "2023-01-01T12:03:00Z",
        }
        mock_refund.return_value = refunded_payment

        refund_request = RefundPaymentRequest(amount=1000)
        result = mock_client.Payments.refund(
            payment_id="pay_123456789", refund_payment_request=refund_request
        )

        assert result["id"] == "pay_123456789"
        assert result["status"] == PaymentStatus("REFUNDED")
        mock_refund.assert_called_once_with(
            payment_id="pay_123456789", refund_payment_request=refund_request
        )

    @patch.object(PaymentsApi, "cancel")
    def test_cancel_payment(self, mock_cancel, mock_client):
        """Test canceling a payment"""
        canceled_payment = {
            "id": "pay_123456789",
            "amount": 1000,
            "currency": "EUR",
            "status": PaymentStatus("CANCELED"),
            "description": "Test payment",
            "created": "2023-01-01T12:00:00Z",
            "updated": "2023-01-01T12:04:00Z",
        }
        mock_cancel.return_value = canceled_payment

        cancel_request = CancelPaymentRequest()
        result = mock_client.Payments.cancel(
            payment_id="pay_123456789", cancel_payment_request=cancel_request
        )

        assert result["id"] == "pay_123456789"
        assert result["status"] == PaymentStatus("CANCELED")
        mock_cancel.assert_called_once_with(
            payment_id="pay_123456789", cancel_payment_request=cancel_request
        )

    @patch.object(PaymentsApi, "recurring")
    def test_recurring_payment(self, mock_recurring, mock_client):
        """Test creating a recurring payment"""
        recurring_payment = {
            "id": "pay_987654321",
            "amount": 1000,
            "currency": "EUR",
            "status": PaymentStatus("PENDING"),
            "description": "Recurring payment",
            "created": "2023-01-02T12:00:00Z",
            "updated": "2023-01-02T12:00:00Z",
        }
        mock_recurring.return_value = recurring_payment

        recurring_request = RecurringPaymentRequest(
            amount=1000, currency="EUR", description="Recurring payment", payment_id="pay_123456789"
        )
        result = mock_client.Payments.recurring(recurring_payment_request=recurring_request)

        assert result["id"] == "pay_987654321"
        assert result["description"] == "Recurring payment"
        mock_recurring.assert_called_once_with(recurring_payment_request=recurring_request)

    @patch.object(PaymentsApi, "send_link")
    def test_send_payment_link(self, mock_send_link, mock_client):
        """Test sending a payment link"""
        success_response = {"success": True}
        mock_send_link.return_value = success_response

        link_request = SendPaymentLinkRequest(
            payment_id="pay_123456789", email="customer@example.com"
        )
        result = mock_client.Payments.send_link(send_payment_link_request=link_request)

        assert result["success"] is True
        mock_send_link.assert_called_once_with(send_payment_link_request=link_request)

    @patch.object(PaymentsApi, "send_receipt")
    def test_send_payment_receipt(self, mock_send_receipt, mock_client):
        """Test sending a payment receipt"""
        success_response = {"success": True}
        mock_send_receipt.return_value = success_response

        receipt_request = SendPaymentReceiptRequest(
            payment_id="pay_123456789", email="customer@example.com"
        )
        result = mock_client.Payments.send_receipt(send_payment_receipt_request=receipt_request)

        assert result["success"] is True
        mock_send_receipt.assert_called_once_with(send_payment_receipt_request=receipt_request)

    @patch.object(PaymentsApi, "send_request")
    def test_send_payment_request(self, mock_send_request, mock_client):
        """Test sending a payment request"""
        success_response = {"success": True}
        mock_send_request.return_value = success_response

        request_request = SendPaymentRequestRequest(
            payment_id="pay_123456789", email="customer@example.com"
        )
        result = mock_client.Payments.send_request(send_payment_request_request=request_request)

        assert result["success"] is True
        mock_send_request.assert_called_once_with(send_payment_request_request=request_request)
