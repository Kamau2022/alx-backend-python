#!/usr/bin/env python3
"""a module on  asynchronous coroutine
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """ asynchronous coroutine that takes in
        an integer argument
    """
    value = random.uniform(0, max_delay)
    await asyncio.sleep(value)
    return value
