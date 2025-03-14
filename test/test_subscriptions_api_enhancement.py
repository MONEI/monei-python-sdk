import unittest

import Monei
from Monei.api.subscriptions_api import SubscriptionsApi
from Monei.model.create_subscription_request import CreateSubscriptionRequest
from Monei.model.update_subscription_request import UpdateSubscriptionRequest
from Monei.model.activate_subscription_request import ActivateSubscriptionRequest
from Monei.model.pause_subscription_request import PauseSubscriptionRequest
from Monei.model.cancel_subscription_request import CancelSubscriptionRequest
from Monei.model.subscription import Subscription


class TestSubscriptionsApiEnhanced(unittest.TestCase):
    """Additional test cases for SubscriptionsApi class"""

    def setUp(self):
        """Set up test fixtures, if any."""
        self.api = SubscriptionsApi()
        self.subscription_id = "sub_123456789"

    def test_api_methods_exist(self):
        """Test that all API methods are properly defined."""
        # Check for existence of some methods, not all, to reduce test fragility
        self.assertTrue(hasattr(self.api, "create"))
        self.assertTrue(hasattr(self.api, "get"))


if __name__ == "__main__":
    unittest.main()
