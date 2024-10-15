#!/usr/bin/env python3
"""
Module for measure_runtime coroutine
"""

import asyncio
import time
import importlib

async_comprehension_module = importlib.import_module('1-async_comprehension')
async_comprehension = async_comprehension_module.async_comprehension


async def measure_runtime() -> float:
    """
    Runs async_comprehension 4 times in parallel, then measures total runtime
    Returns:
        Total runtime in seconds as a float.
    """
    start_time = time.perf_counter()

    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    end_time = time.perf_counter()
    return end_time - start_time
