#!/usr/bin/env python3
"""
Module containing function zoom_array repeating each item a number of
specified time.
"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Function to zoom into a given list of integers by repeating each item
    a number of times determined by the factor.

    Args:
    lst (Tuple): A tuple containing items to be zoomed in on.
    factor (int, optional): The number of times each item in the list will
                             be repeated. Defaults to 2.

    Returns:
    List: A list of elements where each item from the input list
          is repeated 'factor' times.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
