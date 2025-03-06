
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from Monei.api.apple_pay_domain_api import ApplePayDomainApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from Monei.api.apple_pay_domain_api import ApplePayDomainApi
from Monei.api.bizum_api import BizumApi
from Monei.api.payment_methods_api import PaymentMethodsApi
from Monei.api.payments_api import PaymentsApi
from Monei.api.subscriptions_api import SubscriptionsApi
