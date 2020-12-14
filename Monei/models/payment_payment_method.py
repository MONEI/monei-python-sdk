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


class PaymentPaymentMethod(object):
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
        'method': 'str',
        'card': 'PaymentPaymentMethodCard',
        'bizum': 'PaymentPaymentMethodBizum',
        'paypal': 'PaymentPaymentMethodPaypal'
    }

    attribute_map = {
        'method': 'method',
        'card': 'card',
        'bizum': 'bizum',
        'paypal': 'paypal'
    }

    def __init__(self, method=None, card=None, bizum=None, paypal=None, local_vars_configuration=None):  # noqa: E501
        """PaymentPaymentMethod - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._method = None
        self._card = None
        self._bizum = None
        self._paypal = None
        self.discriminator = None

        if method is not None:
            self.method = method
        if card is not None:
            self.card = card
        if bizum is not None:
            self.bizum = bizum
        if paypal is not None:
            self.paypal = paypal

    @property
    def method(self):
        """Gets the method of this PaymentPaymentMethod.  # noqa: E501

        Payment method type.  # noqa: E501

        :return: The method of this PaymentPaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this PaymentPaymentMethod.

        Payment method type.  # noqa: E501

        :param method: The method of this PaymentPaymentMethod.  # noqa: E501
        :type: str
        """
        allowed_values = ["card", "bizum", "googlePay", "applePay", "paypal"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and method not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `method` ({0}), must be one of {1}"  # noqa: E501
                .format(method, allowed_values)
            )

        self._method = method

    @property
    def card(self):
        """Gets the card of this PaymentPaymentMethod.  # noqa: E501


        :return: The card of this PaymentPaymentMethod.  # noqa: E501
        :rtype: PaymentPaymentMethodCard
        """
        return self._card

    @card.setter
    def card(self, card):
        """Sets the card of this PaymentPaymentMethod.


        :param card: The card of this PaymentPaymentMethod.  # noqa: E501
        :type: PaymentPaymentMethodCard
        """

        self._card = card

    @property
    def bizum(self):
        """Gets the bizum of this PaymentPaymentMethod.  # noqa: E501


        :return: The bizum of this PaymentPaymentMethod.  # noqa: E501
        :rtype: PaymentPaymentMethodBizum
        """
        return self._bizum

    @bizum.setter
    def bizum(self, bizum):
        """Sets the bizum of this PaymentPaymentMethod.


        :param bizum: The bizum of this PaymentPaymentMethod.  # noqa: E501
        :type: PaymentPaymentMethodBizum
        """

        self._bizum = bizum

    @property
    def paypal(self):
        """Gets the paypal of this PaymentPaymentMethod.  # noqa: E501


        :return: The paypal of this PaymentPaymentMethod.  # noqa: E501
        :rtype: PaymentPaymentMethodPaypal
        """
        return self._paypal

    @paypal.setter
    def paypal(self, paypal):
        """Sets the paypal of this PaymentPaymentMethod.


        :param paypal: The paypal of this PaymentPaymentMethod.  # noqa: E501
        :type: PaymentPaymentMethodPaypal
        """

        self._paypal = paypal

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
        if not isinstance(other, PaymentPaymentMethod):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PaymentPaymentMethod):
            return True

        return self.to_dict() != other.to_dict()
