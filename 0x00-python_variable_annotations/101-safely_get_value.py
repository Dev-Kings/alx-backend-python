#!/usr/bin/env python3
"""
Module with function safely_get_value returning values and type
annotations to the function.
"""
from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely retrieves a value from a dictionary, returning default
    value is the key is present.
    """
    if key in dct:
        return dct[key]
    else:
        return default
