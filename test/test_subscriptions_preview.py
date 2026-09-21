import json
import unittest
from unittest.mock import MagicMock, patch

from Monei import MoneiClient, PreviewSubscriptionUpdateRequest, SubscriptionInterval
from Monei.api_client import ApiClient


def _response(payload):
    response = MagicMock()
    response.status = 200
    response.data = json.dumps(payload).encode()
    response.getheader.side_effect = lambda name, default=None: (
        "application/json" if name.lower() == "content-type" else default
    )
    response.getheaders.return_value = {"Content-Type": "application/json"}
    return response


class TestSubscriptionsPreview(unittest.TestCase):
    """A preview quotes a proration without moving money, so it must POST to the
    preview endpoint and never PUT the subscription."""

    @patch.object(ApiClient, "request")
    def test_preview_posts_the_change_to_the_preview_endpoint(self, request):
        request.return_value = _response(
            {
                "credit": 500,
                "charge": 1200,
                "net": 700,
                "direction": "charge",
                "refundCapped": False,
                "effectiveAt": 1790000000,
                "currentPeriodEnd": 1792000000,
            }
        )
        monei = MoneiClient(api_key="test_api_key")

        preview = monei.subscriptions.preview(
            "sub_123",
            PreviewSubscriptionUpdateRequest(
                amount=1200, interval=SubscriptionInterval("year"), interval_count=1
            ),
        )

        method, url = request.call_args.args[:2]
        self.assertEqual(method, "POST")
        self.assertTrue(url.endswith("/subscriptions/sub_123/preview"))
        # snake_case model fields must reach the API as the camelCase the spec defines
        self.assertEqual(
            request.call_args.kwargs["body"],
            {"amount": 1200, "interval": "year", "intervalCount": 1},
        )
        self.assertEqual(preview.net, 700)


if __name__ == "__main__":
    unittest.main()
