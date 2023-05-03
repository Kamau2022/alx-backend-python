#!/usr/bin/env python3
"""a module on  asynchronous coroutine
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ asynchronous routine that takes in
        two integer argument
    """
    tasks = await asyncio.gather(*tuple((wait_random(max_delay)
                                 for x in range(n))))
    return sorted(tasks)
