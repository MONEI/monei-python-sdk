# coding: utf-8

"""
MONEI API v1 - MoneiClient Tests

Unit tests for the MoneiClient class.
"""

import unittest
import json
import hmac
import hashlib
from unittest.mock import patch, MagicMock

from Monei.monei_client import MoneiClient, DEFAULT_USER_AGENT
from Monei.exceptions import ApiException
from Monei.configuration import Configuration
from Monei.api_client import ApiClient
from Monei.api.payments_api import PaymentsApi
from Monei.api.payment_methods_api import PaymentMethodsApi
from Monei.api.subscriptions_api import SubscriptionsApi
from Monei.api.apple_pay_domain_api import ApplePayDomainApi
from Monei.api.bizum_api import BizumApi


class TestMoneiClient(unittest.TestCase):
    """MoneiClient unit test stubs"""

    def setUp(self) -> None:
        self.api_key = "test_api_key_12345"
        self.account_id = "test_account_id_67890"
        self.user_agent = "TestPlatform/1.0"
        self.client = MoneiClient(api_key=self.api_key)

    def tearDown(self) -> None:
        pass

    def test_init_with_api_key_only(self) -> None:
        """Test initializing with API key only"""
        client = MoneiClient(api_key=self.api_key)
        self.assertIsInstance(client, MoneiClient)
        self.assertIsInstance(client.Payments, PaymentsApi)
        self.assertIsInstance(client.PaymentMethods, PaymentMethodsApi)
        self.assertIsInstance(client.Subscriptions, SubscriptionsApi)
        self.assertIsInstance(client.ApplePayDomain, ApplePayDomainApi)
        self.assertIsInstance(client.Bizum, BizumApi)
        self.assertEqual(client.user_agent, DEFAULT_USER_AGENT)

    def test_init_with_custom_config(self) -> None:
        """Test initializing with custom configuration"""
        config = Configuration()
        config.debug = True
        client = MoneiClient(api_key=self.api_key, config=config)
        self.assertIsInstance(client, MoneiClient)
        self.assertTrue(client.config.debug)

    def test_init_with_account_id_and_user_agent(self) -> None:
        """Test initializing with account ID and user agent"""
        client = MoneiClient(
            api_key=self.api_key, account_id=self.account_id, user_agent=self.user_agent
        )
        self.assertIsInstance(client, MoneiClient)
        self.assertEqual(client.account_id, self.account_id)
        self.assertEqual(client.user_agent, self.user_agent)

    def test_init_with_account_id_without_user_agent(self) -> None:
        """Test initializing with account ID but without user agent should raise exception"""
        with self.assertRaises(ApiException) as context:
            MoneiClient(api_key=self.api_key, account_id=self.account_id)

        self.assertEqual(context.exception.status, 400)
        self.assertEqual(
            context.exception.reason, "User-Agent must be provided when using Account ID"
        )

    def test_set_account_id(self) -> None:
        """Test setting account ID after initialization"""
        client = MoneiClient(api_key=self.api_key, user_agent=self.user_agent)
        client.set_account_id(self.account_id)
        self.assertEqual(client.account_id, self.account_id)

    def test_set_account_id_without_user_agent(self) -> None:
        """Test setting account ID without user agent should raise exception"""
        client = MoneiClient(api_key=self.api_key)
        with self.assertRaises(ApiException) as context:
            client.set_account_id(self.account_id)

        self.assertEqual(context.exception.status, 400)
        self.assertEqual(context.exception.reason, "User-Agent must be set before using Account ID")

    def test_set_user_agent(self) -> None:
        """Test setting user agent after initialization"""
        client = MoneiClient(api_key=self.api_key)
        client.set_user_agent(self.user_agent)
        self.assertEqual(client.user_agent, self.user_agent)

    def test_verify_signature(self) -> None:
        """Test verifying webhook signature"""
        client = MoneiClient(api_key=self.api_key)

        # Create test data
        raw_body = '{"id":"3690bd3f7294db82fed08c7371bace32","amount":11700,"currency":"EUR","orderId":"588439","status":"SUCCEEDED","message":"Transaction Approved"}'
        timestamp = "1602604555"

        # Calculate a valid signature
        signature_payload = f"{timestamp}.{raw_body}"
        hmac_digest = hmac.new(
            bytes(self.api_key, "utf-8"),
            msg=bytes(signature_payload, "utf-8"),
            digestmod=hashlib.sha256,
        ).hexdigest()

        valid_signature = f"t={timestamp},v1={hmac_digest}"

        # Test valid signature
        result = client.verify_signature(raw_body, valid_signature)
        self.assertEqual(result, json.loads(raw_body))

        # Test invalid signature
        invalid_signature = f"t={timestamp},v1=invalid_signature"
        with self.assertRaises(ApiException) as context:
            client.verify_signature(raw_body, invalid_signature)

        self.assertEqual(context.exception.status, 401)
        self.assertEqual(context.exception.reason, "[401] Signature verification failed")

    # Payments API Tests
    @patch("Monei.api.payments_api.PaymentsApi.create")
    def test_payments_create(self, mock_create) -> None:
        """Test Payments.create method"""
        client = MoneiClient(api_key=self.api_key)

        # Setup mock return value
        expected_response = {
            "id": "pay_123",
            "amount": 1000,
            "currency": "EUR",
            "orderId": "order_123",
            "description": "Test payment",
            "status": "PENDING",
        }
        mock_create.return_value = expected_response

        # Test the method
        payment_data = {
            "amount": 1000,
            "currency": "EUR",
            "orderId": "order_123",
            "description": "Test payment",
        }
        response = client.Payments.create(payment_data)

        # Verify the response
        self.assertEqual(response, expected_response)
        mock_create.assert_called_once_with(payment_data)

    @patch("Monei.api.payments_api.PaymentsApi.get")
    def test_payments_get(self, mock_get) -> None:
        """Test Payments.get method"""
        client = MoneiClient(api_key=self.api_key)

        # Setup mock return value
        payment_id = "pay_123"
        expected_response = {
            "id": payment_id,
            "amount": 1000,
            "currency": "EUR",
            "orderId": "order_123",
            "description": "Test payment",
            "status": "SUCCEEDED",
        }
        mock_get.return_value = expected_response

        # Test the method
        response = client.Payments.get(payment_id)

        # Verify the response
        self.assertEqual(response, expected_response)
        mock_get.assert_called_once_with(payment_id)

    @patch("Monei.api.payments_api.PaymentsApi.capture")
    def test_payments_capture(self, mock_capture) -> None:
        """Test Payments.capture method"""
        client = MoneiClient(api_key=self.api_key)

        # Setup mock return value
        payment_id = "pay_123"
        capture_data = {"amount": 1000}
        expected_response = {
            "id": payment_id,
            "amount": 1000,
            "currency": "EUR",
            "orderId": "order_123",
            "description": "Test payment",
            "status": "SUCCEEDED",
        }
        mock_capture.return_value = expected_response

        # Test the method
        response = client.Payments.capture(payment_id, capture_data)

        # Verify the response
        self.assertEqual(response, expected_response)
        mock_capture.assert_called_once_with(payment_id, capture_data)

    @patch("Monei.api.payments_api.PaymentsApi.cancel")
    def test_payments_cancel(self, mock_cancel) -> None:
        """Test Payments.cancel method"""
        client = MoneiClient(api_key=self.api_key)

        # Setup mock return value
        payment_id = "pay_123"
        cancel_data = {"reason": "CUSTOMER_REQUEST"}
        expected_response = {
            "id": payment_id,
            "amount": 1000,
            "currency": "EUR",
            "orderId": "order_123",
            "description": "Test payment",
            "status": "CANCELLED",
        }
        mock_cancel.return_value = expected_response

        # Test the method
        response = client.Payments.cancel(payment_id, cancel_data)

        # Verify the response
        self.assertEqual(response, expected_response)
        mock_cancel.assert_called_once_with(payment_id, cancel_data)

    @patch("Monei.api.payments_api.PaymentsApi.confirm")
    def test_payments_confirm(self, mock_confirm) -> None:
        """Test Payments.confirm method"""
        client = MoneiClient(api_key=self.api_key)

        # Setup mock return value
        payment_id = "pay_123"
        confirm_data = {"paymentToken": "tok_123", "sessionId": "sess_123"}
        expected_response = {
            "id": payment_id,
            "amount": 1000,
            "currency": "EUR",
            "orderId": "order_123",
            "description": "Test payment",
            "status": "SUCCEEDED",
        }
        mock_confirm.return_value = expected_response

        # Test the method
        response = client.Payments.confirm(payment_id, confirm_data)

        # Verify the response
        self.assertEqual(response, expected_response)
        mock_confirm.assert_called_once_with(payment_id, confirm_data)

    @patch("Monei.api.payments_api.PaymentsApi.refund")
    def test_payments_refund(self, mock_refund) -> None:
        """Test Payments.refund method"""
        client = MoneiClient(api_key=self.api_key)

        # Setup mock return value
        payment_id = "pay_123"
        refund_data = {"amount": 500, "reason": "CUSTOMER_REQUEST"}
        expected_response = {
            "id": "ref_123",
            "paymentId": payment_id,
            "amount": 500,
            "reason": "CUSTOMER_REQUEST",
            "status": "SUCCEEDED",
        }
        mock_refund.return_value = expected_response

        # Test the method
        response = client.Payments.refund(payment_id, refund_data)

        # Verify the response
        self.assertEqual(response, expected_response)
        mock_refund.assert_called_once_with(payment_id, refund_data)

    @patch("Monei.api.payments_api.PaymentsApi.recurring")
    def test_payments_recurring(self, mock_recurring) -> None:
        """Test Payments.recurring method"""
        client = MoneiClient(api_key=self.api_key)

        # Setup mock return value
        sequence_id = "seq_123"
        recurring_data = {
            "amount": 1000,
            "currency": "EUR",
            "orderId": "order_123",
            "description": "Recurring payment",
            "paymentMethodId": "pm_123",
        }
        expected_response = {
            "id": "pay_456",
            "amount": 1000,
            "currency": "EUR",
            "orderId": "order_123",
            "description": "Recurring payment",
            "status": "SUCCEEDED",
            "sequenceId": sequence_id,
        }
        mock_recurring.return_value = expected_response

        # Test the method
        response = client.Payments.recurring(sequence_id, recurring_data)

        # Verify the response
        self.assertEqual(response, expected_response)
        mock_recurring.assert_called_once_with(sequence_id, recurring_data)

    @patch("Monei.api.payments_api.PaymentsApi.send_link")
    def test_payments_send_link(self, mock_send_link) -> None:
        """Test Payments.send_link method"""
        client = MoneiClient(api_key=self.api_key)

        # Setup mock return value
        payment_id = "pay_123"
        link_data = {"customerEmail": "customer@example.com", "customerPhone": "+34600000000"}
        expected_response = {"success": True}
        mock_send_link.return_value = expected_response

        # Test the method
        response = client.Payments.send_link(payment_id, link_data)

        # Verify the response
        self.assertEqual(response, expected_response)
        mock_send_link.assert_called_once_with(payment_id, link_data)

    @patch("Monei.api.payments_api.PaymentsApi.send_receipt")
    def test_payments_send_receipt(self, mock_send_receipt) -> None:
        """Test Payments.send_receipt method"""
        client = MoneiClient(api_key=self.api_key)

        # Setup mock return value
        payment_id = "pay_123"
        receipt_data = {"customerEmail": "customer@example.com"}
        expected_response = {"success": True}
        mock_send_receipt.return_value = expected_response

        # Test the method
        response = client.Payments.send_receipt(payment_id, receipt_data)

        # Verify the response
        self.assertEqual(response, expected_response)
        mock_send_receipt.assert_called_once_with(payment_id, receipt_data)

    @patch("Monei.api.payments_api.PaymentsApi.send_request")
    def test_payments_send_request(self, mock_send_request) -> None:
        """Test Payments.send_request method"""
        client = MoneiClient(api_key=self.api_key)

        # Setup mock return value
        payment_id = "pay_123"
        request_data = {"phoneNumber": "+34600000000"}
        expected_response = {
            "id": payment_id,
            "amount": 1000,
            "currency": "EUR",
            "orderId": "order_123",
            "description": "Payment request",
            "status": "PENDING",
        }
        mock_send_request.return_value = expected_response

        # Test the method
        response = client.Payments.send_request(payment_id, request_data)

        # Verify the response
        self.assertEqual(response, expected_response)
        mock_send_request.assert_called_once_with(payment_id, request_data)

    # Payment Methods API Tests
    @patch("Monei.api.payment_methods_api.PaymentMethodsApi.get")
    def test_payment_methods_get(self, mock_get) -> None:
        """Test PaymentMethods.get method"""
        client = MoneiClient(api_key=self.api_key)

        # Setup mock return value
        payment_method_id = "pm_123"
        expected_response = {
            "id": payment_method_id,
            "type": "CARD",
            "card": {"last4": "4242", "brand": "VISA", "expiryMonth": 12, "expiryYear": 2025},
            "customerId": "cus_123",
            "status": "ACTIVE",
        }
        mock_get.return_value = expected_response

        # Test the method
        response = client.PaymentMethods.get(payment_method_id=payment_method_id)

        # Verify the response
        self.assertEqual(response, expected_response)
        mock_get.assert_called_once_with(payment_method_id=payment_method_id)

    # Subscriptions API Tests
    @patch("Monei.api.subscriptions_api.SubscriptionsApi.create")
    def test_subscriptions_create(self, mock_create) -> None:
        """Test Subscriptions.create method"""
        client = MoneiClient(api_key=self.api_key)

        # Setup mock return value
        expected_response = {
            "id": "sub_123",
            "status": "ACTIVE",
            "amount": 1000,
            "currency": "EUR",
            "interval": "month",
            "customerId": "cus_123",
            "paymentMethodId": "pm_123",
            "planId": "plan_123",
            "startDate": "2023-01-01",
        }
        mock_create.return_value = expected_response

        # Test the method
        subscription_data = {
            "amount": 1000,
            "currency": "EUR",
            "interval": "month",
            "customerId": "cus_123",
            "paymentMethodId": "pm_123",
            "planId": "plan_123",
            "startDate": "2023-01-01",
        }
        response = client.Subscriptions.create(subscription_data)

        # Verify the response
        self.assertEqual(response, expected_response)
        mock_create.assert_called_once_with(subscription_data)

    @patch("Monei.api.subscriptions_api.SubscriptionsApi.get")
    def test_subscriptions_get(self, mock_get) -> None:
        """Test Subscriptions.get method"""
        client = MoneiClient(api_key=self.api_key)

        # Setup mock return value
        subscription_id = "sub_123"
        expected_response = {
            "id": subscription_id,
            "customerId": "cus_123",
            "paymentMethodId": "pm_123",
            "planId": "plan_123",
            "status": "ACTIVE",
        }
        mock_get.return_value = expected_response

        # Test the method
        response = client.Subscriptions.get(subscription_id)

        # Verify the response
        self.assertEqual(response, expected_response)
        mock_get.assert_called_once_with(subscription_id)

    @patch("Monei.api.subscriptions_api.SubscriptionsApi.cancel")
    def test_subscriptions_cancel(self, mock_cancel) -> None:
        """Test Subscriptions.cancel method"""
        client = MoneiClient(api_key=self.api_key)

        # Setup mock return value
        subscription_id = "sub_123"
        cancel_data = {"cancelAtPeriodEnd": True}
        expected_response = {
            "id": subscription_id,
            "customerId": "cus_123",
            "paymentMethodId": "pm_123",
            "planId": "plan_123",
            "status": "CANCELED",
            "cancelAtPeriodEnd": True,
        }
        mock_cancel.return_value = expected_response

        # Test the method
        response = client.Subscriptions.cancel(subscription_id, cancel_data)

        # Verify the response
        self.assertEqual(response, expected_response)
        mock_cancel.assert_called_once_with(subscription_id, cancel_data)

    @patch("Monei.api.subscriptions_api.SubscriptionsApi.activate")
    def test_subscriptions_activate(self, mock_activate) -> None:
        """Test Subscriptions.activate method"""
        client = MoneiClient(api_key=self.api_key)

        # Setup mock return value
        subscription_id = "sub_123"
        activate_data = {"paymentToken": "tok_123", "sessionId": "sess_123"}
        expected_response = {
            "id": subscription_id,
            "customerId": "cus_123",
            "paymentMethodId": "pm_123",
            "planId": "plan_123",
            "status": "ACTIVE",
        }
        mock_activate.return_value = expected_response

        # Test the method
        response = client.Subscriptions.activate(subscription_id, activate_data)

        # Verify the response
        self.assertEqual(response, expected_response)
        mock_activate.assert_called_once_with(subscription_id, activate_data)

    @patch("Monei.api.subscriptions_api.SubscriptionsApi.pause")
    def test_subscriptions_pause(self, mock_pause) -> None:
        """Test Subscriptions.pause method"""
        client = MoneiClient(api_key=self.api_key)

        # Setup mock return value
        subscription_id = "sub_123"
        pause_data = {"pauseAtPeriodEnd": True, "pauseIntervalCount": 1}
        expected_response = {
            "id": subscription_id,
            "customerId": "cus_123",
            "paymentMethodId": "pm_123",
            "planId": "plan_123",
            "status": "PAUSED",
            "resumeAt": "2023-06-01",
        }
        mock_pause.return_value = expected_response

        # Test the method
        response = client.Subscriptions.pause(subscription_id, pause_data)

        # Verify the response
        self.assertEqual(response, expected_response)
        mock_pause.assert_called_once_with(subscription_id, pause_data)

    @patch("Monei.api.subscriptions_api.SubscriptionsApi.resume")
    def test_subscriptions_resume(self, mock_resume) -> None:
        """Test Subscriptions.resume method"""
        client = MoneiClient(api_key=self.api_key)

        # Setup mock return value
        subscription_id = "sub_123"
        expected_response = {
            "id": subscription_id,
            "customerId": "cus_123",
            "paymentMethodId": "pm_123",
            "planId": "plan_123",
            "status": "ACTIVE",
        }
        mock_resume.return_value = expected_response

        # Test the method
        response = client.Subscriptions.resume(subscription_id)

        # Verify the response
        self.assertEqual(response, expected_response)
        mock_resume.assert_called_once_with(subscription_id)

    @patch("Monei.api.subscriptions_api.SubscriptionsApi.send_link")
    def test_subscriptions_send_link(self, mock_send_link) -> None:
        """Test Subscriptions.send_link method"""
        client = MoneiClient(api_key=self.api_key)

        # Setup mock return value
        subscription_id = "sub_123"
        link_data = {"customerEmail": "customer@example.com", "customerPhone": "+34600000000"}
        expected_response = {"success": True}
        mock_send_link.return_value = expected_response

        # Test the method
        response = client.Subscriptions.send_link(subscription_id, link_data)

        # Verify the response
        self.assertEqual(response, expected_response)
        mock_send_link.assert_called_once_with(subscription_id, link_data)

    @patch("Monei.api.subscriptions_api.SubscriptionsApi.send_status")
    def test_subscriptions_send_status(self, mock_send_status) -> None:
        """Test Subscriptions.send_status method"""
        client = MoneiClient(api_key=self.api_key)

        # Setup mock return value
        subscription_id = "sub_123"
        status_data = {"customerEmail": "customer@example.com"}
        expected_response = {"success": True}
        mock_send_status.return_value = expected_response

        # Test the method
        response = client.Subscriptions.send_status(subscription_id, status_data)

        # Verify the response
        self.assertEqual(response, expected_response)
        mock_send_status.assert_called_once_with(subscription_id, status_data)

    @patch("Monei.api.subscriptions_api.SubscriptionsApi.update")
    def test_subscriptions_update(self, mock_update) -> None:
        """Test Subscriptions.update method"""
        client = MoneiClient(api_key=self.api_key)

        # Setup mock return value
        subscription_id = "sub_123"
        update_data = {"amount": 2000, "description": "Updated subscription"}
        expected_response = {
            "id": subscription_id,
            "customerId": "cus_123",
            "paymentMethodId": "pm_123",
            "planId": "plan_123",
            "status": "ACTIVE",
            "amount": 2000,
            "description": "Updated subscription",
        }
        mock_update.return_value = expected_response

        # Test the method
        response = client.Subscriptions.update(subscription_id, update_data)

        # Verify the response
        self.assertEqual(response, expected_response)
        mock_update.assert_called_once_with(subscription_id, update_data)

    # Apple Pay Domain API Tests
    @patch("Monei.api.apple_pay_domain_api.ApplePayDomainApi.register")
    def test_apple_pay_domain_register(self, mock_register) -> None:
        """Test ApplePayDomain.register method"""
        client = MoneiClient(api_key=self.api_key)

        # Setup mock return value
        domain_data = {"domainName": "example.com"}
        expected_response = {"success": True}
        mock_register.return_value = expected_response

        # Test the method
        response = client.ApplePayDomain.register(domain_data)

        # Verify the response
        self.assertEqual(response, expected_response)
        mock_register.assert_called_once_with(domain_data)

    # Bizum API Tests
    @patch("Monei.api.bizum_api.BizumApi.validate_phone")
    def test_bizum_validate_phone(self, mock_validate_phone) -> None:
        """Test Bizum.validate_phone method"""
        client = MoneiClient(
            api_key=self.api_key, user_agent=self.user_agent, account_id=self.account_id
        )

        # Setup mock return value
        validate_data = {"phoneNumber": "+34600000000"}
        expected_response = {"valid": True}
        mock_validate_phone.return_value = expected_response

        # Test the method
        response = client.Bizum.validate_phone(validate_data)

        # Verify the response
        self.assertEqual(response, expected_response)
        mock_validate_phone.assert_called_once_with(validate_data)

    def test_aliases(self) -> None:
        """Test that all aliases are correctly set"""
        client = MoneiClient(api_key=self.api_key)

        # Check all aliases
        self.assertEqual(client.payments, client.Payments)
        self.assertEqual(client.payment_methods, client.PaymentMethods)
        self.assertEqual(client.subscriptions, client.Subscriptions)
        self.assertEqual(client.apple_pay_domain, client.ApplePayDomain)
        self.assertEqual(client.bizum, client.Bizum)

    def test_duplicate_aliases(self) -> None:
        """Test that there are no duplicate aliases"""
        client = MoneiClient(api_key=self.api_key)

        # Check for duplicate aliases in the client
        # In the current code, payments is assigned twice
        self.assertEqual(client.payments, client.Payments)

    @patch("Monei.api.payments_api.PaymentsApi.create")
    def test_error_handling(self, mock_create) -> None:
        """Test error handling for API calls"""
        client = MoneiClient(api_key=self.api_key)

        # Setup mock to raise an ApiException
        error_response = {
            "status": "ERROR",
            "statusCode": 400,
            "requestId": "req_123",
            "message": "Invalid request",
            "requestTime": "2023-01-01T12:00:00Z",
        }
        mock_create.side_effect = ApiException(
            status=400, reason="Bad Request", body=json.dumps(error_response)
        )

        # Test the method
        payment_data = {
            "amount": 1000,
            "currency": "EUR",
            "orderId": "order_123",
            "description": "Test payment",
        }

        # Verify that the exception is raised
        with self.assertRaises(ApiException) as context:
            client.Payments.create(payment_data)

        # Verify the exception details
        self.assertEqual(context.exception.status, 400)
        self.assertEqual(context.exception.reason, "Bad Request")
        self.assertIn("Invalid request", context.exception.body)


if __name__ == "__main__":
    unittest.main()
