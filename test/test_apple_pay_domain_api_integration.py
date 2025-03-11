import unittest
from unittest.mock import patch, MagicMock

from Monei.monei_client import MoneiClient
from Monei.exceptions import ApiException
from Monei.model.register_apple_pay_domain_request import RegisterApplePayDomainRequest


class TestApplePayDomainApiIntegration(unittest.TestCase):
    """ApplePayDomainApi integration test stubs"""

    def setUp(self):
        """Set up test fixtures, if any."""
        self.api_key = "test_api_key_12345"
        self.client = MoneiClient(api_key=self.api_key)
        self.domain = "example.com"

    def tearDown(self):
        """Tear down test fixtures, if any."""
        pass

    @patch("Monei.api.apple_pay_domain_api.ApplePayDomainApi.register")
    def test_register_domain(self, mock_register):
        """Test registering an Apple Pay domain."""
        # Setup mock response
        mock_response = MagicMock()
        mock_response.domain = self.domain
        mock_response.status = "COMPLETED"
        mock_register.return_value = mock_response

        # Create register domain request
        domain_request = RegisterApplePayDomainRequest(domain_name=self.domain)

        # Call the API method
        response = self.client.apple_pay_domain.register(domain_request)

        # Verify the result
        self.assertEqual(response.domain, self.domain)
        self.assertEqual(response.status, "COMPLETED")
        mock_register.assert_called_once()

    @patch("Monei.api.apple_pay_domain_api.ApplePayDomainApi.register")
    def test_register_domain_error(self, mock_register):
        """Test handling API error during domain registration."""
        # Setup mock to raise an exception
        mock_register.side_effect = ApiException(status=400, reason="Bad Request")

        # Create register domain request
        domain_request = RegisterApplePayDomainRequest(domain_name="invalid-domain")

        # Call the API method and verify it raises an exception
        with self.assertRaises(ApiException):
            self.client.apple_pay_domain.register(domain_request)

    @patch("Monei.api.apple_pay_domain_api.ApplePayDomainApi.register")
    def test_register_domain_in_progress(self, mock_register):
        """Test registering an Apple Pay domain that's in progress."""
        # Setup mock response for in-progress registration
        mock_response = MagicMock()
        mock_response.domain = self.domain
        mock_response.status = "IN_PROGRESS"
        mock_register.return_value = mock_response

        # Create register domain request
        domain_request = RegisterApplePayDomainRequest(domain_name=self.domain)

        # Call the API method
        response = self.client.apple_pay_domain.register(domain_request)

        # Verify the result
        self.assertEqual(response.domain, self.domain)
        self.assertEqual(response.status, "IN_PROGRESS")
        mock_register.assert_called_once()


if __name__ == "__main__":
    unittest.main()
