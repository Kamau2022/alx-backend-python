#!/usr/bin/env python3
""" a module on Async Comprehension
"""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[int, None, None]:
    """a coroutine that takes argument
    """
    for i in range(10):
        await asyncio.sleep(1)
        value = random.uniform(0, 10)
        yield value
