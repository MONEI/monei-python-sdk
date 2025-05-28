import unittest

from Monei.model.payment import Payment
from Monei.model.payment_status import PaymentStatus
from Monei.model.payment_payment_method import PaymentPaymentMethod
from Monei.model.payment_payment_method_card import PaymentPaymentMethodCard
from Monei.model.payment_customer import PaymentCustomer
from Monei.model.payment_billing_details import PaymentBillingDetails
from Monei.model.address import Address
from Monei.model.create_payment_request import CreatePaymentRequest
from Monei.model.subscription import Subscription
from Monei.model.subscription_status import SubscriptionStatus
from Monei.model.subscription_interval import SubscriptionInterval


class TestModelSerializationEnhancement(unittest.TestCase):
    """Enhanced tests for model serialization/deserialization"""

    def test_payment_model_serialization(self):
        """Test Payment model serialization and deserialization."""
        # Create a payment object directly
        payment = Payment(
            id="pay_123456789",
            amount=1000,
            currency="EUR",
            account_id="acc_123456789",
            livemode=False,
            status=PaymentStatus("SUCCEEDED"),
            description="Test payment",
        )

        # Add customer
        payment.customer = PaymentCustomer(
            id="cus_123", email="customer@example.com", name="Test Customer"
        )

        # Add billing details
        address = Address(
            city="Test City", country="US", line1="123 Test St", postal_code="12345"
        )
        payment.billing_details = PaymentBillingDetails(
            name="Test Customer", email="customer@example.com", address=address
        )

        # Add payment method
        payment.payment_method = PaymentPaymentMethod(
            type="CARD", card=PaymentPaymentMethodCard(last4="4242", brand="visa")
        )

        # Test serialization to dict
        serialized = payment.to_dict()

        # Verify serialization of simple fields
        self.assertEqual(serialized["id"], "pay_123456789")
        self.assertEqual(serialized["amount"], 1000)
        self.assertEqual(serialized["currency"], "EUR")
        self.assertEqual(serialized["account_id"], "acc_123456789")
        self.assertEqual(serialized["livemode"], False)
        self.assertEqual(serialized["status"], "SUCCEEDED")

        # Verify nested objects
        self.assertEqual(serialized["customer"]["id"], "cus_123")
        self.assertEqual(serialized["customer"]["email"], "customer@example.com")
        self.assertEqual(serialized["billing_details"]["address"]["city"], "Test City")
        self.assertEqual(serialized["payment_method"]["type"], "CARD")
        self.assertEqual(serialized["payment_method"]["card"]["last4"], "4242")

    def test_create_payment_request_serialization(self):
        """Test CreatePaymentRequest serialization."""
        # Create a request with only required fields
        # Instead of try/except, let's just create the object and see if it works
        # If it fails, the test will fail with the actual error

        # First, let's print the required parameters from the class
        from Monei.model.create_payment_request import CreatePaymentRequest

        print("\nRequired parameters for CreatePaymentRequest:")
        print(CreatePaymentRequest._from_openapi_data.__code__.co_varnames)

        # Now create the request with all required parameters
        request = CreatePaymentRequest(
            amount=1000, currency="EUR", order_id="test-order-123"
        )

        # Test serialization
        serialized = request.to_dict()
        print("\nSerialized dictionary keys:", serialized.keys())
        self.assertIn("amount", serialized)
        self.assertIn("currency", serialized)
        self.assertIn("order_id", serialized)  # Check for order_id instead of orderId

    def test_model_validation(self):
        """Test validation logic in models."""
        # Test with invalid values
        with self.assertRaises(Exception):
            # Try to create with negative amount which should fail
            CreatePaymentRequest(amount=-100, currency="EUR")  # Invalid amount

    def test_subscription_model_serialization(self):
        """Test Subscription model serialization with different status types."""
        # Create a subscription with active status
        sub_active = Subscription(
            id="sub_123",
            amount=1000,
            account_id="acc_123456789",
            livemode=False,
            status=SubscriptionStatus("ACTIVE"),
            interval=SubscriptionInterval("month"),
            interval_count=1,
            currency="EUR",
            description="Active subscription",
        )

        # Create a subscription with paused status
        sub_paused = Subscription(
            id="sub_456",
            amount=2000,
            account_id="acc_987654321",
            livemode=True,
            status=SubscriptionStatus("PAUSED"),
            interval=SubscriptionInterval("year"),
            interval_count=1,
            currency="USD",
            description="Paused subscription",
        )

        # Serialize to dict
        serialized_active = sub_active.to_dict()
        serialized_paused = sub_paused.to_dict()

        # Test serialized data
        self.assertEqual(serialized_active["status"], "ACTIVE")
        self.assertEqual(serialized_active["interval"], "month")
        self.assertEqual(serialized_active["account_id"], "acc_123456789")
        self.assertEqual(serialized_active["livemode"], False)
        self.assertEqual(serialized_paused["status"], "PAUSED")
        self.assertEqual(serialized_paused["interval"], "year")
        self.assertEqual(serialized_paused["account_id"], "acc_987654321")
        self.assertEqual(serialized_paused["livemode"], True)

    def test_model_inheritance(self):
        """Test model inheritance and polymorphism."""
        # Test payment method with card
        card = PaymentPaymentMethodCard(last4="4242", brand="visa")

        card_method = PaymentPaymentMethod(type="CARD", card=card)

        # Test serialization
        serialized = card_method.to_dict()
        self.assertEqual(serialized["type"], "CARD")
        self.assertEqual(serialized["card"]["last4"], "4242")
        self.assertEqual(serialized["card"]["brand"], "visa")


if __name__ == "__main__":
    unittest.main()
