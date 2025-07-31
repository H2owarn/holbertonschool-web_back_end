#!/usr/bin/env python3

"""
 Measure the runtime

"""

import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Return total time by n to get
    the average delay per c oroutine
    Args:
            n [int]: The input number.
            mxd_lst[int]: The input number.

        Returns:
            total time by n
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()
    total_time = end - start
    return total_time / n
