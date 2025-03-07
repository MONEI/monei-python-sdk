import json
import hmac
import hashlib

# Import specific modules instead of importing from Monei
import Monei
from Monei.api.payment_methods_api import PaymentMethodsApi
from Monei.configuration import Configuration
from Monei.api_client import ApiClient
from Monei.exceptions import ApiException
from Monei.api.payments_api import PaymentsApi
from Monei.api.subscriptions_api import SubscriptionsApi
from Monei.api.apple_pay_domain_api import ApplePayDomainApi
from Monei.api.bizum_api import BizumApi


DEFAULT_USER_AGENT = f"MONEI/Python/{Monei.__version__}"


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
            self.ApplePayDomain = ApplePayDomainApi(api_client)
            self.Bizum = BizumApi(api_client)

            # Store the api_client for later use
            self._api_client = api_client

            # aliases
            self.payments = self.Payments
            self.payment_methods = self.PaymentMethods
            self.subscriptions = self.Subscriptions
            self.apple_pay_domain = self.ApplePayDomain
            self.bizum = self.Bizum

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

    def verify_signature(self, body, signature):
        """Verifies response signature
        :param body: string JSON content to be verified
        :param signature: string signature to verify against
        :return: parsed object of the body
        """

        parts_dict = {}
        signature_parts = signature.split(",")
        for part in signature_parts:
            parts = part.split("=")
            parts_dict[parts[0]] = parts[1]

        calculated_hmac = hmac.new(
            bytes(self.api_key, "utf-8"),
            msg=bytes("{}.{}".format(parts_dict["t"], body), "utf-8"),
            digestmod=hashlib.sha256,
        ).hexdigest()

        if calculated_hmac != parts_dict["v1"]:
            raise ApiException(status=401, reason="[401] Signature verification failed")

        return json.loads(body)
