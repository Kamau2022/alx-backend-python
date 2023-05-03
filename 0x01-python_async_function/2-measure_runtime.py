#!/usr/bin/env python3
"""a module on asynchronous coroutine
"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """a function that measures the total execution time
    """
    time_start = time.time()
    asyncio.run(wait_n(n, max_delay))
    await asyncio.run(tasks)
    time_end = time.time()
    duration = (time_end - time_start)
    return duration
