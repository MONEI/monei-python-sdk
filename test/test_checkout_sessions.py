import unittest
from unittest.mock import patch

from Monei import (
    CheckoutSessionLineItemRequest,
    CreateCheckoutSessionRequest,
    MoneiClient,
)
from Monei.api_client import ApiClient
from test.test_subscriptions_preview import _response

SESSION = {
    "id": "cs_1",
    "url": "https://checkout.monei.com/cs_1",
    "livemode": False,
    "status": "OPEN",
    "mode": "SUBSCRIPTION",
    "currency": "EUR",
    "lineItems": [
        {
            "priceId": "price_1",
            "productId": "prod_1",
            "productName": "Gold plan",
            "quantity": 1,
            "unitAmount": 1653,
            "type": "RECURRING",
            "billedInFirstPayment": True,
            "amountSubtotal": 1653,
            "amountTax": 347,
            "amountTotal": 2000,
        }
    ],
    "amountSubtotal": 1653,
    "amountTax": 347,
    "amountTotal": 2000,
    "orderId": "order_1",
    "description": "Gold plan",
    "billingAddressCollection": "OPTIONAL",
    "businessPurchase": "DISABLED",
    "successUrl": "https://example.com/success",
    "expiresAt": 1790000000,
    "createdAt": 1789990000,
}


class TestCheckoutSessions(unittest.TestCase):
    """The generated tests patch nothing below the API method, so they would not
    catch a missing client attribute, a wrong path, a wrong body key or a session
    response that does not deserialize."""

    @patch.object(ApiClient, "request")
    def test_create_posts_the_lines_and_returns_the_url(self, request):
        request.return_value = _response(SESSION)
        monei = MoneiClient(api_key="test_api_key")

        session = monei.checkout_sessions.create(
            CreateCheckoutSessionRequest(
                line_items=[
                    CheckoutSessionLineItemRequest(price_id="price_1", quantity=1)
                ],
                success_url="https://example.com/success",
            )
        )

        method, url = request.call_args.args[:2]
        self.assertEqual(method, "POST")
        self.assertTrue(url.endswith("/checkout-sessions"))
        self.assertEqual(
            request.call_args.kwargs["body"],
            {
                "lineItems": [{"priceId": "price_1", "quantity": 1}],
                "successUrl": "https://example.com/success",
            },
        )
        self.assertEqual(session.url, "https://checkout.monei.com/cs_1")
        self.assertEqual(session.line_items[0].amount_total, 2000)

    @patch.object(ApiClient, "request")
    def test_get_reads_the_session_by_id(self, request):
        request.return_value = _response(SESSION)
        monei = MoneiClient(api_key="test_api_key")

        monei.checkout_sessions.get("cs_1")

        method, url = request.call_args.args[:2]
        self.assertEqual(method, "GET")
        self.assertTrue(url.endswith("/checkout-sessions/cs_1"))

    @patch.object(ApiClient, "request")
    def test_list_sends_the_page_cursor(self, request):
        request.return_value = _response({"items": [SESSION], "nextCursor": "c_2"})
        monei = MoneiClient(api_key="test_api_key")

        page = monei.checkout_sessions.list(limit=20, cursor="c_1")

        method, url = request.call_args.args[:2]
        self.assertEqual(method, "GET")
        self.assertTrue(url.endswith("/checkout-sessions"))
        self.assertEqual(
            request.call_args.kwargs["query_params"],
            [("limit", 20), ("cursor", "c_1")],
        )
        self.assertEqual(page.next_cursor, "c_2")

    @patch.object(ApiClient, "request")
    def test_payment_keeps_its_checkout_session_id(self, request):
        request.return_value = _response(
            {
                "id": "pay_1",
                "accountId": "acc_1",
                "amount": 2000,
                "currency": "EUR",
                "livemode": False,
                "status": "SUCCEEDED",
                "checkoutSessionId": "cs_1",
            }
        )
        monei = MoneiClient(api_key="test_api_key")

        payment = monei.payments.get("pay_1")

        self.assertEqual(payment.checkout_session_id, "cs_1")

    @patch.object(ApiClient, "request")
    def test_subscription_keeps_its_checkout_session_id(self, request):
        request.return_value = _response(
            {
                "id": "sub_1",
                "accountId": "acc_1",
                "livemode": False,
                "amount": 1653,
                "interval": "month",
                "intervalCount": 1,
                "status": "ACTIVE",
                "checkoutSessionId": "cs_1",
            }
        )
        monei = MoneiClient(api_key="test_api_key")

        subscription = monei.subscriptions.get("sub_1")

        self.assertEqual(subscription.checkout_session_id, "cs_1")


if __name__ == "__main__":
    unittest.main()
