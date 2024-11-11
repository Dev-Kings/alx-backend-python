#!/usr/bin/env python3
"""
Module with function that multiplies a float by a given multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a given float by the multiplier."""
    return lambda x: x * multiplier
