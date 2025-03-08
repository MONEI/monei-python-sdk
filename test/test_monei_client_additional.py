import unittest
import json
import hmac
import hashlib
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
            api_key=self.api_key, 
            account_id=self.account_id, 
            user_agent=self.user_agent
        )
        
        # Mock the original call_api method to avoid actual API calls
        with patch.object(client._api_client, 'call_api', return_value=(None, 200, {})) as mock_call_api:
            # This should not raise an exception
            client._api_client.call_api(
                "/test", "GET", 
                header_params={}, 
                auth_settings=["APIKey"]
            )
            
            # Check that call_api was called
            mock_call_api.assert_called_once()
            
        # Now set the user_agent back to default
        client.user_agent = DEFAULT_USER_AGENT
        
        # This should raise an exception
        with self.assertRaises(ApiException) as context:
            client._api_client.call_api(
                "/test", "GET", 
                header_params={}, 
                auth_settings=["APIKey"]
            )
        
        self.assertEqual(context.exception.status, 400)
        self.assertEqual(
            context.exception.reason, 
            "User-Agent must be provided when using Account ID"
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
            client._api_client.default_headers.get("MONEI-Account-ID"),
            self.account_id
        )

    def test_set_account_id_to_none(self):
        """Test setting account_id to None removes the header."""
        # Create a client with account_id and user_agent
        client = MoneiClient(
            api_key=self.api_key, 
            account_id=self.account_id, 
            user_agent=self.user_agent
        )
        
        # Check that the header was set
        self.assertEqual(
            client._api_client.default_headers.get("MONEI-Account-ID"),
            self.account_id
        )
        
        # Set account_id to None
        client.set_account_id(None)
        
        # Check that account_id was set to None
        self.assertIsNone(client.account_id)
        
        # Check that the header was removed
        self.assertNotIn("MONEI-Account-ID", client._api_client.default_headers)

    def test_verify_signature_with_invalid_format(self):
        """Test verify_signature with an invalid signature format."""
        client = MoneiClient(api_key=self.api_key)
        
        # Create a test payload
        body = '{"id":"test_payment_id","amount":1000,"currency":"EUR","status":"SUCCEEDED"}'
        
        # Invalid signature format (missing v1)
        invalid_signature = "t=1602604555"
        
        # This should raise an exception
        with self.assertRaises(Exception):
            client.verify_signature(body, invalid_signature)

    def test_verify_signature_with_empty_signature(self):
        """Test verify_signature with an empty signature."""
        client = MoneiClient(api_key=self.api_key)
        
        # Create a test payload
        body = '{"id":"test_payment_id","amount":1000,"currency":"EUR","status":"SUCCEEDED"}'
        
        # Empty signature
        empty_signature = ""
        
        # This should raise an exception
        with self.assertRaises(Exception):
            client.verify_signature(body, empty_signature)

    def test_verify_signature_with_tampered_body(self):
        """Test verify_signature with a tampered body."""
        client = MoneiClient(api_key=self.api_key)
        
        # Create original payload and signature
        original_body = '{"id":"test_payment_id","amount":1000,"currency":"EUR","status":"SUCCEEDED"}'
        timestamp = "1602604555"
        
        # Calculate a valid signature for the original body
        signature_payload = f"{timestamp}.{original_body}"
        hmac_digest = hmac.new(
            bytes(self.api_key, "utf-8"),
            msg=bytes(signature_payload, "utf-8"),
            digestmod=hashlib.sha256
        ).hexdigest()
        
        valid_signature = f"t={timestamp},v1={hmac_digest}"
        
        # Tamper with the body
        tampered_body = '{"id":"test_payment_id","amount":2000,"currency":"EUR","status":"SUCCEEDED"}'
        
        # This should raise an exception
        with self.assertRaises(ApiException) as context:
            client.verify_signature(tampered_body, valid_signature)
        
        self.assertEqual(context.exception.status, 401)
        self.assertEqual(context.exception.reason, "[401] Signature verification failed")


if __name__ == '__main__':
    unittest.main()
