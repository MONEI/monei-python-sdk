import unittest
from unittest.mock import patch, MagicMock

from Monei.monei_client import MoneiClient, DEFAULT_USER_AGENT
from Monei.exceptions import ApiException
from Monei.api.payments_api import PaymentsApi
from Monei.api.payment_methods_api import PaymentMethodsApi
from Monei.api.subscriptions_api import SubscriptionsApi
from Monei.api.apple_pay_domain_api import ApplePayDomainApi
from Monei.api.bizum_api import BizumApi


SIGNED_BODY = '{"id":"af6029f80f5fc73a8ad2753eea0b1be0","status":"SUCCEEDED"}'
SIGNED_OBJECT = {"id": "af6029f80f5fc73a8ad2753eea0b1be0", "status": "SUCCEEDED"}
# The test vector of the signing v2 plan, shared with the PHP and Node SDKs.
# HMAC-SHA256 of "1794643200." + SIGNED_BODY keyed with OLD_SECRET.
V2_SIGNATURE = "8a1968e508d090894e64e50a3162dd9920feec2d4c1d04c385e80f08532226cf"
# HMAC-SHA256 of "1794643200." + SIGNED_BODY keyed with NEW_SECRET.
V2_NEW_SIGNATURE = "e32c238b644e5786f51b2b7205994f2a0d44d56375df5d8bf86d9579a96e0210"
# HMAC-SHA256 of "1794643200." + SIGNED_BODY keyed with the test API key.
V1_SIGNATURE = "10e89af576f82b2601c7ef566b4f048f5efddb4220993a628236e5cb3789bb55"
# The secrets are concatenated so that secret scanners do not flag these test values.
OLD_SECRET = "whsec" + "_dGVzdC1zaWduaW5nLXNlY3JldC1mb3ItdjItdmVjdG9y"
NEW_SECRET = "whsec" + "_bmV3LXNpZ25pbmctc2VjcmV0LWFmdGVyLXRoZS1yb2xs"


class TestMoneiClient(unittest.TestCase):
    """MoneiClient unit test stubs"""

    def setUp(self):
        """Set up test fixtures, if any."""
        self.api_key = "test_api_key_12345"
        self.account_id = "test_account_id_67890"
        self.user_agent = "MONEI/TestPlatform/1.0.0"

    def tearDown(self):
        """Tear down test fixtures, if any."""
        pass

    def test_init_with_api_key_only(self):
        """Test initializing with API key only."""
        client = MoneiClient(api_key=self.api_key)
        self.assertIsInstance(client, MoneiClient)
        self.assertEqual(client.api_key, self.api_key)
        self.assertEqual(client.user_agent, DEFAULT_USER_AGENT)
        self.assertIsNone(client.account_id)

        # Check API instances are initialized
        self.assertIsInstance(client.Payments, PaymentsApi)
        self.assertIsInstance(client.PaymentMethods, PaymentMethodsApi)
        self.assertIsInstance(client.Subscriptions, SubscriptionsApi)
        self.assertIsInstance(client.ApplePayDomain, ApplePayDomainApi)
        self.assertIsInstance(client.Bizum, BizumApi)

        # Check aliases
        self.assertEqual(client.payments, client.Payments)
        self.assertEqual(client.payment_methods, client.PaymentMethods)
        self.assertEqual(client.subscriptions, client.Subscriptions)
        self.assertEqual(client.apple_pay_domain, client.ApplePayDomain)
        self.assertEqual(client.bizum, client.Bizum)

        # Check that the API key is correctly set in the configuration
        self.assertEqual(client.config.api_key["APIKey"], self.api_key)

    def test_init_with_account_id_and_user_agent(self):
        """Test initializing with API key, account ID, and user agent."""
        client = MoneiClient(
            api_key=self.api_key, account_id=self.account_id, user_agent=self.user_agent
        )
        self.assertIsInstance(client, MoneiClient)
        self.assertEqual(client.api_key, self.api_key)
        self.assertEqual(client.account_id, self.account_id)
        self.assertEqual(client.user_agent, self.user_agent)

    def test_init_with_account_id_without_user_agent(self):
        """Test initializing with account ID but without user agent should raise an exception."""
        with self.assertRaises(ApiException) as context:
            MoneiClient(api_key=self.api_key, account_id=self.account_id)
        self.assertEqual(context.exception.status, 400)
        self.assertEqual(
            context.exception.reason,
            "User-Agent must be provided when using Account ID",
        )

    def test_set_account_id(self):
        """Test setting account ID after initialization."""
        client = MoneiClient(api_key=self.api_key, user_agent=self.user_agent)
        client.set_account_id(self.account_id)
        self.assertEqual(client.account_id, self.account_id)

    def test_set_account_id_without_user_agent(self):
        """Test setting account ID without setting user agent first should raise an exception."""
        client = MoneiClient(api_key=self.api_key)
        with self.assertRaises(ApiException) as context:
            client.set_account_id(self.account_id)
        self.assertEqual(context.exception.status, 400)
        self.assertEqual(
            context.exception.reason, "User-Agent must be set before using Account ID"
        )

    def test_set_account_id_to_none(self):
        """Test setting account ID to None should remove the header."""
        client = MoneiClient(api_key=self.api_key, user_agent=self.user_agent)
        client.set_account_id(self.account_id)
        self.assertEqual(client.account_id, self.account_id)

        # Now set it to None
        client.set_account_id(None)
        self.assertIsNone(client.account_id)

    def test_set_user_agent(self):
        """Test setting user agent after initialization."""
        client = MoneiClient(api_key=self.api_key)
        client.set_user_agent(self.user_agent)
        self.assertEqual(client.user_agent, self.user_agent)

    def test_api_key_in_configuration(self):
        """Test that the API key is correctly set in the configuration."""
        # Create a client with a test API key
        client = MoneiClient(api_key=self.api_key)

        # Check that the API key is correctly set in the configuration
        self.assertEqual(client.config.api_key["APIKey"], self.api_key)

        # Check the auth_settings in the configuration
        auth_settings = client.config.auth_settings()
        self.assertIn("APIKey", auth_settings)
        self.assertEqual(auth_settings["APIKey"]["key"], "Authorization")
        self.assertEqual(auth_settings["APIKey"]["value"], self.api_key)

    def test_api_key_in_request_headers(self):
        """Test that the API key is correctly passed in the request headers."""
        # Create a client with a test API key
        client = MoneiClient(api_key=self.api_key)

        # Mock the RESTClientObject.request method to capture the headers
        with patch("Monei.rest.RESTClientObject.request") as mock_request:
            # Configure the mock to return a successful response
            mock_response = MagicMock()
            mock_response.status = 200
            mock_response.data = b"{}"
            mock_response.getheaders.return_value = {}
            mock_request.return_value = mock_response

            # Make a request using the client
            try:
                # Call a method that will make a real HTTP request
                client.payments.get("dummy_payment_id")
            except Exception:
                # We don't care about the actual API call, just the headers
                pass

            # Check that request was called
            mock_request.assert_called()

            # Get the headers from the call arguments
            call_args = mock_request.call_args
            headers = call_args[1].get("headers", {})

            # Verify that the Authorization header contains the API key
            self.assertIn("Authorization", headers)
            self.assertEqual(headers["Authorization"], self.api_key)

            # Verify that the User-Agent header is set
            self.assertIn("User-Agent", headers)
            self.assertEqual(headers["User-Agent"], client.user_agent)

    def test_user_agent_validation_before_request(self):
        """Test that the user agent is validated before making a request."""
        # Create a client with account_id but without custom user agent
        client = MoneiClient(api_key=self.api_key)

        # Set account_id after initialization but don't set user_agent
        # This should not raise an exception yet
        with patch("Monei.monei_client.ApiException") as mock_exception:
            client.account_id = self.account_id
            mock_exception.assert_not_called()

        # Now try to make a request, which should validate the user agent
        with self.assertRaises(ApiException) as context:
            # Directly call the validation function to test it
            client._api_client.call_api(
                "/payments/{id}",
                "GET",
                path_params={"id": "dummy_payment_id"},
                header_params={"Accept": "application/json"},
                auth_settings=["APIKey"],
            )

        # Check that the exception has the correct message
        self.assertEqual(context.exception.status, 400)
        self.assertEqual(
            context.exception.reason,
            "User-Agent must be provided when using Account ID",
        )

        # Now set a custom user agent and try again
        client.set_user_agent(self.user_agent)

        # Mock the __call_api method to avoid actual API calls
        with patch("Monei.api_client.ApiClient._ApiClient__call_api") as mock_call_api:
            mock_call_api.return_value = (None, 200, {})

            # This should not raise an exception now
            try:
                client._api_client.call_api(
                    "/payments/{id}",
                    "GET",
                    path_params={"id": "dummy_payment_id"},
                    header_params={"Accept": "application/json"},
                    auth_settings=["APIKey"],
                )
            except ApiException as e:
                if "User-Agent must be provided" in str(e):
                    self.fail(
                        "User agent validation failed even with custom user agent"
                    )

    def assert_unauthorized(self, signature, secret=None):
        client = MoneiClient(api_key=self.api_key)
        with self.assertRaises(ApiException) as context:
            client.verify_signature(SIGNED_BODY, signature, secret)
        self.assertEqual(context.exception.status, 401)
        self.assertEqual(
            context.exception.reason, "[401] Signature verification failed"
        )

    def test_verify_signature_v1_with_api_key(self):
        """Without a secret, v1 is checked with the API key and v2 is ignored."""
        client = MoneiClient(api_key=self.api_key)

        result = client.verify_signature(
            SIGNED_BODY, f"t=1794643200,v1={V1_SIGNATURE},v2={V2_SIGNATURE}"
        )

        self.assertEqual(result, SIGNED_OBJECT)

    def test_verify_signature_wrong_v1(self):
        self.assert_unauthorized("t=1794643200,v1=" + "0" * 64)

    def test_verify_signature_without_v1_and_secret(self):
        # v2 is valid for OLD_SECRET: only the missing secret makes it fail.
        self.assert_unauthorized(f"t=1794643200,v2={V2_SIGNATURE}")

    def test_verify_signature_v2_with_secret(self):
        """A header without v1 comes from an account without an API key."""
        client = MoneiClient(api_key=self.api_key)

        result = client.verify_signature(
            SIGNED_BODY, f"t=1794643200,v2={V2_SIGNATURE}", OLD_SECRET
        )

        self.assertEqual(result, SIGNED_OBJECT)

    def test_verify_signature_accepts_each_v2_during_a_roll(self):
        """During a roll the header holds two v2 values, newest first.

        A parser that keeps only the last value fails with the new secret.
        """
        client = MoneiClient(api_key=self.api_key)
        signature = (
            f"t=1794643200,v1={V1_SIGNATURE},v2={V2_NEW_SIGNATURE},v2={V2_SIGNATURE}"
        )

        for secret in (NEW_SECRET, OLD_SECRET):
            with self.subTest(secret=secret[:9]):
                self.assertEqual(
                    client.verify_signature(SIGNED_BODY, signature, secret),
                    SIGNED_OBJECT,
                )

    def test_verify_signature_wrong_secret(self):
        # v1 is valid for the API key, so a fallback to v1 passes.
        self.assert_unauthorized(
            f"t=1794643200,v1={V1_SIGNATURE},v2={V2_SIGNATURE}", NEW_SECRET
        )

    def test_verify_signature_empty_secret(self):
        # v2 is HMAC-SHA256 keyed with an empty string, which anyone can make.
        self.assert_unauthorized(
            "t=1794643200,v2=ef198247309de9b0cd6cd622f2cd96b2e292f578aa7108bc21e5fd8e0aa4e5d1",
            "",
        )

    def test_verify_signature_missing_t(self):
        # v1 is valid for t=1794643200: only the missing t makes it fail.
        self.assert_unauthorized(f"v1={V1_SIGNATURE}")

    def test_verify_signature_element_without_equals_sign(self):
        self.assert_unauthorized(f"t=1794643200,v1={V1_SIGNATURE},malformed")

    def test_verify_signature_missing_header(self):
        """request.headers.get() gives None for a missing header."""
        self.assert_unauthorized(None)

    def test_verify_signature_non_ascii_v1(self):
        # hmac.compare_digest raises TypeError on a str with non-ASCII characters.
        self.assert_unauthorized("t=1794643200,v1=" + "é" * 64)

    def test_verify_signature_ignores_unknown_elements(self):
        """The header can carry more elements than t, v1 and v2."""
        client = MoneiClient(api_key=self.api_key)

        result = client.verify_signature(
            SIGNED_BODY, f"t=1794643200,v1={V1_SIGNATURE},v9=a=b"
        )

        self.assertEqual(result, SIGNED_OBJECT)

    def test_default_user_agent_always_set(self):
        """Test that DEFAULT_USER_AGENT is always set when user_agent is None."""
        # Create a client without specifying a user agent
        client = MoneiClient(api_key=self.api_key)

        # Check that the user agent is set to DEFAULT_USER_AGENT
        self.assertEqual(client.user_agent, DEFAULT_USER_AGENT)

        # Check that the user agent is set in the API client
        self.assertEqual(client._api_client.user_agent, DEFAULT_USER_AGENT)

    def test_default_user_agent_format_includes_python_version(self):
        """Test that DEFAULT_USER_AGENT includes Python version in the correct format."""
        import sys
        import Monei

        # Check that the user agent follows the expected format: MONEI/Python/2.0.2 (Python v3.12.9)
        expected_format = f"MONEI/Python/{Monei.__version__} (Python v{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro})"
        self.assertEqual(DEFAULT_USER_AGENT, expected_format)

        # Verify the format components
        self.assertTrue(DEFAULT_USER_AGENT.startswith("MONEI/Python/"))
        self.assertIn(
            f"(Python v{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro})",
            DEFAULT_USER_AGENT,
        )
        self.assertIn(Monei.__version__, DEFAULT_USER_AGENT)


if __name__ == "__main__":
    unittest.main()
