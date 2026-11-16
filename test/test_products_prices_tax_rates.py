import unittest
from unittest.mock import patch

from Monei import (
    CreateSubscriptionRequest,
    CreateTaxRateRequest,
    MoneiClient,
    TaxRateDisplayName,
    TaxRatePercentage,
    UpdateProductRequest,
)
from Monei.api_client import ApiClient
from test.test_subscriptions_preview import _response


class TestProductsPricesTaxRates(unittest.TestCase):
    """The generated tests patch nothing below the API method, so they would not
    catch a missing client attribute, a wrong path or a wrong body key."""

    @patch.object(ApiClient, "request")
    def test_update_product_puts_the_default_price(self, request):
        request.return_value = _response(
            {
                "id": "prod_1",
                "name": "Gold plan",
                "createdAt": 1,
                "defaultPriceId": "price_1",
            }
        )
        monei = MoneiClient(api_key="test_api_key")

        product = monei.products.update(
            "prod_1", UpdateProductRequest(default_price_id="price_1")
        )

        method, url = request.call_args.args[:2]
        self.assertEqual(method, "PUT")
        self.assertTrue(url.endswith("/products/prod_1"))
        self.assertEqual(
            request.call_args.kwargs["body"], {"defaultPriceId": "price_1"}
        )
        self.assertEqual(product.default_price_id, "price_1")

    @patch.object(ApiClient, "request")
    def test_list_prices_filters_by_product(self, request):
        request.return_value = _response({"items": []})
        monei = MoneiClient(api_key="test_api_key")

        monei.prices.list(product_id="prod_1")

        method, url = request.call_args.args[:2]
        self.assertEqual(method, "GET")
        self.assertTrue(url.endswith("/prices"))
        self.assertEqual(
            request.call_args.kwargs["query_params"], [("productId", "prod_1")]
        )

    @patch.object(ApiClient, "request")
    def test_create_tax_rate_posts_to_the_hyphenated_path(self, request):
        request.return_value = _response(
            {"id": "txr_1", "displayName": "IVA", "percentage": 21, "createdAt": 1}
        )
        monei = MoneiClient(api_key="test_api_key")

        monei.tax_rates.create(
            CreateTaxRateRequest(
                display_name=TaxRateDisplayName("IVA"),
                percentage=TaxRatePercentage(21.0),
            )
        )

        method, url = request.call_args.args[:2]
        self.assertEqual(method, "POST")
        self.assertTrue(url.endswith("/tax-rates"))
        self.assertEqual(
            request.call_args.kwargs["body"], {"displayName": "IVA", "percentage": 21.0}
        )

    @patch.object(ApiClient, "request")
    def test_subscription_can_be_created_from_a_price_alone(self, request):
        request.return_value = _response(
            {
                "id": "sub_1",
                "accountId": "acc_1",
                "livemode": False,
                "status": "PENDING",
                "amount": 1990,
                "currency": "EUR",
                "interval": "month",
                "intervalCount": 1,
                "priceId": "price_1",
                "productId": "prod_1",
            }
        )
        monei = MoneiClient(api_key="test_api_key")

        subscription = monei.subscriptions.create(
            CreateSubscriptionRequest(price_id="price_1")
        )

        self.assertEqual(request.call_args.kwargs["body"], {"priceId": "price_1"})
        self.assertEqual(subscription.product_id, "prod_1")


if __name__ == "__main__":
    unittest.main()
