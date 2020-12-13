# Payment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the payment. | [optional] 
**amount** | **int** | Amount intended to be collected by this payment. A positive integer representing how much to charge in the smallest currency unit (e.g., 100 cents to charge 1.00 USD). | [optional] 
**currency** | **str** | Three-letter [ISO currency code](https://en.wikipedia.org/wiki/ISO_4217), in uppercase. Must be a supported currency. | [optional] 
**order_id** | **str** | An order ID from your system. A unique identifier that can be used to reconcile the payment with your internal system. | [optional] 
**description** | **str** | An arbitrary string attached to the payment. Often useful for displaying to users. | [optional] 
**account_id** | **str** | MONEI Account identifier. | [optional] 
**authorization_code** | **str** | Unique identifier provided by the bank performing transaction. | [optional] 
**livemode** | **bool** | Has the value &#x60;true&#x60; if the payment exists in live mode or the value &#x60;false&#x60; if the payment exists in test mode. | [optional] 
**status** | [**PaymentStatus**](PaymentStatus.md) |  | [optional] 
**status_code** | **str** | Payment status code. | [optional] 
**status_message** | **str** | Human readable status message, can be displayed to a user. | [optional] 
**customer** | [**PaymentCustomer**](PaymentCustomer.md) |  | [optional] 
**payment_token** | **str** | A permanent token represents a payment method used in the payment. Pass &#x60;generatePaymentToken: true&#x60; when you creating a payment to generate it. You can pass it as &#x60;paymentToken&#x60; parameter to create other payments with the same payment method. This token does not expire, and should only be used server-side. | [optional] 
**payment_method** | [**PaymentPaymentMethod**](PaymentPaymentMethod.md) |  | [optional] 
**shop** | [**PaymentShop**](PaymentShop.md) |  | [optional] 
**billing_details** | [**PaymentBillingDetails**](PaymentBillingDetails.md) |  | [optional] 
**shipping_details** | [**PaymentShippingDetails**](PaymentShippingDetails.md) |  | [optional] 
**refunded_amount** | **int** | Amount in cents refunded (can be less than the amount attribute on the payment if a partial refund was issued). | [optional] 
**last_refund_amount** | **int** | Amount in cents refunded in the last transaction. | [optional] 
**last_refund_reason** | [**PaymentLastRefundReason**](PaymentLastRefundReason.md) |  | [optional] 
**cancellation_reason** | [**PaymentCancellationReason**](PaymentCancellationReason.md) |  | [optional] 
**session_details** | [**PaymentSessionDetails**](PaymentSessionDetails.md) |  | [optional] 
**trace_details** | [**PaymentTraceDetails**](PaymentTraceDetails.md) |  | [optional] 
**next_action** | [**PaymentNextAction**](PaymentNextAction.md) |  | [optional] 
**created_at** | **int** | Time at which the resource was created. Measured in seconds since the Unix epoch. | [optional] 
**updated_at** | **int** | Time at which the resource updated last time. Measured in seconds since the Unix epoch. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


