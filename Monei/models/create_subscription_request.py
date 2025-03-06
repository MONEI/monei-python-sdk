# coding: utf-8

"""
    MONEI API v1

    <p>The MONEI API is organized around <a href=\"https://en.wikipedia.org/wiki/Representational_State_Transfer\">REST</a> principles. Our API is designed to be intuitive and developer-friendly.</p> <h3>Base URL</h3> <p>All API requests should be made to:</p> <pre><code>https://api.monei.com/v1 </code></pre> <h3>Environment</h3> <p>MONEI provides two environments:</p> <ul> <li><strong>Test Environment</strong>: For development and testing without processing real payments</li> <li><strong>Live Environment</strong>: For processing real transactions in production</li> </ul> <h3>Client Libraries</h3> <p>We provide official SDKs to simplify integration:</p> <ul> <li><a href=\"https://github.com/MONEI/monei-php-sdk\">PHP SDK</a></li> <li><a href=\"https://github.com/MONEI/monei-python-sdk\">Python SDK</a></li> <li><a href=\"https://github.com/MONEI/monei-node-sdk\">Node.js SDK</a></li> <li><a href=\"https://postman.monei.com/\">Postman Collection</a></li> </ul> <p>Our SDKs handle authentication, error handling, and request formatting automatically.</p> <p>You can download the OpenAPI specification from the <a href=\"https://js.monei.com/api/v1/openapi.json\">https://js.monei.com/api/v1/openapi.json</a> and generate your own client library using the <a href=\"https://openapi-generator.tech/\">OpenAPI Generator</a>.</p> <h3>Important Requirements</h3> <ul> <li>All API requests must be made over HTTPS</li> <li>If you are not using our official SDKs, you <strong>must provide a valid <code>User-Agent</code> header</strong> with each request</li> <li>Requests without proper authentication will return a <code>401 Unauthorized</code> error</li> </ul> <h3>Error Handling</h3> <p>The API returns consistent error codes and messages to help you troubleshoot issues. Each response includes a <code>statusCode</code> attribute indicating the outcome of your request.</p> <h3>Rate Limits</h3> <p>The API implements rate limiting to ensure stability. If you exceed the limits, requests will return a <code>429 Too Many Requests</code> status code.</p> 

    The version of the OpenAPI document: 1.5.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from Monei.models.payment_billing_details import PaymentBillingDetails
from Monei.models.payment_customer import PaymentCustomer
from Monei.models.payment_shipping_details import PaymentShippingDetails
from Monei.models.subscription_interval import SubscriptionInterval
from Monei.models.subscription_retry_schedule_inner import SubscriptionRetryScheduleInner
from typing import Optional, Set
from typing_extensions import Self

class CreateSubscriptionRequest(BaseModel):
    """
    CreateSubscriptionRequest
    """ # noqa: E501
    amount: StrictInt = Field(description="Amount intended to be collected by this payment. A positive integer representing how much to charge in the smallest currency unit (e.g., 100 cents to charge 1.00 USD). ")
    currency: StrictStr = Field(description="Three-letter [ISO currency code](https://en.wikipedia.org/wiki/ISO_4217), in uppercase. Must be a supported currency. ")
    interval: SubscriptionInterval
    interval_count: Optional[StrictInt] = Field(default=None, description="Number of intervals between subscription payments.", alias="intervalCount")
    description: Optional[StrictStr] = Field(default=None, description="An arbitrary string attached to the subscription. Often useful for displaying to users. ")
    customer: Optional[PaymentCustomer] = None
    billing_details: Optional[PaymentBillingDetails] = Field(default=None, alias="billingDetails")
    shipping_details: Optional[PaymentShippingDetails] = Field(default=None, alias="shippingDetails")
    trial_period_end: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The end date of the trial period. Measured in seconds since the Unix epoch.", alias="trialPeriodEnd")
    trial_period_days: Optional[StrictInt] = Field(default=None, description="Number of days the trial period lasts.", alias="trialPeriodDays")
    retry_schedule: Optional[List[SubscriptionRetryScheduleInner]] = Field(default=None, description="Defines a custom schedule for retrying failed subscription payments. Each entry in the array specifies how long to wait before attempting the next payment retry. If not specified, the system's default retry schedule will be used. ", alias="retrySchedule")
    callback_url: Optional[StrictStr] = Field(default=None, description="The URL will be called each time subscription status changes. You will receive a subscription object in the body of the request. ", alias="callbackUrl")
    payment_callback_url: Optional[StrictStr] = Field(default=None, description="The URL will be called each time subscription creates a new payments. You will receive the payment object in the body of the request. ", alias="paymentCallbackUrl")
    metadata: Optional[Dict[str, Any]] = Field(default=None, description="A set of key-value pairs that you can attach to a resource. This can be useful for storing additional information about the resource in a structured format.")
    __properties: ClassVar[List[str]] = ["amount", "currency", "interval", "intervalCount", "description", "customer", "billingDetails", "shippingDetails", "trialPeriodEnd", "trialPeriodDays", "retrySchedule", "callbackUrl", "paymentCallbackUrl", "metadata"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of CreateSubscriptionRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of customer
        if self.customer:
            _dict['customer'] = self.customer.to_dict()
        # override the default output from pydantic by calling `to_dict()` of billing_details
        if self.billing_details:
            _dict['billingDetails'] = self.billing_details.to_dict()
        # override the default output from pydantic by calling `to_dict()` of shipping_details
        if self.shipping_details:
            _dict['shippingDetails'] = self.shipping_details.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in retry_schedule (list)
        _items = []
        if self.retry_schedule:
            for _item_retry_schedule in self.retry_schedule:
                if _item_retry_schedule:
                    _items.append(_item_retry_schedule.to_dict())
            _dict['retrySchedule'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateSubscriptionRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "amount": obj.get("amount"),
            "currency": obj.get("currency"),
            "interval": obj.get("interval"),
            "intervalCount": obj.get("intervalCount"),
            "description": obj.get("description"),
            "customer": PaymentCustomer.from_dict(obj["customer"]) if obj.get("customer") is not None else None,
            "billingDetails": PaymentBillingDetails.from_dict(obj["billingDetails"]) if obj.get("billingDetails") is not None else None,
            "shippingDetails": PaymentShippingDetails.from_dict(obj["shippingDetails"]) if obj.get("shippingDetails") is not None else None,
            "trialPeriodEnd": obj.get("trialPeriodEnd"),
            "trialPeriodDays": obj.get("trialPeriodDays"),
            "retrySchedule": [SubscriptionRetryScheduleInner.from_dict(_item) for _item in obj["retrySchedule"]] if obj.get("retrySchedule") is not None else None,
            "callbackUrl": obj.get("callbackUrl"),
            "paymentCallbackUrl": obj.get("paymentCallbackUrl"),
            "metadata": obj.get("metadata")
        })
        return _obj


