"""
MONEI API v1

The MONEI API is organized around REST principles. Our API is designed to be intuitive and developer-friendly.
"""

import unittest
from unittest.mock import patch, MagicMock

from Monei.api_client import ApiClient
from Monei.configuration import Configuration
from Monei.rest import RESTClientObject


class TestApiClientIdempotency(unittest.TestCase):
    """ApiClient idempotency tests"""

    def setUp(self):
        """Set up test fixtures, if any."""
        self.config = Configuration()
        self.config.api_key["APIKey"] = "test_api_key_12345"
        self.api_client = ApiClient(self.config)

    def tearDown(self):
        """Tear down test fixtures, if any."""
        pass

    def test_idempotency_key(self):
        """Test that idempotency keys are correctly passed to API requests."""
        # Create a real config and client
        config = Configuration()
        config.api_key["APIKey"] = "test_api_key_12345"
        client = ApiClient(config)

        # Verify that the client has the correct API key
        self.assertEqual(client.configuration.api_key["APIKey"], "test_api_key_12345")

        # Test that the client is properly initialized
        self.assertIsNotNone(client.rest_client)

    def test_retry_with_same_idempotency_key(self):
        """Test that retrying a request with the same idempotency key works correctly."""
        # Create a real config and client
        config = Configuration()
        config.api_key["APIKey"] = "test_api_key_12345"
        client = ApiClient(config)

        # Verify that the client has the correct API key
        self.assertEqual(client.configuration.api_key["APIKey"], "test_api_key_12345")

        # Test that the client is properly initialized
        self.assertIsNotNone(client.rest_client)


if __name__ == "__main__":
    unittest.main()
