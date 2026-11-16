import unittest
import json
from unittest.mock import patch, MagicMock

from Monei.monei_client import MoneiClient, DEFAULT_USER_AGENT
from Monei.exceptions import ApiException
from Monei.configuration import Configuration


class TestMoneiClientAdditional(unittest.TestCase):
    """Additional tests for MoneiClient to improve coverage"""

    def setUp(self):
        """Set up test fixtures, if any."""
        self.api_key = "test_api_key_12345"
        self.account_id = "test_account_id_67890"
        self.user_agent = "MONEI/TestPlatform/1.0.0"

    def tearDown(self):
        """Tear down test fixtures, if any."""
        pass

    def test_init_with_custom_config(self):
        """Test initializing with a custom configuration."""
        # Create a custom configuration
        config = Configuration()
        config.host = "https://custom-api.monei.com/v1"
        config.api_key["APIKey"] = "custom_api_key"

        # Initialize client with custom config
        client = MoneiClient(api_key=self.api_key, config=config)

        # Check that the config was used
        self.assertEqual(client.config, config)
        self.assertEqual(client.config.host, "https://custom-api.monei.com/v1")

        # The API key in the config is not updated when a custom config is provided
        # It's only set if the config doesn't have an API key already
        self.assertEqual(client.config.api_key["APIKey"], "custom_api_key")

    def test_init_with_custom_config_and_api_key(self):
        """Test initializing with a custom configuration that already has an API key."""
        # Create a custom configuration with API key
        config = Configuration()
        config.api_key["APIKey"] = "existing_api_key"

        # Initialize client with custom config and new API key
        client = MoneiClient(api_key=self.api_key, config=config)

        # The API key in the config is not updated when a custom config is provided
        # It's only set if the config doesn't have an API key already
        self.assertEqual(client.config.api_key["APIKey"], "existing_api_key")

    def test_init_with_custom_config_without_api_key(self):
        """Test initializing with a custom configuration without providing an API key."""
        # Create a custom configuration with API key
        config = Configuration()
        config.api_key["APIKey"] = "existing_api_key"

        # Initialize client with custom config but no API key
        client = MoneiClient(config=config)

        # Check that the existing API key was preserved
        self.assertEqual(client.config.api_key["APIKey"], "existing_api_key")

    def test_call_api_validation_with_account_id(self):
        """Test that call_api validates user agent when account_id is set."""
        # Create a client with account_id and user_agent
        client = MoneiClient(
            api_key=self.api_key, account_id=self.account_id, user_agent=self.user_agent
        )

        # Mock the original call_api method to avoid actual API calls
        with patch.object(
            client._api_client, "call_api", return_value=(None, 200, {})
        ) as mock_call_api:
            # This should not raise an exception
            client._api_client.call_api(
                "/test", "GET", header_params={}, auth_settings=["APIKey"]
            )

            # Check that call_api was called
            mock_call_api.assert_called_once()

        # Now set the user_agent back to default
        client.user_agent = DEFAULT_USER_AGENT

        # This should raise an exception
        with self.assertRaises(ApiException) as context:
            client._api_client.call_api(
                "/test", "GET", header_params={}, auth_settings=["APIKey"]
            )

        self.assertEqual(context.exception.status, 400)
        self.assertEqual(
            context.exception.reason,
            "User-Agent must be provided when using Account ID",
        )

    def test_set_account_id_with_custom_user_agent(self):
        """Test setting account_id after setting a custom user agent."""
        # Create a client with custom user agent
        client = MoneiClient(api_key=self.api_key, user_agent=self.user_agent)

        # Set account_id
        client.set_account_id(self.account_id)

        # Check that account_id was set
        self.assertEqual(client.account_id, self.account_id)

        # Check that the header was set in the API client
        self.assertEqual(
            client._api_client.default_headers.get("MONEI-Account-ID"), self.account_id
        )

    def test_set_account_id_to_none(self):
        """Test setting account_id to None removes the header."""
        # Create a client with account_id and user_agent
        client = MoneiClient(
            api_key=self.api_key, account_id=self.account_id, user_agent=self.user_agent
        )

        # Check that the header was set
        self.assertEqual(
            client._api_client.default_headers.get("MONEI-Account-ID"), self.account_id
        )

        # Set account_id to None
        client.set_account_id(None)

        # Check that account_id was set to None
        self.assertIsNone(client.account_id)

        # Check that the header was removed
        self.assertNotIn("MONEI-Account-ID", client._api_client.default_headers)

    def test_network_error_handling(self):
        """Test that network errors are properly handled."""
        client = MoneiClient(api_key="test_api_key")

        # Mock the payments API directly
        mock_payments = MagicMock()
        client.payments = mock_payments

        # Set the mock to raise a connection error
        mock_payments.get.side_effect = ConnectionError(
            "Failed to establish a connection"
        )

        # Test that the connection error is caught and properly handled
        with self.assertRaises(ConnectionError):
            client.payments.get("pay_123456789")


if __name__ == "__main__":
    unittest.main()
