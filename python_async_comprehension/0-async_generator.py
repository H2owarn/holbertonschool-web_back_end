#!/usr/bin/env python3
"""
This module asynchronous generator coroutine
that loops 10 times, waits 1 second each time,
and yields a random number between 0 and 10
"""

import random
from typing import Generator
import asyncio


async def async_generator() -> Generator[float, None, None]:
    """Return random float number
    Args:
    ()
    Return:
    Random [float] between 1 to 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(1.00, 10.00)
