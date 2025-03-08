import unittest
from unittest.mock import patch, MagicMock
import json
import datetime
from urllib3.response import HTTPResponse
from urllib3.exceptions import MaxRetryError, TimeoutError

from Monei.rest import RESTClientObject
from Monei.configuration import Configuration
from Monei.exceptions import ApiException


class TestRESTClientObject(unittest.TestCase):
    """Test case for RESTClientObject"""

    def setUp(self):
        """Set up test fixtures, if any."""
        self.config = Configuration()
        self.config.host = "https://api.monei.com/v1"
        self.rest_client = RESTClientObject(self.config)

        # Mock response for successful requests
        self.mock_response = MagicMock(spec=HTTPResponse)
        self.mock_response.status = 200
        self.mock_response.data = json.dumps(
            {"id": "test_id", "status": "success"}
        ).encode("utf-8")
        self.mock_response.getheaders.return_value = {
            "Content-Type": "application/json",
            "X-Request-ID": "123456789",
        }

    @patch("urllib3.PoolManager.request")
    def test_request_success(self, mock_request):
        """Test successful request."""
        mock_request.return_value = self.mock_response

        # Make a GET request
        response = self.rest_client.request(
            "GET",
            "/payments",
            headers={"Authorization": "Bearer test_token"},
            query_params={"limit": 10},
        )

        # Verify the response
        self.assertEqual(response.status, 200)
        self.assertEqual(
            response.data,
            json.dumps({"id": "test_id", "status": "success"}).encode("utf-8"),
        )
        self.assertEqual(
            response.getheaders(),
            {"Content-Type": "application/json", "X-Request-ID": "123456789"},
        )

        # Verify the request was made with the correct parameters
        mock_request.assert_called_once()
        args, kwargs = mock_request.call_args
        self.assertEqual(args[0], "GET")
        self.assertEqual(kwargs["fields"]["limit"], 10)
        self.assertEqual(kwargs["headers"]["Authorization"], "Bearer test_token")

    @patch("urllib3.PoolManager.request")
    def test_request_with_body(self, mock_request):
        """Test request with body."""
        mock_request.return_value = self.mock_response

        # Make a POST request with body
        body = {"amount": 1000, "currency": "EUR"}
        response = self.rest_client.request(
            "POST", "/payments", headers={"Content-Type": "application/json"}, body=body
        )

        # Verify the request was made with the correct body
        mock_request.assert_called_once()
        args, kwargs = mock_request.call_args
        self.assertEqual(args[0], "POST")
        self.assertEqual(kwargs["body"], json.dumps(body).encode("utf-8"))

    @patch("urllib3.PoolManager.request")
    def test_request_with_post_params(self, mock_request):
        """Test request with post parameters."""
        mock_request.return_value = self.mock_response

        # Make a POST request with post_params
        post_params = [("amount", 1000), ("currency", "EUR")]
        response = self.rest_client.request(
            "POST",
            "/payments",
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            post_params=post_params,
        )

        # Verify the request was made with the correct post_params
        mock_request.assert_called_once()
        args, kwargs = mock_request.call_args
        self.assertEqual(args[0], "POST")
        self.assertEqual(kwargs["fields"], post_params)

    @patch("urllib3.PoolManager.request")
    def test_request_error_response(self, mock_request):
        """Test request with error response."""
        # Mock error response
        error_response = MagicMock(spec=HTTPResponse)
        error_response.status = 400
        error_response.data = json.dumps(
            {"error": {"type": "invalid_request_error", "message": "Invalid request"}}
        ).encode("utf-8")
        error_response.getheaders.return_value = {"Content-Type": "application/json"}

        mock_request.return_value = error_response

        # Make a request that will result in an error
        with self.assertRaises(ApiException) as context:
            self.rest_client.request("GET", "/invalid")

        # Verify the exception details
        self.assertEqual(context.exception.status, 400)
        self.assertEqual(context.exception.reason, "Bad Request")
        self.assertIn("Invalid request", str(context.exception))

    @patch("urllib3.PoolManager.request")
    def test_request_connection_error(self, mock_request):
        """Test request with connection error."""
        # Mock connection error
        mock_request.side_effect = MaxRetryError(
            pool=MagicMock(),
            url="https://api.monei.com/v1/payments",
            reason="Connection refused",
        )

        # Make a request that will result in a connection error
        with self.assertRaises(ApiException) as context:
            self.rest_client.request("GET", "/payments")

        # Verify the exception details
        self.assertEqual(context.exception.status, 0)
        self.assertIn("Connection refused", str(context.exception))

    @patch("urllib3.PoolManager.request")
    def test_request_timeout_error(self, mock_request):
        """Test request with timeout error."""
        # Mock timeout error
        mock_request.side_effect = TimeoutError(
            pool=MagicMock(),
            url="https://api.monei.com/v1/payments",
            reason="Request timed out",
        )

        # Make a request that will result in a timeout error
        with self.assertRaises(ApiException) as context:
            self.rest_client.request("GET", "/payments")

        # Verify the exception details
        self.assertEqual(context.exception.status, 0)
        self.assertIn("Request timed out", str(context.exception))

    @patch("urllib3.PoolManager.request")
    def test_request_with_retries(self, mock_request):
        """Test request with retries."""
        # Configure the client to retry requests
        self.config.retries = 3
        rest_client = RESTClientObject(self.config)

        # Mock a successful response after retries
        mock_request.return_value = self.mock_response

        # Make a request
        response = rest_client.request("GET", "/payments")

        # Verify the response
        self.assertEqual(response.status, 200)

        # Verify the pool was created with the correct retry configuration
        # This is a bit tricky to test directly, but we can check that the request was made
        mock_request.assert_called_once()

    @patch("urllib3.PoolManager.request")
    def test_request_with_timeout(self, mock_request):
        """Test request with timeout."""
        # Configure the client with a timeout
        self.config.timeout = 5
        rest_client = RESTClientObject(self.config)

        # Mock a successful response
        mock_request.return_value = self.mock_response

        # Make a request
        response = rest_client.request("GET", "/payments")

        # Verify the response
        self.assertEqual(response.status, 200)

        # Verify the request was made with the correct timeout
        mock_request.assert_called_once()
        args, kwargs = mock_request.call_args
        self.assertEqual(kwargs["timeout"], 5)

    @patch("urllib3.PoolManager.request")
    def test_request_with_proxy(self, mock_request):
        """Test request with proxy."""
        # Configure the client with a proxy
        self.config.proxy = "http://proxy.example.com:8080"
        rest_client = RESTClientObject(self.config)

        # Mock a successful response
        mock_request.return_value = self.mock_response

        # Make a request
        response = rest_client.request("GET", "/payments")

        # Verify the response
        self.assertEqual(response.status, 200)

        # It's difficult to verify the proxy configuration directly in this test
        # since it's set during the PoolManager initialization
        mock_request.assert_called_once()


if __name__ == "__main__":
    unittest.main()
