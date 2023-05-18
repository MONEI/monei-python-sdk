# coding: utf-8

"""
    MONEI API v1

    <p>The MONEI API is organized around <a href=\"https://en.wikipedia.org/wiki/Representational_State_Transfer\">REST</a>. Our API has predictable resource-oriented URLs, accepts JSON-encoded request bodies, returns JSON-encoded responses, and uses standard HTTP response codes, authentication, and verbs.</p> <h4 id=\"base-url\">Base URL:</h4> <p><a href=\"https://api.monei.com/v1\">https://api.monei.com/v1</a></p> <h4 id=\"client-libraries\">Client libraries:</h4> <ul> <li><a href=\"https://github.com/MONEI/monei-php-sdk\">PHP SDK</a></li> <li><a href=\"https://github.com/MONEI/monei-python-sdk\">Python SDK</a></li> <li><a href=\"https://github.com/MONEI/monei-node-sdk\">Node.js SDK</a></li> <li><a href=\"https://postman.monei.com/\">Postman</a></li> </ul> <h4 id=\"important\">Important:</h4> <p><strong>If you are not using our official SDKs, you need to provide a valid <code>User-Agent</code> header in each request, otherwise your requests will be rejected.</strong></p>   # noqa: E501

    The version of the OpenAPI document: 1.4.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from Monei.configuration import Configuration


class CancelSubscriptionRequest(object):
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
        'cancel_at_period_end': 'bool'
    }

    attribute_map = {
        'cancel_at_period_end': 'cancelAtPeriodEnd'
    }

    def __init__(self, cancel_at_period_end=None, local_vars_configuration=None):  # noqa: E501
        """CancelSubscriptionRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._cancel_at_period_end = None
        self.discriminator = None

        if cancel_at_period_end is not None:
            self.cancel_at_period_end = cancel_at_period_end

    @property
    def cancel_at_period_end(self):
        """Gets the cancel_at_period_end of this CancelSubscriptionRequest.  # noqa: E501

        If true, the subscription will be canceled at the end of the current period.   # noqa: E501

        :return: The cancel_at_period_end of this CancelSubscriptionRequest.  # noqa: E501
        :rtype: bool
        """
        return self._cancel_at_period_end

    @cancel_at_period_end.setter
    def cancel_at_period_end(self, cancel_at_period_end):
        """Sets the cancel_at_period_end of this CancelSubscriptionRequest.

        If true, the subscription will be canceled at the end of the current period.   # noqa: E501

        :param cancel_at_period_end: The cancel_at_period_end of this CancelSubscriptionRequest.  # noqa: E501
        :type: bool
        """

        self._cancel_at_period_end = cancel_at_period_end

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
        if not isinstance(other, CancelSubscriptionRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CancelSubscriptionRequest):
            return True

        return self.to_dict() != other.to_dict()
