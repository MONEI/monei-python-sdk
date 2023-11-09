# coding: utf-8

"""
    MONEI API v1

    <p>The MONEI API is organized around <a href=\"https://en.wikipedia.org/wiki/Representational_State_Transfer\">REST</a>. Our API has predictable resource-oriented URLs, accepts JSON-encoded request bodies, returns JSON-encoded responses, and uses standard HTTP response codes, authentication, and verbs.</p> <h4 id=\"base-url\">Base URL:</h4> <p><a href=\"https://api.monei.com/v1\">https://api.monei.com/v1</a></p> <h4 id=\"client-libraries\">Client libraries:</h4> <ul> <li><a href=\"https://github.com/MONEI/monei-php-sdk\">PHP SDK</a></li> <li><a href=\"https://github.com/MONEI/monei-python-sdk\">Python SDK</a></li> <li><a href=\"https://github.com/MONEI/monei-node-sdk\">Node.js SDK</a></li> <li><a href=\"https://postman.monei.com/\">Postman</a></li> </ul> <h4 id=\"important\">Important:</h4> <p><strong>If you are not using our official SDKs, you need to provide a valid <code>User-Agent</code> header in each request, otherwise your requests will be rejected.</strong></p>   # noqa: E501

    The version of the OpenAPI document: 1.4.4
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from Monei.configuration import Configuration


class PaymentPaymentMethodCard(object):
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
        'country': 'str',
        'brand': 'str',
        'type': 'str',
        'three_d_secure': 'bool',
        'three_d_secure_version': 'str',
        'three_d_secure_flow': 'str',
        'expiration': 'int',
        'last4': 'str',
        'tokenization_method': 'str',
        'cardholder_name': 'str',
        'cardholder_email': 'str'
    }

    attribute_map = {
        'country': 'country',
        'brand': 'brand',
        'type': 'type',
        'three_d_secure': 'threeDSecure',
        'three_d_secure_version': 'threeDSecureVersion',
        'three_d_secure_flow': 'threeDSecureFlow',
        'expiration': 'expiration',
        'last4': 'last4',
        'tokenization_method': 'tokenizationMethod',
        'cardholder_name': 'cardholderName',
        'cardholder_email': 'cardholderEmail'
    }

    def __init__(self, country=None, brand=None, type=None, three_d_secure=None, three_d_secure_version=None, three_d_secure_flow=None, expiration=None, last4=None, tokenization_method=None, cardholder_name=None, cardholder_email=None, local_vars_configuration=None):  # noqa: E501
        """PaymentPaymentMethodCard - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._country = None
        self._brand = None
        self._type = None
        self._three_d_secure = None
        self._three_d_secure_version = None
        self._three_d_secure_flow = None
        self._expiration = None
        self._last4 = None
        self._tokenization_method = None
        self._cardholder_name = None
        self._cardholder_email = None
        self.discriminator = None

        if country is not None:
            self.country = country
        if brand is not None:
            self.brand = brand
        if type is not None:
            self.type = type
        if three_d_secure is not None:
            self.three_d_secure = three_d_secure
        if three_d_secure_version is not None:
            self.three_d_secure_version = three_d_secure_version
        if three_d_secure_flow is not None:
            self.three_d_secure_flow = three_d_secure_flow
        if expiration is not None:
            self.expiration = expiration
        if last4 is not None:
            self.last4 = last4
        if tokenization_method is not None:
            self.tokenization_method = tokenization_method
        if cardholder_name is not None:
            self.cardholder_name = cardholder_name
        if cardholder_email is not None:
            self.cardholder_email = cardholder_email

    @property
    def country(self):
        """Gets the country of this PaymentPaymentMethodCard.  # noqa: E501

        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).  # noqa: E501

        :return: The country of this PaymentPaymentMethodCard.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this PaymentPaymentMethodCard.

        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).  # noqa: E501

        :param country: The country of this PaymentPaymentMethodCard.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def brand(self):
        """Gets the brand of this PaymentPaymentMethodCard.  # noqa: E501

        Card brand.  # noqa: E501

        :return: The brand of this PaymentPaymentMethodCard.  # noqa: E501
        :rtype: str
        """
        return self._brand

    @brand.setter
    def brand(self, brand):
        """Sets the brand of this PaymentPaymentMethodCard.

        Card brand.  # noqa: E501

        :param brand: The brand of this PaymentPaymentMethodCard.  # noqa: E501
        :type: str
        """
        allowed_values = ["visa", "mastercard", "diners", "amex", "jcb", "unionpay", "unknown"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and brand not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `brand` ({0}), must be one of {1}"  # noqa: E501
                .format(brand, allowed_values)
            )

        self._brand = brand

    @property
    def type(self):
        """Gets the type of this PaymentPaymentMethodCard.  # noqa: E501

        Card type `debit` or `credit`.  # noqa: E501

        :return: The type of this PaymentPaymentMethodCard.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PaymentPaymentMethodCard.

        Card type `debit` or `credit`.  # noqa: E501

        :param type: The type of this PaymentPaymentMethodCard.  # noqa: E501
        :type: str
        """
        allowed_values = ["debit", "credit"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def three_d_secure(self):
        """Gets the three_d_secure of this PaymentPaymentMethodCard.  # noqa: E501

        Whether this transaction used 3D Secure authentication.  # noqa: E501

        :return: The three_d_secure of this PaymentPaymentMethodCard.  # noqa: E501
        :rtype: bool
        """
        return self._three_d_secure

    @three_d_secure.setter
    def three_d_secure(self, three_d_secure):
        """Sets the three_d_secure of this PaymentPaymentMethodCard.

        Whether this transaction used 3D Secure authentication.  # noqa: E501

        :param three_d_secure: The three_d_secure of this PaymentPaymentMethodCard.  # noqa: E501
        :type: bool
        """

        self._three_d_secure = three_d_secure

    @property
    def three_d_secure_version(self):
        """Gets the three_d_secure_version of this PaymentPaymentMethodCard.  # noqa: E501

        The protocol version of the 3DS challenge.  # noqa: E501

        :return: The three_d_secure_version of this PaymentPaymentMethodCard.  # noqa: E501
        :rtype: str
        """
        return self._three_d_secure_version

    @three_d_secure_version.setter
    def three_d_secure_version(self, three_d_secure_version):
        """Sets the three_d_secure_version of this PaymentPaymentMethodCard.

        The protocol version of the 3DS challenge.  # noqa: E501

        :param three_d_secure_version: The three_d_secure_version of this PaymentPaymentMethodCard.  # noqa: E501
        :type: str
        """

        self._three_d_secure_version = three_d_secure_version

    @property
    def three_d_secure_flow(self):
        """Gets the three_d_secure_flow of this PaymentPaymentMethodCard.  # noqa: E501

        The flow used for 3DS authentication. - `CHALLENGE` - In a challenge flow, the issuer requires additional shopper interaction, either through biometrics, two-factor authentication, or similar methods based on [Strong Customer Authentication (SCA)](https://en.wikipedia.org/wiki/Strong_customer_authentication) factors. - `FRICTIONLESS` - In a frictionless flow, the acquirer, issuer, and card scheme exchange all necessary     information in the background through passive authentication using the shopper's device     fingerprint. The transaction is completed without further shopper interaction. - `FRICTIONLESS_CHALLENGE` - This flow is the complete 3DS flow. It is similar to the 3DS frictionless flow but     includes an additional authentication step (challenge) that will be invoked if the     information provided in the data collection step does not suffice to determine the     risk-level of the transaction. - `DIRECT` - This transaction did not require [Strong Customer Authentication (SCA)](https://en.wikipedia.org/wiki/Strong_customer_authentication) due to the low risk   # noqa: E501

        :return: The three_d_secure_flow of this PaymentPaymentMethodCard.  # noqa: E501
        :rtype: str
        """
        return self._three_d_secure_flow

    @three_d_secure_flow.setter
    def three_d_secure_flow(self, three_d_secure_flow):
        """Sets the three_d_secure_flow of this PaymentPaymentMethodCard.

        The flow used for 3DS authentication. - `CHALLENGE` - In a challenge flow, the issuer requires additional shopper interaction, either through biometrics, two-factor authentication, or similar methods based on [Strong Customer Authentication (SCA)](https://en.wikipedia.org/wiki/Strong_customer_authentication) factors. - `FRICTIONLESS` - In a frictionless flow, the acquirer, issuer, and card scheme exchange all necessary     information in the background through passive authentication using the shopper's device     fingerprint. The transaction is completed without further shopper interaction. - `FRICTIONLESS_CHALLENGE` - This flow is the complete 3DS flow. It is similar to the 3DS frictionless flow but     includes an additional authentication step (challenge) that will be invoked if the     information provided in the data collection step does not suffice to determine the     risk-level of the transaction. - `DIRECT` - This transaction did not require [Strong Customer Authentication (SCA)](https://en.wikipedia.org/wiki/Strong_customer_authentication) due to the low risk   # noqa: E501

        :param three_d_secure_flow: The three_d_secure_flow of this PaymentPaymentMethodCard.  # noqa: E501
        :type: str
        """
        allowed_values = ["CHALLENGE", "FRICTIONLESS", "FRICTIONLESS_CHALLENGE", "DIRECT"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and three_d_secure_flow not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `three_d_secure_flow` ({0}), must be one of {1}"  # noqa: E501
                .format(three_d_secure_flow, allowed_values)
            )

        self._three_d_secure_flow = three_d_secure_flow

    @property
    def expiration(self):
        """Gets the expiration of this PaymentPaymentMethodCard.  # noqa: E501

        Time at which the card will expire. Measured in seconds since the Unix epoch.   # noqa: E501

        :return: The expiration of this PaymentPaymentMethodCard.  # noqa: E501
        :rtype: int
        """
        return self._expiration

    @expiration.setter
    def expiration(self, expiration):
        """Sets the expiration of this PaymentPaymentMethodCard.

        Time at which the card will expire. Measured in seconds since the Unix epoch.   # noqa: E501

        :param expiration: The expiration of this PaymentPaymentMethodCard.  # noqa: E501
        :type: int
        """

        self._expiration = expiration

    @property
    def last4(self):
        """Gets the last4 of this PaymentPaymentMethodCard.  # noqa: E501

        The last four digits of the card.  # noqa: E501

        :return: The last4 of this PaymentPaymentMethodCard.  # noqa: E501
        :rtype: str
        """
        return self._last4

    @last4.setter
    def last4(self, last4):
        """Sets the last4 of this PaymentPaymentMethodCard.

        The last four digits of the card.  # noqa: E501

        :param last4: The last4 of this PaymentPaymentMethodCard.  # noqa: E501
        :type: str
        """

        self._last4 = last4

    @property
    def tokenization_method(self):
        """Gets the tokenization_method of this PaymentPaymentMethodCard.  # noqa: E501

        The digital wallet used to tokenize the card.  # noqa: E501

        :return: The tokenization_method of this PaymentPaymentMethodCard.  # noqa: E501
        :rtype: str
        """
        return self._tokenization_method

    @tokenization_method.setter
    def tokenization_method(self, tokenization_method):
        """Sets the tokenization_method of this PaymentPaymentMethodCard.

        The digital wallet used to tokenize the card.  # noqa: E501

        :param tokenization_method: The tokenization_method of this PaymentPaymentMethodCard.  # noqa: E501
        :type: str
        """
        allowed_values = ["applePay", "googlePay", "clickToPay"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and tokenization_method not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `tokenization_method` ({0}), must be one of {1}"  # noqa: E501
                .format(tokenization_method, allowed_values)
            )

        self._tokenization_method = tokenization_method

    @property
    def cardholder_name(self):
        """Gets the cardholder_name of this PaymentPaymentMethodCard.  # noqa: E501

        The name of the cardholder.  # noqa: E501

        :return: The cardholder_name of this PaymentPaymentMethodCard.  # noqa: E501
        :rtype: str
        """
        return self._cardholder_name

    @cardholder_name.setter
    def cardholder_name(self, cardholder_name):
        """Sets the cardholder_name of this PaymentPaymentMethodCard.

        The name of the cardholder.  # noqa: E501

        :param cardholder_name: The cardholder_name of this PaymentPaymentMethodCard.  # noqa: E501
        :type: str
        """

        self._cardholder_name = cardholder_name

    @property
    def cardholder_email(self):
        """Gets the cardholder_email of this PaymentPaymentMethodCard.  # noqa: E501

        The email of the cardholder.  # noqa: E501

        :return: The cardholder_email of this PaymentPaymentMethodCard.  # noqa: E501
        :rtype: str
        """
        return self._cardholder_email

    @cardholder_email.setter
    def cardholder_email(self, cardholder_email):
        """Sets the cardholder_email of this PaymentPaymentMethodCard.

        The email of the cardholder.  # noqa: E501

        :param cardholder_email: The cardholder_email of this PaymentPaymentMethodCard.  # noqa: E501
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
        if not isinstance(other, PaymentPaymentMethodCard):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PaymentPaymentMethodCard):
            return True

        return self.to_dict() != other.to_dict()
