import json
import hmac
import hashlib

from Monei import Configuration, ApiClient, PaymentsApi, ApiException


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
            api_client.user_agent = 'MONEI/PYTHON/0.1.11'
            self.payments = PaymentsApi(api_client)

    def verifySignature(self, body, signature):
        """Verifies response signature
        :param body: string JSON content to be verified
        :param signature: string signature to verify against
        :return: parsed object of the body
        """

        parts = {}
        signature_parts = signature.split(',')
        for part in signature_parts:
            subparts = part.split('=')
            parts[subparts[0]] = subparts[1]

        calculatedHmac = hmac.new(
            bytes(self.api_key, 'utf-8'),
            msg=bytes('{}.{}'.format(parts['t'], body), 'utf-8'),
            digestmod=hashlib.sha256
        ).hexdigest()

        if calculatedHmac != parts['v1']:
            raise ApiException(
                status=401,
                reason='[401] Signature verification failed'
            )

        return json.loads(body)
