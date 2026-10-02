import unittest
from unittest.mock import patch

from Monei import CreatePaymentRequest, MoneiClient, UpdateCustomerRequest
from Monei.api_client import ApiClient
from test.test_subscriptions_preview import _response


class TestCustomers(unittest.TestCase):
    """The generated tests patch nothing below the API method, so they would not
    catch a wrong method, path or body key."""

    @patch.object(ApiClient, "request")
    def test_update_puts_the_default_token_to_the_customer(self, request):
        request.return_value = _response({"id": "cus_123", "defaultTokenId": "tok_456"})
        monei = MoneiClient(api_key="test_api_key")

        customer = monei.customers.update(
            "cus_123", UpdateCustomerRequest(default_token_id="tok_456")
        )

        method, url = request.call_args.args[:2]
        self.assertEqual(method, "PUT")
        self.assertTrue(url.endswith("/customers/cus_123"))
        self.assertEqual(
            request.call_args.kwargs["body"], {"defaultTokenId": "tok_456"}
        )
        self.assertEqual(customer.default_token_id, "tok_456")

    @patch.object(ApiClient, "request")
    def test_delete_payment_method_puts_both_ids_in_the_path(self, request):
        request.return_value = _response({"success": True})
        monei = MoneiClient(api_key="test_api_key")

        monei.customers.delete_payment_method("cus_123", "tok_456")

        method, url = request.call_args.args[:2]
        self.assertEqual(method, "DELETE")
        self.assertTrue(url.endswith("/customers/cus_123/payment-methods/tok_456"))

    @patch.object(ApiClient, "request")
    def test_payment_can_charge_the_customer_default_method(self, request):
        request.return_value = _response(
            {
                "id": "pay_123",
                "accountId": "acc_1",
                "livemode": False,
                "status": "PENDING",
                "amount": 100,
                "currency": "EUR",
                "customerId": "cus_123",
            }
        )
        monei = MoneiClient(api_key="test_api_key")

        monei.payments.create(
            CreatePaymentRequest(
                amount=100,
                currency="EUR",
                order_id="1",
                customer_id="cus_123",
                use_default_payment_method=True,
            )
        )

        body = request.call_args.kwargs["body"]
        self.assertEqual(body["customerId"], "cus_123")
        self.assertIs(body["useDefaultPaymentMethod"], True)


if __name__ == "__main__":
    unittest.main()
