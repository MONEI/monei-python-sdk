# MONEI PYTHON SDK

The MONEI API is organized around [REST](https://en.wikipedia.org/wiki/Representational_State_Transfer). Our API has predictable resource-oriented URLs, accepts JSON-encoded request bodies, returns JSON-encoded responses, and uses standard HTTP response codes, authentication, and verbs.

This library is intended to help you develop an integration around our API, by using the MONEI Python Client and it's methods.

## Docs in our portal

**You can find the complete information and details in [our documentation portal](https://docs.monei.com/api/).**

## Requirements

Python 2.7 and 3.4+

## Installation & Usage

### Using uv (Recommended)

[uv](https://github.com/astral-sh/uv) is a modern Python package installer and resolver that's significantly faster than pip. To install and use this package with uv:

```sh
# Install uv if you don't have it yet
curl -sSf https://astral.sh/uv/install.sh | sh

# Create a virtual environment and install the package
uv venv
uv pip install --upgrade Monei
```

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

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import Monei
```

## Authorization

The MONEI API uses API key to authenticate requests. You can view and manage your API key in the [MONEI Dashboard](https://dashboard.monei.com/settings/api).

For more information about this process, please refer to [our documentation portal](https://docs.monei.com/api/#section/Authentication).



## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
import Monei
from Monei import ApiException
from pprint import pprint

# Instantiate the client using the API key
monei = Monei.MoneiClient(api_key='YOUR_API_KEY')

try:
    # Create Payment
    result = monei.payments.create({
        'amount': 1250, # 12.50€
        'orderId': '100200000001',
        'currency': 'EUR',
        'description': 'Items description',
        'customer': {
            'email': 'john.doe@monei.com',
            'name': 'John Doe'
        }
    })
    pprint(result)
except ApiException as e:
    print("Error while creating payment: %s\n" % e)

```

## Documentation for API Endpoints

For more detailed information about this library and the full list of methods, please refer to [our documentation portal](https://docs.monei.com/api/).

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
