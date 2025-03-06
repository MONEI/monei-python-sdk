import pytest
from unittest.mock import patch, MagicMock

from Monei.monei_client import MoneiClient
from Monei.api.apple_pay_domain_api import ApplePayDomainApi
from Monei.model.register_apple_pay_domain_request import RegisterApplePayDomainRequest


@pytest.mark.unit
class TestApplePayDomainApiIntegration:
    """Integration tests for the Apple Pay Domain API with mocked responses"""

    @pytest.fixture
    def mock_client(self):
        """Fixture for creating a mock client"""
        return MoneiClient(api_key="test_api_key")

    @patch.object(ApplePayDomainApi, 'register')
    def test_register_apple_pay_domain(self, mock_register, mock_client):
        """Test registering an Apple Pay domain"""
        success_response = {
            "success": True,
            "domain": "example.com"
        }
        mock_register.return_value = success_response
        
        register_request = RegisterApplePayDomainRequest(
            domain="example.com"
        )
        
        result = mock_client.ApplePayDomain.register(register_apple_pay_domain_request=register_request)
        
        assert result["success"] is True
        assert result["domain"] == "example.com"
        mock_register.assert_called_once_with(register_apple_pay_domain_request=register_request)

    @patch.object(ApplePayDomainApi, 'list')
    def test_list_apple_pay_domains(self, mock_list, mock_client):
        """Test listing Apple Pay domains"""
        domains_response = {
            "data": [
                {"domain": "example.com", "created": "2023-01-01T12:00:00Z"},
                {"domain": "shop.example.com", "created": "2023-01-02T12:00:00Z"}
            ],
            "hasMore": False,
            "totalCount": 2
        }
        mock_list.return_value = domains_response
        
        result = mock_client.ApplePayDomain.list()
        
        assert "data" in result
        assert len(result["data"]) == 2
        assert result["data"][0]["domain"] == "example.com"
        assert result["data"][1]["domain"] == "shop.example.com"
        assert result["hasMore"] is False
        assert result["totalCount"] == 2
        mock_list.assert_called_once()

    @patch.object(ApplePayDomainApi, 'delete')
    def test_delete_apple_pay_domain(self, mock_delete, mock_client):
        """Test deleting an Apple Pay domain"""
        success_response = {
            "success": True,
            "domain": "example.com",
            "deleted": True
        }
        mock_delete.return_value = success_response
        
        result = mock_client.ApplePayDomain.delete(domain="example.com")
        
        assert result["success"] is True
        assert result["domain"] == "example.com"
        assert result["deleted"] is True
        mock_delete.assert_called_once_with(domain="example.com") 