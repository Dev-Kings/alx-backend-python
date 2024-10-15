#!/usr/bin/env python3
"""
Module for async_generator coroutine
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Coroutine looping 10 times asynchronously, then waits for a second
    and yields random float number between 0 and 10.
    Returns:
        A generator of float numbers between 0 and 10.
    """
    for x in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
