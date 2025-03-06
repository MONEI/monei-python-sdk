import pytest
import hmac
import hashlib
import json
from unittest.mock import patch, MagicMock

from Monei.monei_client import MoneiClient
from Monei.exceptions import ApiException
from Monei.api.payments_api import PaymentsApi
from Monei.api.payment_methods_api import PaymentMethodsApi
from Monei.api.subscriptions_api import SubscriptionsApi
from Monei.api.apple_pay_domain_api import ApplePayDomainApi
from Monei.api.bizum_api import BizumApi


@pytest.mark.unit
class TestMoneiClient:
    """Tests for the MoneiClient class"""

    def test_init_with_api_key(self):
        """Test initializing the client with an API key"""
        client = MoneiClient(api_key="test_api_key")
        assert client.api_key == "test_api_key"
        assert client.account_id is None
        assert "MONEI/Python" in client.user_agent
        assert isinstance(client.Payments, PaymentsApi)
        assert isinstance(client.PaymentMethods, PaymentMethodsApi)
        assert isinstance(client.Subscriptions, SubscriptionsApi)
        assert isinstance(client.ApplePayDomain, ApplePayDomainApi)
        assert isinstance(client.Bizum, BizumApi)
        # Test alias
        assert client.payments is client.Payments

    def test_init_with_account_id_and_user_agent(self):
        """Test initializing the client with an account ID and custom user agent"""
        client = MoneiClient(
            api_key="test_api_key",
            account_id="acc_123456789",
            user_agent="CustomApp/1.0"
        )
        assert client.api_key == "test_api_key"
        assert client.account_id == "acc_123456789"
        assert client.user_agent == "CustomApp/1.0"
        assert "MONEI-Account-ID" in client._api_client.default_headers
        assert client._api_client.default_headers["MONEI-Account-ID"] == "acc_123456789"

    def test_init_with_account_id_without_user_agent_raises_exception(self):
        """Test that initializing with account_id but no user_agent raises an exception"""
        with pytest.raises(ApiException) as excinfo:
            MoneiClient(api_key="test_api_key", account_id="acc_123456789")
        assert "User-Agent must be provided" in str(excinfo.value)

    def test_set_account_id_with_user_agent(self):
        """Test setting account ID after initialization with custom user agent"""
        client = MoneiClient(api_key="test_api_key", user_agent="CustomApp/1.0")
        client.set_account_id("acc_123456789")
        assert client.account_id == "acc_123456789"
        # Check that the header was set in the API client
        assert client._api_client.default_headers.get("MONEI-Account-ID") == "acc_123456789"

    def test_set_account_id_without_user_agent_raises_exception(self):
        """Test that setting account_id without a custom user_agent raises an exception"""
        client = MoneiClient(api_key="test_api_key")
        with pytest.raises(ApiException) as excinfo:
            client.set_account_id("acc_123456789")
        assert "User-Agent must be set" in str(excinfo.value)

    def test_set_user_agent(self):
        """Test setting a custom user agent"""
        client = MoneiClient(api_key="test_api_key")
        client.set_user_agent("CustomApp/1.0")
        assert client.user_agent == "CustomApp/1.0"
        assert client._api_client.user_agent == "CustomApp/1.0"

    def test_verify_signature_valid(self):
        """Test verifying a valid signature"""
        client = MoneiClient(api_key="test_api_key")
        body = '{"event":"payment.created","data":{"id":"pay_123"}}'
        
        # Calculate a valid signature
        timestamp = "1620000000000"
        calculated_hmac = hmac.new(
            bytes("test_api_key", "utf-8"),
            msg=bytes(f"{timestamp}.{body}", "utf-8"),
            digestmod=hashlib.sha256
        ).hexdigest()
        
        signature = f"t={timestamp},v1={calculated_hmac}"
        
        # Verify the signature
        result = client.verify_signature(body, signature)
        assert result == {"event": "payment.created", "data": {"id": "pay_123"}}

    def test_verify_signature_invalid(self):
        """Test verifying an invalid signature"""
        client = MoneiClient(api_key="test_api_key")
        body = '{"event":"payment.created","data":{"id":"pay_123"}}'
        signature = "t=1620000000000,v1=invalid_signature"
        
        with pytest.raises(ApiException) as excinfo:
            client.verify_signature(body, signature)
        assert "Signature verification failed" in str(excinfo.value)
        
    def test_remove_account_id(self):
        """Test removing the account ID"""
        client = MoneiClient(api_key="test_api_key", user_agent="CustomApp/1.0", account_id="acc_123456789")
        assert client.account_id == "acc_123456789"
        assert "MONEI-Account-ID" in client._api_client.default_headers
        
        # Remove account ID
        client.set_account_id(None)
        assert client.account_id is None
        assert "MONEI-Account-ID" not in client._api_client.default_headers 