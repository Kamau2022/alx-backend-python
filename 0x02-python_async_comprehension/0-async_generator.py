#!/usr/bin/env python3
""" a module on Async Comprehension
"""
import random
import asyncio


async def async_generator() -> float:
    """a coroutine that takes argument
    """
    for i in range(10):
        await asyncio.sleep(1)
        value = random.uniform(1, 10)
        yield value
