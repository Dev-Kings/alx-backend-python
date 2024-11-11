#!/usr/bin/env python3
"""
Module containing function zoom_array repeating each item a number of
specified time.
"""
from typing import List, Tuple


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    """
    Function to zoom into a list of integers by repeating each item a number
    of times determined by the factor.

    Args:
        lst (Tuple[int, ...]): A tuple containinf integers to be zoomed in on.
        factor (int, optional) : The number of times each item in the list
                                 will be repeated. Defaults to 2.
    Returns:
        List[int]: A List of integers where each item from the input tuple is
                   repeated 'factor' times.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
