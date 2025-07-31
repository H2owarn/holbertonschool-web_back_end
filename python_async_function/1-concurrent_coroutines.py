#!/usr/bin/env python3

"""
 execute multiple coroutines at the same time with async

"""

import heapq
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """The list of the delays
        Args:
        n [int]: The input number.
        mxd_lst[int]: default 10

    Returns:
        The list of the delays
    """

    heap = []   # pop them in order

    async def track_delay():
        delay = await wait_random(max_delay)
        heapq.heappush(heap, delay)  # collect results out of order

    await asyncio.gather(*(track_delay() for _ in range(n)))
    return [heapq.heappop(heap) for _ in range(len(heap))]
