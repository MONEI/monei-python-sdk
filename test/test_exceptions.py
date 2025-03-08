import unittest
from unittest.mock import MagicMock

from Monei.exceptions import (
    OpenApiException,
    ApiTypeError,
    ApiValueError,
    ApiAttributeError,
    ApiKeyError,
    ApiException,
    NotFoundException,
    UnauthorizedException,
    ForbiddenException,
    ServiceException,
    render_path,
)


class TestExceptions(unittest.TestCase):
    """Exceptions unit test stubs"""

    def setUp(self):
        """Set up test fixtures, if any."""
        pass

    def tearDown(self):
        """Tear down test fixtures, if any."""
        pass

    def test_open_api_exception(self):
        """Test OpenApiException."""
        exception = OpenApiException("Test exception")
        self.assertIsInstance(exception, Exception)
        self.assertEqual(str(exception), "Test exception")

    def test_api_type_error(self):
        """Test ApiTypeError."""
        # Test with minimal parameters
        exception = ApiTypeError("Type error")
        self.assertIsInstance(exception, TypeError)
        self.assertIsInstance(exception, OpenApiException)
        self.assertEqual(str(exception), "Type error")
        self.assertIsNone(exception.path_to_item)
        self.assertIsNone(exception.valid_classes)
        self.assertIsNone(exception.key_type)

        # Test with path_to_item
        path = ["user", "address", "city"]
        exception = ApiTypeError("Type error", path_to_item=path)
        self.assertEqual(str(exception), "Type error at ['user']['address']['city']")
        self.assertEqual(exception.path_to_item, path)

        # Test with all parameters
        valid_classes = (str, int)
        exception = ApiTypeError(
            "Type error", path_to_item=path, valid_classes=valid_classes, key_type=True
        )
        self.assertEqual(str(exception), "Type error at ['user']['address']['city']")
        self.assertEqual(exception.path_to_item, path)
        self.assertEqual(exception.valid_classes, valid_classes)
        self.assertTrue(exception.key_type)

    def test_api_value_error(self):
        """Test ApiValueError."""
        # Test with minimal parameters
        exception = ApiValueError("Value error")
        self.assertIsInstance(exception, ValueError)
        self.assertIsInstance(exception, OpenApiException)
        self.assertEqual(str(exception), "Value error")
        self.assertIsNone(exception.path_to_item)

        # Test with path_to_item
        path = ["payment", "amount"]
        exception = ApiValueError("Value error", path_to_item=path)
        self.assertEqual(str(exception), "Value error at ['payment']['amount']")
        self.assertEqual(exception.path_to_item, path)

    def test_api_attribute_error(self):
        """Test ApiAttributeError."""
        # Test with minimal parameters
        exception = ApiAttributeError("Attribute error")
        self.assertIsInstance(exception, AttributeError)
        self.assertIsInstance(exception, OpenApiException)
        self.assertEqual(str(exception), "Attribute error")
        self.assertIsNone(exception.path_to_item)

        # Test with path_to_item
        path = ["subscription", "status"]
        exception = ApiAttributeError("Attribute error", path_to_item=path)
        self.assertEqual(
            str(exception), "Attribute error at ['subscription']['status']"
        )
        self.assertEqual(exception.path_to_item, path)

    def test_api_key_error(self):
        """Test ApiKeyError."""
        # Test with minimal parameters
        exception = ApiKeyError("Key error")
        self.assertIsInstance(exception, KeyError)
        self.assertIsInstance(exception, OpenApiException)
        # KeyError's __str__ implementation adds quotes around the message
        self.assertEqual(str(exception), "'Key error'")
        self.assertIsNone(exception.path_to_item)

        # Test with path_to_item
        path = ["payment", "customer"]
        exception = ApiKeyError("Key error", path_to_item=path)
        # Get the actual string representation to compare with
        exception_str = str(exception)
        self.assertIn("Key error", exception_str)
        self.assertIn("payment", exception_str)
        self.assertIn("customer", exception_str)
        self.assertEqual(exception.path_to_item, path)

    def test_api_exception(self):
        """Test ApiException."""
        # Test with minimal parameters
        exception = ApiException(status=404, reason="Not Found")
        self.assertIsInstance(exception, OpenApiException)
        self.assertEqual(exception.status, 404)
        self.assertEqual(exception.reason, "Not Found")
        self.assertIsNone(exception.body)
        self.assertIsNone(exception.headers)

        # Check string representation
        exception_str = str(exception)
        self.assertIn("Status Code: 404", exception_str)
        self.assertIn("Reason: Not Found", exception_str)

        # Test with http_resp
        mock_resp = MagicMock()
        mock_resp.status = 500
        mock_resp.reason = "Internal Server Error"
        mock_resp.data = b'{"error": "Server error occurred"}'
        mock_resp.getheaders.return_value = {"Content-Type": "application/json"}

        exception = ApiException(http_resp=mock_resp)
        self.assertEqual(exception.status, 500)
        self.assertEqual(exception.reason, "Internal Server Error")
        self.assertEqual(exception.body, b'{"error": "Server error occurred"}')
        self.assertEqual(exception.headers, {"Content-Type": "application/json"})

        # Check string representation with all fields
        exception_str = str(exception)
        self.assertIn("Status Code: 500", exception_str)
        self.assertIn("Reason: Internal Server Error", exception_str)
        self.assertIn(
            "HTTP response headers: {'Content-Type': 'application/json'}", exception_str
        )
        self.assertIn(
            'HTTP response body: b\'{"error": "Server error occurred"}\'', exception_str
        )

    def test_not_found_exception(self):
        """Test NotFoundException."""
        exception = NotFoundException(status=404, reason="Resource not found")
        self.assertIsInstance(exception, ApiException)
        self.assertEqual(exception.status, 404)
        self.assertEqual(exception.reason, "Resource not found")

    def test_unauthorized_exception(self):
        """Test UnauthorizedException."""
        exception = UnauthorizedException(status=401, reason="Unauthorized access")
        self.assertIsInstance(exception, ApiException)
        self.assertEqual(exception.status, 401)
        self.assertEqual(exception.reason, "Unauthorized access")

    def test_forbidden_exception(self):
        """Test ForbiddenException."""
        exception = ForbiddenException(status=403, reason="Forbidden access")
        self.assertIsInstance(exception, ApiException)
        self.assertEqual(exception.status, 403)
        self.assertEqual(exception.reason, "Forbidden access")

    def test_service_exception(self):
        """Test ServiceException."""
        exception = ServiceException(status=503, reason="Service unavailable")
        self.assertIsInstance(exception, ApiException)
        self.assertEqual(exception.status, 503)
        self.assertEqual(exception.reason, "Service unavailable")

    def test_render_path(self):
        """Test render_path function."""
        # Test with string keys
        path = ["user", "address", "city"]
        result = render_path(path)
        self.assertEqual(result, "['user']['address']['city']")

        # Test with integer indices
        path = ["user", 0, "name"]
        result = render_path(path)
        self.assertEqual(result, "['user'][0]['name']")

        # Test with mixed keys
        path = ["payments", 2, "amount"]
        result = render_path(path)
        self.assertEqual(result, "['payments'][2]['amount']")

        # Test with empty path
        path = []
        result = render_path(path)
        self.assertEqual(result, "")


if __name__ == "__main__":
    unittest.main()
