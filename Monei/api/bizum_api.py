"""
    MONEI API v1

    <p>The MONEI API is organized around <a href=\"https://en.wikipedia.org/wiki/Representational_State_Transfer\">REST</a> principles. Our API is designed to be intuitive and developer-friendly.</p> <h3>Base URL</h3> <p>All API requests should be made to:</p> <pre><code>https://api.monei.com/v1 </code></pre> <h3>Environment</h3> <p>MONEI provides two environments:</p> <ul> <li><strong>Test Environment</strong>: For development and testing without processing real payments</li> <li><strong>Live Environment</strong>: For processing real transactions in production</li> </ul> <h3>Client Libraries</h3> <p>We provide official SDKs to simplify integration:</p> <ul> <li><a href=\"https://github.com/MONEI/monei-php-sdk\">PHP SDK</a></li> <li><a href=\"https://github.com/MONEI/monei-python-sdk\">Python SDK</a></li> <li><a href=\"https://github.com/MONEI/monei-node-sdk\">Node.js SDK</a></li> <li><a href=\"https://postman.monei.com/\">Postman Collection</a></li> </ul> <p>Our SDKs handle authentication, error handling, and request formatting automatically.</p> <p>You can download the OpenAPI specification from the <a href=\"https://js.monei.com/api/v1/openapi.json\">https://js.monei.com/api/v1/openapi.json</a> and generate your own client library using the <a href=\"https://openapi-generator.tech/\">OpenAPI Generator</a>.</p> <h3>Important Requirements</h3> <ul> <li>All API requests must be made over HTTPS</li> <li>If you are not using our official SDKs, you <strong>must provide a valid <code>User-Agent</code> header</strong> with each request</li> <li>Requests without proper authentication will return a <code>401 Unauthorized</code> error</li> </ul> <h3>Error Handling</h3> <p>The API returns consistent error codes and messages to help you troubleshoot issues. Each response includes a <code>statusCode</code> attribute indicating the outcome of your request.</p> <h3>Rate Limits</h3> <p>The API implements rate limiting to ensure stability. If you exceed the limits, requests will return a <code>429 Too Many Requests</code> status code.</p>   # noqa: E501

    The version of the OpenAPI document: 1.5.7
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
from Monei.model.bad_request_error import BadRequestError
from Monei.model.bizum_validate_phone200_response import BizumValidatePhone200Response
from Monei.model.internal_server_error import InternalServerError
from Monei.model.not_found_error import NotFoundError
from Monei.model.service_unavailable_error import ServiceUnavailableError
from Monei.model.unauthorized_error import UnauthorizedError
from Monei.model.unprocessable_entity_error import UnprocessableEntityError
from Monei.model.validate_bizum_phone_request import ValidateBizumPhoneRequest


class BizumApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.validate_phone_endpoint = _Endpoint(
            settings={
                'response_type': (BizumValidatePhone200Response,),
                'auth': [
                    'APIKey'
                ],
                'endpoint_path': '/bizum/validate-phone',
                'operation_id': 'validate_phone',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'validate_bizum_phone_request',
                ],
                'required': [
                    'validate_bizum_phone_request',
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
                    'validate_bizum_phone_request':
                        (ValidateBizumPhoneRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'validate_bizum_phone_request': 'body',
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

    def validate_phone(
        self,
        validate_bizum_phone_request,
        **kwargs
    ):
        """Validate Phone  # noqa: E501

        <p>Validates if a phone number is registered with Bizum.</p> <p>Use this endpoint to check if a customer&#39;s phone number can be used for Bizum payments before attempting to process a payment. This helps provide a better user experience by preventing failed payment attempts for non-registered numbers.</p> <p>The response will indicate whether the phone number is valid for Bizum payments.</p>   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.validate_phone(validate_bizum_phone_request, async_req=True)
        >>> result = thread.get()

        Args:
            validate_bizum_phone_request (ValidateBizumPhoneRequest):

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
            BizumValidatePhone200Response
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
        kwargs['validate_bizum_phone_request'] = \
            validate_bizum_phone_request
        return self.validate_phone_endpoint.call_with_http_info(**kwargs)

