# coding: utf-8

"""
    MONEI API v1

    <p>The MONEI API is organized around <a href=\"https://en.wikipedia.org/wiki/Representational_State_Transfer\">REST</a>. Our API has predictable resource-oriented URLs, accepts JSON-encoded request bodies, returns JSON-encoded responses, and uses standard HTTP response codes, authentication, and verbs.</p> <h4 id=\"base-url\">Base URL:</h4> <p><a href=\"https://api.monei.com/v1\">https://api.monei.com/v1</a></p> <h4 id=\"client-libraries\">Client libraries:</h4> <ul> <li><a href=\"https://github.com/MONEI/monei-php-sdk\">PHP SDK</a></li> <li><a href=\"https://github.com/MONEI/monei-python-sdk\">Python SDK</a></li> <li><a href=\"https://github.com/MONEI/monei-node-sdk\">Node.js SDK</a></li> <li><a href=\"https://postman.monei.com/\">Postman Collection</a></li> </ul>   # noqa: E501

    The version of the OpenAPI document: 1.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from Monei.configuration import Configuration


class CreateSubscriptionRequest(object):
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
        'interval': 'SubscriptionInterval',
        'interval_count': 'int',
        'description': 'str',
        'customer': 'PaymentCustomer',
        'billing_details': 'PaymentBillingDetails',
        'shipping_details': 'PaymentShippingDetails',
        'trial_period_end': 'float',
        'trial_period_days': 'int',
        'callback_url': 'str',
        'payment_callback_url': 'str'
    }

    attribute_map = {
        'amount': 'amount',
        'currency': 'currency',
        'interval': 'interval',
        'interval_count': 'intervalCount',
        'description': 'description',
        'customer': 'customer',
        'billing_details': 'billingDetails',
        'shipping_details': 'shippingDetails',
        'trial_period_end': 'trialPeriodEnd',
        'trial_period_days': 'trialPeriodDays',
        'callback_url': 'callbackUrl',
        'payment_callback_url': 'paymentCallbackUrl'
    }

    def __init__(self, amount=None, currency=None, interval=None, interval_count=None, description=None, customer=None, billing_details=None, shipping_details=None, trial_period_end=None, trial_period_days=None, callback_url=None, payment_callback_url=None, local_vars_configuration=None):  # noqa: E501
        """CreateSubscriptionRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._amount = None
        self._currency = None
        self._interval = None
        self._interval_count = None
        self._description = None
        self._customer = None
        self._billing_details = None
        self._shipping_details = None
        self._trial_period_end = None
        self._trial_period_days = None
        self._callback_url = None
        self._payment_callback_url = None
        self.discriminator = None

        self.amount = amount
        self.currency = currency
        self.interval = interval
        self.interval_count = interval_count
        if description is not None:
            self.description = description
        if customer is not None:
            self.customer = customer
        if billing_details is not None:
            self.billing_details = billing_details
        if shipping_details is not None:
            self.shipping_details = shipping_details
        if trial_period_end is not None:
            self.trial_period_end = trial_period_end
        if trial_period_days is not None:
            self.trial_period_days = trial_period_days
        self.callback_url = callback_url
        self.payment_callback_url = payment_callback_url

    @property
    def amount(self):
        """Gets the amount of this CreateSubscriptionRequest.  # noqa: E501

        Amount intended to be collected by this payment. A positive integer representing how much to charge in the smallest currency unit (e.g., 100 cents to charge 1.00 USD).   # noqa: E501

        :return: The amount of this CreateSubscriptionRequest.  # noqa: E501
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this CreateSubscriptionRequest.

        Amount intended to be collected by this payment. A positive integer representing how much to charge in the smallest currency unit (e.g., 100 cents to charge 1.00 USD).   # noqa: E501

        :param amount: The amount of this CreateSubscriptionRequest.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and amount is None:  # noqa: E501
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def currency(self):
        """Gets the currency of this CreateSubscriptionRequest.  # noqa: E501

        Three-letter [ISO currency code](https://en.wikipedia.org/wiki/ISO_4217), in uppercase. Must be a supported currency.   # noqa: E501

        :return: The currency of this CreateSubscriptionRequest.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this CreateSubscriptionRequest.

        Three-letter [ISO currency code](https://en.wikipedia.org/wiki/ISO_4217), in uppercase. Must be a supported currency.   # noqa: E501

        :param currency: The currency of this CreateSubscriptionRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and currency is None:  # noqa: E501
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def interval(self):
        """Gets the interval of this CreateSubscriptionRequest.  # noqa: E501


        :return: The interval of this CreateSubscriptionRequest.  # noqa: E501
        :rtype: SubscriptionInterval
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this CreateSubscriptionRequest.


        :param interval: The interval of this CreateSubscriptionRequest.  # noqa: E501
        :type: SubscriptionInterval
        """
        if self.local_vars_configuration.client_side_validation and interval is None:  # noqa: E501
            raise ValueError("Invalid value for `interval`, must not be `None`")  # noqa: E501

        self._interval = interval

    @property
    def interval_count(self):
        """Gets the interval_count of this CreateSubscriptionRequest.  # noqa: E501

        Number of intervals between subscription payments.  # noqa: E501

        :return: The interval_count of this CreateSubscriptionRequest.  # noqa: E501
        :rtype: int
        """
        return self._interval_count

    @interval_count.setter
    def interval_count(self, interval_count):
        """Sets the interval_count of this CreateSubscriptionRequest.

        Number of intervals between subscription payments.  # noqa: E501

        :param interval_count: The interval_count of this CreateSubscriptionRequest.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and interval_count is None:  # noqa: E501
            raise ValueError("Invalid value for `interval_count`, must not be `None`")  # noqa: E501

        self._interval_count = interval_count

    @property
    def description(self):
        """Gets the description of this CreateSubscriptionRequest.  # noqa: E501

        An arbitrary string attached to the subscription. Often useful for displaying to users.   # noqa: E501

        :return: The description of this CreateSubscriptionRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateSubscriptionRequest.

        An arbitrary string attached to the subscription. Often useful for displaying to users.   # noqa: E501

        :param description: The description of this CreateSubscriptionRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def customer(self):
        """Gets the customer of this CreateSubscriptionRequest.  # noqa: E501


        :return: The customer of this CreateSubscriptionRequest.  # noqa: E501
        :rtype: PaymentCustomer
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this CreateSubscriptionRequest.


        :param customer: The customer of this CreateSubscriptionRequest.  # noqa: E501
        :type: PaymentCustomer
        """

        self._customer = customer

    @property
    def billing_details(self):
        """Gets the billing_details of this CreateSubscriptionRequest.  # noqa: E501


        :return: The billing_details of this CreateSubscriptionRequest.  # noqa: E501
        :rtype: PaymentBillingDetails
        """
        return self._billing_details

    @billing_details.setter
    def billing_details(self, billing_details):
        """Sets the billing_details of this CreateSubscriptionRequest.


        :param billing_details: The billing_details of this CreateSubscriptionRequest.  # noqa: E501
        :type: PaymentBillingDetails
        """

        self._billing_details = billing_details

    @property
    def shipping_details(self):
        """Gets the shipping_details of this CreateSubscriptionRequest.  # noqa: E501


        :return: The shipping_details of this CreateSubscriptionRequest.  # noqa: E501
        :rtype: PaymentShippingDetails
        """
        return self._shipping_details

    @shipping_details.setter
    def shipping_details(self, shipping_details):
        """Sets the shipping_details of this CreateSubscriptionRequest.


        :param shipping_details: The shipping_details of this CreateSubscriptionRequest.  # noqa: E501
        :type: PaymentShippingDetails
        """

        self._shipping_details = shipping_details

    @property
    def trial_period_end(self):
        """Gets the trial_period_end of this CreateSubscriptionRequest.  # noqa: E501

        The end date of the trial period. Measured in seconds since the Unix epoch.  # noqa: E501

        :return: The trial_period_end of this CreateSubscriptionRequest.  # noqa: E501
        :rtype: float
        """
        return self._trial_period_end

    @trial_period_end.setter
    def trial_period_end(self, trial_period_end):
        """Sets the trial_period_end of this CreateSubscriptionRequest.

        The end date of the trial period. Measured in seconds since the Unix epoch.  # noqa: E501

        :param trial_period_end: The trial_period_end of this CreateSubscriptionRequest.  # noqa: E501
        :type: float
        """

        self._trial_period_end = trial_period_end

    @property
    def trial_period_days(self):
        """Gets the trial_period_days of this CreateSubscriptionRequest.  # noqa: E501

        Number of days the trial period lasts.  # noqa: E501

        :return: The trial_period_days of this CreateSubscriptionRequest.  # noqa: E501
        :rtype: int
        """
        return self._trial_period_days

    @trial_period_days.setter
    def trial_period_days(self, trial_period_days):
        """Sets the trial_period_days of this CreateSubscriptionRequest.

        Number of days the trial period lasts.  # noqa: E501

        :param trial_period_days: The trial_period_days of this CreateSubscriptionRequest.  # noqa: E501
        :type: int
        """

        self._trial_period_days = trial_period_days

    @property
    def callback_url(self):
        """Gets the callback_url of this CreateSubscriptionRequest.  # noqa: E501

        The URL will be called each time subscription status changes.   # noqa: E501

        :return: The callback_url of this CreateSubscriptionRequest.  # noqa: E501
        :rtype: str
        """
        return self._callback_url

    @callback_url.setter
    def callback_url(self, callback_url):
        """Sets the callback_url of this CreateSubscriptionRequest.

        The URL will be called each time subscription status changes.   # noqa: E501

        :param callback_url: The callback_url of this CreateSubscriptionRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and callback_url is None:  # noqa: E501
            raise ValueError("Invalid value for `callback_url`, must not be `None`")  # noqa: E501

        self._callback_url = callback_url

    @property
    def payment_callback_url(self):
        """Gets the payment_callback_url of this CreateSubscriptionRequest.  # noqa: E501

        The URL will be called each time subscription creates a new payments.   # noqa: E501

        :return: The payment_callback_url of this CreateSubscriptionRequest.  # noqa: E501
        :rtype: str
        """
        return self._payment_callback_url

    @payment_callback_url.setter
    def payment_callback_url(self, payment_callback_url):
        """Sets the payment_callback_url of this CreateSubscriptionRequest.

        The URL will be called each time subscription creates a new payments.   # noqa: E501

        :param payment_callback_url: The payment_callback_url of this CreateSubscriptionRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and payment_callback_url is None:  # noqa: E501
            raise ValueError("Invalid value for `payment_callback_url`, must not be `None`")  # noqa: E501

        self._payment_callback_url = payment_callback_url

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
        if not isinstance(other, CreateSubscriptionRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateSubscriptionRequest):
            return True

        return self.to_dict() != other.to_dict()
