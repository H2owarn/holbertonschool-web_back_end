#!/usr/bin/env python3


import heapq
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    heap = []

    async def track_delay():
        delay = await wait_random(max_delay)
        heapq.heappush(heap, delay)

    await asyncio.gather(*(track_delay() for _ in range(n)))
    return [heapq.heappop(heap) for _ in range(len(heap))]


