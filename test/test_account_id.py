import unittest
import pytest
from Monei import MoneiClient, ApiException


class TestAccountId(unittest.TestCase):
    """Test case for accountId and user agent functionality"""

    def test_init_with_account_id_no_user_agent(self):
        """Test initialization with account_id but no custom user_agent"""
        with pytest.raises(ApiException) as excinfo:
            MoneiClient(api_key="test_key", account_id="test_account_id")
        assert "User-Agent must be provided when using Account ID" in str(excinfo.value)

    def test_init_with_account_id_and_user_agent(self):
        """Test initialization with account_id and custom user_agent"""
        client = MoneiClient(
            api_key="test_key", account_id="test_account_id", user_agent="TestApp/1.0.0"
        )
        assert client.account_id == "test_account_id"
        assert client.user_agent == "TestApp/1.0.0"
        assert client._api_client.default_headers["User-Agent"] == "TestApp/1.0.0"
        assert client._api_client.default_headers["MONEI-Account-ID"] == "test_account_id"

    def test_set_account_id_no_user_agent(self):
        """Test setting account_id without custom user_agent"""
        client = MoneiClient(api_key="test_key")
        with pytest.raises(ApiException) as excinfo:
            client.set_account_id("test_account_id")
        assert "User-Agent must be set before using Account ID" in str(excinfo.value)

    def test_set_account_id_with_user_agent(self):
        """Test setting account_id with custom user_agent"""
        client = MoneiClient(api_key="test_key", user_agent="TestApp/1.0.0")
        client.set_account_id("test_account_id")
        assert client.account_id == "test_account_id"
        assert client._api_client.default_headers["MONEI-Account-ID"] == "test_account_id"

    def test_set_user_agent(self):
        """Test setting user_agent"""
        client = MoneiClient(api_key="test_key")
        client.set_user_agent("TestApp/1.0.0")
        assert client.user_agent == "TestApp/1.0.0"
        assert client._api_client.default_headers["User-Agent"] == "TestApp/1.0.0"

    def test_remove_account_id(self):
        """Test removing account_id"""
        client = MoneiClient(
            api_key="test_key", account_id="test_account_id", user_agent="TestApp/1.0.0"
        )
        assert "MONEI-Account-ID" in client._api_client.default_headers

        client.set_account_id(None)
        assert client.account_id is None
        assert "MONEI-Account-ID" not in client._api_client.default_headers


if __name__ == "__main__":
    unittest.main()
