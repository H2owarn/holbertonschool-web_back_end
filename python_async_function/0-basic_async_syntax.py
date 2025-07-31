#!/usr/bin/env python3

"""
Module  takes in an integer argument
waits for a random delay and eventually returns it.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ Return dalay time
    Args:
        max_delay [int] : with a default value of 10

    Returns:
        delay time
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
