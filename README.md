# MONEI PYTHON SDK

The MONEI API is organized around [REST](https://en.wikipedia.org/wiki/Representational_State_Transfer). Our API has predictable resource-oriented URLs, accepts JSON-encoded request bodies, returns JSON-encoded responses, and uses standard HTTP response codes, authentication, and verbs.

This library is intended to help you develop an integration around our API, by using the MONEI Python Client and it's methods.

## Installation

### Using uv (Recommended)

[uv](https://github.com/astral-sh/uv) is a modern Python package installer and resolver that's significantly faster than pip. To install and use this package with uv:

```sh
# Install uv if you don't have it yet
curl -sSf https://astral.sh/uv/install.sh | sh

# Create a virtual environment and install the package
uv venv
uv pip install --upgrade Monei
```

### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install --upgrade Monei
```
(you may need to run `pip` with root permission: `sudo pip install --upgrade Monei`)

Then import the package:
```python
import Monei
```

## Quick Start

```python
import Monei
from Monei import ApiException
from pprint import pprint

# Initialize the client with your API key
monei = Monei.MoneiClient(api_key='YOUR_API_KEY')

try:
    # Create a payment
    payment = monei.payments.create({
        'amount': 1250,  # 12.50€
        'currency': 'EUR',
        'orderId': '123456',
        'description': 'Order #123456',
        'customer': {
            'email': 'customer@example.com',
            'name': 'John Doe'
        }
    })
    
    print(f"Payment created with ID: {payment.id}")
    print(f"Redirect URL: {payment.nextAction.redirectUrl}")
    
except ApiException as e:
    print(f"Error: {e}")
```

## Creating a Payment

To create a payment, you need to provide the amount, currency, and other details:

```python
payment = monei.payments.create({
    'amount': 1250,  # Amount in cents (12.50€)
    'currency': 'EUR',
    'orderId': '123456',
    'description': 'Order #123456',
    'completeUrl': 'https://example.com/complete',
    'cancelUrl': 'https://example.com/cancel',
    'callbackUrl': 'https://example.com/webhook',
    'customer': {
        'email': 'customer@example.com',
        'name': 'John Doe'
    }
})
```

### Hosted Payment Page Flow

1. **Create a payment**

```python
payment = monei.payments.create({
    'amount': 1250,
    'currency': 'EUR',
    'orderId': '123456',
    'description': 'Order #123456',
    'completeUrl': 'https://example.com/complete',
    'cancelUrl': 'https://example.com/cancel',
    'callbackUrl': 'https://example.com/webhook'
})
```

After creating a payment, you'll receive a response with a `nextAction.redirectUrl`. Redirect your customer to this URL to show them the MONEI Hosted payment page.

2. **Customer completes the payment**

The customer enters their payment information and completes any required verification steps (like 3D Secure).

3. **Customer is redirected back to your website**
   * If the customer completes the payment, they are redirected to the `completeUrl` with a `payment_id` query parameter
   * If the customer cancels, they are redirected to the `cancelUrl`

4. **Receive asynchronous notification**

MONEI sends an HTTP POST request to your `callbackUrl` with the payment result. This ensures you receive the payment status even if the customer closes their browser during the redirect.

For more information about the hosted payment page, visit the MONEI Hosted Payment Page documentation.

## Webhooks

Webhooks can be configured in the MONEI Dashboard → Settings → Webhooks.

### Signature Verification

When receiving webhooks from MONEI, you should verify the signature to ensure the request is authentic:

```python
import Monei
from flask import Flask, request, jsonify

app = Flask(__name__)
monei = Monei.MoneiClient(api_key='YOUR_API_KEY')

# Parse raw body for signature verification
@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        # Get the signature from the headers
        signature = request.headers.get('monei-signature')
        
        # Verify the signature and get the decoded payload
        payload = monei.verify_signature(request.data.decode('utf-8'), signature)
        
        # Process the webhook
        event_type = payload['type']
        
        # The data field contains the Payment object
        payment = payload['object']
        
        # Access Payment object properties directly
        payment_id = payment['id']
        amount = payment['amount']
        currency = payment['currency']
        status = payment['status']
        
        # Handle the event based on its type
        if event_type == 'payment.succeeded':
            # Handle successful payment
            print(f"Payment {payment_id} succeeded: {amount/100} {currency}")
        elif event_type == 'payment.failed':
            # Handle failed payment
            print(f"Payment {payment_id} failed with status: {status}")
        # Handle other event types
        
        return jsonify({'received': True}), 200
    except Exception as e:
        print(f"Webhook signature verification failed: {e}")
        return jsonify({'error': 'Invalid signature'}), 401

if __name__ == '__main__':
    app.run(port=3000)
```

### Handling Payment Callbacks

MONEI sends an HTTP POST request to your `callbackUrl` with the payment result. This ensures you receive the payment status even if the customer closes their browser during the redirect.

Example of handling the callback in a Flask server:

```python
from Monei.model.payment_status import PaymentStatus

@app.route('/checkout/callback', methods=['POST'])
def callback():
    signature = request.headers.get('monei-signature')
    
    try:
        # Verify the signature
        payment = monei.verify_signature(request.data.decode('utf-8'), signature)
        
        # Update your order status based on the payment status
        # Could be PaymentStatus.AUTHORIZED for pre-authorization payments
        if payment['status'] == PaymentStatus.SUCCEEDED:
            # Payment successful - fulfill the order
            pass
        elif payment['status'] == PaymentStatus.FAILED:
            # Payment failed - notify the customer
            pass
        
        # Acknowledge receipt of the webhook
        return jsonify({'received': True}), 200
    except Exception as e:
        print(f"Invalid webhook signature: {e}")
        return jsonify({'error': 'Invalid signature'}), 401
```

#### Important Notes About Webhooks

1. Always verify the signature to ensure the webhook is coming from MONEI
2. Use the raw request body for signature verification
3. Return a 2xx status code to acknowledge receipt of the webhook
4. Process webhooks asynchronously for time-consuming operations
5. Implement idempotency to handle duplicate webhook events

For more information about webhooks, visit the MONEI Webhooks documentation.

## MONEI Connect for Partners

If you're a partner or platform integrating with MONEI, you can act on behalf of your merchants by providing their Account ID. This is part of MONEI Connect, which allows platforms to manage multiple merchant accounts.

**Important:** When using Account ID functionality, you must:

1. Use a partner API key (not a regular merchant API key)
2. Provide a custom User-Agent to identify your platform

For more information about MONEI Connect and becoming a partner, visit the MONEI Connect documentation.

### Account ID

#### Setting Account ID in the constructor

```python
import Monei
from Monei import ApiException

# Initialize with Account ID and User-Agent using a partner API key
monei = Monei.MoneiClient(
    api_key='pk_partner_test_...',
    account_id='merchant_account_id',
    user_agent='MONEI/YourPlatform/1.0.0'
)

# Make API calls on behalf of the merchant
try:
    payment = monei.payments.create({
        'orderId': '12345',
        'amount': 1100,
        'currency': 'EUR'
    })
    print(payment)
except ApiException as e:
    print(f"Error: {e}")
```

#### Setting Account ID after initialization

```python
import Monei
from Monei import ApiException

# Initialize with a partner API key
monei = Monei.MoneiClient(api_key='pk_partner_test_...')

# Set User-Agent for your platform (required before setting Account ID)
monei.set_user_agent('MONEI/YourPlatform/1.0.0')

# Set Account ID to act on behalf of a merchant
monei.set_account_id('merchant_account_id')

# Make API calls on behalf of the merchant
try:
    payment = monei.payments.create({
        'orderId': '12345',
        'amount': 1100,
        'currency': 'EUR'
    })
    print(payment)
except ApiException as e:
    print(f"Error: {e}")

# Remove Account ID to stop acting on behalf of the merchant
monei.set_account_id(None)
```

### Custom User-Agent

You can set a custom User-Agent to identify your application or platform. This is required when using Account ID.

When integrating as a MONEI Connect partner, your User-Agent should follow this format:

```
MONEI/<PARTNER_NAME>/<VERSION>
```

For example: `MONEI/YourPlatform/1.0.0`

This format helps MONEI identify your platform in API requests and is required when using the Partner API Key.

```python
import Monei
from Monei import ApiException

# Set User-Agent in constructor with proper format
monei = Monei.MoneiClient(
    api_key='pk_partner_test_...',
    user_agent='MONEI/YourPlatform/1.0.0'
)

# Or set it after initialization
monei.set_user_agent('MONEI/YourPlatform/1.0.0')
```

#### Examples with Proper User-Agent Format

```python
import Monei
from Monei import ApiException

# For a platform named "ShopManager" with version 2.1.0
monei = Monei.MoneiClient(
    api_key='pk_partner_test_...',
    account_id='merchant_account_id',
    user_agent='MONEI/ShopManager/2.1.0'
)

# For a platform named "PaymentHub" with version 3.0.1
monei.set_user_agent('MONEI/PaymentHub/3.0.1')
```

### Managing Multiple Merchant Accounts

```python
import Monei
from Monei import ApiException
import time

# Initialize with a partner API key
monei = Monei.MoneiClient(
    api_key='pk_partner_test_...',
    user_agent='MONEI/YourPlatform/1.0.0'
)

# Function to process payments for multiple merchants
def process_payments_for_merchants(merchant_accounts):
    results = {}
    
    for merchant_id in merchant_accounts:
        # Set the current merchant account
        monei.set_account_id(merchant_id)
        
        # Process payment for this merchant
        try:
            payment = monei.payments.create({
                'orderId': f'order-{merchant_id}-{int(time.time())}',
                'amount': 1000,
                'currency': 'EUR'
            })
            
            results[merchant_id] = {'success': True, 'payment': payment}
        except ApiException as e:
            results[merchant_id] = {'success': False, 'error': str(e)}
    
    return results

# Example usage
merchant_accounts = ['merchant_1', 'merchant_2', 'merchant_3']
results = process_payments_for_merchants(merchant_accounts)
print(results)
```

## Documentation

For the full documentation, check our [Documentation portal](https://docs.monei.com/api/).

## Development

For development:

```sh
# Clone the repository
git clone https://github.com/monei/monei-python-sdk.git
cd monei-python-sdk

# Create a virtual environment and install dependencies
uv venv
uv pip install -e .

# Install development dependencies
uv pip install -e ".[test,lint]"

# Create lock files
uv pip compile pyproject.toml -o uv.lock
uv pip compile pyproject.toml --extra test --extra lint -o uv-dev.lock

# Sync dependencies using lock files
uv pip sync uv.lock  # For production dependencies
uv pip sync uv-dev.lock  # For development dependencies
```

## Testing

This project uses pytest for testing. The tests are automatically generated by the OpenAPI Generator, with additional tests for the main functionality.

To run the tests:

```sh
# Install test dependencies
uv pip install -e ".[test]"

# Run all tests
python -m pytest

# Run specific tests
python -m pytest test/test_main.py

# Run tests with coverage
python -m pytest --cov=Monei
```

The test configuration is defined in `pytest.ini` and includes settings for test discovery, coverage reporting, and custom markers.
