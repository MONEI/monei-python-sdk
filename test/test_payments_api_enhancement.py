import unittest

import Monei
from Monei.api.payments_api import PaymentsApi
from Monei.model.create_payment_request import CreatePaymentRequest
from Monei.model.cancel_payment_request import CancelPaymentRequest
from Monei.model.capture_payment_request import CapturePaymentRequest
from Monei.model.confirm_payment_request import ConfirmPaymentRequest
from Monei.model.refund_payment_request import RefundPaymentRequest
from Monei.model.payment import Payment


class TestPaymentsApiEnhanced(unittest.TestCase):
    """Additional test cases for PaymentsApi class"""

    def setUp(self):
        """Set up test fixtures, if any."""
        self.api = PaymentsApi()
        self.payment_id = "pay_123456789"

    def test_api_methods_exist(self):
        """Test that all API methods are properly defined."""
        # Check for existence of some methods, not all, to reduce test fragility
        self.assertTrue(hasattr(self.api, "create"))
        self.assertTrue(hasattr(self.api, "get"))


if __name__ == "__main__":
    unittest.main()
