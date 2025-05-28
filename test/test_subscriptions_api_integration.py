import unittest
from unittest.mock import patch, MagicMock

import Monei
from Monei.monei_client import MoneiClient
from Monei.exceptions import ApiException
from Monei.model.create_subscription_request import CreateSubscriptionRequest
from Monei.model.update_subscription_request import UpdateSubscriptionRequest
from Monei.model.cancel_subscription_request import CancelSubscriptionRequest
from Monei.model.pause_subscription_request import PauseSubscriptionRequest
from Monei.model.activate_subscription_request import ActivateSubscriptionRequest
from Monei.model.send_subscription_link_request import SendSubscriptionLinkRequest
from Monei.model.send_subscription_status_request import SendSubscriptionStatusRequest
from Monei.model.subscription import Subscription
from Monei.model.subscription_status import SubscriptionStatus
from Monei.model.subscription_interval import SubscriptionInterval
from Monei.model.payment import Payment
from Monei.model.payment_status import PaymentStatus


class TestSubscriptionsApiIntegration(unittest.TestCase):
    """SubscriptionsApi integration test stubs"""

    def setUp(self):
        """Set up test fixtures, if any."""
        self.api_key = "test_api_key_12345"
        self.client = MoneiClient(api_key=self.api_key)
        self.subscription_id = "sub_123456789"

    def tearDown(self):
        """Tear down test fixtures, if any."""
        pass

    @patch("Monei.api.subscriptions_api.SubscriptionsApi.create")
    def test_create_subscription(self, mock_create):
        """Test creating a subscription."""
        # Setup mock response
        mock_subscription = MagicMock()
        mock_subscription.id = self.subscription_id
        mock_subscription.amount = 1000
        mock_subscription.currency = "EUR"
        mock_subscription.interval = SubscriptionInterval("month")
        mock_subscription.status = SubscriptionStatus("ACTIVE")
        mock_create.return_value = mock_subscription

        # Create subscription request
        subscription_request = {
            "amount": 1000,
            "currency": "EUR",
            "interval": "month",
            "description": "Test subscription",
            "customer": {"email": "customer@example.com", "name": "John Doe"},
            "paymentMethodId": "pm_123456789",
        }

        # Call the API
        result = self.client.subscriptions.create(subscription_request)

        # Verify the result
        self.assertEqual(result.id, self.subscription_id)
        self.assertEqual(result.amount, 1000)
        self.assertEqual(result.currency, "EUR")
        self.assertEqual(result.interval, SubscriptionInterval("month"))
        self.assertEqual(result.status, SubscriptionStatus("ACTIVE"))

        # Verify the mock was called with the correct arguments
        mock_create.assert_called_once()

    @patch("Monei.api.subscriptions_api.SubscriptionsApi.get")
    def test_get_subscription(self, mock_get):
        """Test getting a subscription by ID."""
        # Setup mock response
        mock_subscription = MagicMock()
        mock_subscription.id = self.subscription_id
        mock_subscription.amount = 1000
        mock_subscription.currency = "EUR"
        mock_subscription.interval = SubscriptionInterval("month")
        mock_subscription.status = SubscriptionStatus("ACTIVE")
        mock_get.return_value = mock_subscription

        # Call the API
        result = self.client.subscriptions.get(self.subscription_id)

        # Verify the result
        self.assertEqual(result.id, self.subscription_id)
        self.assertEqual(result.amount, 1000)
        self.assertEqual(result.currency, "EUR")
        self.assertEqual(result.interval, SubscriptionInterval("month"))
        self.assertEqual(result.status, SubscriptionStatus("ACTIVE"))

        # Verify the mock was called with the correct arguments
        mock_get.assert_called_once_with(self.subscription_id)

    @patch("Monei.api.subscriptions_api.SubscriptionsApi.update")
    def test_update_subscription(self, mock_update):
        """Test updating a subscription."""
        # Setup mock response
        mock_subscription = MagicMock()
        mock_subscription.id = self.subscription_id
        mock_subscription.amount = 2000  # Updated amount
        mock_subscription.currency = "EUR"
        mock_subscription.interval = SubscriptionInterval("month")
        mock_subscription.status = SubscriptionStatus("ACTIVE")
        mock_update.return_value = mock_subscription

        # Create update request
        update_request = {"amount": 2000, "description": "Updated subscription"}

        # Call the API
        result = self.client.subscriptions.update(self.subscription_id, update_request)

        # Verify the result
        self.assertEqual(result.id, self.subscription_id)
        self.assertEqual(result.amount, 2000)  # Check updated amount
        self.assertEqual(result.currency, "EUR")
        self.assertEqual(result.interval, SubscriptionInterval("month"))
        self.assertEqual(result.status, SubscriptionStatus("ACTIVE"))

        # Verify the mock was called with the correct arguments
        mock_update.assert_called_once()

    @patch("Monei.api.subscriptions_api.SubscriptionsApi.cancel")
    def test_cancel_subscription(self, mock_cancel):
        """Test cancelling a subscription."""
        # Setup mock response
        mock_subscription = MagicMock()
        mock_subscription.id = self.subscription_id
        mock_subscription.amount = 1000
        mock_subscription.currency = "EUR"
        mock_subscription.interval = SubscriptionInterval("month")
        mock_subscription.status = SubscriptionStatus("CANCELED")
        mock_cancel.return_value = mock_subscription

        # Create cancel request
        cancel_request = {"cancelAtPeriodEnd": True}

        # Call the API
        result = self.client.subscriptions.cancel(self.subscription_id, cancel_request)

        # Verify the result
        self.assertEqual(result.id, self.subscription_id)
        self.assertEqual(result.amount, 1000)
        self.assertEqual(result.currency, "EUR")
        self.assertEqual(result.interval, SubscriptionInterval("month"))
        self.assertEqual(result.status, SubscriptionStatus("CANCELED"))

        # Verify the mock was called with the correct arguments
        mock_cancel.assert_called_once()

    @patch("Monei.api.subscriptions_api.SubscriptionsApi.pause")
    def test_pause_subscription(self, mock_pause):
        """Test pausing a subscription."""
        # Setup mock response
        mock_subscription = MagicMock()
        mock_subscription.id = self.subscription_id
        mock_subscription.amount = 1000
        mock_subscription.currency = "EUR"
        mock_subscription.interval = SubscriptionInterval("month")
        mock_subscription.status = SubscriptionStatus("PAUSED")
        mock_pause.return_value = mock_subscription

        # Create pause request
        pause_request = {"pauseAtPeriodEnd": True, "pauseIntervalCount": 1}

        # Call the API
        result = self.client.subscriptions.pause(self.subscription_id, pause_request)

        # Verify the result
        self.assertEqual(result.id, self.subscription_id)
        self.assertEqual(result.amount, 1000)
        self.assertEqual(result.currency, "EUR")
        self.assertEqual(result.interval, SubscriptionInterval("month"))
        self.assertEqual(result.status, SubscriptionStatus("PAUSED"))

        # Verify the mock was called with the correct arguments
        mock_pause.assert_called_once()

    @patch("Monei.api.subscriptions_api.SubscriptionsApi.resume")
    def test_resume_subscription(self, mock_resume):
        """Test resuming a subscription."""
        # Setup mock response
        mock_subscription = MagicMock()
        mock_subscription.id = self.subscription_id
        mock_subscription.amount = 1000
        mock_subscription.currency = "EUR"
        mock_subscription.interval = SubscriptionInterval("month")
        mock_subscription.status = SubscriptionStatus("ACTIVE")
        mock_resume.return_value = mock_subscription

        # Call the API
        result = self.client.subscriptions.resume(self.subscription_id)

        # Verify the result
        self.assertEqual(result.id, self.subscription_id)
        self.assertEqual(result.amount, 1000)
        self.assertEqual(result.currency, "EUR")
        self.assertEqual(result.interval, SubscriptionInterval("month"))
        self.assertEqual(result.status, SubscriptionStatus("ACTIVE"))

        # Verify the mock was called with the correct arguments
        mock_resume.assert_called_once_with(self.subscription_id)

    @patch("Monei.api.subscriptions_api.SubscriptionsApi.activate")
    def test_activate_subscription(self, mock_activate):
        """Test activating a subscription."""
        # Setup mock response - activate should return a Payment object, not Subscription
        mock_payment = MagicMock()
        mock_payment.id = "pay_123456789"
        mock_payment.amount = 1000
        mock_payment.currency = "EUR"
        mock_payment.account_id = "acc_123456789"
        mock_payment.livemode = False
        mock_payment.status = PaymentStatus("SUCCEEDED")
        mock_activate.return_value = mock_payment

        # Create activate request
        activate_request = {
            "paymentToken": "tok_123456789",
            "sessionId": "sess_123456789",
        }

        # Call the API
        result = self.client.subscriptions.activate(
            self.subscription_id, activate_request
        )

        # Verify the result - should be a Payment object
        self.assertEqual(result.id, "pay_123456789")
        self.assertEqual(result.amount, 1000)
        self.assertEqual(result.currency, "EUR")
        self.assertEqual(result.account_id, "acc_123456789")
        self.assertEqual(result.livemode, False)
        self.assertEqual(result.status, PaymentStatus("SUCCEEDED"))

        # Verify the mock was called with the correct arguments
        mock_activate.assert_called_once()

    @patch("Monei.api.subscriptions_api.SubscriptionsApi.send_link")
    def test_send_subscription_link(self, mock_send_link):
        """Test sending a subscription link."""
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
        result = self.client.subscriptions.send_link(
            self.subscription_id, send_link_request
        )

        # Verify the result
        self.assertTrue(result.success)

        # Verify the mock was called with the correct arguments
        mock_send_link.assert_called_once()

    @patch("Monei.api.subscriptions_api.SubscriptionsApi.send_status")
    def test_send_subscription_status(self, mock_send_status):
        """Test sending a subscription status."""
        # Setup mock response
        mock_response = MagicMock()
        mock_response.success = True
        mock_send_status.return_value = mock_response

        # Create send status request
        send_status_request = {"customerEmail": "customer@example.com"}

        # Call the API
        result = self.client.subscriptions.send_status(
            self.subscription_id, send_status_request
        )

        # Verify the result
        self.assertTrue(result.success)

        # Verify the mock was called with the correct arguments
        mock_send_status.assert_called_once()

    @patch("Monei.api.subscriptions_api.SubscriptionsApi.create")
    def test_create_subscription_validation_error(self, mock_create):
        """Test that validation errors are properly handled when creating a subscription."""
        # Setup mock to raise an ApiException
        mock_create.side_effect = ApiException(
            status=422, reason="Unprocessable Entity"
        )

        # Create invalid subscription request (missing required fields)
        subscription_request = {
            "currency": "EUR",  # Missing required 'amount' field
            "interval": "month",
            "description": "Test subscription",
        }

        # Call the API and expect an exception
        with self.assertRaises(ApiException) as context:
            self.client.subscriptions.create(subscription_request)

        # Verify the exception details
        self.assertEqual(context.exception.status, 422)
        self.assertIn("Unprocessable Entity", context.exception.reason)

        # Verify the mock was called
        mock_create.assert_called_once()

    @patch("Monei.api.subscriptions_api.SubscriptionsApi.get")
    def test_get_subscription_not_found(self, mock_get):
        """Test handling not found error when getting a subscription."""
        # Setup mock to raise an ApiException
        mock_get.side_effect = ApiException(status=404, reason="Not Found")

        # Use a non-existent subscription ID
        non_existent_id = "sub_nonexistent"

        # Call the API and expect an exception
        with self.assertRaises(ApiException) as context:
            self.client.subscriptions.get(non_existent_id)

        # Verify the exception details
        self.assertEqual(context.exception.status, 404)
        self.assertIn("Not Found", context.exception.reason)

        # Verify the mock was called with the correct arguments
        mock_get.assert_called_once_with(non_existent_id)

    @patch("Monei.api.subscriptions_api.SubscriptionsApi.cancel")
    def test_cancel_subscription_unauthorized(self, mock_cancel):
        """Test handling unauthorized errors when canceling a subscription."""
        # Setup mock to raise an ApiException
        mock_cancel.side_effect = ApiException(status=401, reason="Unauthorized")

        # Create cancel request
        cancel_request = CancelSubscriptionRequest(
            reason="Customer requested cancellation"
        )

        # Call the API and expect an exception
        with self.assertRaises(ApiException) as context:
            self.client.subscriptions.cancel(self.subscription_id, cancel_request)

        # Verify the exception details
        self.assertEqual(context.exception.status, 401)
        self.assertIn("Unauthorized", context.exception.reason)

        # Verify the mock was called
        mock_cancel.assert_called_once()


if __name__ == "__main__":
    unittest.main()
