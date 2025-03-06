import pytest
from unittest.mock import patch, MagicMock
import json

from Monei.api_client import ApiClient
from Monei.configuration import Configuration
from Monei.exceptions import ApiException
from Monei.rest import RESTResponse


@pytest.mark.unit
class TestApiClientIntegration:
    """Integration tests for the API client with mocked responses"""

    @pytest.fixture
    def mock_api_client(self):
        """Fixture for creating a mock API client"""
        config = Configuration()
        config.api_key["Authorization"] = "test_api_key"
        return ApiClient(configuration=config)

    @pytest.fixture
    def mock_response(self):
        """Fixture for creating a mock response"""
        mock_resp = MagicMock(spec=RESTResponse)
        mock_resp.getheaders.return_value = {"Content-Type": "application/json"}
        mock_resp.status = 200
        return mock_resp

    def test_deserialize_json_response(self, mock_api_client, mock_response):
        """Test deserializing a JSON response"""
        payment_data = {
            "id": "pay_123456789",
            "amount": 1000,
            "currency": "EUR",
            "status": "PENDING",
        }
        mock_response.data = json.dumps(payment_data).encode("utf-8")

        result = mock_api_client.deserialize(mock_response, "Payment")

        assert result == payment_data

    def test_deserialize_empty_response(self, mock_api_client, mock_response):
        """Test deserializing an empty response"""
        mock_response.data = b""

        result = mock_api_client.deserialize(mock_response, "Payment")

        assert result is None

    def test_deserialize_non_json_response(self, mock_api_client, mock_response):
        """Test deserializing a non-JSON response"""
        mock_response.getheaders.return_value = {"Content-Type": "text/plain"}
        mock_response.data = b"Not a JSON response"

        with pytest.raises(ApiException) as excinfo:
            mock_api_client.deserialize(mock_response, "Payment")

        assert "Content type 'text/plain' is not supported" in str(excinfo.value)

    @patch.object(ApiClient, "request")
    def test_call_api_success(self, mock_request, mock_api_client, mock_response):
        """Test successful API call"""
        payment_data = {
            "id": "pay_123456789",
            "amount": 1000,
            "currency": "EUR",
            "status": "PENDING",
        }
        mock_response.data = json.dumps(payment_data).encode("utf-8")
        mock_request.return_value = mock_response

        data, status, headers = mock_api_client.call_api(
            "/payments",
            "POST",
            path_params={},
            query_params={},
            header_params={},
            body={"amount": 1000, "currency": "EUR"},
            post_params=[],
            files={},
            response_type="Payment",
            auth_settings=["apiKey"],
            async_req=False,
            _return_http_data_only=True,
            _preload_content=True,
            _request_timeout=None,
            collection_formats={},
        )

        assert data == payment_data
        assert status == 200
        assert headers == {"Content-Type": "application/json"}

    @patch.object(ApiClient, "request")
    def test_call_api_error(self, mock_request, mock_api_client):
        """Test API call with error response"""
        error_response = {"statusCode": 400, "error": "Bad Request", "message": "Invalid amount"}

        mock_resp = MagicMock(spec=RESTResponse)
        mock_resp.getheaders.return_value = {"Content-Type": "application/json"}
        mock_resp.status = 400
        mock_resp.data = json.dumps(error_response).encode("utf-8")
        mock_request.return_value = mock_resp

        with pytest.raises(ApiException) as excinfo:
            mock_api_client.call_api(
                "/payments",
                "POST",
                path_params={},
                query_params={},
                header_params={},
                body={"amount": -1000, "currency": "EUR"},
                post_params=[],
                files={},
                response_type="Payment",
                auth_settings=["apiKey"],
                async_req=False,
                _return_http_data_only=True,
                _preload_content=True,
                _request_timeout=None,
                collection_formats={},
            )

        assert excinfo.value.status == 400
        assert "Invalid amount" in str(excinfo.value)

    def test_set_default_header(self, mock_api_client):
        """Test setting a default header"""
        mock_api_client.set_default_header("User-Agent", "CustomApp/1.0")

        assert "User-Agent" in mock_api_client.default_headers
        assert mock_api_client.default_headers["User-Agent"] == "CustomApp/1.0"

        # Test overwriting an existing header
        mock_api_client.set_default_header("User-Agent", "AnotherApp/2.0")
        assert mock_api_client.default_headers["User-Agent"] == "AnotherApp/2.0"

    def test_select_header_accept(self, mock_api_client):
        """Test selecting the Accept header"""
        # Test with supported content types
        accept = mock_api_client.select_header_accept(["application/json", "application/xml"])
        assert accept == "application/json, application/xml"

        # Test with no content types
        accept = mock_api_client.select_header_accept([])
        assert accept is None

    def test_select_header_content_type(self, mock_api_client):
        """Test selecting the Content-Type header"""
        # Test with supported content types
        content_type = mock_api_client.select_header_content_type(
            ["application/json", "application/xml"]
        )
        assert content_type == "application/json"

        # Test with no content types
        content_type = mock_api_client.select_header_content_type([])
        assert content_type == "application/json"
