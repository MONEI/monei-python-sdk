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


class PaymentPaymentMethodSepa(object):
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
        'accountholder_address': 'str',
        'accountholder_email': 'str',
        'accountholder_name': 'str',
        'country_code': 'str',
        'bank_address': 'str',
        'bank_code': 'str',
        'bank_name': 'str',
        'bic': 'str',
        'last4': 'str'
    }

    attribute_map = {
        'accountholder_address': 'accountholderAddress',
        'accountholder_email': 'accountholderEmail',
        'accountholder_name': 'accountholderName',
        'country_code': 'countryCode',
        'bank_address': 'bankAddress',
        'bank_code': 'bankCode',
        'bank_name': 'bankName',
        'bic': 'bic',
        'last4': 'last4'
    }

    def __init__(self, accountholder_address=None, accountholder_email=None, accountholder_name=None, country_code=None, bank_address=None, bank_code=None, bank_name=None, bic=None, last4=None, local_vars_configuration=None):  # noqa: E501
        """PaymentPaymentMethodSepa - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._accountholder_address = None
        self._accountholder_email = None
        self._accountholder_name = None
        self._country_code = None
        self._bank_address = None
        self._bank_code = None
        self._bank_name = None
        self._bic = None
        self._last4 = None
        self.discriminator = None

        if accountholder_address is not None:
            self.accountholder_address = accountholder_address
        if accountholder_email is not None:
            self.accountholder_email = accountholder_email
        if accountholder_name is not None:
            self.accountholder_name = accountholder_name
        if country_code is not None:
            self.country_code = country_code
        if bank_address is not None:
            self.bank_address = bank_address
        if bank_code is not None:
            self.bank_code = bank_code
        if bank_name is not None:
            self.bank_name = bank_name
        if bic is not None:
            self.bic = bic
        if last4 is not None:
            self.last4 = last4

    @property
    def accountholder_address(self):
        """Gets the accountholder_address of this PaymentPaymentMethodSepa.  # noqa: E501

        The address of the account holder.  # noqa: E501

        :return: The accountholder_address of this PaymentPaymentMethodSepa.  # noqa: E501
        :rtype: str
        """
        return self._accountholder_address

    @accountholder_address.setter
    def accountholder_address(self, accountholder_address):
        """Sets the accountholder_address of this PaymentPaymentMethodSepa.

        The address of the account holder.  # noqa: E501

        :param accountholder_address: The accountholder_address of this PaymentPaymentMethodSepa.  # noqa: E501
        :type: str
        """

        self._accountholder_address = accountholder_address

    @property
    def accountholder_email(self):
        """Gets the accountholder_email of this PaymentPaymentMethodSepa.  # noqa: E501

        The email of the account holder.  # noqa: E501

        :return: The accountholder_email of this PaymentPaymentMethodSepa.  # noqa: E501
        :rtype: str
        """
        return self._accountholder_email

    @accountholder_email.setter
    def accountholder_email(self, accountholder_email):
        """Sets the accountholder_email of this PaymentPaymentMethodSepa.

        The email of the account holder.  # noqa: E501

        :param accountholder_email: The accountholder_email of this PaymentPaymentMethodSepa.  # noqa: E501
        :type: str
        """

        self._accountholder_email = accountholder_email

    @property
    def accountholder_name(self):
        """Gets the accountholder_name of this PaymentPaymentMethodSepa.  # noqa: E501

        The name of the account holder.  # noqa: E501

        :return: The accountholder_name of this PaymentPaymentMethodSepa.  # noqa: E501
        :rtype: str
        """
        return self._accountholder_name

    @accountholder_name.setter
    def accountholder_name(self, accountholder_name):
        """Sets the accountholder_name of this PaymentPaymentMethodSepa.

        The name of the account holder.  # noqa: E501

        :param accountholder_name: The accountholder_name of this PaymentPaymentMethodSepa.  # noqa: E501
        :type: str
        """

        self._accountholder_name = accountholder_name

    @property
    def country_code(self):
        """Gets the country_code of this PaymentPaymentMethodSepa.  # noqa: E501

        The country code of the account holder.  # noqa: E501

        :return: The country_code of this PaymentPaymentMethodSepa.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this PaymentPaymentMethodSepa.

        The country code of the account holder.  # noqa: E501

        :param country_code: The country_code of this PaymentPaymentMethodSepa.  # noqa: E501
        :type: str
        """

        self._country_code = country_code

    @property
    def bank_address(self):
        """Gets the bank_address of this PaymentPaymentMethodSepa.  # noqa: E501

        The address of the bank.  # noqa: E501

        :return: The bank_address of this PaymentPaymentMethodSepa.  # noqa: E501
        :rtype: str
        """
        return self._bank_address

    @bank_address.setter
    def bank_address(self, bank_address):
        """Sets the bank_address of this PaymentPaymentMethodSepa.

        The address of the bank.  # noqa: E501

        :param bank_address: The bank_address of this PaymentPaymentMethodSepa.  # noqa: E501
        :type: str
        """

        self._bank_address = bank_address

    @property
    def bank_code(self):
        """Gets the bank_code of this PaymentPaymentMethodSepa.  # noqa: E501

        The code of the bank.  # noqa: E501

        :return: The bank_code of this PaymentPaymentMethodSepa.  # noqa: E501
        :rtype: str
        """
        return self._bank_code

    @bank_code.setter
    def bank_code(self, bank_code):
        """Sets the bank_code of this PaymentPaymentMethodSepa.

        The code of the bank.  # noqa: E501

        :param bank_code: The bank_code of this PaymentPaymentMethodSepa.  # noqa: E501
        :type: str
        """

        self._bank_code = bank_code

    @property
    def bank_name(self):
        """Gets the bank_name of this PaymentPaymentMethodSepa.  # noqa: E501

        The name of the bank.  # noqa: E501

        :return: The bank_name of this PaymentPaymentMethodSepa.  # noqa: E501
        :rtype: str
        """
        return self._bank_name

    @bank_name.setter
    def bank_name(self, bank_name):
        """Sets the bank_name of this PaymentPaymentMethodSepa.

        The name of the bank.  # noqa: E501

        :param bank_name: The bank_name of this PaymentPaymentMethodSepa.  # noqa: E501
        :type: str
        """

        self._bank_name = bank_name

    @property
    def bic(self):
        """Gets the bic of this PaymentPaymentMethodSepa.  # noqa: E501

        The BIC of the bank.  # noqa: E501

        :return: The bic of this PaymentPaymentMethodSepa.  # noqa: E501
        :rtype: str
        """
        return self._bic

    @bic.setter
    def bic(self, bic):
        """Sets the bic of this PaymentPaymentMethodSepa.

        The BIC of the bank.  # noqa: E501

        :param bic: The bic of this PaymentPaymentMethodSepa.  # noqa: E501
        :type: str
        """

        self._bic = bic

    @property
    def last4(self):
        """Gets the last4 of this PaymentPaymentMethodSepa.  # noqa: E501

        The last 4 digits of the IBAN.  # noqa: E501

        :return: The last4 of this PaymentPaymentMethodSepa.  # noqa: E501
        :rtype: str
        """
        return self._last4

    @last4.setter
    def last4(self, last4):
        """Sets the last4 of this PaymentPaymentMethodSepa.

        The last 4 digits of the IBAN.  # noqa: E501

        :param last4: The last4 of this PaymentPaymentMethodSepa.  # noqa: E501
        :type: str
        """

        self._last4 = last4

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
        if not isinstance(other, PaymentPaymentMethodSepa):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PaymentPaymentMethodSepa):
            return True

        return self.to_dict() != other.to_dict()
