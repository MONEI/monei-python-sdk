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

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from Monei.models.payment_payment_method_bizum_input import PaymentPaymentMethodBizumInput
from Monei.models.payment_payment_method_card_input import PaymentPaymentMethodCardInput
from typing import Optional, Set
from typing_extensions import Self

class PaymentPaymentMethodInput(BaseModel):
    """
    An information about a payment method used for this payment. We recommend using `paymentToken` instead, as it is more secure way to pass sensitive payment information. Processing credit card information on your server requires [PCI DSS compliance](https://www.investopedia.com/terms/p/pci-compliance.asp). 
    """ # noqa: E501
    card: Optional[PaymentPaymentMethodCardInput] = None
    bizum: Optional[PaymentPaymentMethodBizumInput] = None
    __properties: ClassVar[List[str]] = ["card", "bizum"]

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
        """Create an instance of PaymentPaymentMethodInput from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of card
        if self.card:
            _dict['card'] = self.card.to_dict()
        # override the default output from pydantic by calling `to_dict()` of bizum
        if self.bizum:
            _dict['bizum'] = self.bizum.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PaymentPaymentMethodInput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "card": PaymentPaymentMethodCardInput.from_dict(obj["card"]) if obj.get("card") is not None else None,
            "bizum": PaymentPaymentMethodBizumInput.from_dict(obj["bizum"]) if obj.get("bizum") is not None else None
        })
        return _obj


