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


class ConfirmPaymentRequestPaymentMethodCard(object):
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
        'cardholder_name': 'str',
        'cardholder_email': 'str'
    }

    attribute_map = {
        'cardholder_name': 'cardholderName',
        'cardholder_email': 'cardholderEmail'
    }

    def __init__(self, cardholder_name=None, cardholder_email=None, local_vars_configuration=None):  # noqa: E501
        """ConfirmPaymentRequestPaymentMethodCard - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._cardholder_name = None
        self._cardholder_email = None
        self.discriminator = None

        if cardholder_name is not None:
            self.cardholder_name = cardholder_name
        if cardholder_email is not None:
            self.cardholder_email = cardholder_email

    @property
    def cardholder_name(self):
        """Gets the cardholder_name of this ConfirmPaymentRequestPaymentMethodCard.  # noqa: E501

        The cardholder's name, as stated in the credit card.  # noqa: E501

        :return: The cardholder_name of this ConfirmPaymentRequestPaymentMethodCard.  # noqa: E501
        :rtype: str
        """
        return self._cardholder_name

    @cardholder_name.setter
    def cardholder_name(self, cardholder_name):
        """Sets the cardholder_name of this ConfirmPaymentRequestPaymentMethodCard.

        The cardholder's name, as stated in the credit card.  # noqa: E501

        :param cardholder_name: The cardholder_name of this ConfirmPaymentRequestPaymentMethodCard.  # noqa: E501
        :type: str
        """

        self._cardholder_name = cardholder_name

    @property
    def cardholder_email(self):
        """Gets the cardholder_email of this ConfirmPaymentRequestPaymentMethodCard.  # noqa: E501

        The cardholder's email address.  # noqa: E501

        :return: The cardholder_email of this ConfirmPaymentRequestPaymentMethodCard.  # noqa: E501
        :rtype: str
        """
        return self._cardholder_email

    @cardholder_email.setter
    def cardholder_email(self, cardholder_email):
        """Sets the cardholder_email of this ConfirmPaymentRequestPaymentMethodCard.

        The cardholder's email address.  # noqa: E501

        :param cardholder_email: The cardholder_email of this ConfirmPaymentRequestPaymentMethodCard.  # noqa: E501
        :type: str
        """

        self._cardholder_email = cardholder_email

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
        if not isinstance(other, ConfirmPaymentRequestPaymentMethodCard):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConfirmPaymentRequestPaymentMethodCard):
            return True

        return self.to_dict() != other.to_dict()
