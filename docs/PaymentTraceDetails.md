# PaymentTraceDetails

Information related to the browsing session of the user who initiated the payment.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip** | **str** | The IP address where the operation originated. | [optional] 
**country_code** | **str** | Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)). | [optional] 
**lang** | **str** | Two-letter language code ([ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1)). | [optional] 
**device_type** | **str** | Device type, could be &#x60;desktop&#x60;, &#x60;mobile&#x60;, &#x60;smartTV&#x60;, &#x60;tablet&#x60;. | [optional] 
**device_model** | **str** | Information about the device used for the browser session (e.g., &#x60;iPhone&#x60;). | [optional] 
**browser** | **str** | The browser used in this browser session (e.g., &#x60;Mobile Safari&#x60;). | [optional] 
**browser_version** | **str** | The version for the browser session (e.g., &#x60;13.1.1&#x60;). | [optional] 
**os** | **str** | Operation system (e.g., &#x60;iOS&#x60;). | [optional] 
**os_version** | **str** | Operation system version (e.g., &#x60;13.5.1&#x60;). | [optional] 
**source** | **str** | The source component from where the operation was generated (mostly for our SDK&#39;s). | [optional] 
**source_version** | **str** | The source component version from where the operation was generated (mostly for our SDK&#39;s). | [optional] 
**user_agent** | **str** | Full user agent string of the browser session. | [optional] 
**user_id** | **str** | The ID of the user that started the operation. | [optional] 
**user_email** | **str** | The email of the user that started the operation. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


