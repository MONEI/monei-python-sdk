# coding: utf-8

"""
    MONEI API v1

    <p>The MONEI API is organized around <a href=\"https://en.wikipedia.org/wiki/Representational_State_Transfer\">REST</a> principles. Our API is designed to be intuitive and developer-friendly.</p> <h3>Base URL</h3> <p>All API requests should be made to:</p> <pre><code>https://api.monei.com/v1 </code></pre> <h3>Environment</h3> <p>MONEI provides two environments:</p> <ul> <li><strong>Test Environment</strong>: For development and testing without processing real payments</li> <li><strong>Live Environment</strong>: For processing real transactions in production</li> </ul> <h3>Client Libraries</h3> <p>We provide official SDKs to simplify integration:</p> <ul> <li><a href=\"https://github.com/MONEI/monei-php-sdk\">PHP SDK</a></li> <li><a href=\"https://github.com/MONEI/monei-python-sdk\">Python SDK</a></li> <li><a href=\"https://github.com/MONEI/monei-node-sdk\">Node.js SDK</a></li> <li><a href=\"https://postman.monei.com/\">Postman Collection</a></li> </ul> <p>Our SDKs handle authentication, error handling, and request formatting automatically.</p> <h3>Important Requirements</h3> <ul> <li>All API requests must be made over HTTPS</li> <li>If you are not using our official SDKs, you <strong>must provide a valid <code>User-Agent</code> header</strong> with each request</li> <li>Requests without proper authentication will return a <code>401 Unauthorized</code> error</li> </ul> <h3>Error Handling</h3> <p>The API returns consistent error codes and messages to help you troubleshoot issues. Each response includes a <code>statusCode</code> attribute indicating the outcome of your request.</p> <p><a href=\"https://docs.monei.com/api/errors\">View complete list of status codes →</a></p> <h3>Rate Limits</h3> <p>The API implements rate limiting to ensure stability. If you exceed the limits, requests will return a <code>429 Too Many Requests</code> status code.</p>   # noqa: E501

    The version of the OpenAPI document: 1.5.0
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
        'billing_category': 'str',
        'auth_payment_method': 'str'
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
        :rtype: str
        """
        return self._billing_category

    @billing_category.setter
    def billing_category(self, billing_category):
        """Sets the billing_category of this PaymentPaymentMethodKlarna.


        :param billing_category: The billing_category of this PaymentPaymentMethodKlarna.  # noqa: E501
        :type: str
        """
        allowed_values = ["PAY_LATER", "PAY_NOW", "SLICE_IT", "SLICE_IT_BY_CARD"]  # noqa: E501
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
        :rtype: str
        """
        return self._auth_payment_method

    @auth_payment_method.setter
    def auth_payment_method(self, auth_payment_method):
        """Sets the auth_payment_method of this PaymentPaymentMethodKlarna.


        :param auth_payment_method: The auth_payment_method of this PaymentPaymentMethodKlarna.  # noqa: E501
        :type: str
        """
        allowed_values = ["invoice", "fixed_amount", "pix", "base_account", "deferred_interest", "direct_debit", "direct_bank_transfer", "b2b_invoice", "card", "slice_it_by_card"]  # noqa: E501
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
