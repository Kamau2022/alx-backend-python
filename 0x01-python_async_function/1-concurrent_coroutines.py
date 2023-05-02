#!/usr/bin/env python3
"""a module on  asynchronous coroutine
"""
import asyncio
import random
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int):
    """ asynchronous routine that takes in
        two integer argument
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for n in range(n)]
    await asyncio.wait(tasks)
    return tasks
