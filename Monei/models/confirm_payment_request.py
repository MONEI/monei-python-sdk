# coding: utf-8

"""
    MONEI API v1

    The MONEI API is organized around [REST](https://en.wikipedia.org/wiki/Representational_State_Transfer). Our API has predictable resource-oriented URLs, accepts JSON-encoded request bodies, returns JSON-encoded responses, and uses standard HTTP response codes, authentication, and verbs.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from Monei.configuration import Configuration


class ConfirmPaymentRequest(object):
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
        'payment_token': 'str',
        'generate_payment_token': 'bool',
        'customer': 'PaymentCustomer',
        'billing_details': 'PaymentBillingDetails',
        'shipping_details': 'PaymentShippingDetails'
    }

    attribute_map = {
        'payment_token': 'paymentToken',
        'generate_payment_token': 'generatePaymentToken',
        'customer': 'customer',
        'billing_details': 'billingDetails',
        'shipping_details': 'shippingDetails'
    }

    def __init__(self, payment_token=None, generate_payment_token=False, customer=None, billing_details=None, shipping_details=None, local_vars_configuration=None):  # noqa: E501
        """ConfirmPaymentRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._payment_token = None
        self._generate_payment_token = None
        self._customer = None
        self._billing_details = None
        self._shipping_details = None
        self.discriminator = None

        self.payment_token = payment_token
        if generate_payment_token is not None:
            self.generate_payment_token = generate_payment_token
        if customer is not None:
            self.customer = customer
        if billing_details is not None:
            self.billing_details = billing_details
        if shipping_details is not None:
            self.shipping_details = shipping_details

    @property
    def payment_token(self):
        """Gets the payment_token of this ConfirmPaymentRequest.  # noqa: E501

        A payment token generated by monei.js [UI Components](https://docs.monei.com/docs/monei-js-overview) or a paymentToken [saved after a previous successful payment](https://docs.monei.com/docs/save-payment-method).  # noqa: E501

        :return: The payment_token of this ConfirmPaymentRequest.  # noqa: E501
        :rtype: str
        """
        return self._payment_token

    @payment_token.setter
    def payment_token(self, payment_token):
        """Sets the payment_token of this ConfirmPaymentRequest.

        A payment token generated by monei.js [UI Components](https://docs.monei.com/docs/monei-js-overview) or a paymentToken [saved after a previous successful payment](https://docs.monei.com/docs/save-payment-method).  # noqa: E501

        :param payment_token: The payment_token of this ConfirmPaymentRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and payment_token is None:  # noqa: E501
            raise ValueError("Invalid value for `payment_token`, must not be `None`")  # noqa: E501

        self._payment_token = payment_token

    @property
    def generate_payment_token(self):
        """Gets the generate_payment_token of this ConfirmPaymentRequest.  # noqa: E501

        If set to true a permanent token that represents a payment method used in the payment will be generated.  # noqa: E501

        :return: The generate_payment_token of this ConfirmPaymentRequest.  # noqa: E501
        :rtype: bool
        """
        return self._generate_payment_token

    @generate_payment_token.setter
    def generate_payment_token(self, generate_payment_token):
        """Sets the generate_payment_token of this ConfirmPaymentRequest.

        If set to true a permanent token that represents a payment method used in the payment will be generated.  # noqa: E501

        :param generate_payment_token: The generate_payment_token of this ConfirmPaymentRequest.  # noqa: E501
        :type: bool
        """

        self._generate_payment_token = generate_payment_token

    @property
    def customer(self):
        """Gets the customer of this ConfirmPaymentRequest.  # noqa: E501


        :return: The customer of this ConfirmPaymentRequest.  # noqa: E501
        :rtype: PaymentCustomer
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this ConfirmPaymentRequest.


        :param customer: The customer of this ConfirmPaymentRequest.  # noqa: E501
        :type: PaymentCustomer
        """

        self._customer = customer

    @property
    def billing_details(self):
        """Gets the billing_details of this ConfirmPaymentRequest.  # noqa: E501


        :return: The billing_details of this ConfirmPaymentRequest.  # noqa: E501
        :rtype: PaymentBillingDetails
        """
        return self._billing_details

    @billing_details.setter
    def billing_details(self, billing_details):
        """Sets the billing_details of this ConfirmPaymentRequest.


        :param billing_details: The billing_details of this ConfirmPaymentRequest.  # noqa: E501
        :type: PaymentBillingDetails
        """

        self._billing_details = billing_details

    @property
    def shipping_details(self):
        """Gets the shipping_details of this ConfirmPaymentRequest.  # noqa: E501


        :return: The shipping_details of this ConfirmPaymentRequest.  # noqa: E501
        :rtype: PaymentShippingDetails
        """
        return self._shipping_details

    @shipping_details.setter
    def shipping_details(self, shipping_details):
        """Sets the shipping_details of this ConfirmPaymentRequest.


        :param shipping_details: The shipping_details of this ConfirmPaymentRequest.  # noqa: E501
        :type: PaymentShippingDetails
        """

        self._shipping_details = shipping_details

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
        if not isinstance(other, ConfirmPaymentRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConfirmPaymentRequest):
            return True

        return self.to_dict() != other.to_dict()
