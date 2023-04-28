#!/usr/bin/env python3

"""a module that shows type-annotated function"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """a function that takes a string and a float and
       returns a tuple"""
    return (k, v * v)
