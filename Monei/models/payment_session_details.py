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


class PaymentSessionDetails(object):
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
        'ip': 'str',
        'country_code': 'str',
        'lang': 'str',
        'device_type': 'str',
        'device_model': 'str',
        'browser': 'str',
        'browser_version': 'str',
        'os': 'str',
        'os_version': 'str',
        'source': 'str',
        'source_version': 'str',
        'user_agent': 'str'
    }

    attribute_map = {
        'ip': 'ip',
        'country_code': 'countryCode',
        'lang': 'lang',
        'device_type': 'deviceType',
        'device_model': 'deviceModel',
        'browser': 'browser',
        'browser_version': 'browserVersion',
        'os': 'os',
        'os_version': 'osVersion',
        'source': 'source',
        'source_version': 'sourceVersion',
        'user_agent': 'userAgent'
    }

    def __init__(self, ip=None, country_code=None, lang=None, device_type=None, device_model=None, browser=None, browser_version=None, os=None, os_version=None, source=None, source_version=None, user_agent=None, local_vars_configuration=None):  # noqa: E501
        """PaymentSessionDetails - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._ip = None
        self._country_code = None
        self._lang = None
        self._device_type = None
        self._device_model = None
        self._browser = None
        self._browser_version = None
        self._os = None
        self._os_version = None
        self._source = None
        self._source_version = None
        self._user_agent = None
        self.discriminator = None

        if ip is not None:
            self.ip = ip
        if country_code is not None:
            self.country_code = country_code
        if lang is not None:
            self.lang = lang
        if device_type is not None:
            self.device_type = device_type
        if device_model is not None:
            self.device_model = device_model
        if browser is not None:
            self.browser = browser
        if browser_version is not None:
            self.browser_version = browser_version
        if os is not None:
            self.os = os
        if os_version is not None:
            self.os_version = os_version
        if source is not None:
            self.source = source
        if source_version is not None:
            self.source_version = source_version
        if user_agent is not None:
            self.user_agent = user_agent

    @property
    def ip(self):
        """Gets the ip of this PaymentSessionDetails.  # noqa: E501

        The IP address where the operation originated.  # noqa: E501

        :return: The ip of this PaymentSessionDetails.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this PaymentSessionDetails.

        The IP address where the operation originated.  # noqa: E501

        :param ip: The ip of this PaymentSessionDetails.  # noqa: E501
        :type: str
        """

        self._ip = ip

    @property
    def country_code(self):
        """Gets the country_code of this PaymentSessionDetails.  # noqa: E501

        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).  # noqa: E501

        :return: The country_code of this PaymentSessionDetails.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this PaymentSessionDetails.

        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).  # noqa: E501

        :param country_code: The country_code of this PaymentSessionDetails.  # noqa: E501
        :type: str
        """

        self._country_code = country_code

    @property
    def lang(self):
        """Gets the lang of this PaymentSessionDetails.  # noqa: E501

        Two-letter language code ([ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1)).  # noqa: E501

        :return: The lang of this PaymentSessionDetails.  # noqa: E501
        :rtype: str
        """
        return self._lang

    @lang.setter
    def lang(self, lang):
        """Sets the lang of this PaymentSessionDetails.

        Two-letter language code ([ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1)).  # noqa: E501

        :param lang: The lang of this PaymentSessionDetails.  # noqa: E501
        :type: str
        """

        self._lang = lang

    @property
    def device_type(self):
        """Gets the device_type of this PaymentSessionDetails.  # noqa: E501

        Device type, could be `desktop`, `mobile`, `smartTV`, `tablet`.  # noqa: E501

        :return: The device_type of this PaymentSessionDetails.  # noqa: E501
        :rtype: str
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        """Sets the device_type of this PaymentSessionDetails.

        Device type, could be `desktop`, `mobile`, `smartTV`, `tablet`.  # noqa: E501

        :param device_type: The device_type of this PaymentSessionDetails.  # noqa: E501
        :type: str
        """

        self._device_type = device_type

    @property
    def device_model(self):
        """Gets the device_model of this PaymentSessionDetails.  # noqa: E501

        Information about the device used for the browser session (e.g., `iPhone`).  # noqa: E501

        :return: The device_model of this PaymentSessionDetails.  # noqa: E501
        :rtype: str
        """
        return self._device_model

    @device_model.setter
    def device_model(self, device_model):
        """Sets the device_model of this PaymentSessionDetails.

        Information about the device used for the browser session (e.g., `iPhone`).  # noqa: E501

        :param device_model: The device_model of this PaymentSessionDetails.  # noqa: E501
        :type: str
        """

        self._device_model = device_model

    @property
    def browser(self):
        """Gets the browser of this PaymentSessionDetails.  # noqa: E501

        The browser used in this browser session (e.g., `Mobile Safari`).  # noqa: E501

        :return: The browser of this PaymentSessionDetails.  # noqa: E501
        :rtype: str
        """
        return self._browser

    @browser.setter
    def browser(self, browser):
        """Sets the browser of this PaymentSessionDetails.

        The browser used in this browser session (e.g., `Mobile Safari`).  # noqa: E501

        :param browser: The browser of this PaymentSessionDetails.  # noqa: E501
        :type: str
        """

        self._browser = browser

    @property
    def browser_version(self):
        """Gets the browser_version of this PaymentSessionDetails.  # noqa: E501

        The version for the browser session (e.g., `13.1.1`).  # noqa: E501

        :return: The browser_version of this PaymentSessionDetails.  # noqa: E501
        :rtype: str
        """
        return self._browser_version

    @browser_version.setter
    def browser_version(self, browser_version):
        """Sets the browser_version of this PaymentSessionDetails.

        The version for the browser session (e.g., `13.1.1`).  # noqa: E501

        :param browser_version: The browser_version of this PaymentSessionDetails.  # noqa: E501
        :type: str
        """

        self._browser_version = browser_version

    @property
    def os(self):
        """Gets the os of this PaymentSessionDetails.  # noqa: E501

        Operation system (e.g., `iOS`).  # noqa: E501

        :return: The os of this PaymentSessionDetails.  # noqa: E501
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        """Sets the os of this PaymentSessionDetails.

        Operation system (e.g., `iOS`).  # noqa: E501

        :param os: The os of this PaymentSessionDetails.  # noqa: E501
        :type: str
        """

        self._os = os

    @property
    def os_version(self):
        """Gets the os_version of this PaymentSessionDetails.  # noqa: E501

        Operation system version (e.g., `13.5.1`).  # noqa: E501

        :return: The os_version of this PaymentSessionDetails.  # noqa: E501
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        """Sets the os_version of this PaymentSessionDetails.

        Operation system version (e.g., `13.5.1`).  # noqa: E501

        :param os_version: The os_version of this PaymentSessionDetails.  # noqa: E501
        :type: str
        """

        self._os_version = os_version

    @property
    def source(self):
        """Gets the source of this PaymentSessionDetails.  # noqa: E501

        The source component from where the operation was generated (mostly for our SDK's).  # noqa: E501

        :return: The source of this PaymentSessionDetails.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this PaymentSessionDetails.

        The source component from where the operation was generated (mostly for our SDK's).  # noqa: E501

        :param source: The source of this PaymentSessionDetails.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def source_version(self):
        """Gets the source_version of this PaymentSessionDetails.  # noqa: E501

        The source component version from where the operation was generated (mostly for our SDK's).  # noqa: E501

        :return: The source_version of this PaymentSessionDetails.  # noqa: E501
        :rtype: str
        """
        return self._source_version

    @source_version.setter
    def source_version(self, source_version):
        """Sets the source_version of this PaymentSessionDetails.

        The source component version from where the operation was generated (mostly for our SDK's).  # noqa: E501

        :param source_version: The source_version of this PaymentSessionDetails.  # noqa: E501
        :type: str
        """

        self._source_version = source_version

    @property
    def user_agent(self):
        """Gets the user_agent of this PaymentSessionDetails.  # noqa: E501

        Full user agent string of the browser session.  # noqa: E501

        :return: The user_agent of this PaymentSessionDetails.  # noqa: E501
        :rtype: str
        """
        return self._user_agent

    @user_agent.setter
    def user_agent(self, user_agent):
        """Sets the user_agent of this PaymentSessionDetails.

        Full user agent string of the browser session.  # noqa: E501

        :param user_agent: The user_agent of this PaymentSessionDetails.  # noqa: E501
        :type: str
        """

        self._user_agent = user_agent

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
        if not isinstance(other, PaymentSessionDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PaymentSessionDetails):
            return True

        return self.to_dict() != other.to_dict()