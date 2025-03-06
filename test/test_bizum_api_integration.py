import pytest
from unittest.mock import patch, MagicMock

from Monei.monei_client import MoneiClient
from Monei.api.bizum_api import BizumApi
from Monei.model.validate_bizum_phone_request import ValidateBizumPhoneRequest


@pytest.mark.unit
class TestBizumApiIntegration:
    """Integration tests for the Bizum API with mocked responses"""

    @pytest.fixture
    def mock_client(self):
        """Fixture for creating a mock client"""
        return MoneiClient(api_key="test_api_key")

    @patch.object(BizumApi, 'validate_phone')
    def test_validate_bizum_phone(self, mock_validate_phone, mock_client):
        """Test validating a Bizum phone number"""
        success_response = {
            "valid": True,
            "phone": "+34600000000"
        }
        mock_validate_phone.return_value = success_response
        
        validate_request = ValidateBizumPhoneRequest(
            phone="+34600000000"
        )
        
        result = mock_client.Bizum.validate_phone(validate_bizum_phone_request=validate_request)
        
        assert result["valid"] is True
        assert result["phone"] == "+34600000000"
        mock_validate_phone.assert_called_once_with(validate_bizum_phone_request=validate_request)

    @patch.object(BizumApi, 'validate_phone')
    def test_validate_invalid_bizum_phone(self, mock_validate_phone, mock_client):
        """Test validating an invalid Bizum phone number"""
        invalid_response = {
            "valid": False,
            "phone": "+34600000000",
            "error": {
                "code": "invalid_phone",
                "message": "The phone number is not registered with Bizum"
            }
        }
        mock_validate_phone.return_value = invalid_response
        
        validate_request = ValidateBizumPhoneRequest(
            phone="+34600000000"
        )
        
        result = mock_client.Bizum.validate_phone(validate_bizum_phone_request=validate_request)
        
        assert result["valid"] is False
        assert result["phone"] == "+34600000000"
        assert "error" in result
        assert result["error"]["code"] == "invalid_phone"
        mock_validate_phone.assert_called_once_with(validate_bizum_phone_request=validate_request) 