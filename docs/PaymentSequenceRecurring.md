# PaymentSequenceRecurring

Specific configurations for recurring payments. Will only be used when `sequence`.`type` is `recurring`.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expiry** | **str** | Date after which no further recurring payments will be performed. Must be formatted as &#x60;YYYYMMDD&#x60;. | [optional] [default to '*(The payment method or card expiration)*']
**frequency** | **int** | The minimum number of **days** between the different recurring payments. | [optional] [default to 25]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


