# monei.PaymentsApi

All URIs are relative to *http://api.monei.net/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel**](PaymentsApi.md#cancel) | **POST** /payments/{id}/cancel | Cancel Payment
[**capture**](PaymentsApi.md#capture) | **POST** /payments/{id}/capture | Capture Payment
[**confirm**](PaymentsApi.md#confirm) | **POST** /payments/{id}/confirm | Confirm Payment
[**create**](PaymentsApi.md#create) | **POST** /payments | Create Payment
[**get**](PaymentsApi.md#get) | **GET** /payments/{id} | Get Payment
[**recurring**](PaymentsApi.md#recurring) | **POST** /payments/{sequenceId}/recurring | Recurring Payment
[**refund**](PaymentsApi.md#refund) | **POST** /payments/{id}/refund | Refund Payment


# **cancel**
> Payment cancel(id, cancel_payment_request=cancel_payment_request)

Cancel Payment

Release customer's funds that were reserved earlier. You can only cancel a payment with the `AUTHORIZED` status. <br/><br/> This is the second half of the two-step payment flow, where first you created a payment with the `transactionType` set to `AUTH`.

### Example

* Api Key Authentication (APIKey):
```python
from __future__ import print_function
import time
import monei
from monei.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.monei.net/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = monei.Configuration(
    host = "http://api.monei.net/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKey
configuration = monei.Configuration(
    host = "http://api.monei.net/v1",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with monei.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monei.PaymentsApi(api_client)
    id = 'id_example' # str | The payment ID
cancel_payment_request = monei.CancelPaymentRequest() # CancelPaymentRequest |  (optional)

    try:
        # Cancel Payment
        api_response = api_instance.cancel(id, cancel_payment_request=cancel_payment_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PaymentsApi->cancel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The payment ID | 
 **cancel_payment_request** | [**CancelPaymentRequest**](CancelPaymentRequest.md)|  | [optional] 

### Return type

[**Payment**](Payment.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A payment object along with the &#x60;nextAction&#x60; attribute |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **capture**
> Payment capture(id, capture_payment_request=capture_payment_request)

Capture Payment

Capture the payment of an existing, uncaptured, payment. This is the second half of the two-step payment flow, where first you created a payment with the `transactionType` set to `AUTH`. <br/><br/> Uncaptured payments expire exactly seven days after they are created. If they are not captured by that point in time, they will be marked as expired and will no longer be capturable.

### Example

* Api Key Authentication (APIKey):
```python
from __future__ import print_function
import time
import monei
from monei.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.monei.net/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = monei.Configuration(
    host = "http://api.monei.net/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKey
configuration = monei.Configuration(
    host = "http://api.monei.net/v1",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with monei.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monei.PaymentsApi(api_client)
    id = 'id_example' # str | The payment ID
capture_payment_request = monei.CapturePaymentRequest() # CapturePaymentRequest |  (optional)

    try:
        # Capture Payment
        api_response = api_instance.capture(id, capture_payment_request=capture_payment_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PaymentsApi->capture: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The payment ID | 
 **capture_payment_request** | [**CapturePaymentRequest**](CapturePaymentRequest.md)|  | [optional] 

### Return type

[**Payment**](Payment.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A payment object along with the &#x60;nextAction&#x60; attribute |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **confirm**
> Payment confirm(id, confirm_payment_request=confirm_payment_request)

Confirm Payment

Confirm a payment that was created without a `paymentToken` or `paymentMethod`. You can only confirm a payment with the `PENDING` status. <br/><br/> You can charge a customer in two steps. First create a payment without payment details and then confirm it after you generate a `paymentToken` on the front-end with monei.js [UI Components](https://docs.monei.net/docs/monei-js-overview). <br/><br/> You can provide additional customer information, it will override the information passed in **create payment** request.

### Example

* Api Key Authentication (APIKey):
```python
from __future__ import print_function
import time
import monei
from monei.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.monei.net/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = monei.Configuration(
    host = "http://api.monei.net/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKey
configuration = monei.Configuration(
    host = "http://api.monei.net/v1",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with monei.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monei.PaymentsApi(api_client)
    id = 'id_example' # str | The payment ID
confirm_payment_request = monei.ConfirmPaymentRequest() # ConfirmPaymentRequest |  (optional)

    try:
        # Confirm Payment
        api_response = api_instance.confirm(id, confirm_payment_request=confirm_payment_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PaymentsApi->confirm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The payment ID | 
 **confirm_payment_request** | [**ConfirmPaymentRequest**](ConfirmPaymentRequest.md)|  | [optional] 

### Return type

[**Payment**](Payment.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A payment object along with the &#x60;nextAction&#x60; attribute |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create**
> Payment create(create_payment_request)

Create Payment

To charge a credit card or other payment method, you create a Payment. <br/><br/> Payment can also be created without a payment method to initiate a payment process and redirect a customer to the hosted payment page.

### Example

* Api Key Authentication (APIKey):
```python
from __future__ import print_function
import time
import monei
from monei.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.monei.net/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = monei.Configuration(
    host = "http://api.monei.net/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKey
configuration = monei.Configuration(
    host = "http://api.monei.net/v1",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with monei.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monei.PaymentsApi(api_client)
    create_payment_request = monei.CreatePaymentRequest() # CreatePaymentRequest | 

    try:
        # Create Payment
        api_response = api_instance.create(create_payment_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PaymentsApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_payment_request** | [**CreatePaymentRequest**](CreatePaymentRequest.md)|  | 

### Return type

[**Payment**](Payment.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A payment object along with the &#x60;nextAction&#x60; attribute |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> Payment get(id)

Get Payment

Get the details of a payment that has previously been created. Supply the unique payment ID that was returned from your previous request.

### Example

* Api Key Authentication (APIKey):
```python
from __future__ import print_function
import time
import monei
from monei.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.monei.net/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = monei.Configuration(
    host = "http://api.monei.net/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKey
configuration = monei.Configuration(
    host = "http://api.monei.net/v1",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with monei.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monei.PaymentsApi(api_client)
    id = 'id_example' # str | The payment ID

    try:
        # Get Payment
        api_response = api_instance.get(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PaymentsApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The payment ID | 

### Return type

[**Payment**](Payment.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A payment object along with the &#x60;nextAction&#x60; attribute |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recurring**
> Payment recurring(sequence_id, recurring_payment_request=recurring_payment_request)

Recurring Payment

Creates a subsequent operation for a recurring payment, previously created. The specified amount will be charged to the same credit or debit card of the originally payment. <br/><br/> If amount is not specified, it will default to the same amount from the original payment.

### Example

* Api Key Authentication (APIKey):
```python
from __future__ import print_function
import time
import monei
from monei.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.monei.net/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = monei.Configuration(
    host = "http://api.monei.net/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKey
configuration = monei.Configuration(
    host = "http://api.monei.net/v1",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with monei.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monei.PaymentsApi(api_client)
    sequence_id = 'sequence_id_example' # str | The sequence ID
recurring_payment_request = monei.RecurringPaymentRequest() # RecurringPaymentRequest |  (optional)

    try:
        # Recurring Payment
        api_response = api_instance.recurring(sequence_id, recurring_payment_request=recurring_payment_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PaymentsApi->recurring: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sequence_id** | **str**| The sequence ID | 
 **recurring_payment_request** | [**RecurringPaymentRequest**](RecurringPaymentRequest.md)|  | [optional] 

### Return type

[**Payment**](Payment.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A payment object along with the &#x60;nextAction&#x60; attribute |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refund**
> Payment refund(id, refund_payment_request=refund_payment_request)

Refund Payment

Refund a payment that has previously been created but not yet refunded. Funds will be refunded to the credit or debit card that was originally charged. <br/><br/> You can optionally refund only part of a payment. You can do so multiple times, until the entire payment has been refunded. <br/><br/> Once entirely refunded, a payment can’t be refunded again. This method will throw an error when called on an already-refunded payment, or when trying to refund more money than is left on a payment.

### Example

* Api Key Authentication (APIKey):
```python
from __future__ import print_function
import time
import monei
from monei.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://api.monei.net/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = monei.Configuration(
    host = "http://api.monei.net/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKey
configuration = monei.Configuration(
    host = "http://api.monei.net/v1",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with monei.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monei.PaymentsApi(api_client)
    id = 'id_example' # str | The payment ID
refund_payment_request = monei.RefundPaymentRequest() # RefundPaymentRequest |  (optional)

    try:
        # Refund Payment
        api_response = api_instance.refund(id, refund_payment_request=refund_payment_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PaymentsApi->refund: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The payment ID | 
 **refund_payment_request** | [**RefundPaymentRequest**](RefundPaymentRequest.md)|  | [optional] 

### Return type

[**Payment**](Payment.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A payment object along with the &#x60;nextAction&#x60; attribute |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

