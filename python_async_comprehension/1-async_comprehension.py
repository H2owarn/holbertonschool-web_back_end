#!/usr/bin/env python3

"""
This module that takes no arguments.
The coroutine will collect 10 random numbers
using an async comprehensing over async_generator,
then return the 10 random numbers.
"""

import asyncio
import random
from typing import List

async_generator = __import__('0-async_generator').async_generator

async def async_comprehension() -> List[float]:
    """Return 10 random number

    return the 10 random numbers
    over async_generator
    """
    return [num async for num in async_generator()]
