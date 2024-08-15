"""
A tiny module to wrap json decode/decode functionality.
"""
import json
from typing import Any

import canonicaljson

from . import errors


def encode(data: Any) -> str:
    """
    Encode data into a json string.
    """
    try:
        return canonicaljson.encode_canonical_json(data).decode()
    except TypeError:
        raise errors.PybovValidationError(
            'Validation error',
                **{'_jsondata': f'Data type cannot be converted to json: "{data}"'}
        )


def decode(data: str) -> Any:
    """
    Decode json string into a python parsed type.
    """
    try:
        return json.loads(data)
    except json.JSONDecodeError:
        raise errors.PybovValidationError(
            'Validation error',
                **{'_jsondata': f'Invalid json string: "{data}"'}
        )
