import unittest

from Monei import (
    CardholderVerificationCard,
    CreatePaymentRequest,
    PaymentPaymentMethodCardInput,
    PaymentPaymentMethodInput,
    VerifyCardholderRequest,
)
from Monei.api_client import ApiClient

NUMBER = "4000000000000002"
CVC = "987"


class TestCardReprMasking(unittest.TestCase):
    """A merchant that prints or logs a card model must not write the card number
    or the CVC to its logs (PCI), but MONEI still needs both in the request."""

    def setUp(self):
        self.card = CardholderVerificationCard(
            number=NUMBER, exp_month="12", exp_year="29", cvc=CVC
        )
        self.request = VerifyCardholderRequest(
            first_name="Ana", last_name="Ruiz", card=self.card
        )

    def test_card_repr_shows_only_the_last_four_digits(self):
        for text in (repr(self.card), str(self.card)):
            self.assertNotIn(NUMBER, text)
            self.assertNotIn(CVC, text)
            self.assertIn("**** 0002", text)

    def test_request_repr_masks_the_nested_card(self):
        for text in (repr(self.request), str(self.request)):
            self.assertNotIn(NUMBER, text)
            self.assertNotIn(CVC, text)
            self.assertIn("Ana", text)

    def test_payment_request_repr_masks_the_raw_card(self):
        payment = CreatePaymentRequest(
            amount=110,
            currency="EUR",
            order_id="14379133960355",
            payment_method=PaymentPaymentMethodInput(
                card=PaymentPaymentMethodCardInput(
                    number=NUMBER, cvc=CVC, exp_month="12", exp_year="29"
                )
            ),
        )

        text = repr(payment)

        self.assertNotIn(NUMBER, text)
        self.assertNotIn(CVC, text)
        self.assertIn("**** 0002", text)
        body = ApiClient().sanitize_for_serialization(payment)
        self.assertEqual(body["paymentMethod"]["card"]["number"], NUMBER)
        self.assertEqual(body["paymentMethod"]["card"]["cvc"], CVC)

    def test_request_body_keeps_the_card_data(self):
        body = ApiClient().sanitize_for_serialization(self.request)

        self.assertEqual(body["card"]["number"], NUMBER)
        self.assertEqual(body["card"]["cvc"], CVC)
        self.assertEqual(self.card.to_dict()["cvc"], CVC)


if __name__ == "__main__":
    unittest.main()
