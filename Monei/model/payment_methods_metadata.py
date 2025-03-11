"""
MONEI API v1

The MONEI API is organized around [REST](https://en.wikipedia.org/wiki/Representational_State_Transfer) principles. Our API is designed to be intuitive and developer-friendly.  ### Base URL  All API requests should be made to:  ``` https://api.monei.com/v1 ```  ### Environment  MONEI provides two environments:  - **Test Environment**: For development and testing without processing real payments - **Live Environment**: For processing real transactions in production  ### Client Libraries  We provide official SDKs to simplify integration:  - [PHP SDK](https://github.com/MONEI/monei-php-sdk) - [Python SDK](https://github.com/MONEI/monei-python-sdk) - [Node.js SDK](https://github.com/MONEI/monei-node-sdk) - [Postman Collection](https://postman.monei.com/)  Our SDKs handle authentication, error handling, and request formatting automatically.  You can download the OpenAPI specification from the https://js.monei.com/api/v1/openapi.json and generate your own client library using the [OpenAPI Generator](https://openapi-generator.tech/).  ### Important Requirements  - All API requests must be made over HTTPS - If you are not using our official SDKs, you **must provide a valid `User-Agent` header** with each request - Requests without proper authentication will return a `401 Unauthorized` error  ### Error Handling  The API returns consistent error codes and messages to help you troubleshoot issues. Each response includes a `statusCode` attribute indicating the outcome of your request.  ### Rate Limits  The API implements rate limiting to ensure stability. If you exceed the limits, requests will return a `429 Too Many Requests` status code.  # Authentication  <!-- Redoc-Inject: <security-definitions> -->   # noqa: E501

The version of the OpenAPI document: 1.5.8
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
    OpenApiModel,
)
from Monei.exceptions import ApiAttributeError


def lazy_import():
    from Monei.model.payment_methods_metadata_alipay import PaymentMethodsMetadataAlipay
    from Monei.model.payment_methods_metadata_apple_pay import (
        PaymentMethodsMetadataApplePay,
    )
    from Monei.model.payment_methods_metadata_bancontact import (
        PaymentMethodsMetadataBancontact,
    )
    from Monei.model.payment_methods_metadata_bizum import PaymentMethodsMetadataBizum
    from Monei.model.payment_methods_metadata_blik import PaymentMethodsMetadataBlik
    from Monei.model.payment_methods_metadata_card import PaymentMethodsMetadataCard
    from Monei.model.payment_methods_metadata_click_to_pay import (
        PaymentMethodsMetadataClickToPay,
    )
    from Monei.model.payment_methods_metadata_eps import PaymentMethodsMetadataEps
    from Monei.model.payment_methods_metadata_giropay import (
        PaymentMethodsMetadataGiropay,
    )
    from Monei.model.payment_methods_metadata_google_pay import (
        PaymentMethodsMetadataGooglePay,
    )
    from Monei.model.payment_methods_metadata_i_deal import PaymentMethodsMetadataIDeal
    from Monei.model.payment_methods_metadata_klarna import PaymentMethodsMetadataKlarna
    from Monei.model.payment_methods_metadata_mbway import PaymentMethodsMetadataMbway
    from Monei.model.payment_methods_metadata_sepa import PaymentMethodsMetadataSepa
    from Monei.model.payment_methods_metadata_sofort import PaymentMethodsMetadataSofort
    from Monei.model.payment_methods_metadata_trustly import (
        PaymentMethodsMetadataTrustly,
    )

    globals()["PaymentMethodsMetadataAlipay"] = PaymentMethodsMetadataAlipay
    globals()["PaymentMethodsMetadataApplePay"] = PaymentMethodsMetadataApplePay
    globals()["PaymentMethodsMetadataBancontact"] = PaymentMethodsMetadataBancontact
    globals()["PaymentMethodsMetadataBizum"] = PaymentMethodsMetadataBizum
    globals()["PaymentMethodsMetadataBlik"] = PaymentMethodsMetadataBlik
    globals()["PaymentMethodsMetadataCard"] = PaymentMethodsMetadataCard
    globals()["PaymentMethodsMetadataClickToPay"] = PaymentMethodsMetadataClickToPay
    globals()["PaymentMethodsMetadataEps"] = PaymentMethodsMetadataEps
    globals()["PaymentMethodsMetadataGiropay"] = PaymentMethodsMetadataGiropay
    globals()["PaymentMethodsMetadataGooglePay"] = PaymentMethodsMetadataGooglePay
    globals()["PaymentMethodsMetadataIDeal"] = PaymentMethodsMetadataIDeal
    globals()["PaymentMethodsMetadataKlarna"] = PaymentMethodsMetadataKlarna
    globals()["PaymentMethodsMetadataMbway"] = PaymentMethodsMetadataMbway
    globals()["PaymentMethodsMetadataSepa"] = PaymentMethodsMetadataSepa
    globals()["PaymentMethodsMetadataSofort"] = PaymentMethodsMetadataSofort
    globals()["PaymentMethodsMetadataTrustly"] = PaymentMethodsMetadataTrustly


class PaymentMethodsMetadata(ModelNormal):
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

    allowed_values = {}

    validations = {}

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (
            bool,
            date,
            datetime,
            dict,
            float,
            int,
            list,
            str,
            none_type,
        )  # noqa: E501

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
        lazy_import()
        return {
            "alipay": (PaymentMethodsMetadataAlipay,),  # noqa: E501
            "bancontact": (PaymentMethodsMetadataBancontact,),  # noqa: E501
            "bizum": (PaymentMethodsMetadataBizum,),  # noqa: E501
            "blik": (PaymentMethodsMetadataBlik,),  # noqa: E501
            "card": (PaymentMethodsMetadataCard,),  # noqa: E501
            "eps": (PaymentMethodsMetadataEps,),  # noqa: E501
            "i_deal": (PaymentMethodsMetadataIDeal,),  # noqa: E501
            "mbway": (PaymentMethodsMetadataMbway,),  # noqa: E501
            "multibanco": (PaymentMethodsMetadataMbway,),  # noqa: E501
            "sofort": (PaymentMethodsMetadataSofort,),  # noqa: E501
            "trustly": (PaymentMethodsMetadataTrustly,),  # noqa: E501
            "sepa": (PaymentMethodsMetadataSepa,),  # noqa: E501
            "klarna": (PaymentMethodsMetadataKlarna,),  # noqa: E501
            "giropay": (PaymentMethodsMetadataGiropay,),  # noqa: E501
            "google_pay": (PaymentMethodsMetadataGooglePay,),  # noqa: E501
            "apple_pay": (PaymentMethodsMetadataApplePay,),  # noqa: E501
            "click_to_pay": (PaymentMethodsMetadataClickToPay,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None

    attribute_map = {
        "alipay": "alipay",  # noqa: E501
        "bancontact": "bancontact",  # noqa: E501
        "bizum": "bizum",  # noqa: E501
        "blik": "blik",  # noqa: E501
        "card": "card",  # noqa: E501
        "eps": "eps",  # noqa: E501
        "i_deal": "iDeal",  # noqa: E501
        "mbway": "mbway",  # noqa: E501
        "multibanco": "multibanco",  # noqa: E501
        "sofort": "sofort",  # noqa: E501
        "trustly": "trustly",  # noqa: E501
        "sepa": "sepa",  # noqa: E501
        "klarna": "klarna",  # noqa: E501
        "giropay": "giropay",  # noqa: E501
        "google_pay": "googlePay",  # noqa: E501
        "apple_pay": "applePay",  # noqa: E501
        "click_to_pay": "clickToPay",  # noqa: E501
    }

    read_only_vars = {}

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """PaymentMethodsMetadata - a model defined in OpenAPI

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
            alipay (PaymentMethodsMetadataAlipay): [optional]  # noqa: E501
            bancontact (PaymentMethodsMetadataBancontact): [optional]  # noqa: E501
            bizum (PaymentMethodsMetadataBizum): [optional]  # noqa: E501
            blik (PaymentMethodsMetadataBlik): [optional]  # noqa: E501
            card (PaymentMethodsMetadataCard): [optional]  # noqa: E501
            eps (PaymentMethodsMetadataEps): [optional]  # noqa: E501
            i_deal (PaymentMethodsMetadataIDeal): [optional]  # noqa: E501
            mbway (PaymentMethodsMetadataMbway): [optional]  # noqa: E501
            multibanco (PaymentMethodsMetadataMbway): [optional]  # noqa: E501
            sofort (PaymentMethodsMetadataSofort): [optional]  # noqa: E501
            trustly (PaymentMethodsMetadataTrustly): [optional]  # noqa: E501
            sepa (PaymentMethodsMetadataSepa): [optional]  # noqa: E501
            klarna (PaymentMethodsMetadataKlarna): [optional]  # noqa: E501
            giropay (PaymentMethodsMetadataGiropay): [optional]  # noqa: E501
            google_pay (PaymentMethodsMetadataGooglePay): [optional]  # noqa: E501
            apple_pay (PaymentMethodsMetadataApplePay): [optional]  # noqa: E501
            click_to_pay (PaymentMethodsMetadataClickToPay): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop("_check_type", True)
        _spec_property_naming = kwargs.pop("_spec_property_naming", True)
        _path_to_item = kwargs.pop("_path_to_item", ())
        _configuration = kwargs.pop("_configuration", None)
        _visited_composed_classes = kwargs.pop("_visited_composed_classes", ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments."
                        % (
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
            if (
                var_name not in self.attribute_map
                and self._configuration is not None
                and self._configuration.discard_unknown_keys
                and self.additional_properties_type is None
            ):
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set(
        [
            "_data_store",
            "_check_type",
            "_spec_property_naming",
            "_path_to_item",
            "_configuration",
            "_visited_composed_classes",
        ]
    )

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """PaymentMethodsMetadata - a model defined in OpenAPI

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
            alipay (PaymentMethodsMetadataAlipay): [optional]  # noqa: E501
            bancontact (PaymentMethodsMetadataBancontact): [optional]  # noqa: E501
            bizum (PaymentMethodsMetadataBizum): [optional]  # noqa: E501
            blik (PaymentMethodsMetadataBlik): [optional]  # noqa: E501
            card (PaymentMethodsMetadataCard): [optional]  # noqa: E501
            eps (PaymentMethodsMetadataEps): [optional]  # noqa: E501
            i_deal (PaymentMethodsMetadataIDeal): [optional]  # noqa: E501
            mbway (PaymentMethodsMetadataMbway): [optional]  # noqa: E501
            multibanco (PaymentMethodsMetadataMbway): [optional]  # noqa: E501
            sofort (PaymentMethodsMetadataSofort): [optional]  # noqa: E501
            trustly (PaymentMethodsMetadataTrustly): [optional]  # noqa: E501
            sepa (PaymentMethodsMetadataSepa): [optional]  # noqa: E501
            klarna (PaymentMethodsMetadataKlarna): [optional]  # noqa: E501
            giropay (PaymentMethodsMetadataGiropay): [optional]  # noqa: E501
            google_pay (PaymentMethodsMetadataGooglePay): [optional]  # noqa: E501
            apple_pay (PaymentMethodsMetadataApplePay): [optional]  # noqa: E501
            click_to_pay (PaymentMethodsMetadataClickToPay): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop("_check_type", True)
        _spec_property_naming = kwargs.pop("_spec_property_naming", False)
        _path_to_item = kwargs.pop("_path_to_item", ())
        _configuration = kwargs.pop("_configuration", None)
        _visited_composed_classes = kwargs.pop("_visited_composed_classes", ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments."
                        % (
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
            if (
                var_name not in self.attribute_map
                and self._configuration is not None
                and self._configuration.discard_unknown_keys
                and self.additional_properties_type is None
            ):
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(
                    f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                    f"class with read only attributes."
                )
