#!/usr/bin/env python3
"""a module on Async Comprehension"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ coroutine that will execute async_comprehension
        four times in parallel using asyncio.gather
    """
    time_start = time.time()
    await asyncio.gather(*[async_comprehension()
                         for x in range(4)])
    time_end = time.time()
    duration = (time_end - time_start)
    return duration
