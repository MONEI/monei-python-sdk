import pytest
from unittest.mock import patch, MagicMock

from Monei.monei_client import MoneiClient
from Monei.api.payment_methods_api import PaymentMethodsApi


@pytest.mark.unit
class TestPaymentMethodsApiIntegration:
    """Integration tests for the Payment Methods API with mocked responses"""

    @pytest.fixture
    def mock_payment_method(self):
        """Fixture for a mock payment method response"""
        return {
            "id": "pm_123456789",
            "type": "card",
            "card": {
                "brand": "visa",
                "last4": "4242",
                "expMonth": 12,
                "expYear": 2025
            },
            "created": "2023-01-01T12:00:00Z"
        }

    @pytest.fixture
    def mock_client(self):
        """Fixture for creating a mock client"""
        return MoneiClient(api_key="test_api_key")

    @patch.object(PaymentMethodsApi, 'list')
    def test_list_payment_methods(self, mock_list, mock_client, mock_payment_method):
        """Test listing payment methods"""
        mock_list.return_value = {
            "data": [
                mock_payment_method,
                {
                    "id": "pm_987654321",
                    "type": "sepa",
                    "sepa": {
                        "iban": "DE89370400440532013000",
                        "last4": "3000"
                    },
                    "created": "2023-01-02T12:00:00Z"
                }
            ],
            "hasMore": False,
            "totalCount": 2
        }
        
        result = mock_client.PaymentMethods.list()
        
        assert "data" in result
        assert len(result["data"]) == 2
        assert result["data"][0]["id"] == "pm_123456789"
        assert result["data"][0]["type"] == "card"
        assert result["data"][1]["id"] == "pm_987654321"
        assert result["data"][1]["type"] == "sepa"
        assert result["hasMore"] is False
        assert result["totalCount"] == 2
        mock_list.assert_called_once()

    @patch.object(PaymentMethodsApi, 'get')
    def test_get_payment_method(self, mock_get, mock_client, mock_payment_method):
        """Test retrieving a payment method"""
        mock_get.return_value = mock_payment_method
        
        result = mock_client.PaymentMethods.get(payment_method_id="pm_123456789")
        
        assert result["id"] == "pm_123456789"
        assert result["type"] == "card"
        assert result["card"]["brand"] == "visa"
        assert result["card"]["last4"] == "4242"
        mock_get.assert_called_once_with(payment_method_id="pm_123456789")

    @patch.object(PaymentMethodsApi, 'delete')
    def test_delete_payment_method(self, mock_delete, mock_client):
        """Test deleting a payment method"""
        mock_delete.return_value = {
            "id": "pm_123456789",
            "deleted": True
        }
        
        result = mock_client.PaymentMethods.delete(payment_method_id="pm_123456789")
        
        assert result["id"] == "pm_123456789"
        assert result["deleted"] is True
        mock_delete.assert_called_once_with(payment_method_id="pm_123456789")

    @patch.object(PaymentMethodsApi, 'list')
    def test_list_payment_methods_with_params(self, mock_list, mock_client, mock_payment_method):
        """Test listing payment methods with parameters"""
        mock_list.return_value = {
            "data": [mock_payment_method],
            "hasMore": False,
            "totalCount": 1
        }
        
        # Test with customer_id parameter
        result = mock_client.PaymentMethods.list(customer_id="cus_123456789")
        
        assert len(result["data"]) == 1
        assert result["data"][0]["id"] == "pm_123456789"
        mock_list.assert_called_with(customer_id="cus_123456789")
        
        # Test with type parameter
        mock_list.reset_mock()
        mock_list.return_value = {
            "data": [mock_payment_method],
            "hasMore": False,
            "totalCount": 1
        }
        
        result = mock_client.PaymentMethods.list(type="card")
        
        assert len(result["data"]) == 1
        assert result["data"][0]["type"] == "card"
        mock_list.assert_called_with(type="card")
        
        # Test with limit and starting_after parameters
        mock_list.reset_mock()
        mock_list.return_value = {
            "data": [mock_payment_method],
            "hasMore": True,
            "totalCount": 10
        }
        
        result = mock_client.PaymentMethods.list(limit=1, starting_after="pm_000000000")
        
        assert len(result["data"]) == 1
        assert result["hasMore"] is True
        mock_list.assert_called_with(limit=1, starting_after="pm_000000000") 