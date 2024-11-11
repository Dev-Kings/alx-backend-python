#!/usr/bin/env python3
"""
Module is all about Duck typing - first element of a sequence.
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Returns the first element of lst if it exists, else None."""
    if lst:
        return lst[0]
    else:
        return None
