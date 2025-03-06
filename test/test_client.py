"""
Unit tests for the MONEI client.
"""

import pytest
from unittest.mock import patch


class TestMoneiClient:
    """Tests for the MoneiClient class."""

    def test_client_initialization(self, api_key):
        """Test that the client is initialized with the correct API key."""
        # Import here to avoid circular imports
        from Monei import MoneiClient
        client = MoneiClient(api_key=api_key)
        assert client.api_key == api_key
        assert client.api_client is not None

    def test_client_initialization_without_api_key(self):
        """Test that an error is raised when no API key is provided."""
        # Import here to avoid circular imports
        from Monei import MoneiClient
        with pytest.raises(ValueError, match="API key is required"):
            MoneiClient(api_key=None)

    @patch("Monei.api_client.ApiClient")
    def test_client_with_custom_configuration(self, mock_api_client, api_key):
        """Test that the client can be initialized with a custom configuration."""
        # Import here to avoid circular imports
        from Monei import MoneiClient
        MoneiClient(
            api_key=api_key,
            host="https://custom-api.monei.com",
            ssl_ca_cert="/path/to/cert",
            verify_ssl=False,
        )
        
        # Check that the configuration was passed to the API client
        mock_api_client.assert_called_once()
        config = mock_api_client.call_args[0][0]
        assert config.host == "https://custom-api.monei.com"
        assert config.ssl_ca_cert == "/path/to/cert"
        assert config.verify_ssl is False 