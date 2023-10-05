# coding: utf-8

"""
    MONEI API v1

    <p>The MONEI API is organized around <a href=\"https://en.wikipedia.org/wiki/Representational_State_Transfer\">REST</a>. Our API has predictable resource-oriented URLs, accepts JSON-encoded request bodies, returns JSON-encoded responses, and uses standard HTTP response codes, authentication, and verbs.</p> <h4 id=\"base-url\">Base URL:</h4> <p><a href=\"https://api.monei.com/v1\">https://api.monei.com/v1</a></p> <h4 id=\"client-libraries\">Client libraries:</h4> <ul> <li><a href=\"https://github.com/MONEI/monei-php-sdk\">PHP SDK</a></li> <li><a href=\"https://github.com/MONEI/monei-python-sdk\">Python SDK</a></li> <li><a href=\"https://github.com/MONEI/monei-node-sdk\">Node.js SDK</a></li> <li><a href=\"https://postman.monei.com/\">Postman</a></li> </ul> <h4 id=\"important\">Important:</h4> <p><strong>If you are not using our official SDKs, you need to provide a valid <code>User-Agent</code> header in each request, otherwise your requests will be rejected.</strong></p>   # noqa: E501

    The version of the OpenAPI document: 1.4.3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from Monei.configuration import Configuration


class PaymentPaymentMethodKlarna(object):
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
        'billing_category': 'Enum',
        'auth_payment_method': 'Enum'
    }

    attribute_map = {
        'billing_category': 'billingCategory',
        'auth_payment_method': 'authPaymentMethod'
    }

    def __init__(self, billing_category=None, auth_payment_method=None, local_vars_configuration=None):  # noqa: E501
        """PaymentPaymentMethodKlarna - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._billing_category = None
        self._auth_payment_method = None
        self.discriminator = None

        if billing_category is not None:
            self.billing_category = billing_category
        if auth_payment_method is not None:
            self.auth_payment_method = auth_payment_method

    @property
    def billing_category(self):
        """Gets the billing_category of this PaymentPaymentMethodKlarna.  # noqa: E501


        :return: The billing_category of this PaymentPaymentMethodKlarna.  # noqa: E501
        :rtype: Enum
        """
        return self._billing_category

    @billing_category.setter
    def billing_category(self, billing_category):
        """Sets the billing_category of this PaymentPaymentMethodKlarna.


        :param billing_category: The billing_category of this PaymentPaymentMethodKlarna.  # noqa: E501
        :type: Enum
        """
        allowed_values = [PAY_LATER, PAY_NOW, SLICE_IT, SLICE_IT_BY_CARD]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and billing_category not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `billing_category` ({0}), must be one of {1}"  # noqa: E501
                .format(billing_category, allowed_values)
            )

        self._billing_category = billing_category

    @property
    def auth_payment_method(self):
        """Gets the auth_payment_method of this PaymentPaymentMethodKlarna.  # noqa: E501


        :return: The auth_payment_method of this PaymentPaymentMethodKlarna.  # noqa: E501
        :rtype: Enum
        """
        return self._auth_payment_method

    @auth_payment_method.setter
    def auth_payment_method(self, auth_payment_method):
        """Sets the auth_payment_method of this PaymentPaymentMethodKlarna.


        :param auth_payment_method: The auth_payment_method of this PaymentPaymentMethodKlarna.  # noqa: E501
        :type: Enum
        """
        allowed_values = [invoice, fixed_amount, pix, base_account, deferred_interest, direct_debit, direct_bank_transfer, b2b_invoice, card, slice_it_by_card]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and auth_payment_method not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `auth_payment_method` ({0}), must be one of {1}"  # noqa: E501
                .format(auth_payment_method, allowed_values)
            )

        self._auth_payment_method = auth_payment_method

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
        if not isinstance(other, PaymentPaymentMethodKlarna):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PaymentPaymentMethodKlarna):
            return True

        return self.to_dict() != other.to_dict()
