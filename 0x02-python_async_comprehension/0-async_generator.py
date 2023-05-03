#!/usr/bin/env python3
""" a module on Async Comprehension
"""
import random
import asyncio
from typing import List


async def async_generator() -> float:
    """a coroutine that takes argument
    """
    for i in range(10):
        value = random.uniform(0, 10)
        await asyncio.sleep(1)
        yield value
