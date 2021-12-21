# MONEI PYTHON SDK

The MONEI API is organized around [REST](https://en.wikipedia.org/wiki/Representational_State_Transfer). Our API has predictable resource-oriented URLs, accepts JSON-encoded request bodies, returns JSON-encoded responses, and uses standard HTTP response codes, authentication, and verbs.

This library is intended to help you develop an integration around our API, by using the MONEI Python Client and it's methods.

## Docs in our portal

**You can find the complete information and details in [our documentation portal](https://docs.monei.com/api/).**

## Requirements

Python 2.7 and 3.4+

## Installation & Usage

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
