"""
    MONEI API v1

    <p>The MONEI API is organized around <a href=\"https://en.wikipedia.org/wiki/Representational_State_Transfer\">REST</a> principles. Our API is designed to be intuitive and developer-friendly.</p> <h3>Base URL</h3> <p>All API requests should be made to:</p> <pre><code>https://api.monei.com/v1 </code></pre> <h3>Environment</h3> <p>MONEI provides two environments:</p> <ul> <li><strong>Test Environment</strong>: For development and testing without processing real payments</li> <li><strong>Live Environment</strong>: For processing real transactions in production</li> </ul> <h3>Client Libraries</h3> <p>We provide official SDKs to simplify integration:</p> <ul> <li><a href=\"https://github.com/MONEI/monei-php-sdk\">PHP SDK</a></li> <li><a href=\"https://github.com/MONEI/monei-python-sdk\">Python SDK</a></li> <li><a href=\"https://github.com/MONEI/monei-node-sdk\">Node.js SDK</a></li> <li><a href=\"https://postman.monei.com/\">Postman Collection</a></li> </ul> <p>Our SDKs handle authentication, error handling, and request formatting automatically.</p> <p>You can download the OpenAPI specification from the <a href=\"https://js.monei.com/api/v1/openapi.json\">https://js.monei.com/api/v1/openapi.json</a> and generate your own client library using the <a href=\"https://openapi-generator.tech/\">OpenAPI Generator</a>.</p> <h3>Important Requirements</h3> <ul> <li>All API requests must be made over HTTPS</li> <li>If you are not using our official SDKs, you <strong>must provide a valid <code>User-Agent</code> header</strong> with each request</li> <li>Requests without proper authentication will return a <code>401 Unauthorized</code> error</li> </ul> <h3>Error Handling</h3> <p>The API returns consistent error codes and messages to help you troubleshoot issues. Each response includes a <code>statusCode</code> attribute indicating the outcome of your request.</p> <h3>Rate Limits</h3> <p>The API implements rate limiting to ensure stability. If you exceed the limits, requests will return a <code>429 Too Many Requests</code> status code.</p>   # noqa: E501

    The version of the OpenAPI document: 1.5.4
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from Monei.api_client import ApiClient, Endpoint as _Endpoint
from Monei.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from Monei.model.apple_pay_domain_register200_response import ApplePayDomainRegister200Response
from Monei.model.apple_pay_domain_register400_response import ApplePayDomainRegister400Response
from Monei.model.apple_pay_domain_register401_response import ApplePayDomainRegister401Response
from Monei.model.apple_pay_domain_register404_response import ApplePayDomainRegister404Response
from Monei.model.apple_pay_domain_register422_response import ApplePayDomainRegister422Response
from Monei.model.apple_pay_domain_register500_response import ApplePayDomainRegister500Response
from Monei.model.apple_pay_domain_register503_response import ApplePayDomainRegister503Response
from Monei.model.register_apple_pay_domain_request import RegisterApplePayDomainRequest


class ApplePayDomainApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.register_endpoint = _Endpoint(
            settings={
                'response_type': (ApplePayDomainRegister200Response,),
                'auth': [
                    'APIKey'
                ],
                'endpoint_path': '/apple-pay/domains',
                'operation_id': 'register',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'register_apple_pay_domain_request',
                ],
                'required': [
                    'register_apple_pay_domain_request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'register_apple_pay_domain_request':
                        (RegisterApplePayDomainRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'register_apple_pay_domain_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )

    def register(
        self,
        register_apple_pay_domain_request,
        **kwargs
    ):
        """Register Domain  # noqa: E501

        <p>Registers a domain with Apple Pay.</p> <p>This endpoint allows you to register your website domain with Apple Pay, which is required before you can accept Apple Pay payments on your website. The domain must be accessible via HTTPS and have a valid SSL certificate.</p> <p>Before registering, you must download this <a href=\"https://assets.monei.com/apple-pay/apple-developer-merchantid-domain-association/\">domain association file</a> and host it at <code>/.well-known/apple-developer-merchantid-domain-association</code> on your site.</p> <p>For example, if you&#39;re registering <code>example.com</code>, make that file available at <code>https://example.com/.well-known/apple-developer-merchantid-domain-association</code>.</p> <p>After registration, Apple will verify your domain. Once verified, you can display Apple Pay buttons and process Apple Pay payments on your website.</p>   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.register(register_apple_pay_domain_request, async_req=True)
        >>> result = thread.get()

        Args:
            register_apple_pay_domain_request (RegisterApplePayDomainRequest):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            ApplePayDomainRegister200Response
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['register_apple_pay_domain_request'] = \
            register_apple_pay_domain_request
        return self.register_endpoint.call_with_http_info(**kwargs)

