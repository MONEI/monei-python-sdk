import unittest
from unittest.mock import patch, MagicMock

import Monei
from Monei.monei_client import MoneiClient
from Monei.exceptions import ApiException
from Monei.model.validate_bizum_phone_request import ValidateBizumPhoneRequest


class TestBizumApiIntegration(unittest.TestCase):
    """BizumApi integration test stubs"""

    def setUp(self):
        """Set up test fixtures, if any."""
        self.api_key = "test_api_key_12345"
        self.client = MoneiClient(api_key=self.api_key)
        self.phone_number = "+34600000000"

    def tearDown(self):
        """Tear down test fixtures, if any."""
        pass

    @patch('Monei.api.bizum_api.BizumApi.validate_phone')
    def test_validate_bizum_phone(self, mock_validate_phone):
        """Test validating a Bizum phone number."""
        # Setup mock response
        mock_response = MagicMock()
        mock_response.valid = True
        mock_validate_phone.return_value = mock_response

        # Create validate phone request
        validate_request = {
            "phoneNumber": self.phone_number
        }

        # Call the API
        result = self.client.bizum.validate_phone(validate_request)

        # Verify the result
        self.assertTrue(result.valid)

        # Verify the mock was called with the correct arguments
        mock_validate_phone.assert_called_once()


if __name__ == "__main__":
    unittest.main() 