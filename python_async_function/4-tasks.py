#!/usr/bin/env python3

"""
This module is nearly identical to wait_n
except task_wait_random is being called.
"""
import asyncio
from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n
wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Schedule n tasks using task_wait_random and return the sorted delays.

    Args:
        n (int): Number of tasks
        max_delay (int): Maximum delay per task

    Returns:
        List[float]: Sorted list of delays
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
