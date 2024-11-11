#!/usr/bin/env python3
"""
Module with function returning a set.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple: first element is string k, second element is
    square of v as the float.
    """
    return (k, float(v ** 2))
