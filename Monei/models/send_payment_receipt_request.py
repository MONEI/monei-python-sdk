# coding: utf-8

"""
    MONEI API v1

    <p>The MONEI API is organized around <a href=\"https://en.wikipedia.org/wiki/Representational_State_Transfer\">REST</a>. Our API has predictable resource-oriented URLs, accepts JSON-encoded request bodies, returns JSON-encoded responses, and uses standard HTTP response codes, authentication, and verbs.</p> <h4 id=\"base-url\">Base URL:</h4> <p><a href=\"https://api.monei.com/v1\">https://api.monei.com/v1</a></p> <h4 id=\"client-libraries\">Client libraries:</h4> <ul> <li><a href=\"https://github.com/MONEI/monei-php-sdk\">PHP SDK</a></li> <li><a href=\"https://github.com/MONEI/monei-python-sdk\">Python SDK</a></li> <li><a href=\"https://github.com/MONEI/monei-node-sdk\">Node.js SDK</a></li> <li><a href=\"https://postman.monei.com/\">Postman</a></li> </ul> <h4 id=\"important\">Important:</h4> <p><strong>If you are not using our official SDKs, you need to provide a valid <code>User-Agent</code> header in each request, otherwise your requests will be rejected.</strong></p>   # noqa: E501

    The version of the OpenAPI document: 1.4.6
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from Monei.configuration import Configuration


class SendPaymentReceiptRequest(object):
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
        'customer_email': 'str',
        'customer_phone': 'str',
        'channel': 'PaymentMessageChannel',
        'language': 'PaymentMessageLanguage'
    }

    attribute_map = {
        'customer_email': 'customerEmail',
        'customer_phone': 'customerPhone',
        'channel': 'channel',
        'language': 'language'
    }

    def __init__(self, customer_email=None, customer_phone=None, channel=None, language=None, local_vars_configuration=None):  # noqa: E501
        """SendPaymentReceiptRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._customer_email = None
        self._customer_phone = None
        self._channel = None
        self._language = None
        self.discriminator = None

        if customer_email is not None:
            self.customer_email = customer_email
        if customer_phone is not None:
            self.customer_phone = customer_phone
        if channel is not None:
            self.channel = channel
        if language is not None:
            self.language = language

    @property
    def customer_email(self):
        """Gets the customer_email of this SendPaymentReceiptRequest.  # noqa: E501

        The customer will receive payment receipt on this email address.  # noqa: E501

        :return: The customer_email of this SendPaymentReceiptRequest.  # noqa: E501
        :rtype: str
        """
        return self._customer_email

    @customer_email.setter
    def customer_email(self, customer_email):
        """Sets the customer_email of this SendPaymentReceiptRequest.

        The customer will receive payment receipt on this email address.  # noqa: E501

        :param customer_email: The customer_email of this SendPaymentReceiptRequest.  # noqa: E501
        :type: str
        """

        self._customer_email = customer_email

    @property
    def customer_phone(self):
        """Gets the customer_phone of this SendPaymentReceiptRequest.  # noqa: E501

        Phone number in E.164 format. The customer will receive payment receipt link on this phone number.  # noqa: E501

        :return: The customer_phone of this SendPaymentReceiptRequest.  # noqa: E501
        :rtype: str
        """
        return self._customer_phone

    @customer_phone.setter
    def customer_phone(self, customer_phone):
        """Sets the customer_phone of this SendPaymentReceiptRequest.

        Phone number in E.164 format. The customer will receive payment receipt link on this phone number.  # noqa: E501

        :param customer_phone: The customer_phone of this SendPaymentReceiptRequest.  # noqa: E501
        :type: str
        """

        self._customer_phone = customer_phone

    @property
    def channel(self):
        """Gets the channel of this SendPaymentReceiptRequest.  # noqa: E501


        :return: The channel of this SendPaymentReceiptRequest.  # noqa: E501
        :rtype: PaymentMessageChannel
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this SendPaymentReceiptRequest.


        :param channel: The channel of this SendPaymentReceiptRequest.  # noqa: E501
        :type: PaymentMessageChannel
        """

        self._channel = channel

    @property
    def language(self):
        """Gets the language of this SendPaymentReceiptRequest.  # noqa: E501


        :return: The language of this SendPaymentReceiptRequest.  # noqa: E501
        :rtype: PaymentMessageLanguage
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this SendPaymentReceiptRequest.


        :param language: The language of this SendPaymentReceiptRequest.  # noqa: E501
        :type: PaymentMessageLanguage
        """

        self._language = language

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
        if not isinstance(other, SendPaymentReceiptRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SendPaymentReceiptRequest):
            return True

        return self.to_dict() != other.to_dict()
