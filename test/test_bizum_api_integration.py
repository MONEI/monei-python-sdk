import unittest
from unittest.mock import patch, MagicMock

import Monei  # noqa: F401
from Monei.monei_client import MoneiClient
from Monei.exceptions import ApiException
from Monei.model.validate_bizum_phone_request import ValidateBizumPhoneRequest


class TestBizumApiIntegration(unittest.TestCase):
    """BizumApi integration test stubs"""

    def setUp(self):
        """Set up test fixtures, if any."""
        self.api_key = "test_api_key_12345"
        self.client = MoneiClient(api_key=self.api_key)
        self.account_id = "acc_12345"

    def tearDown(self):
        """Tear down test fixtures, if any."""
        pass

    @patch("Monei.api.bizum_api.BizumApi.validate_phone")
    def test_validate_phone(self, mock_validate_phone):
        """Test validating a Bizum phone number."""
        # Setup mock response
        mock_response = MagicMock()
        mock_response.valid = True
        mock_validate_phone.return_value = mock_response

        # Create validate phone request
        phone_request = ValidateBizumPhoneRequest(
            account_id=self.account_id, phone_number="+34600000000"
        )

        # Call the API method
        response = self.client.bizum.validate_phone(phone_request)

        # Verify the result
        self.assertTrue(response.valid)
        mock_validate_phone.assert_called_once()

    @patch("Monei.api.bizum_api.BizumApi.validate_phone")
    def test_validate_phone_invalid(self, mock_validate_phone):
        """Test validating an invalid Bizum phone number."""
        # Setup mock response
        mock_response = MagicMock()
        mock_response.valid = False
        mock_validate_phone.return_value = mock_response

        # Create validate phone request
        phone_request = ValidateBizumPhoneRequest(
            account_id=self.account_id, phone_number="+34999999999"
        )

        # Call the API method
        response = self.client.bizum.validate_phone(phone_request)

        # Verify the result
        self.assertFalse(response.valid)
        mock_validate_phone.assert_called_once()

    @patch("Monei.api.bizum_api.BizumApi.validate_phone")
    def test_validate_phone_error(self, mock_validate_phone):
        """Test handling API error during phone validation."""
        # Setup mock to raise an exception
        mock_validate_phone.side_effect = ApiException(status=400, reason="Bad Request")

        # Create validate phone request
        phone_request = ValidateBizumPhoneRequest(
            account_id=self.account_id, phone_number="invalid_phone"
        )

        # Call the API method and verify it raises an exception
        with self.assertRaises(ApiException):
            self.client.bizum.validate_phone(phone_request)


if __name__ == "__main__":
    unittest.main()
