#!/usr/bin/env python3
"""
Module for async_comprehension coroutine
"""

from typing import List
import importlib

async_generator_module = importlib.import_module('0-async_generator')
async_generator = async_generator_module.async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine collecting 10 random numbers from async_generator function
    using an async_comprehension.
    Returns:
        A list of 10 random float numbers.
    """
    return [i async for i in async_generator()]
