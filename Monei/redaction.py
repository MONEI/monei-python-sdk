"""Masks card data in the string representation of models.

The generated `to_str` prints `to_dict()`, so `print` or a log line would show the
full card number and CVC of a card, also when the card is nested in a request.
This module is hand-written (the generator does not create it) and
`scripts/post-build.sh` imports it from `Monei/__init__.py` after each
regeneration. `to_dict()` and the request body keep the real values.
"""

import pprint

from Monei.model.cardholder_verification_card import CardholderVerificationCard
from Monei.model_utils import ModelComposed, ModelNormal


def _mask_card(plain):
    masked = dict(plain)
    number = masked.get("number")
    if number is not None:
        masked["number"] = "**** " + number[-4:] if len(number) > 4 else "****"
    if masked.get("cvc") is not None:
        masked["cvc"] = "***"
    return masked


def _mask_value(value, plain):
    if isinstance(value, CardholderVerificationCard) and isinstance(plain, dict):
        return _mask_card(plain)
    if hasattr(value, "_data_store") and isinstance(plain, dict):
        _mask_model(value, plain)
        return plain
    if isinstance(value, list) and isinstance(plain, list):
        return [_mask_value(v, p) for v, p in zip(value, plain)]
    if isinstance(value, dict) and isinstance(plain, dict):
        return {k: _mask_value(value.get(k), p) for k, p in plain.items()}
    return plain


def _mask_model(model, plain):
    """Walks the model next to its `to_dict()` output, which has lost the model
    classes, and masks the entries that come from a card."""
    instances = [model]
    if model._composed_schemas:
        instances.extend(model._composed_instances)
    for instance in instances:
        for attr, value in instance._data_store.items():
            if attr in plain:
                plain[attr] = _mask_value(value, plain[attr])


def _masked_to_str(self):
    """Returns the string representation of the model, with card data masked"""
    plain = self.to_dict()
    if isinstance(self, CardholderVerificationCard):
        plain = _mask_card(plain)
    else:
        _mask_model(self, plain)
    return pprint.pformat(plain)


ModelNormal.to_str = _masked_to_str  # type: ignore[method-assign]
ModelComposed.to_str = _masked_to_str  # type: ignore[method-assign]
