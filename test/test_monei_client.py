import unittest
import json
import hmac
import hashlib
from unittest.mock import patch, MagicMock

import Monei
from Monei.monei_client import MoneiClient, DEFAULT_USER_AGENT
from Monei.exceptions import ApiException
from Monei.api.payments_api import PaymentsApi
from Monei.api.payment_methods_api import PaymentMethodsApi
from Monei.api.subscriptions_api import SubscriptionsApi
from Monei.api.apple_pay_domain_api import ApplePayDomainApi
from Monei.api.bizum_api import BizumApi


class TestMoneiClient(unittest.TestCase):
    """MoneiClient unit test stubs"""

    def setUp(self):
        """Set up test fixtures, if any."""
        self.api_key = "test_api_key_12345"
        self.account_id = "test_account_id_67890"
        self.user_agent = "MONEI/TestPlatform/1.0.0"

    def tearDown(self):
        """Tear down test fixtures, if any."""
        pass

    def test_init_with_api_key_only(self):
        """Test initializing with API key only."""
        client = MoneiClient(api_key=self.api_key)
        self.assertIsInstance(client, MoneiClient)
        self.assertEqual(client.api_key, self.api_key)
        self.assertEqual(client.user_agent, DEFAULT_USER_AGENT)
        self.assertIsNone(client.account_id)

        # Check API instances are initialized
        self.assertIsInstance(client.Payments, PaymentsApi)
        self.assertIsInstance(client.PaymentMethods, PaymentMethodsApi)
        self.assertIsInstance(client.Subscriptions, SubscriptionsApi)
        self.assertIsInstance(client.ApplePayDomain, ApplePayDomainApi)
        self.assertIsInstance(client.Bizum, BizumApi)

        # Check aliases
        self.assertEqual(client.payments, client.Payments)
        self.assertEqual(client.payment_methods, client.PaymentMethods)
        self.assertEqual(client.subscriptions, client.Subscriptions)
        self.assertEqual(client.apple_pay_domain, client.ApplePayDomain)
        self.assertEqual(client.bizum, client.Bizum)

    def test_init_with_account_id_and_user_agent(self):
        """Test initializing with API key, account ID, and user agent."""
        client = MoneiClient(
            api_key=self.api_key, account_id=self.account_id, user_agent=self.user_agent
        )
        self.assertIsInstance(client, MoneiClient)
        self.assertEqual(client.api_key, self.api_key)
        self.assertEqual(client.account_id, self.account_id)
        self.assertEqual(client.user_agent, self.user_agent)

    def test_init_with_account_id_without_user_agent(self):
        """Test initializing with account ID but without user agent should raise an exception."""
        with self.assertRaises(ApiException) as context:
            MoneiClient(api_key=self.api_key, account_id=self.account_id)
        self.assertEqual(context.exception.status, 400)
        self.assertEqual(
            context.exception.reason, "User-Agent must be provided when using Account ID"
        )

    def test_set_account_id(self):
        """Test setting account ID after initialization."""
        client = MoneiClient(api_key=self.api_key, user_agent=self.user_agent)
        client.set_account_id(self.account_id)
        self.assertEqual(client.account_id, self.account_id)

    def test_set_account_id_without_user_agent(self):
        """Test setting account ID without setting user agent first should raise an exception."""
        client = MoneiClient(api_key=self.api_key)
        with self.assertRaises(ApiException) as context:
            client.set_account_id(self.account_id)
        self.assertEqual(context.exception.status, 400)
        self.assertEqual(context.exception.reason, "User-Agent must be set before using Account ID")

    def test_set_account_id_to_none(self):
        """Test setting account ID to None should remove the header."""
        client = MoneiClient(api_key=self.api_key, user_agent=self.user_agent)
        client.set_account_id(self.account_id)
        self.assertEqual(client.account_id, self.account_id)

        # Now set it to None
        client.set_account_id(None)
        self.assertIsNone(client.account_id)

    def test_set_user_agent(self):
        """Test setting user agent after initialization."""
        client = MoneiClient(api_key=self.api_key)
        client.set_user_agent(self.user_agent)
        self.assertEqual(client.user_agent, self.user_agent)

    def test_verify_signature_valid(self):
        """Test verifying a valid signature."""
        client = MoneiClient(api_key=self.api_key)

        # Create a test payload and signature
        body = '{"id":"test_payment_id","amount":1000,"currency":"EUR","status":"SUCCEEDED"}'
        timestamp = "1602604555"

        # Calculate a valid signature
        signature_payload = f"{timestamp}.{body}"
        hmac_digest = hmac.new(
            bytes(self.api_key, "utf-8"),
            msg=bytes(signature_payload, "utf-8"),
            digestmod=hashlib.sha256,
        ).hexdigest()

        valid_signature = f"t={timestamp},v1={hmac_digest}"

        # Verify the signature
        result = client.verify_signature(body, valid_signature)
        self.assertEqual(result, json.loads(body))

    def test_verify_signature_invalid(self):
        """Test verifying an invalid signature should raise an exception."""
        client = MoneiClient(api_key=self.api_key)

        # Create a test payload and invalid signature
        body = '{"id":"test_payment_id","amount":1000,"currency":"EUR","status":"SUCCEEDED"}'
        timestamp = "1602604555"
        invalid_signature = f"t={timestamp},v1=invalid_signature"

        # Verify the signature should raise an exception
        with self.assertRaises(ApiException) as context:
            client.verify_signature(body, invalid_signature)
        self.assertEqual(context.exception.status, 401)
        self.assertEqual(context.exception.reason, "[401] Signature verification failed")

    def test_verify_signature_malformed(self):
        """Test verifying a malformed signature should raise an exception."""
        client = MoneiClient(api_key=self.api_key)

        # Create a test payload and malformed signature
        body = '{"id":"test_payment_id","amount":1000,"currency":"EUR","status":"SUCCEEDED"}'
        malformed_signature = "malformed_signature"

        # Verify the signature should raise an exception
        with self.assertRaises(Exception):
            client.verify_signature(body, malformed_signature)


if __name__ == "__main__":
    unittest.main()
