import unittest
from unittest.mock import patch, MagicMock

import Monei
from Monei.monei_client import MoneiClient
from Monei.exceptions import ApiException
from Monei.model.register_apple_pay_domain_request import RegisterApplePayDomainRequest


class TestApplePayDomainApiIntegration(unittest.TestCase):
    """ApplePayDomainApi integration test stubs"""

    def setUp(self):
        """Set up test fixtures, if any."""
        self.api_key = "test_api_key_12345"
        self.client = MoneiClient(api_key=self.api_key)
        self.domain_name = "example.com"

    def tearDown(self):
        """Tear down test fixtures, if any."""
        pass

    @patch("Monei.api.apple_pay_domain_api.ApplePayDomainApi.register")
    def test_register_apple_pay_domain(self, mock_register):
        """Test registering an Apple Pay domain."""
        # Setup mock response
        mock_response = MagicMock()
        mock_response.success = True
        mock_register.return_value = mock_response

        # Create register request
        register_request = {"domainName": self.domain_name}

        # Call the API
        result = self.client.apple_pay_domain.register(register_request)

        # Verify the result
        self.assertTrue(result.success)

        # Verify the mock was called with the correct arguments
        mock_register.assert_called_once()


if __name__ == "__main__":
    unittest.main()
