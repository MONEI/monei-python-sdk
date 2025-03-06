import pytest
from unittest.mock import patch, MagicMock

from Monei.monei_client import MoneiClient
from Monei.api.subscriptions_api import SubscriptionsApi
from Monei.model.create_subscription_request import CreateSubscriptionRequest
from Monei.model.update_subscription_request import UpdateSubscriptionRequest
from Monei.model.pause_subscription_request import PauseSubscriptionRequest
from Monei.model.cancel_subscription_request import CancelSubscriptionRequest
from Monei.model.activate_subscription_request import ActivateSubscriptionRequest
from Monei.model.send_subscription_link_request import SendSubscriptionLinkRequest
from Monei.model.send_subscription_status_request import SendSubscriptionStatusRequest
from Monei.model.subscription_status import SubscriptionStatus
from Monei.model.subscription_interval import SubscriptionInterval


@pytest.mark.unit
class TestSubscriptionsApiIntegration:
    """Integration tests for the Subscriptions API with mocked responses"""

    @pytest.fixture
    def mock_subscription(self):
        """Fixture for a mock subscription response"""
        return {
            "id": "sub_123456789",
            "status": SubscriptionStatus("ACTIVE"),
            "amount": 1000,
            "currency": "EUR",
            "description": "Test subscription",
            "interval": SubscriptionInterval("MONTH"),
            "intervalCount": 1,
            "startDate": "2023-01-01",
            "endDate": None,
            "cancelAtPeriodEnd": False,
            "created": "2023-01-01T12:00:00Z",
            "updated": "2023-01-01T12:00:00Z",
        }

    @pytest.fixture
    def mock_client(self):
        """Fixture for creating a mock client"""
        return MoneiClient(api_key="test_api_key")

    @patch.object(SubscriptionsApi, "create")
    def test_create_subscription(self, mock_create, mock_client, mock_subscription):
        """Test creating a subscription"""
        mock_create.return_value = mock_subscription

        subscription_request = CreateSubscriptionRequest(
            amount=1000,
            currency="EUR",
            description="Test subscription",
            interval=SubscriptionInterval("MONTH"),
            interval_count=1,
            payment_method_id="pm_123456789",
        )

        result = mock_client.Subscriptions.create(create_subscription_request=subscription_request)

        assert result["id"] == "sub_123456789"
        assert result["status"] == SubscriptionStatus("ACTIVE")
        assert result["amount"] == 1000
        assert result["currency"] == "EUR"
        assert result["interval"] == SubscriptionInterval("MONTH")
        mock_create.assert_called_once_with(create_subscription_request=subscription_request)

    @patch.object(SubscriptionsApi, "get")
    def test_get_subscription(self, mock_get, mock_client, mock_subscription):
        """Test retrieving a subscription"""
        mock_get.return_value = mock_subscription

        result = mock_client.Subscriptions.get(subscription_id="sub_123456789")

        assert result["id"] == "sub_123456789"
        assert result["status"] == SubscriptionStatus("ACTIVE")
        mock_get.assert_called_once_with(subscription_id="sub_123456789")

    @patch.object(SubscriptionsApi, "list")
    def test_list_subscriptions(self, mock_list, mock_client, mock_subscription):
        """Test listing subscriptions"""
        mock_list.return_value = {
            "data": [
                mock_subscription,
                {
                    "id": "sub_987654321",
                    "status": SubscriptionStatus("PAUSED"),
                    "amount": 2000,
                    "currency": "EUR",
                    "description": "Another subscription",
                    "interval": SubscriptionInterval("YEAR"),
                    "intervalCount": 1,
                    "startDate": "2023-01-02",
                    "endDate": None,
                    "cancelAtPeriodEnd": False,
                    "created": "2023-01-02T12:00:00Z",
                    "updated": "2023-01-02T12:00:00Z",
                },
            ],
            "hasMore": False,
            "totalCount": 2,
        }

        result = mock_client.Subscriptions.list()

        assert "data" in result
        assert len(result["data"]) == 2
        assert result["data"][0]["id"] == "sub_123456789"
        assert result["data"][0]["status"] == SubscriptionStatus("ACTIVE")
        assert result["data"][1]["id"] == "sub_987654321"
        assert result["data"][1]["status"] == SubscriptionStatus("PAUSED")
        assert result["hasMore"] is False
        assert result["totalCount"] == 2
        mock_list.assert_called_once()

    @patch.object(SubscriptionsApi, "update")
    def test_update_subscription(self, mock_update, mock_client, mock_subscription):
        """Test updating a subscription"""
        updated_subscription = mock_subscription.copy()
        updated_subscription["amount"] = 1500
        updated_subscription["description"] = "Updated subscription"
        mock_update.return_value = updated_subscription

        update_request = UpdateSubscriptionRequest(amount=1500, description="Updated subscription")

        result = mock_client.Subscriptions.update(
            subscription_id="sub_123456789", update_subscription_request=update_request
        )

        assert result["id"] == "sub_123456789"
        assert result["amount"] == 1500
        assert result["description"] == "Updated subscription"
        mock_update.assert_called_once_with(
            subscription_id="sub_123456789", update_subscription_request=update_request
        )

    @patch.object(SubscriptionsApi, "pause")
    def test_pause_subscription(self, mock_pause, mock_client, mock_subscription):
        """Test pausing a subscription"""
        paused_subscription = mock_subscription.copy()
        paused_subscription["status"] = SubscriptionStatus("PAUSED")
        mock_pause.return_value = paused_subscription

        pause_request = PauseSubscriptionRequest()

        result = mock_client.Subscriptions.pause(
            subscription_id="sub_123456789", pause_subscription_request=pause_request
        )

        assert result["id"] == "sub_123456789"
        assert result["status"] == SubscriptionStatus("PAUSED")
        mock_pause.assert_called_once_with(
            subscription_id="sub_123456789", pause_subscription_request=pause_request
        )

    @patch.object(SubscriptionsApi, "cancel")
    def test_cancel_subscription(self, mock_cancel, mock_client, mock_subscription):
        """Test canceling a subscription"""
        canceled_subscription = mock_subscription.copy()
        canceled_subscription["status"] = SubscriptionStatus("CANCELED")
        mock_cancel.return_value = canceled_subscription

        cancel_request = CancelSubscriptionRequest()

        result = mock_client.Subscriptions.cancel(
            subscription_id="sub_123456789", cancel_subscription_request=cancel_request
        )

        assert result["id"] == "sub_123456789"
        assert result["status"] == SubscriptionStatus("CANCELED")
        mock_cancel.assert_called_once_with(
            subscription_id="sub_123456789", cancel_subscription_request=cancel_request
        )

    @patch.object(SubscriptionsApi, "activate")
    def test_activate_subscription(self, mock_activate, mock_client, mock_subscription):
        """Test activating a subscription"""
        paused_subscription = mock_subscription.copy()
        paused_subscription["status"] = SubscriptionStatus("PAUSED")

        activated_subscription = paused_subscription.copy()
        activated_subscription["status"] = SubscriptionStatus("ACTIVE")
        mock_activate.return_value = activated_subscription

        activate_request = ActivateSubscriptionRequest()

        result = mock_client.Subscriptions.activate(
            subscription_id="sub_123456789", activate_subscription_request=activate_request
        )

        assert result["id"] == "sub_123456789"
        assert result["status"] == SubscriptionStatus("ACTIVE")
        mock_activate.assert_called_once_with(
            subscription_id="sub_123456789", activate_subscription_request=activate_request
        )

    @patch.object(SubscriptionsApi, "send_link")
    def test_send_subscription_link(self, mock_send_link, mock_client):
        """Test sending a subscription link"""
        success_response = {"success": True}
        mock_send_link.return_value = success_response

        link_request = SendSubscriptionLinkRequest(
            subscription_id="sub_123456789", email="customer@example.com"
        )

        result = mock_client.Subscriptions.send_link(send_subscription_link_request=link_request)

        assert result["success"] is True
        mock_send_link.assert_called_once_with(send_subscription_link_request=link_request)

    @patch.object(SubscriptionsApi, "send_status")
    def test_send_subscription_status(self, mock_send_status, mock_client):
        """Test sending a subscription status"""
        success_response = {"success": True}
        mock_send_status.return_value = success_response

        status_request = SendSubscriptionStatusRequest(
            subscription_id="sub_123456789", email="customer@example.com"
        )

        result = mock_client.Subscriptions.send_status(
            send_subscription_status_request=status_request
        )

        assert result["success"] is True
        mock_send_status.assert_called_once_with(send_subscription_status_request=status_request)
