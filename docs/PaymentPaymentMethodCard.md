# PaymentPaymentMethodCard

Details about the card used as payment method at the time of the transaction.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **str** | Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)). | [optional] 
**brand** | **str** | Card brand. | [optional] 
**type** | **str** | Card type &#x60;debit&#x60; or &#x60;credit&#x60;. | [optional] 
**three_d_secure** | **bool** | Wether this transaction used 3D Secure authentication. | [optional] 
**three_d_secure_version** | **str** | The protocol version of the 3DS challenge. | [optional] 
**last4** | **str** | The last four digits of the card. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


