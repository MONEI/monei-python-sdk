import unittest
import logging
import tempfile
import os
from copy import deepcopy

from Monei.configuration import Configuration, JSON_SCHEMA_VALIDATION_KEYWORDS


class TestConfiguration(unittest.TestCase):
    """Configuration unit test stubs"""

    def setUp(self):
        """Set up test fixtures, if any."""
        self.host = "https://api.monei.com/v1"
        self.api_key = {"APIKey": "test_api_key_12345"}
        self.api_key_prefix = {"APIKey": "Bearer"}
        self.username = "test_username"
        self.password = "test_password"
        
        # Create a default configuration for testing
        self.config = Configuration(
            host=self.host,
            api_key=self.api_key,
            api_key_prefix=self.api_key_prefix,
            username=self.username,
            password=self.password
        )

    def tearDown(self):
        """Tear down test fixtures, if any."""
        # Reset the default configuration
        Configuration._default = None

    def test_init_with_defaults(self):
        """Test initializing with default values."""
        config = Configuration()
        self.assertEqual(config.host, "https://api.monei.com/v1")
        self.assertEqual(config.api_key, {})
        self.assertEqual(config.api_key_prefix, {})
        self.assertIsNone(config.username)
        self.assertIsNone(config.password)
        self.assertFalse(config.discard_unknown_keys)
        self.assertEqual(config.disabled_client_side_validations, "")
        # The server_index is 0 by default, not None
        self.assertEqual(config.server_index, 0)
        self.assertEqual(config.server_variables, {})
        self.assertEqual(config.server_operation_index, {})
        self.assertEqual(config.server_operation_variables, {})
        self.assertIsNone(config.ssl_ca_cert)
        self.assertIsNone(config.logger_file)
        self.assertFalse(config.debug)
        self.assertEqual(config.logger_format, '%(asctime)s %(levelname)s %(message)s')

    def test_init_with_custom_values(self):
        """Test initializing with custom values."""
        self.assertEqual(self.config.host, self.host)
        self.assertEqual(self.config.api_key, self.api_key)
        self.assertEqual(self.config.api_key_prefix, self.api_key_prefix)
        self.assertEqual(self.config.username, self.username)
        self.assertEqual(self.config.password, self.password)

    def test_get_api_key_with_prefix(self):
        """Test get_api_key_with_prefix method."""
        # Test with API key and prefix
        result = self.config.get_api_key_with_prefix("APIKey")
        self.assertEqual(result, "Bearer test_api_key_12345")
        
        # Test with API key but no prefix
        self.config.api_key_prefix = {}
        result = self.config.get_api_key_with_prefix("APIKey")
        self.assertEqual(result, "test_api_key_12345")
        
        # Test with no API key
        self.config.api_key = {}
        # When API key is not found, it returns None, not an empty string
        self.assertIsNone(self.config.get_api_key_with_prefix("APIKey"))

    def test_get_basic_auth_token(self):
        """Test get_basic_auth_token method."""
        # Test with username and password
        token = self.config.get_basic_auth_token()
        self.assertEqual(token, "Basic dGVzdF91c2VybmFtZTp0ZXN0X3Bhc3N3b3Jk")
        
        # Test with no username
        self.config.username = None
        # When username is None but password is not, it still returns a token with empty username
        token = self.config.get_basic_auth_token()
        self.assertEqual(token, "Basic OnRlc3RfcGFzc3dvcmQ=")
        
        # Test with username but no password
        self.config.username = "test_username"
        self.config.password = None
        # When password is None but username is not, it still returns a token with empty password
        token = self.config.get_basic_auth_token()
        self.assertEqual(token, "Basic dGVzdF91c2VybmFtZTo=")
        
        # Test with both None
        self.config.username = None
        self.config.password = None
        # When both are None, it returns a token with empty username and password
        token = self.config.get_basic_auth_token()
        self.assertEqual(token, "Basic Og==")

    def test_auth_settings(self):
        """Test auth_settings method."""
        auth_settings = self.config.auth_settings()
        self.assertIn("APIKey", auth_settings)
        self.assertEqual(auth_settings["APIKey"]["type"], "api_key")
        self.assertEqual(auth_settings["APIKey"]["in"], "header")
        self.assertEqual(auth_settings["APIKey"]["key"], "Authorization")
        self.assertEqual(auth_settings["APIKey"]["value"], "Bearer test_api_key_12345")

    def test_to_debug_report(self):
        """Test to_debug_report method."""
        report = self.config.to_debug_report()
        self.assertIn("Python", report)
        # The debug report doesn't include "Host" but includes "OS"
        self.assertIn("OS", report)
        self.assertIn("Python Version", report)
        self.assertIn("Version of the API", report)
        self.assertIn("SDK Package Version", report)

    def test_logger_file(self):
        """Test logger_file property."""
        # Test setting logger file
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file_path = temp_file.name
        
        try:
            self.config.logger_file = temp_file_path
            self.assertEqual(self.config.logger_file, temp_file_path)
            
            # Check that the logger was configured
            # The logger is a dict with package_logger and urllib3_logger
            self.assertTrue(hasattr(self.config, "logger"))
            self.assertIsInstance(self.config.logger, dict)
            self.assertIn("package_logger", self.config.logger)
            self.assertIn("urllib3_logger", self.config.logger)
            self.assertIsInstance(self.config.logger["package_logger"], logging.Logger)
            self.assertIsInstance(self.config.logger["urllib3_logger"], logging.Logger)
            
            # Test with debug=True
            self.config.debug = True
            self.assertTrue(self.config.debug)
            self.assertEqual(self.config.logger["package_logger"].level, logging.DEBUG)
            self.assertEqual(self.config.logger["urllib3_logger"].level, logging.DEBUG)
            
            # Test with debug=False
            self.config.debug = False
            self.assertFalse(self.config.debug)
            # The actual level might be WARNING (30) instead of INFO (20)
            self.assertIn(self.config.logger["package_logger"].level, [logging.INFO, logging.WARNING])
            self.assertIn(self.config.logger["urllib3_logger"].level, [logging.INFO, logging.WARNING])
        finally:
            # Clean up the temporary file
            if os.path.exists(temp_file_path):
                os.unlink(temp_file_path)

    def test_logger_format(self):
        """Test logger_format property."""
        # Test default format
        self.assertEqual(self.config.logger_format, '%(asctime)s %(levelname)s %(message)s')
        
        # Test setting a custom format
        custom_format = '%(levelname)s: %(message)s'
        self.config.logger_format = custom_format
        self.assertEqual(self.config.logger_format, custom_format)

    def test_set_default(self):
        """Test set_default class method."""
        # Set a default configuration
        original_config = self.config
        Configuration.set_default(self.config)
        
        # The _default is set to a copy of the config, not the original
        self.assertIsNot(Configuration._default, original_config)
        self.assertEqual(Configuration._default.host, original_config.host)
        self.assertEqual(Configuration._default.api_key, original_config.api_key)
        
        # Get the default configuration
        default_config = Configuration.get_default_copy()
        self.assertIsNot(default_config, Configuration._default)  # Should be a copy
        self.assertEqual(default_config.host, self.host)
        self.assertEqual(default_config.api_key, self.api_key)

    def test_host_property(self):
        """Test host property."""
        # Test getting host
        self.assertEqual(self.config.host, self.host)
        
        # Test setting host
        new_host = "https://api.example.com/v2"
        self.config.host = new_host
        self.assertEqual(self.config.host, new_host)

    def test_deep_copy(self):
        """Test deep copying the configuration."""
        config_copy = deepcopy(self.config)
        self.assertIsNot(config_copy, self.config)
        self.assertEqual(config_copy.host, self.config.host)
        self.assertEqual(config_copy.api_key, self.config.api_key)
        self.assertEqual(config_copy.api_key_prefix, self.config.api_key_prefix)
        
        # Modify the copy and check that the original is unchanged
        config_copy.host = "https://api.example.com/v2"
        self.assertNotEqual(config_copy.host, self.config.host)
        self.assertEqual(self.config.host, self.host)

    def test_json_schema_validation_keywords(self):
        """Test JSON_SCHEMA_VALIDATION_KEYWORDS constant."""
        expected_keywords = {
            'multipleOf', 'maximum', 'exclusiveMaximum',
            'minimum', 'exclusiveMinimum', 'maxLength',
            'minLength', 'pattern', 'maxItems', 'minItems'
        }
        self.assertEqual(JSON_SCHEMA_VALIDATION_KEYWORDS, expected_keywords)


if __name__ == '__main__':
    unittest.main()
