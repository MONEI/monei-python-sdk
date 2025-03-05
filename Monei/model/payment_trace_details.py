"""
    MONEI API v1

    <p>The MONEI API is organized around <a href=\"https://en.wikipedia.org/wiki/Representational_State_Transfer\">REST</a> principles. Our API is designed to be intuitive and developer-friendly.</p> <h3>Base URL</h3> <p>All API requests should be made to:</p> <pre><code>https://api.monei.com/v1 </code></pre> <h3>Environment</h3> <p>MONEI provides two environments:</p> <ul> <li><strong>Test Environment</strong>: For development and testing without processing real payments</li> <li><strong>Live Environment</strong>: For processing real transactions in production</li> </ul> <h3>Client Libraries</h3> <p>We provide official SDKs to simplify integration:</p> <ul> <li><a href=\"https://github.com/MONEI/monei-php-sdk\">PHP SDK</a></li> <li><a href=\"https://github.com/MONEI/monei-python-sdk\">Python SDK</a></li> <li><a href=\"https://github.com/MONEI/monei-node-sdk\">Node.js SDK</a></li> <li><a href=\"https://postman.monei.com/\">Postman Collection</a></li> </ul> <p>Our SDKs handle authentication, error handling, and request formatting automatically.</p> <h3>Important Requirements</h3> <ul> <li>All API requests must be made over HTTPS</li> <li>If you are not using our official SDKs, you <strong>must provide a valid <code>User-Agent</code> header</strong> with each request</li> <li>Requests without proper authentication will return a <code>401 Unauthorized</code> error</li> </ul> <h3>Error Handling</h3> <p>The API returns consistent error codes and messages to help you troubleshoot issues. Each response includes a <code>statusCode</code> attribute indicating the outcome of your request.</p> <p><a href=\"https://docs.monei.com/api/errors\">View complete list of status codes →</a></p> <h3>Rate Limits</h3> <p>The API implements rate limiting to ensure stability. If you exceed the limits, requests will return a <code>429 Too Many Requests</code> status code.</p>   # noqa: E501

    The version of the OpenAPI document: 1.5.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from Monei.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from Monei.exceptions import ApiAttributeError



class PaymentTraceDetails(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            'ip': (str,),  # noqa: E501
            'country_code': (str,),  # noqa: E501
            'lang': (str,),  # noqa: E501
            'device_type': (str,),  # noqa: E501
            'device_model': (str,),  # noqa: E501
            'browser': (str,),  # noqa: E501
            'browser_version': (str,),  # noqa: E501
            'os': (str,),  # noqa: E501
            'os_version': (str,),  # noqa: E501
            'source': (str,),  # noqa: E501
            'source_version': (str,),  # noqa: E501
            'user_agent': (str,),  # noqa: E501
            'browser_accept': (str,),  # noqa: E501
            'browser_color_depth': (int,),  # noqa: E501
            'browser_screen_height': (int,),  # noqa: E501
            'browser_screen_width': (int,),  # noqa: E501
            'browser_timezone_offset': (str,),  # noqa: E501
            'user_id': (str,),  # noqa: E501
            'user_email': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'ip': 'ip',  # noqa: E501
        'country_code': 'countryCode',  # noqa: E501
        'lang': 'lang',  # noqa: E501
        'device_type': 'deviceType',  # noqa: E501
        'device_model': 'deviceModel',  # noqa: E501
        'browser': 'browser',  # noqa: E501
        'browser_version': 'browserVersion',  # noqa: E501
        'os': 'os',  # noqa: E501
        'os_version': 'osVersion',  # noqa: E501
        'source': 'source',  # noqa: E501
        'source_version': 'sourceVersion',  # noqa: E501
        'user_agent': 'userAgent',  # noqa: E501
        'browser_accept': 'browserAccept',  # noqa: E501
        'browser_color_depth': 'browserColorDepth',  # noqa: E501
        'browser_screen_height': 'browserScreenHeight',  # noqa: E501
        'browser_screen_width': 'browserScreenWidth',  # noqa: E501
        'browser_timezone_offset': 'browserTimezoneOffset',  # noqa: E501
        'user_id': 'userId',  # noqa: E501
        'user_email': 'userEmail',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """PaymentTraceDetails - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            ip (str): The IP address where the operation originated.. [optional]  # noqa: E501
            country_code (str): Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).. [optional]  # noqa: E501
            lang (str): Two-letter language code ([ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1)).. [optional]  # noqa: E501
            device_type (str): Device type, could be `desktop`, `mobile`, `smartTV`, `tablet`.. [optional]  # noqa: E501
            device_model (str): Information about the device used for the browser session (e.g., `iPhone`).. [optional]  # noqa: E501
            browser (str): The browser used in this browser session (e.g., `Mobile Safari`).. [optional]  # noqa: E501
            browser_version (str): The version for the browser session (e.g., `13.1.1`).. [optional]  # noqa: E501
            os (str): Operation system (e.g., `iOS`).. [optional]  # noqa: E501
            os_version (str): Operation system version (e.g., `13.5.1`).. [optional]  # noqa: E501
            source (str): The source component from where the operation was generated (mostly for our SDK's).. [optional]  # noqa: E501
            source_version (str): The source component version from where the operation was generated (mostly for our SDK's).. [optional]  # noqa: E501
            user_agent (str): Full user agent string of the browser session.. [optional]  # noqa: E501
            browser_accept (str): Browser accept header.. [optional]  # noqa: E501
            browser_color_depth (int): The color depth of the browser session (e.g., `24`).. [optional]  # noqa: E501
            browser_screen_height (int): The screen height of the browser session (e.g., `1152`).. [optional]  # noqa: E501
            browser_screen_width (int): The screen width of the browser session (e.g., `2048`).. [optional]  # noqa: E501
            browser_timezone_offset (str): The timezone offset of the browser session (e.g., `-120`).. [optional]  # noqa: E501
            user_id (str): The ID of the user that started the operation.. [optional]  # noqa: E501
            user_email (str): The email of the user that started the operation.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', True)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """PaymentTraceDetails - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            ip (str): The IP address where the operation originated.. [optional]  # noqa: E501
            country_code (str): Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).. [optional]  # noqa: E501
            lang (str): Two-letter language code ([ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1)).. [optional]  # noqa: E501
            device_type (str): Device type, could be `desktop`, `mobile`, `smartTV`, `tablet`.. [optional]  # noqa: E501
            device_model (str): Information about the device used for the browser session (e.g., `iPhone`).. [optional]  # noqa: E501
            browser (str): The browser used in this browser session (e.g., `Mobile Safari`).. [optional]  # noqa: E501
            browser_version (str): The version for the browser session (e.g., `13.1.1`).. [optional]  # noqa: E501
            os (str): Operation system (e.g., `iOS`).. [optional]  # noqa: E501
            os_version (str): Operation system version (e.g., `13.5.1`).. [optional]  # noqa: E501
            source (str): The source component from where the operation was generated (mostly for our SDK's).. [optional]  # noqa: E501
            source_version (str): The source component version from where the operation was generated (mostly for our SDK's).. [optional]  # noqa: E501
            user_agent (str): Full user agent string of the browser session.. [optional]  # noqa: E501
            browser_accept (str): Browser accept header.. [optional]  # noqa: E501
            browser_color_depth (int): The color depth of the browser session (e.g., `24`).. [optional]  # noqa: E501
            browser_screen_height (int): The screen height of the browser session (e.g., `1152`).. [optional]  # noqa: E501
            browser_screen_width (int): The screen width of the browser session (e.g., `2048`).. [optional]  # noqa: E501
            browser_timezone_offset (str): The timezone offset of the browser session (e.g., `-120`).. [optional]  # noqa: E501
            user_id (str): The ID of the user that started the operation.. [optional]  # noqa: E501
            user_email (str): The email of the user that started the operation.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
