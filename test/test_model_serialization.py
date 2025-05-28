"""
MONEI API v1 - Model Serialization Tests

This module tests the serialization and deserialization of complex model objects
in the MONEI Python SDK.
"""

import unittest
import json
from datetime import datetime

from Monei.model.payment import Payment
from Monei.model.payment_customer import PaymentCustomer
from Monei.model.payment_billing_details import PaymentBillingDetails
from Monei.model.address import Address
from Monei.model.payment_status import PaymentStatus
from Monei.model.payment_payment_method import PaymentPaymentMethod
from Monei.model.payment_payment_method_card import PaymentPaymentMethodCard


class TestModelSerialization(unittest.TestCase):
    """Tests for model serialization and deserialization"""

    def setUp(self):
        """Set up test fixtures, if any."""
        # Create a sample payment JSON that would come from the API
        self.payment_json = {
            "id": "pay_123456789",
            "amount": 1000,
            "currency": "EUR",
            "accountId": "acc_123456789",
            "livemode": False,
            "description": "Test payment",
            "status": {
                "value": "SUCCEEDED"
            },  # Use a dict format that will convert to PaymentStatus
            "orderId": "order_123",
            "customer": {
                "email": "customer@example.com",
                "name": "John Doe",
                "phone": "+1234567890",
            },
            "billingDetails": {
                "address": {
                    "city": "Madrid",
                    "country": "ES",
                    "line1": "Calle Mayor 1",
                    "line2": "Floor 2",
                    "zip": "28001",
                    "state": "Madrid",
                }
            },
            "paymentMethod": {
                "type": "card",
                "card": {
                    "brand": "visa",
                    "country": "ES",
                    "expiration": 1767225600,
                    "last4": "4242",
                    "type": "credit",
                },
            },
            # Using integer timestamps instead of string dates
            "createdAt": int(datetime(2023, 1, 1, 12, 0, 0).timestamp()),
            "updatedAt": int(datetime(2023, 1, 1, 12, 5, 0).timestamp()),
        }

    def tearDown(self):
        """Tear down test fixtures, if any."""
        pass

    def test_complex_object_deserialization(self):
        """Test deserialization of complex nested objects."""
        # Convert JSON string to Payment object with PaymentStatus directly instantiated
        payment_data = self.payment_json.copy()
        # Create a proper PaymentStatus instance for the test
        payment_data["status"] = PaymentStatus("SUCCEEDED")

        # Remove timestamp fields if they're causing issues
        if "createdAt" in payment_data:
            payment_data["createdAt"] = int(datetime(2023, 1, 1, 12, 0, 0).timestamp())
        if "updatedAt" in payment_data:
            payment_data["updatedAt"] = int(datetime(2023, 1, 1, 12, 5, 0).timestamp())

        # Create the Payment object
        payment = Payment(**payment_data, _spec_property_naming=True)

        # Verify top-level properties
        self.assertEqual(payment.id, "pay_123456789")
        self.assertEqual(payment.amount, 1000)
        self.assertEqual(payment.currency, "EUR")
        self.assertEqual(payment.account_id, "acc_123456789")
        self.assertEqual(payment.livemode, False)
        self.assertEqual(payment.description, "Test payment")
        self.assertEqual(payment.status.value, "SUCCEEDED")
        self.assertEqual(payment.order_id, "order_123")

        # Verify nested customer object
        self.assertIsInstance(payment.customer, PaymentCustomer)
        self.assertEqual(payment.customer.email, "customer@example.com")
        self.assertEqual(payment.customer.name, "John Doe")
        self.assertEqual(payment.customer.phone, "+1234567890")

        # Verify nested billing details and address
        self.assertIsInstance(payment.billing_details, PaymentBillingDetails)
        self.assertIsInstance(payment.billing_details.address, Address)
        self.assertEqual(payment.billing_details.address.city, "Madrid")
        self.assertEqual(payment.billing_details.address.country, "ES")
        self.assertEqual(payment.billing_details.address.line1, "Calle Mayor 1")
        self.assertEqual(payment.billing_details.address.zip, "28001")

        # Verify nested payment method
        self.assertIsInstance(payment.payment_method, PaymentPaymentMethod)
        self.assertEqual(payment.payment_method.type, "card")
        self.assertIsInstance(payment.payment_method.card, PaymentPaymentMethodCard)
        self.assertEqual(payment.payment_method.card.brand, "visa")
        self.assertEqual(payment.payment_method.card.last4, "4242")
        self.assertEqual(payment.payment_method.card.type, "credit")
        self.assertEqual(payment.payment_method.card.expiration, 1767225600)

    def test_complex_object_serialization(self):
        """Test serialization of complex nested objects."""
        # Create a complex Payment object programmatically
        payment = Payment(
            id="pay_987654321",
            amount=2000,
            currency="USD",
            account_id="acc_987654321",
            livemode=True,
            description="Test serialization",
            status=PaymentStatus("PENDING"),
            order_id="order_456",
        )

        # Add customer
        payment.customer = PaymentCustomer(
            email="test@example.com", name="Jane Smith", phone="+9876543210"
        )

        # Add billing details with address
        address = Address(
            city="New York", country="US", line1="123 Broadway", postal_code="10001"
        )
        payment.billing_details = PaymentBillingDetails(address=address)

        # Add payment method
        card = PaymentPaymentMethodCard(
            brand="mastercard", last4="9876", expiry_month=6, expiry_year=2024
        )
        payment.payment_method = PaymentPaymentMethod(type="card", card=card)

        # Serialize to dictionary
        serialized = payment.to_dict()

        # Verify top-level properties
        self.assertEqual(serialized["id"], "pay_987654321")
        self.assertEqual(serialized["amount"], 2000)
        self.assertEqual(serialized["currency"], "USD")
        self.assertEqual(serialized["account_id"], "acc_987654321")
        self.assertEqual(serialized["livemode"], True)
        self.assertEqual(serialized["description"], "Test serialization")
        self.assertEqual(serialized["status"], "PENDING")
        self.assertEqual(serialized["order_id"], "order_456")

        # Verify nested customer object
        self.assertEqual(serialized["customer"]["email"], "test@example.com")
        self.assertEqual(serialized["customer"]["name"], "Jane Smith")
        self.assertEqual(serialized["customer"]["phone"], "+9876543210")

        # Verify nested billing details and address
        self.assertEqual(serialized["billing_details"]["address"]["city"], "New York")
        self.assertEqual(serialized["billing_details"]["address"]["country"], "US")
        self.assertEqual(
            serialized["billing_details"]["address"]["line1"], "123 Broadway"
        )
        self.assertEqual(
            serialized["billing_details"]["address"]["postal_code"], "10001"
        )

        # Verify nested payment method
        self.assertEqual(serialized["payment_method"]["type"], "card")
        self.assertEqual(serialized["payment_method"]["card"]["brand"], "mastercard")
        self.assertEqual(serialized["payment_method"]["card"]["last4"], "9876")
        self.assertEqual(serialized["payment_method"]["card"]["expiry_month"], 6)
        self.assertEqual(serialized["payment_method"]["card"]["expiry_year"], 2024)


if __name__ == "__main__":
    unittest.main()
