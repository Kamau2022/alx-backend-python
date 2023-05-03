#!/usr/bin/env python3
""" a module on Async Comprehension
"""
import random
import asyncio
from typing import Iterator
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Iterator[float]:
    """a coroutine that uses async comprehensing
    """
    values = [item async for item in async_generator()]
    return values
