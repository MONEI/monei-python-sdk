# MONEI PYTHON SDK

[![PyPI version](https://img.shields.io/pypi/v/Monei.svg)](https://pypi.org/project/Monei/)
[![PyPI Downloads](https://img.shields.io/pypi/dm/Monei.svg)](https://pypi.org/project/Monei/)
[![PyPI Status](https://img.shields.io/pypi/status/Monei.svg)](https://pypi.org/project/Monei/)
[![Python Versions](https://img.shields.io/pypi/pyversions/Monei.svg)](https://pypi.org/project/Monei/)
[![License](https://img.shields.io/github/license/MONEI/monei-python-sdk.svg)](https://github.com/MONEI/monei-python-sdk/blob/main/LICENSE)

The MONEI Python SDK provides convenient access to the [MONEI](https://monei.com/) API from applications written in server-side Python.

For collecting customer and payment information in the browser, use [monei.js](https://docs.monei.com/docs/monei-js-overview).

## Table of Contents

- [MONEI PYTHON SDK](#monei-python-sdk)
  - [Table of Contents](#table-of-contents)
  - [Requirements](#requirements)
  - [Installation](#installation)
    - [Using uv (Recommended)](#using-uv-recommended)
    - [pip install](#pip-install)
  - [Basic Usage](#basic-usage)
    - [API Keys](#api-keys)
      - [Types of API Keys](#types-of-api-keys)
      - [API Key Security](#api-key-security)
    - [Test Mode](#test-mode)
    - [Basic Client Usage](#basic-client-usage)
  - [Payment Operations](#payment-operations)
    - [Creating a Payment](#creating-a-payment)
    - [Retrieving a Payment](#retrieving-a-payment)
    - [Refunding a Payment](#refunding-a-payment)
  - [Integration Methods](#integration-methods)
    - [Using the Prebuilt Payment Page](#using-the-prebuilt-payment-page)
      - [Features](#features)
      - [Integration Flow](#integration-flow)
  - [Webhooks](#webhooks)
    - [Signature Verification](#signature-verification)
    - [Handling Payment Callbacks](#handling-payment-callbacks)
      - [Important Notes About Webhooks](#important-notes-about-webhooks)
  - [MONEI Connect for Partners](#monei-connect-for-partners)
    - [Account ID](#account-id)
      - [Setting Account ID in the constructor](#setting-account-id-in-the-constructor)
      - [Setting Account ID after initialization](#setting-account-id-after-initialization)
    - [Custom User-Agent](#custom-user-agent)
      - [Examples with Proper User-Agent Format](#examples-with-proper-user-agent-format)
    - [Managing Multiple Merchant Accounts](#managing-multiple-merchant-accounts)
  - [Development](#development)
    - [Building the SDK](#building-the-sdk)
  - [Tests](#tests)
  - [Code Style](#code-style)
  - [Documentation](#documentation)

## Requirements

- Python 3.7 or later

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

If the Python package is hosted on a repository, you can install directly using:

```sh
pip install --upgrade Monei
```
(you may need to run `pip` with root permission: `sudo pip install --upgrade Monei`)

Then import the package:
```python
import Monei
```

## Basic Usage

### API Keys

The MONEI API uses API keys for authentication. You can obtain and manage your API keys in the [MONEI Dashboard](https://dashboard.monei.com/settings/api).

#### Types of API Keys

MONEI provides two types of API keys:

- **Test API Keys**: Use these for development and testing. Transactions made with test API keys are not processed by real payment providers.
- **Live API Keys**: Use these in production environments. Transactions made with live API keys are processed by real payment providers and will move actual money.

Each API key has a distinct prefix that indicates its environment:

- Test API keys start with `pk_test_` (e.g., `pk_test_12345abcdef`)
- Live API keys start with `pk_live_` (e.g., `pk_live_12345abcdef`)

By checking the prefix of an API key, you can quickly determine which environment you're working in. This is especially useful when you're managing multiple projects or environments.

#### API Key Security

Your API keys carry significant privileges, so be sure to keep them secure:

- Keep your API keys confidential and never share them in publicly accessible areas such as GitHub, client-side code, or in your frontend application.
- Use environment variables or a secure vault to store your API keys.
- Restrict API key access to only the IP addresses that need them.
- Regularly rotate your API keys, especially if you suspect they may have been compromised.

```python
# Example of loading API key from environment variable (recommended)
import os
import Monei

api_key = os.getenv('MONEI_API_KEY')
monei = Monei.MoneiClient(api_key)
```

### Test Mode

To test your integration with MONEI, you need to switch to **test mode** using the toggle in the header of your MONEI Dashboard. When in test mode:

1. Generate your test API key in [MONEI Dashboard → Settings → API Access](https://dashboard.monei.com/settings/api)
2. Configure your payment methods in [MONEI Dashboard → Settings → Payment Methods](https://dashboard.monei.com/settings/payment-methods)

**Important:** Account ID and API key generated in test mode are different from those in live (production) mode and can only be used for testing purposes.

When using test mode, you can simulate various payment scenarios using test card numbers, Bizum phone numbers, and PayPal accounts provided in the [MONEI Testing documentation](https://docs.monei.com/docs/testing/).

### Basic Client Usage

```python
import Monei
from Monei import ApiException
from Monei.model.create_payment_request import CreatePaymentRequest
from Monei.model.payment_customer import PaymentCustomer
from pprint import pprint

# Initialize the client with your API key
monei = Monei.MoneiClient(api_key='YOUR_API_KEY')

try:
    # Create a payment using request classes
    customer = PaymentCustomer(
        email='customer@example.com',
        name='John Doe'
    )
    
    payment_request = CreatePaymentRequest(
        amount=1250,  # 12.50€
        currency='EUR',
        order_id='123456',
        description='Order #123456',
        customer=customer
    )
    
    payment = monei.payments.create(payment_request)
    
    print(f"Payment created with ID: {payment.id}")
    print(f"Redirect URL: {payment.nextAction.redirectUrl}")
    
except ApiException as e:
    print(f"Error: {e}")
```

## Payment Operations

### Creating a Payment

To create a payment, you need to provide the amount, currency, and other details using request classes:

```python
from Monei.model.create_payment_request import CreatePaymentRequest
from Monei.model.payment_customer import PaymentCustomer

# Create a customer object
customer = PaymentCustomer(
    email='customer@example.com',
    name='John Doe'
)

# Create the payment request
payment_request = CreatePaymentRequest(
    amount=1250,  # Amount in cents (12.50€)
    currency='EUR',
    order_id='123456',
    description='Order #123456',
    complete_url='https://example.com/complete',
    cancel_url='https://example.com/cancel',
    callback_url='https://example.com/webhook',
    customer=customer
)

# Create the payment
payment = monei.payments.create(payment_request)
```

### Retrieving a Payment

Retrieve an existing payment by ID:

```python
try:
    payment = monei.payments.get('pay_123456789')
    print(f"Payment status: {payment.status}")
except ApiException as e:
    print(f"Error retrieving payment: {e}")
```

### Refunding a Payment

Process a full or partial refund:

```python
from Monei.model.refund_payment_request import RefundPaymentRequest

try:
    refund_request = RefundPaymentRequest(
        amount=500,  # Partial refund of 5.00€
        refund_reason='Customer request'
    )
    
    result = monei.payments.refund('pay_123456789', refund_request)
    print(f"Refund created with ID: {result.id}")
except ApiException as e:
    print(f"Error refunding payment: {e}")
```

## Integration Methods

### Using the Prebuilt Payment Page

MONEI Hosted Payment Page is the simplest way to securely collect payments from your customers without building your own payment form.

#### Features

- **Designed to remove friction** — Real-time card validation with built-in error messaging
- **Mobile-ready** — Fully responsive design
- **International** — Supports 13 languages
- **Multiple payment methods** — Supports multiple payment methods including Cards, PayPal, Bizum, GooglePay, Apple Pay & Click to Pay
- **Customization and branding** — Customizable logo, buttons and background color
- **3D Secure** — Supports 3D Secure - SCA verification process
- **Fraud and compliance** — Simplified PCI compliance and SCA-ready

You can customize the appearance in your MONEI Dashboard → Settings → Branding.

#### Integration Flow

1. **Create a payment**

```python
from Monei.model.create_payment_request import CreatePaymentRequest

# Create the payment request
payment_request = CreatePaymentRequest(
    amount=1250,
    currency='EUR',
    order_id='123456',
    description='Order #123456',
    complete_url='https://example.com/complete',
    cancel_url='https://example.com/cancel',
    callback_url='https://example.com/webhook'
)

# Create the payment
payment = monei.payments.create(payment_request)
```

After creating a payment, you'll receive a response with a `nextAction.redirectUrl`. Redirect your customer to this URL to show them the MONEI Hosted payment page.

2. **Customer completes the payment**

The customer enters their payment information and completes any required verification steps (like 3D Secure).

3. **Customer is redirected back to your website**
   * If the customer completes the payment, they are redirected to the `complete_url` with a `payment_id` query parameter
   * If the customer cancels, they are redirected to the `cancel_url`

4. **Receive asynchronous notification**

MONEI sends an HTTP POST request to your `callback_url` with the payment result. This ensures you receive the payment status even if the customer closes their browser during the redirect.

For more information about the hosted payment page, visit the [MONEI Hosted Payment Page documentation](https://docs.monei.com/docs/integrations/use-prebuilt-payment-page).

## Webhooks

Webhooks can be configured in the [MONEI Dashboard → Settings → Webhooks](https://dashboard.monei.com/settings/webhooks).

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

MONEI sends an HTTP POST request to your `callback_url` with the payment result. This ensures you receive the payment status even if the customer closes their browser during the redirect.

Example of handling the callback in a Flask server:

```python
from Monei.model.payment_status import PaymentStatus

@app.route('/checkout/callback', methods=['POST'])
def callback():
    signature = request.headers.get('monei-signature')
    
    try:
        # Verify the signature
        payload = monei.verify_signature(request.data.decode('utf-8'), signature)
        payment = payload['object']
        
        # Update your order status based on the payment status
        if payment['status'] == PaymentStatus.SUCCEEDED:
            # Payment successful - fulfill the order
            # Update your database, send confirmation email, etc.
            pass
        elif payment['status'] == PaymentStatus.FAILED:
            # Payment failed - notify the customer
            # Log the failure, update your database, etc.
            pass
        elif payment['status'] == PaymentStatus.AUTHORIZED:
            # Payment is authorized but not yet captured
            # You can capture it later
            pass
        elif payment['status'] == PaymentStatus.CANCELED:
            # Payment was canceled
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

## MONEI Connect for Partners

If you're a partner or platform integrating with MONEI, you can act on behalf of your merchants by providing their Account ID. This is part of [MONEI Connect](https://docs.monei.com/docs/monei-connect/), which allows platforms to manage multiple merchant accounts.

**Important:** When using Account ID functionality, you must:

1. Use a partner API key (not a regular merchant API key)
2. Provide a custom User-Agent to identify your platform

For more information about MONEI Connect and becoming a partner, visit the [MONEI Connect documentation](https://docs.monei.com/docs/monei-connect/).

### Account ID

#### Setting Account ID in the constructor

```python
import Monei
from Monei import ApiException
from Monei.model.create_payment_request import CreatePaymentRequest

# Initialize with Account ID and User-Agent using a partner API key
monei = Monei.MoneiClient(
    api_key='pk_partner_test_...',
    account_id='merchant_account_id',
    user_agent='MONEI/YourPlatform/1.0.0'
)

# Make API calls on behalf of the merchant
try:
    payment_request = CreatePaymentRequest(
        order_id='12345',
        amount=1100,
        currency='EUR'
    )
    payment = monei.payments.create(payment_request)
    print(payment)
except ApiException as e:
    print(f"Error: {e}")
```

#### Setting Account ID after initialization

```python
import Monei
from Monei import ApiException
from Monei.model.create_payment_request import CreatePaymentRequest

# Initialize with a partner API key
monei = Monei.MoneiClient(api_key='pk_partner_test_...')

# Set User-Agent for your platform (required before setting Account ID)
monei.set_user_agent('MONEI/YourPlatform/1.0.0')

# Set Account ID to act on behalf of a merchant
monei.set_account_id('merchant_account_id')

# Make API calls on behalf of the merchant
try:
    payment_request = CreatePaymentRequest(
        order_id='12345',
        amount=1100,
        currency='EUR'
    )
    payment = monei.payments.create(payment_request)
    print(payment)
except ApiException as e:
    print(f"Error: {e}")

# Remove Account ID to stop acting on behalf of the merchant
monei.set_account_id(None)
```

### Custom User-Agent

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

> **Note:** When using Account ID, you must set a custom User-Agent before making any API calls. The User-Agent is validated when making API requests.
> 
> **Important:** To use this feature, you need to be registered as a MONEI partner and use your partner API key. Please contact connect@monei.com to register as a partner.

### Managing Multiple Merchant Accounts

```python
import Monei
from Monei import ApiException
from Monei.model.create_payment_request import CreatePaymentRequest
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
            payment_request = CreatePaymentRequest(
                order_id=f'order-{merchant_id}-{int(time.time())}',
                amount=1000,
                currency='EUR'
            )
            payment = monei.payments.create(payment_request)
            
            results[merchant_id] = {'success': True, 'payment': payment}
        except ApiException as e:
            results[merchant_id] = {'success': False, 'error': str(e)}
    
    return results

# Example usage
merchant_accounts = ['merchant_1', 'merchant_2', 'merchant_3']
results = process_payments_for_merchants(merchant_accounts)
print(results)
```

## Development

### Building the SDK

The SDK is built using OpenAPI Generator. To build the SDK from the OpenAPI specification:

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

## Tests

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

The test configuration is defined in `pyproject.toml` under the `[tool.pytest.ini_options]` section and includes settings for test discovery, coverage reporting, and custom markers.

## Code Style

This project follows the [PEP 8](https://peps.python.org/pep-0008/) style guide for Python code. We use tools like flake8, black, and isort to enforce coding standards.

To check code style:

```sh
# Check code style with flake8
flake8 Monei

# Format code with black
black Monei

# Sort imports with isort
isort Monei
```

## Documentation

For the full documentation, check our [Documentation portal](https://docs.monei.com/api/).

For a comprehensive overview of all MONEI features and integration options, visit our [main documentation portal](https://docs.monei.com/). There you can explore guides for:

* Using a prebuilt payment page with MONEI Hosted payment page
* Building a custom checkout with MONEI UI components
* Integrating with multiple e-commerce platforms
* Connecting with business platforms and marketplaces
