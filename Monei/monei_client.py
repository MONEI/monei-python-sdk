import json
import hmac
import hashlib

from Monei import Configuration, ApiClient, PaymentsApi, ApiException, SubscriptionsApi, ApplePayDomainApi, __version__


class MoneiClient(object):
    _default = None

    def __init__(self, api_key=None, config=None):

        self.api_key = api_key

        self.config = config if config else Configuration()

        self.config.api_key = {
            'Authorization': api_key
        }

        # Enter a context with an instance of the API client
        with ApiClient(self.config) as api_client:
            api_client.user_agent = "MONEI/Python/" + __version__
            self.Payments = PaymentsApi(api_client)
            self.Subscriptions = SubscriptionsApi(api_client)
            self.ApplePayDomain = ApplePayDomainApi(api_client)

            # aliases
            self.payments = self.Payments

    def verify_signature(self, body, signature):
        """Verifies response signature
        :param body: string JSON content to be verified
        :param signature: string signature to verify against
        :return: parsed object of the body
        """

        parts = {}
        signature_parts = signature.split(',')
        for part in signature_parts:
            parts = part.split('=')
            parts[parts[0]] = parts[1]

        calculated_hmac = hmac.new(
            bytes(self.api_key, 'utf-8'),
            msg=bytes('{}.{}'.format(parts['t'], body), 'utf-8'),
            digestmod=hashlib.sha256
        ).hexdigest()

        if calculated_hmac != parts['v1']:
            raise ApiException(
                status=401,
                reason='[401] Signature verification failed'
            )

        return json.loads(body)
