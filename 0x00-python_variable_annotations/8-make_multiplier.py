#!/usr/bin/env python3
"""a module showing a type-annotated function"""
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """a function that takes float as argument
       Args:
           multiplier: float
       returns
    """
    return make_multiplier(multiplier)
