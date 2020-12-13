# PaymentNextAction

If present, this property tells you what actions you need to take in order for your customer to fulfill a payment using the provided source.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | - &#x60;CONFIRM&#x60; - Your customer needs to be redirected to a   [hosted payment page](https://docs.monei.net/docs/use-prebuilt-payment-page)   or confirm payment using   [payment token](https://docs.monei.net/docs/accept-card-payment#3-submitting-the-payment-to-monei-client-side).   The **redirectUrl** will point to the hosted payment page. - &#x60;CHALLENGE&#x60; - Your customer needs to be redirected to the   3d secure challenge page provided by the bank. The **redirectUrl**   will point to the 3d secure challenge page provided by the bank. - &#x60;COMPLETE&#x60; - The payment is completed. The **redirectUrl** will be   the **completeUrl** if it was provided when the payment was created. | [optional] 
**must_redirect** | **bool** | If &#x60;true&#x60; you have to redirect your customer to the **redirectUrl** to continue payment process. | [optional] 
**redirect_url** | **str** | Redirect your customer to this url to continue payment process. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


