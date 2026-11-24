import json
import hmac
import hashlib
import sys

# Import specific modules instead of importing from Monei
import Monei
from Monei.apis import (
    PaymentsApi,
    PaymentMethodsApi,
    SubscriptionsApi,
    CustomersApi,
    ProductsApi,
    PricesApi,
    TaxRatesApi,
    CheckoutSessionsApi,
    ApplePayDomainApi,
    ApplePayCertificateApi,
    BizumApi,
    POSAuthTokenApi,
)
from Monei.configuration import Configuration
from Monei.api_client import ApiClient
from Monei.exceptions import ApiException

DEFAULT_USER_AGENT = (
    f"MONEI/Python/{Monei.__version__} "
    f"(Python v{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro})"
)


class MoneiClient(object):
    _default = None

    def __init__(self, api_key=None, config=None, account_id=None, user_agent=None):
        """Initialize the MONEI client

        Args:
            api_key (str): Your MONEI API key
            config (Configuration, optional): Custom configuration
            account_id (str, optional): The merchant's account ID to act on behalf of
            user_agent (str, optional): Custom User-Agent string
        """
        self.api_key = api_key
        self.account_id = account_id
        self.user_agent = user_agent or DEFAULT_USER_AGENT

        # Create a new configuration if one wasn't provided
        if config is None:
            self.config = Configuration()
            # Set the API key directly in the configuration
            self.config.api_key["APIKey"] = api_key
        else:
            self.config = config
            # If a config was provided, ensure the API key is set
            if "APIKey" not in self.config.api_key:
                self.config.api_key["APIKey"] = api_key

        # Enter a context with an instance of the API client
        with ApiClient(self.config) as api_client:
            # Set user agent
            api_client.user_agent = self.user_agent

            # Validate user agent when using account ID
            # Similar to Node.js SDK implementation
            if self.account_id and self.user_agent == DEFAULT_USER_AGENT:
                raise ApiException(
                    status=400,
                    reason="User-Agent must be provided when using Account ID",
                )

            # Add a request interceptor to validate user agent before each request
            original_call_api = api_client.call_api

            def call_api_with_validation(*args, **kwargs):
                # Validate that a custom user agent is set when using account ID
                if self.account_id and self.user_agent == DEFAULT_USER_AGENT:
                    raise ApiException(
                        status=400,
                        reason="User-Agent must be provided when using Account ID",
                    )
                return original_call_api(*args, **kwargs)

            api_client.call_api = call_api_with_validation

            # Set account ID if provided
            if self.account_id:
                api_client.set_default_header("MONEI-Account-ID", self.account_id)

            # Initialize API instances
            self.Payments = PaymentsApi(api_client)
            self.PaymentMethods = PaymentMethodsApi(api_client)
            self.Subscriptions = SubscriptionsApi(api_client)
            self.Customers = CustomersApi(api_client)
            self.Products = ProductsApi(api_client)
            self.Prices = PricesApi(api_client)
            self.TaxRates = TaxRatesApi(api_client)
            self.CheckoutSessions = CheckoutSessionsApi(api_client)
            self.ApplePayDomain = ApplePayDomainApi(api_client)
            self.Bizum = BizumApi(api_client)
            self.ApplePayCertificate = ApplePayCertificateApi(api_client)
            self.POSAuthToken = POSAuthTokenApi(api_client)
            # Store the api_client for later use
            self._api_client = api_client

            # aliases
            self.payments = self.Payments
            self.payment_methods = self.PaymentMethods
            self.subscriptions = self.Subscriptions
            self.customers = self.Customers
            self.products = self.Products
            self.prices = self.Prices
            self.tax_rates = self.TaxRates
            self.checkout_sessions = self.CheckoutSessions
            self.apple_pay_domain = self.ApplePayDomain
            self.apple_pay_certificate = self.ApplePayCertificate
            self.bizum = self.Bizum
            self.pos_auth_token = self.POSAuthToken

    def set_account_id(self, account_id):
        """Set the account ID to act on behalf of a merchant

        Args:
            account_id (str): The merchant's account ID

        Raises:
            ApiException: If trying to set account_id with default User-Agent
        """
        # If setting accountId and using default User-Agent
        if account_id and self.user_agent == DEFAULT_USER_AGENT:
            raise ApiException(
                status=400, reason="User-Agent must be set before using Account ID"
            )

        self.account_id = account_id

        # Update headers in api_client
        if account_id:
            self._api_client.set_default_header("MONEI-Account-ID", account_id)
        else:
            # Remove the header if account_id is None
            if "MONEI-Account-ID" in self._api_client.default_headers:
                del self._api_client.default_headers["MONEI-Account-ID"]

    def set_user_agent(self, user_agent):
        """Set a custom User-Agent header

        Args:
            user_agent (str): Custom User-Agent string
        """
        self.user_agent = user_agent
        self._api_client.user_agent = user_agent

    def verify_signature(self, body, signature, secret=None):
        """Verifies the MONEI-Signature header of a webhook or callback

        Without a secret, ``v1`` is checked with the API key of the client.
        With a secret, the ``v2`` values are checked with that secret, and ``v1`` is not used.

        :param body: string raw request body
        :param signature: string value of the MONEI-Signature header
        :param secret: string signing secret for v2 (``whsec_...`` or ``mksec_...``)
        :return: parsed object of the body
        :raises ApiException: with status 401 when the signature is missing, malformed or invalid
        """
        failure = ApiException(status=401, reason="[401] Signature verification failed")

        # An empty key gives an HMAC that anyone can make, for example from an empty variable.
        if secret is not None and (not isinstance(secret, str) or secret == ""):
            raise failure
        if not isinstance(signature, str):
            raise failure

        parts = {"v2": []}
        for element in signature.split(","):
            name, separator, value = element.partition("=")
            if not separator:
                raise failure
            if name == "v2":
                parts["v2"].append(value)
            else:
                parts[name] = value
        if not parts.get("t"):
            raise failure

        # Frameworks give the raw body as bytes (Flask request.data); format() would sign "b'...'".
        if isinstance(body, (bytes, bytearray)):
            body = body.decode("utf-8")
        payload = "{}.{}".format(parts["t"], body).encode("utf-8")
        if secret is None:
            key = self.api_key
            candidates = [parts["v1"]] if "v1" in parts else []
        else:
            key = secret
            candidates = parts["v2"]
        expected = hmac.new(
            key.encode("utf-8"), msg=payload, digestmod=hashlib.sha256
        ).hexdigest()

        # Compare bytes: compare_digest raises TypeError on a str with non-ASCII characters.
        for candidate in candidates:
            if hmac.compare_digest(expected.encode(), candidate.encode("utf-8")):
                return json.loads(body)
        raise failure

    def configure_retries(self, max_retries=3, retry_delay=0.1):
        """Configure retry behavior for API requests

        Args:
            max_retries (int): Maximum number of retry attempts
            retry_delay (float): Delay in seconds between retry attempts
        """
        # Store retry configuration
        self.max_retries = max_retries
        self.retry_delay = retry_delay

        # In a real implementation, this would configure the retry behavior
        # of the underlying client, but for now it's just a placeholder
        pass
