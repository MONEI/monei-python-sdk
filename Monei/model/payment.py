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


def lazy_import():
    from Monei.model.payment_billing_details import PaymentBillingDetails
    from Monei.model.payment_cancellation_reason import PaymentCancellationReason
    from Monei.model.payment_customer import PaymentCustomer
    from Monei.model.payment_last_refund_reason import PaymentLastRefundReason
    from Monei.model.payment_next_action import PaymentNextAction
    from Monei.model.payment_payment_method import PaymentPaymentMethod
    from Monei.model.payment_sequence import PaymentSequence
    from Monei.model.payment_session_details import PaymentSessionDetails
    from Monei.model.payment_shipping_details import PaymentShippingDetails
    from Monei.model.payment_shop import PaymentShop
    from Monei.model.payment_status import PaymentStatus
    from Monei.model.payment_trace_details import PaymentTraceDetails
    globals()['PaymentBillingDetails'] = PaymentBillingDetails
    globals()['PaymentCancellationReason'] = PaymentCancellationReason
    globals()['PaymentCustomer'] = PaymentCustomer
    globals()['PaymentLastRefundReason'] = PaymentLastRefundReason
    globals()['PaymentNextAction'] = PaymentNextAction
    globals()['PaymentPaymentMethod'] = PaymentPaymentMethod
    globals()['PaymentSequence'] = PaymentSequence
    globals()['PaymentSessionDetails'] = PaymentSessionDetails
    globals()['PaymentShippingDetails'] = PaymentShippingDetails
    globals()['PaymentShop'] = PaymentShop
    globals()['PaymentStatus'] = PaymentStatus
    globals()['PaymentTraceDetails'] = PaymentTraceDetails


class Payment(ModelNormal):
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
        lazy_import()
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
        lazy_import()
        return {
            'id': (str,),  # noqa: E501
            'amount': (int,),  # noqa: E501
            'currency': (str,),  # noqa: E501
            'order_id': (str,),  # noqa: E501
            'description': (str,),  # noqa: E501
            'account_id': (str,),  # noqa: E501
            'authorization_code': (str,),  # noqa: E501
            'livemode': (bool,),  # noqa: E501
            'status': (PaymentStatus,),  # noqa: E501
            'status_code': (str,),  # noqa: E501
            'status_message': (str,),  # noqa: E501
            'customer': (PaymentCustomer,),  # noqa: E501
            'shop': (PaymentShop,),  # noqa: E501
            'billing_details': (PaymentBillingDetails,),  # noqa: E501
            'shipping_details': (PaymentShippingDetails,),  # noqa: E501
            'refunded_amount': (int,),  # noqa: E501
            'last_refund_amount': (int,),  # noqa: E501
            'last_refund_reason': (PaymentLastRefundReason,),  # noqa: E501
            'cancellation_reason': (PaymentCancellationReason,),  # noqa: E501
            'session_details': (PaymentSessionDetails,),  # noqa: E501
            'trace_details': (PaymentTraceDetails,),  # noqa: E501
            'payment_token': (str,),  # noqa: E501
            'payment_method': (PaymentPaymentMethod,),  # noqa: E501
            'sequence': (PaymentSequence,),  # noqa: E501
            'sequence_id': (str,),  # noqa: E501
            'store_id': (str,),  # noqa: E501
            'point_of_sale_id': (str,),  # noqa: E501
            'metadata': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'next_action': (PaymentNextAction,),  # noqa: E501
            'created_at': (int,),  # noqa: E501
            'updated_at': (int,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'amount': 'amount',  # noqa: E501
        'currency': 'currency',  # noqa: E501
        'order_id': 'orderId',  # noqa: E501
        'description': 'description',  # noqa: E501
        'account_id': 'accountId',  # noqa: E501
        'authorization_code': 'authorizationCode',  # noqa: E501
        'livemode': 'livemode',  # noqa: E501
        'status': 'status',  # noqa: E501
        'status_code': 'statusCode',  # noqa: E501
        'status_message': 'statusMessage',  # noqa: E501
        'customer': 'customer',  # noqa: E501
        'shop': 'shop',  # noqa: E501
        'billing_details': 'billingDetails',  # noqa: E501
        'shipping_details': 'shippingDetails',  # noqa: E501
        'refunded_amount': 'refundedAmount',  # noqa: E501
        'last_refund_amount': 'lastRefundAmount',  # noqa: E501
        'last_refund_reason': 'lastRefundReason',  # noqa: E501
        'cancellation_reason': 'cancellationReason',  # noqa: E501
        'session_details': 'sessionDetails',  # noqa: E501
        'trace_details': 'traceDetails',  # noqa: E501
        'payment_token': 'paymentToken',  # noqa: E501
        'payment_method': 'paymentMethod',  # noqa: E501
        'sequence': 'sequence',  # noqa: E501
        'sequence_id': 'sequenceId',  # noqa: E501
        'store_id': 'storeId',  # noqa: E501
        'point_of_sale_id': 'pointOfSaleId',  # noqa: E501
        'metadata': 'metadata',  # noqa: E501
        'next_action': 'nextAction',  # noqa: E501
        'created_at': 'createdAt',  # noqa: E501
        'updated_at': 'updatedAt',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """Payment - a model defined in OpenAPI

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
            id (str): Unique identifier for the payment.. [optional]  # noqa: E501
            amount (int): Amount intended to be collected by this payment. A positive integer representing how much to charge in the smallest currency unit (e.g., 100 cents to charge 1.00 USD). . [optional]  # noqa: E501
            currency (str): Three-letter [ISO currency code](https://en.wikipedia.org/wiki/ISO_4217), in uppercase. Must be a supported currency. . [optional]  # noqa: E501
            order_id (str): An order ID from your system. A unique identifier that can be used to reconcile the payment with your internal system. . [optional]  # noqa: E501
            description (str): An arbitrary string attached to the payment. Often useful for displaying to users. . [optional]  # noqa: E501
            account_id (str): MONEI Account identifier.. [optional]  # noqa: E501
            authorization_code (str): Unique identifier provided by the bank performing transaction. . [optional]  # noqa: E501
            livemode (bool): Has the value `true` if the resource exists in live mode or the value `false` if the resource exists in test mode.. [optional]  # noqa: E501
            status (PaymentStatus): [optional]  # noqa: E501
            status_code (str): Payment status code. . [optional]  # noqa: E501
            status_message (str): Human readable status message, can be displayed to a user. . [optional]  # noqa: E501
            customer (PaymentCustomer): [optional]  # noqa: E501
            shop (PaymentShop): [optional]  # noqa: E501
            billing_details (PaymentBillingDetails): [optional]  # noqa: E501
            shipping_details (PaymentShippingDetails): [optional]  # noqa: E501
            refunded_amount (int): Amount in cents refunded (can be less than the amount attribute on the payment if a partial refund was issued). . [optional]  # noqa: E501
            last_refund_amount (int): Amount in cents refunded in the last transaction.. [optional]  # noqa: E501
            last_refund_reason (PaymentLastRefundReason): [optional]  # noqa: E501
            cancellation_reason (PaymentCancellationReason): [optional]  # noqa: E501
            session_details (PaymentSessionDetails): [optional]  # noqa: E501
            trace_details (PaymentTraceDetails): [optional]  # noqa: E501
            payment_token (str): A permanent token represents a payment method used in the payment. Pass `generatePaymentToken: true` when you creating a payment to generate it. You can pass it as `paymentToken` parameter to create other payments with the same payment method. This token does not expire, and should only be used server-side. . [optional]  # noqa: E501
            payment_method (PaymentPaymentMethod): [optional]  # noqa: E501
            sequence (PaymentSequence): [optional]  # noqa: E501
            sequence_id (str): A permanent identifier that refers to the initial payment of a sequence of payments. This value needs to be sent in the path for `RECURRING` payments. . [optional]  # noqa: E501
            store_id (str): A unique identifier of the Store. If specified the payment is attached to this Store. . [optional]  # noqa: E501
            point_of_sale_id (str): A unique identifier of the Point of Sale. If specified the payment is attached to this Point of Sale. If there is a QR code attached to the same Point of Sale, this payment will be available by scanning the QR code. . [optional]  # noqa: E501
            metadata ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): A set of key-value pairs that you can attach to a resource. This can be useful for storing additional information about the resource in a structured format.. [optional]  # noqa: E501
            next_action (PaymentNextAction): [optional]  # noqa: E501
            created_at (int): Time at which the resource was created. Measured in seconds since the Unix epoch.. [optional]  # noqa: E501
            updated_at (int): Time at which the resource updated last time. Measured in seconds since the Unix epoch.. [optional]  # noqa: E501
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
        """Payment - a model defined in OpenAPI

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
            id (str): Unique identifier for the payment.. [optional]  # noqa: E501
            amount (int): Amount intended to be collected by this payment. A positive integer representing how much to charge in the smallest currency unit (e.g., 100 cents to charge 1.00 USD). . [optional]  # noqa: E501
            currency (str): Three-letter [ISO currency code](https://en.wikipedia.org/wiki/ISO_4217), in uppercase. Must be a supported currency. . [optional]  # noqa: E501
            order_id (str): An order ID from your system. A unique identifier that can be used to reconcile the payment with your internal system. . [optional]  # noqa: E501
            description (str): An arbitrary string attached to the payment. Often useful for displaying to users. . [optional]  # noqa: E501
            account_id (str): MONEI Account identifier.. [optional]  # noqa: E501
            authorization_code (str): Unique identifier provided by the bank performing transaction. . [optional]  # noqa: E501
            livemode (bool): Has the value `true` if the resource exists in live mode or the value `false` if the resource exists in test mode.. [optional]  # noqa: E501
            status (PaymentStatus): [optional]  # noqa: E501
            status_code (str): Payment status code. . [optional]  # noqa: E501
            status_message (str): Human readable status message, can be displayed to a user. . [optional]  # noqa: E501
            customer (PaymentCustomer): [optional]  # noqa: E501
            shop (PaymentShop): [optional]  # noqa: E501
            billing_details (PaymentBillingDetails): [optional]  # noqa: E501
            shipping_details (PaymentShippingDetails): [optional]  # noqa: E501
            refunded_amount (int): Amount in cents refunded (can be less than the amount attribute on the payment if a partial refund was issued). . [optional]  # noqa: E501
            last_refund_amount (int): Amount in cents refunded in the last transaction.. [optional]  # noqa: E501
            last_refund_reason (PaymentLastRefundReason): [optional]  # noqa: E501
            cancellation_reason (PaymentCancellationReason): [optional]  # noqa: E501
            session_details (PaymentSessionDetails): [optional]  # noqa: E501
            trace_details (PaymentTraceDetails): [optional]  # noqa: E501
            payment_token (str): A permanent token represents a payment method used in the payment. Pass `generatePaymentToken: true` when you creating a payment to generate it. You can pass it as `paymentToken` parameter to create other payments with the same payment method. This token does not expire, and should only be used server-side. . [optional]  # noqa: E501
            payment_method (PaymentPaymentMethod): [optional]  # noqa: E501
            sequence (PaymentSequence): [optional]  # noqa: E501
            sequence_id (str): A permanent identifier that refers to the initial payment of a sequence of payments. This value needs to be sent in the path for `RECURRING` payments. . [optional]  # noqa: E501
            store_id (str): A unique identifier of the Store. If specified the payment is attached to this Store. . [optional]  # noqa: E501
            point_of_sale_id (str): A unique identifier of the Point of Sale. If specified the payment is attached to this Point of Sale. If there is a QR code attached to the same Point of Sale, this payment will be available by scanning the QR code. . [optional]  # noqa: E501
            metadata ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): A set of key-value pairs that you can attach to a resource. This can be useful for storing additional information about the resource in a structured format.. [optional]  # noqa: E501
            next_action (PaymentNextAction): [optional]  # noqa: E501
            created_at (int): Time at which the resource was created. Measured in seconds since the Unix epoch.. [optional]  # noqa: E501
            updated_at (int): Time at which the resource updated last time. Measured in seconds since the Unix epoch.. [optional]  # noqa: E501
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
