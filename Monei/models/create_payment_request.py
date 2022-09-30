# coding: utf-8

"""
    MONEI API v1

    <p>The MONEI API is organized around <a href=\"https://en.wikipedia.org/wiki/Representational_State_Transfer\">REST</a>. Our API has predictable resource-oriented URLs, accepts JSON-encoded request bodies, returns JSON-encoded responses, and uses standard HTTP response codes, authentication, and verbs.</p> <h4 id=\"base-url\">Base URL:</h4> <p><a href=\"https://api.monei.com/v1\">https://api.monei.com/v1</a></p> <h4 id=\"client-libraries\">Client libraries:</h4> <ul> <li><a href=\"https://github.com/MONEI/monei-php-sdk\">PHP SDK</a></li> <li><a href=\"https://github.com/MONEI/monei-python-sdk\">Python SDK</a></li> <li><a href=\"https://github.com/MONEI/monei-node-sdk\">Node.js SDK</a></li> <li><a href=\"https://postman.monei.com/\">Postman Collection</a></li> </ul> <h4 id=\"important\">Important:</h4> <p><strong>If you are not using our official SDKs, you need to provide a valid <code>User-Agent</code> header in each request, otherwise your requests will be rejected.</strong></p>   # noqa: E501

    The version of the OpenAPI document: 1.2.2
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from Monei.configuration import Configuration


class CreatePaymentRequest(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'amount': 'int',
        'currency': 'str',
        'order_id': 'str',
        'callback_url': 'str',
        'complete_url': 'str',
        'fail_url': 'str',
        'cancel_url': 'str',
        'payment_token': 'str',
        'session_id': 'str',
        'generate_payment_token': 'bool',
        'payment_method': 'PaymentPaymentMethodInput',
        'allowed_payment_methods': 'PaymentPaymentMethods',
        'transaction_type': 'PaymentTransactionType',
        'sequence': 'PaymentSequence',
        'point_of_sale_id': 'str',
        'subscription_id': 'str',
        'auto_recover': 'bool',
        'description': 'str',
        'customer': 'PaymentCustomer',
        'billing_details': 'PaymentBillingDetails',
        'shipping_details': 'PaymentShippingDetails',
        'session_details': 'PaymentSessionDetails',
        'expire_at': 'float'
    }

    attribute_map = {
        'amount': 'amount',
        'currency': 'currency',
        'order_id': 'orderId',
        'callback_url': 'callbackUrl',
        'complete_url': 'completeUrl',
        'fail_url': 'failUrl',
        'cancel_url': 'cancelUrl',
        'payment_token': 'paymentToken',
        'session_id': 'sessionId',
        'generate_payment_token': 'generatePaymentToken',
        'payment_method': 'paymentMethod',
        'allowed_payment_methods': 'allowedPaymentMethods',
        'transaction_type': 'transactionType',
        'sequence': 'sequence',
        'point_of_sale_id': 'pointOfSaleId',
        'subscription_id': 'subscriptionId',
        'auto_recover': 'autoRecover',
        'description': 'description',
        'customer': 'customer',
        'billing_details': 'billingDetails',
        'shipping_details': 'shippingDetails',
        'session_details': 'sessionDetails',
        'expire_at': 'expireAt'
    }

    def __init__(self, amount=None, currency=None, order_id=None, callback_url=None, complete_url=None, fail_url=None, cancel_url=None, payment_token=None, session_id=None, generate_payment_token=False, payment_method=None, allowed_payment_methods=None, transaction_type=None, sequence=None, point_of_sale_id=None, subscription_id=None, auto_recover=None, description=None, customer=None, billing_details=None, shipping_details=None, session_details=None, expire_at=None, local_vars_configuration=None):  # noqa: E501
        """CreatePaymentRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._amount = None
        self._currency = None
        self._order_id = None
        self._callback_url = None
        self._complete_url = None
        self._fail_url = None
        self._cancel_url = None
        self._payment_token = None
        self._session_id = None
        self._generate_payment_token = None
        self._payment_method = None
        self._allowed_payment_methods = None
        self._transaction_type = None
        self._sequence = None
        self._point_of_sale_id = None
        self._subscription_id = None
        self._auto_recover = None
        self._description = None
        self._customer = None
        self._billing_details = None
        self._shipping_details = None
        self._session_details = None
        self._expire_at = None
        self.discriminator = None

        self.amount = amount
        self.currency = currency
        self.order_id = order_id
        if callback_url is not None:
            self.callback_url = callback_url
        if complete_url is not None:
            self.complete_url = complete_url
        if fail_url is not None:
            self.fail_url = fail_url
        if cancel_url is not None:
            self.cancel_url = cancel_url
        if payment_token is not None:
            self.payment_token = payment_token
        if session_id is not None:
            self.session_id = session_id
        if generate_payment_token is not None:
            self.generate_payment_token = generate_payment_token
        if payment_method is not None:
            self.payment_method = payment_method
        if allowed_payment_methods is not None:
            self.allowed_payment_methods = allowed_payment_methods
        if transaction_type is not None:
            self.transaction_type = transaction_type
        if sequence is not None:
            self.sequence = sequence
        if point_of_sale_id is not None:
            self.point_of_sale_id = point_of_sale_id
        if subscription_id is not None:
            self.subscription_id = subscription_id
        if auto_recover is not None:
            self.auto_recover = auto_recover
        if description is not None:
            self.description = description
        if customer is not None:
            self.customer = customer
        if billing_details is not None:
            self.billing_details = billing_details
        if shipping_details is not None:
            self.shipping_details = shipping_details
        if session_details is not None:
            self.session_details = session_details
        if expire_at is not None:
            self.expire_at = expire_at

    @property
    def amount(self):
        """Gets the amount of this CreatePaymentRequest.  # noqa: E501

        Amount intended to be collected by this payment. A positive integer representing how much to charge in the smallest currency unit (e.g., 100 cents to charge 1.00 USD).   # noqa: E501

        :return: The amount of this CreatePaymentRequest.  # noqa: E501
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this CreatePaymentRequest.

        Amount intended to be collected by this payment. A positive integer representing how much to charge in the smallest currency unit (e.g., 100 cents to charge 1.00 USD).   # noqa: E501

        :param amount: The amount of this CreatePaymentRequest.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and amount is None:  # noqa: E501
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def currency(self):
        """Gets the currency of this CreatePaymentRequest.  # noqa: E501

        Three-letter [ISO currency code](https://en.wikipedia.org/wiki/ISO_4217), in uppercase. Must be a supported currency.   # noqa: E501

        :return: The currency of this CreatePaymentRequest.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this CreatePaymentRequest.

        Three-letter [ISO currency code](https://en.wikipedia.org/wiki/ISO_4217), in uppercase. Must be a supported currency.   # noqa: E501

        :param currency: The currency of this CreatePaymentRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and currency is None:  # noqa: E501
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def order_id(self):
        """Gets the order_id of this CreatePaymentRequest.  # noqa: E501

        An order ID from your system. A unique identifier that can be used to reconcile the payment with your internal system.   # noqa: E501

        :return: The order_id of this CreatePaymentRequest.  # noqa: E501
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this CreatePaymentRequest.

        An order ID from your system. A unique identifier that can be used to reconcile the payment with your internal system.   # noqa: E501

        :param order_id: The order_id of this CreatePaymentRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and order_id is None:  # noqa: E501
            raise ValueError("Invalid value for `order_id`, must not be `None`")  # noqa: E501

        self._order_id = order_id

    @property
    def callback_url(self):
        """Gets the callback_url of this CreatePaymentRequest.  # noqa: E501

        The URL to which a payment result should be sent asynchronously.   # noqa: E501

        :return: The callback_url of this CreatePaymentRequest.  # noqa: E501
        :rtype: str
        """
        return self._callback_url

    @callback_url.setter
    def callback_url(self, callback_url):
        """Sets the callback_url of this CreatePaymentRequest.

        The URL to which a payment result should be sent asynchronously.   # noqa: E501

        :param callback_url: The callback_url of this CreatePaymentRequest.  # noqa: E501
        :type: str
        """

        self._callback_url = callback_url

    @property
    def complete_url(self):
        """Gets the complete_url of this CreatePaymentRequest.  # noqa: E501

        The URL the customer will be directed to after transaction completed (successful or failed - except if `failUrl` is provided).   # noqa: E501

        :return: The complete_url of this CreatePaymentRequest.  # noqa: E501
        :rtype: str
        """
        return self._complete_url

    @complete_url.setter
    def complete_url(self, complete_url):
        """Sets the complete_url of this CreatePaymentRequest.

        The URL the customer will be directed to after transaction completed (successful or failed - except if `failUrl` is provided).   # noqa: E501

        :param complete_url: The complete_url of this CreatePaymentRequest.  # noqa: E501
        :type: str
        """

        self._complete_url = complete_url

    @property
    def fail_url(self):
        """Gets the fail_url of this CreatePaymentRequest.  # noqa: E501

        The URL the customer will be directed to after transaction has failed, instead of `completeUrl` (used in hosted payment page). This allows to provide two different URLs for successful and failed payments.   # noqa: E501

        :return: The fail_url of this CreatePaymentRequest.  # noqa: E501
        :rtype: str
        """
        return self._fail_url

    @fail_url.setter
    def fail_url(self, fail_url):
        """Sets the fail_url of this CreatePaymentRequest.

        The URL the customer will be directed to after transaction has failed, instead of `completeUrl` (used in hosted payment page). This allows to provide two different URLs for successful and failed payments.   # noqa: E501

        :param fail_url: The fail_url of this CreatePaymentRequest.  # noqa: E501
        :type: str
        """

        self._fail_url = fail_url

    @property
    def cancel_url(self):
        """Gets the cancel_url of this CreatePaymentRequest.  # noqa: E501

        The URL the customer will be directed to if they decide to cancel payment and return to your website (used in hosted payment page).   # noqa: E501

        :return: The cancel_url of this CreatePaymentRequest.  # noqa: E501
        :rtype: str
        """
        return self._cancel_url

    @cancel_url.setter
    def cancel_url(self, cancel_url):
        """Sets the cancel_url of this CreatePaymentRequest.

        The URL the customer will be directed to if they decide to cancel payment and return to your website (used in hosted payment page).   # noqa: E501

        :param cancel_url: The cancel_url of this CreatePaymentRequest.  # noqa: E501
        :type: str
        """

        self._cancel_url = cancel_url

    @property
    def payment_token(self):
        """Gets the payment_token of this CreatePaymentRequest.  # noqa: E501

        A payment token generated by monei.js [Components](https://docs.monei.com/docs/monei-js-overview) or a paymentToken [saved after a previous successful payment](https://docs.monei.com/docs/save-payment-method). In case of the first one, you will also need to send the `sessionId` used to generate the token in the first place.   # noqa: E501

        :return: The payment_token of this CreatePaymentRequest.  # noqa: E501
        :rtype: str
        """
        return self._payment_token

    @payment_token.setter
    def payment_token(self, payment_token):
        """Sets the payment_token of this CreatePaymentRequest.

        A payment token generated by monei.js [Components](https://docs.monei.com/docs/monei-js-overview) or a paymentToken [saved after a previous successful payment](https://docs.monei.com/docs/save-payment-method). In case of the first one, you will also need to send the `sessionId` used to generate the token in the first place.   # noqa: E501

        :param payment_token: The payment_token of this CreatePaymentRequest.  # noqa: E501
        :type: str
        """

        self._payment_token = payment_token

    @property
    def session_id(self):
        """Gets the session_id of this CreatePaymentRequest.  # noqa: E501

        A unique identifier within your system that adds security to the payment process. You need to pass the same session ID as the one used on the frontend to initialize MONEI Component (if you needed to). This is required if a payment token (not permanent) was already generated in the frontend.   # noqa: E501

        :return: The session_id of this CreatePaymentRequest.  # noqa: E501
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        """Sets the session_id of this CreatePaymentRequest.

        A unique identifier within your system that adds security to the payment process. You need to pass the same session ID as the one used on the frontend to initialize MONEI Component (if you needed to). This is required if a payment token (not permanent) was already generated in the frontend.   # noqa: E501

        :param session_id: The session_id of this CreatePaymentRequest.  # noqa: E501
        :type: str
        """

        self._session_id = session_id

    @property
    def generate_payment_token(self):
        """Gets the generate_payment_token of this CreatePaymentRequest.  # noqa: E501

        If set to true a permanent token that represents a payment method used in the payment will be generated.   # noqa: E501

        :return: The generate_payment_token of this CreatePaymentRequest.  # noqa: E501
        :rtype: bool
        """
        return self._generate_payment_token

    @generate_payment_token.setter
    def generate_payment_token(self, generate_payment_token):
        """Sets the generate_payment_token of this CreatePaymentRequest.

        If set to true a permanent token that represents a payment method used in the payment will be generated.   # noqa: E501

        :param generate_payment_token: The generate_payment_token of this CreatePaymentRequest.  # noqa: E501
        :type: bool
        """

        self._generate_payment_token = generate_payment_token

    @property
    def payment_method(self):
        """Gets the payment_method of this CreatePaymentRequest.  # noqa: E501


        :return: The payment_method of this CreatePaymentRequest.  # noqa: E501
        :rtype: PaymentPaymentMethodInput
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """Sets the payment_method of this CreatePaymentRequest.


        :param payment_method: The payment_method of this CreatePaymentRequest.  # noqa: E501
        :type: PaymentPaymentMethodInput
        """

        self._payment_method = payment_method

    @property
    def allowed_payment_methods(self):
        """Gets the allowed_payment_methods of this CreatePaymentRequest.  # noqa: E501


        :return: The allowed_payment_methods of this CreatePaymentRequest.  # noqa: E501
        :rtype: PaymentPaymentMethods
        """
        return self._allowed_payment_methods

    @allowed_payment_methods.setter
    def allowed_payment_methods(self, allowed_payment_methods):
        """Sets the allowed_payment_methods of this CreatePaymentRequest.


        :param allowed_payment_methods: The allowed_payment_methods of this CreatePaymentRequest.  # noqa: E501
        :type: PaymentPaymentMethods
        """

        self._allowed_payment_methods = allowed_payment_methods

    @property
    def transaction_type(self):
        """Gets the transaction_type of this CreatePaymentRequest.  # noqa: E501


        :return: The transaction_type of this CreatePaymentRequest.  # noqa: E501
        :rtype: PaymentTransactionType
        """
        return self._transaction_type

    @transaction_type.setter
    def transaction_type(self, transaction_type):
        """Sets the transaction_type of this CreatePaymentRequest.


        :param transaction_type: The transaction_type of this CreatePaymentRequest.  # noqa: E501
        :type: PaymentTransactionType
        """

        self._transaction_type = transaction_type

    @property
    def sequence(self):
        """Gets the sequence of this CreatePaymentRequest.  # noqa: E501


        :return: The sequence of this CreatePaymentRequest.  # noqa: E501
        :rtype: PaymentSequence
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        """Sets the sequence of this CreatePaymentRequest.


        :param sequence: The sequence of this CreatePaymentRequest.  # noqa: E501
        :type: PaymentSequence
        """

        self._sequence = sequence

    @property
    def point_of_sale_id(self):
        """Gets the point_of_sale_id of this CreatePaymentRequest.  # noqa: E501

        A unique identifier of the Point of Sale. If specified the payment is attached to this Point of Sale. If there is a QR code attached to the same Point of Sale, this payment will be available by scanning the QR code.   # noqa: E501

        :return: The point_of_sale_id of this CreatePaymentRequest.  # noqa: E501
        :rtype: str
        """
        return self._point_of_sale_id

    @point_of_sale_id.setter
    def point_of_sale_id(self, point_of_sale_id):
        """Sets the point_of_sale_id of this CreatePaymentRequest.

        A unique identifier of the Point of Sale. If specified the payment is attached to this Point of Sale. If there is a QR code attached to the same Point of Sale, this payment will be available by scanning the QR code.   # noqa: E501

        :param point_of_sale_id: The point_of_sale_id of this CreatePaymentRequest.  # noqa: E501
        :type: str
        """

        self._point_of_sale_id = point_of_sale_id

    @property
    def subscription_id(self):
        """Gets the subscription_id of this CreatePaymentRequest.  # noqa: E501

        A unique identifier of the Subscription. If specified the payment is attached to this Subscription.   # noqa: E501

        :return: The subscription_id of this CreatePaymentRequest.  # noqa: E501
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """Sets the subscription_id of this CreatePaymentRequest.

        A unique identifier of the Subscription. If specified the payment is attached to this Subscription.   # noqa: E501

        :param subscription_id: The subscription_id of this CreatePaymentRequest.  # noqa: E501
        :type: str
        """

        self._subscription_id = subscription_id

    @property
    def auto_recover(self):
        """Gets the auto_recover of this CreatePaymentRequest.  # noqa: E501

        If set to `true`, the new payment will be automatically created when customer visits the payment link of the previously failed payment. Is automatically set to `true` if `completeUrl` is not provided.(set this value to `true` to create \"Pay By Link\" payments).  # noqa: E501

        :return: The auto_recover of this CreatePaymentRequest.  # noqa: E501
        :rtype: bool
        """
        return self._auto_recover

    @auto_recover.setter
    def auto_recover(self, auto_recover):
        """Sets the auto_recover of this CreatePaymentRequest.

        If set to `true`, the new payment will be automatically created when customer visits the payment link of the previously failed payment. Is automatically set to `true` if `completeUrl` is not provided.(set this value to `true` to create \"Pay By Link\" payments).  # noqa: E501

        :param auto_recover: The auto_recover of this CreatePaymentRequest.  # noqa: E501
        :type: bool
        """

        self._auto_recover = auto_recover

    @property
    def description(self):
        """Gets the description of this CreatePaymentRequest.  # noqa: E501

        An arbitrary string attached to the payment. Often useful for displaying to users.   # noqa: E501

        :return: The description of this CreatePaymentRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreatePaymentRequest.

        An arbitrary string attached to the payment. Often useful for displaying to users.   # noqa: E501

        :param description: The description of this CreatePaymentRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def customer(self):
        """Gets the customer of this CreatePaymentRequest.  # noqa: E501


        :return: The customer of this CreatePaymentRequest.  # noqa: E501
        :rtype: PaymentCustomer
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this CreatePaymentRequest.


        :param customer: The customer of this CreatePaymentRequest.  # noqa: E501
        :type: PaymentCustomer
        """

        self._customer = customer

    @property
    def billing_details(self):
        """Gets the billing_details of this CreatePaymentRequest.  # noqa: E501


        :return: The billing_details of this CreatePaymentRequest.  # noqa: E501
        :rtype: PaymentBillingDetails
        """
        return self._billing_details

    @billing_details.setter
    def billing_details(self, billing_details):
        """Sets the billing_details of this CreatePaymentRequest.


        :param billing_details: The billing_details of this CreatePaymentRequest.  # noqa: E501
        :type: PaymentBillingDetails
        """

        self._billing_details = billing_details

    @property
    def shipping_details(self):
        """Gets the shipping_details of this CreatePaymentRequest.  # noqa: E501


        :return: The shipping_details of this CreatePaymentRequest.  # noqa: E501
        :rtype: PaymentShippingDetails
        """
        return self._shipping_details

    @shipping_details.setter
    def shipping_details(self, shipping_details):
        """Sets the shipping_details of this CreatePaymentRequest.


        :param shipping_details: The shipping_details of this CreatePaymentRequest.  # noqa: E501
        :type: PaymentShippingDetails
        """

        self._shipping_details = shipping_details

    @property
    def session_details(self):
        """Gets the session_details of this CreatePaymentRequest.  # noqa: E501


        :return: The session_details of this CreatePaymentRequest.  # noqa: E501
        :rtype: PaymentSessionDetails
        """
        return self._session_details

    @session_details.setter
    def session_details(self, session_details):
        """Sets the session_details of this CreatePaymentRequest.


        :param session_details: The session_details of this CreatePaymentRequest.  # noqa: E501
        :type: PaymentSessionDetails
        """

        self._session_details = session_details

    @property
    def expire_at(self):
        """Gets the expire_at of this CreatePaymentRequest.  # noqa: E501

        Payment expiration time.  # noqa: E501

        :return: The expire_at of this CreatePaymentRequest.  # noqa: E501
        :rtype: float
        """
        return self._expire_at

    @expire_at.setter
    def expire_at(self, expire_at):
        """Sets the expire_at of this CreatePaymentRequest.

        Payment expiration time.  # noqa: E501

        :param expire_at: The expire_at of this CreatePaymentRequest.  # noqa: E501
        :type: float
        """

        self._expire_at = expire_at

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreatePaymentRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreatePaymentRequest):
            return True

        return self.to_dict() != other.to_dict()
