import unittest
from unittest.mock import patch, MagicMock
import requests

from Monei.monei_client import MoneiClient


class TestApiKeyIntegration(unittest.TestCase):
    """Integration tests for API key handling"""

    def setUp(self):
        """Set up test fixtures, if any."""
        self.api_key = "test_api_key_12345"
        self.user_agent = "MONEI/TestPlatform/1.0.0"

    def test_api_key_in_real_request(self):
        """Test that the API key is correctly passed in the Authorization header in a real request."""
        # Create a client with a test API key
        client = MoneiClient(api_key=self.api_key, user_agent=self.user_agent)

        # Mock the requests.request method to capture the headers
        with patch("requests.request") as mock_request:
            # Configure the mock to return a successful response
            mock_response = MagicMock()
            mock_response.status_code = 200
            mock_response.text = "{}"
            mock_response.headers = {}
            mock_request.return_value = mock_response

            # Make a request using the client
            try:
                # Call a method that will make a real HTTP request
                client.payments.get("dummy_payment_id")
            except Exception:
                # We don't care about the actual API call, just the headers
                pass

            # Check that request was called
            mock_request.assert_called()

            # Get the headers from the call arguments
            call_args = mock_request.call_args
            headers = call_args[1].get("headers", {})

            # Verify that the Authorization header contains the API key
            self.assertIn("Authorization", headers)
            self.assertEqual(headers["Authorization"], self.api_key)

            # Verify that the User-Agent header is set
            self.assertIn("User-Agent", headers)
            self.assertEqual(headers["User-Agent"], self.user_agent)


if __name__ == "__main__":
    unittest.main()
