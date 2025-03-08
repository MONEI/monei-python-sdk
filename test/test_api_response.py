import unittest
from typing import Dict, List, Optional
from Monei.api_response import ApiResponse


class TestApiResponse(unittest.TestCase):
    """ApiResponse unit test stubs"""

    def setUp(self):
        """Set up test fixtures, if any."""
        self.status_code = 200
        self.headers = {"Content-Type": "application/json", "X-Request-ID": "req_123456"}
        self.data = {"id": "pay_123456", "amount": 1000, "currency": "EUR"}
        self.raw_data = b'{"id":"pay_123456","amount":1000,"currency":"EUR"}'

    def tearDown(self):
        """Tear down test fixtures, if any."""
        pass

    def test_create_api_response(self):
        """Test creating an ApiResponse object."""
        response = ApiResponse[Dict](
            status_code=self.status_code,
            headers=self.headers,
            data=self.data,
            raw_data=self.raw_data
        )
        
        self.assertEqual(response.status_code, self.status_code)
        self.assertEqual(response.headers, self.headers)
        self.assertEqual(response.data, self.data)
        self.assertEqual(response.raw_data, self.raw_data)

    def test_create_api_response_without_headers(self):
        """Test creating an ApiResponse object without headers."""
        response = ApiResponse[Dict](
            status_code=self.status_code,
            data=self.data,
            raw_data=self.raw_data
        )
        
        self.assertEqual(response.status_code, self.status_code)
        self.assertIsNone(response.headers)
        self.assertEqual(response.data, self.data)
        self.assertEqual(response.raw_data, self.raw_data)

    def test_api_response_with_list_data(self):
        """Test ApiResponse with list data."""
        list_data = [{"id": "pay_1"}, {"id": "pay_2"}]
        raw_list_data = b'[{"id":"pay_1"},{"id":"pay_2"}]'
        
        response = ApiResponse[List[Dict]](
            status_code=self.status_code,
            headers=self.headers,
            data=list_data,
            raw_data=raw_list_data
        )
        
        self.assertEqual(response.status_code, self.status_code)
        self.assertEqual(response.headers, self.headers)
        self.assertEqual(response.data, list_data)
        self.assertEqual(response.raw_data, raw_list_data)

    def test_api_response_with_primitive_data(self):
        """Test ApiResponse with primitive data."""
        string_data = "Success"
        raw_string_data = b'"Success"'
        
        response = ApiResponse[str](
            status_code=self.status_code,
            headers=self.headers,
            data=string_data,
            raw_data=raw_string_data
        )
        
        self.assertEqual(response.status_code, self.status_code)
        self.assertEqual(response.headers, self.headers)
        self.assertEqual(response.data, string_data)
        self.assertEqual(response.raw_data, raw_string_data)

    def test_api_response_with_none_data(self):
        """Test ApiResponse with None data."""
        response = ApiResponse[Optional[Dict]](
            status_code=204,
            headers=self.headers,
            data=None,
            raw_data=b''
        )
        
        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.headers, self.headers)
        self.assertIsNone(response.data)
        self.assertEqual(response.raw_data, b'') 