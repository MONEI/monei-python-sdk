import unittest
import datetime
from unittest.mock import patch
from Monei.model.payment import Payment
from Monei.model.payment_status import PaymentStatus
from Monei.model.payment_payment_method import PaymentPaymentMethod


class TestPayment(unittest.TestCase):
    """Test case for Payment model"""

    def setUp(self):
        """Set up test fixtures, if any."""
        self.payment_dict = {
            "id": "pay_123456789",
            "amount": 1000,
            "currency": "EUR",
            "status": "succeeded",
            "description": "Test payment",
            "created": "2023-01-01T12:00:00Z",
            "updated": "2023-01-01T12:05:00Z",
            "metadata": {"order_id": "order_123"},
        }

        self.payment = Payment(
            id="pay_123456789",
            amount=1000,
            currency="EUR",
            status="succeeded",
            description="Test payment",
            created=datetime.datetime(
                2023, 1, 1, 12, 0, 0, tzinfo=datetime.timezone.utc
            ),
            updated=datetime.datetime(
                2023, 1, 1, 12, 5, 0, tzinfo=datetime.timezone.utc
            ),
            metadata={"order_id": "order_123"},
        )

    def test_payment_initialization(self):
        """Test Payment initialization."""
        self.assertEqual(self.payment.id, "pay_123456789")
        self.assertEqual(self.payment.amount, 1000)
        self.assertEqual(self.payment.currency, "EUR")
        self.assertEqual(self.payment.status, "succeeded")
        self.assertEqual(self.payment.description, "Test payment")
        self.assertEqual(self.payment.metadata, {"order_id": "order_123"})

    def test_payment_to_dict(self):
        """Test Payment to_dict method."""
        payment_dict = self.payment.to_dict()
        self.assertEqual(payment_dict["id"], "pay_123456789")
        self.assertEqual(payment_dict["amount"], 1000)
        self.assertEqual(payment_dict["currency"], "EUR")
        self.assertEqual(payment_dict["status"], "succeeded")
        self.assertEqual(payment_dict["description"], "Test payment")
        self.assertEqual(payment_dict["metadata"], {"order_id": "order_123"})

    def test_payment_from_dict(self):
        """Test Payment from_dict method."""
        payment = Payment.from_dict(self.payment_dict)
        self.assertEqual(payment.id, "pay_123456789")
        self.assertEqual(payment.amount, 1000)
        self.assertEqual(payment.currency, "EUR")
        self.assertEqual(payment.status, "succeeded")
        self.assertEqual(payment.description, "Test payment")
        self.assertEqual(payment.metadata, {"order_id": "order_123"})

    def test_payment_to_str(self):
        """Test Payment __str__ method."""
        payment_str = str(self.payment)
        self.assertIn("id='pay_123456789'", payment_str)
        self.assertIn("amount=1000", payment_str)
        self.assertIn("currency='EUR'", payment_str)
        self.assertIn("status='succeeded'", payment_str)

    def test_payment_equality(self):
        """Test Payment equality."""
        payment2 = Payment(
            id="pay_123456789",
            amount=1000,
            currency="EUR",
            status="succeeded",
            description="Test payment",
            created=datetime.datetime(
                2023, 1, 1, 12, 0, 0, tzinfo=datetime.timezone.utc
            ),
            updated=datetime.datetime(
                2023, 1, 1, 12, 5, 0, tzinfo=datetime.timezone.utc
            ),
            metadata={"order_id": "order_123"},
        )
        self.assertEqual(self.payment, payment2)

        # Different payment
        payment3 = Payment(
            id="pay_987654321",
            amount=2000,
            currency="USD",
            status="pending",
            description="Another payment",
        )
        self.assertNotEqual(self.payment, payment3)

    def test_payment_with_nested_objects(self):
        """Test Payment with nested objects."""
        payment_method = PaymentPaymentMethod(type="card")
        payment = Payment(
            id="pay_123456789",
            amount=1000,
            currency="EUR",
            status="succeeded",
            payment_method=payment_method,
        )

        payment_dict = payment.to_dict()
        self.assertEqual(payment_dict["payment_method"]["type"], "card")

        # Test deserialization with nested objects
        payment_dict = {
            "id": "pay_123456789",
            "amount": 1000,
            "currency": "EUR",
            "status": "succeeded",
            "payment_method": {"type": "card"},
        }

        payment = Payment.from_dict(payment_dict)
        self.assertEqual(payment.payment_method.type, "card")

    def test_payment_with_enum_values(self):
        """Test Payment with enum values."""
        # Test with enum object
        payment = Payment(
            id="pay_123456789",
            amount=1000,
            currency="EUR",
            status=PaymentStatus("succeeded"),
        )
        self.assertEqual(payment.status, "succeeded")

        # Test with string value
        payment = Payment(
            id="pay_123456789", amount=1000, currency="EUR", status="succeeded"
        )
        self.assertEqual(payment.status, "succeeded")

    def test_payment_with_null_values(self):
        """Test Payment with null values."""
        payment = Payment(
            id="pay_123456789",
            amount=1000,
            currency="EUR",
            status="succeeded",
            description=None,
            metadata=None,
        )

        payment_dict = payment.to_dict()
        self.assertNotIn("description", payment_dict)
        self.assertNotIn("metadata", payment_dict)

    def test_payment_with_empty_values(self):
        """Test Payment with empty values."""
        payment = Payment(
            id="pay_123456789",
            amount=1000,
            currency="EUR",
            status="succeeded",
            description="",
            metadata={},
        )

        payment_dict = payment.to_dict()
        self.assertEqual(payment_dict["description"], "")
        self.assertEqual(payment_dict["metadata"], {})


if __name__ == "__main__":
    unittest.main()
