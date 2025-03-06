"""
Pytest configuration file with fixtures for testing the MONEI Python SDK.
"""

import pytest
from unittest.mock import MagicMock, patch


@pytest.fixture
def api_key():
    """Return a test API key."""
    return "test_api_key_12345"


@pytest.fixture
def monei_client(api_key):
    """Return a MONEI client instance with a test API key."""
    # Import here to avoid circular imports
    from Monei import MoneiClient
    return MoneiClient(api_key=api_key)


@pytest.fixture
def mock_response():
    """Return a mock response object."""
    mock = MagicMock()
    mock.status_code = 200
    mock.json.return_value = {"success": True}
    return mock


@pytest.fixture
def mock_payment_response():
    """Return a mock payment response."""
    return {
        "id": "pay_test123456789",
        "amount": 1250,
        "currency": "EUR",
        "status": "COMPLETED",
        "orderId": "order_123",
        "description": "Test payment",
        "customer": {"email": "test@example.com", "name": "Test Customer"},
        "createdAt": "2023-01-01T12:00:00.000Z",
        "updatedAt": "2023-01-01T12:01:00.000Z",
    }


@pytest.fixture
def mock_error_response():
    """Return a mock error response."""
    return {
        "error": {
            "code": "invalid_request",
            "message": "Invalid request parameters",
            "param": "amount",
        }
    }


@pytest.fixture
def mock_http_client():
    """Return a mock HTTP client."""
    with patch("Monei.api_client.ApiClient.request") as mock_request:
        yield mock_request
