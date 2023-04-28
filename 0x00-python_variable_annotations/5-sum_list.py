#!/usr/bin/env python3

"""a module that defines a type-annotated function"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """a function that which takes a list input_list of
       floats as argument
    Args:
       input_list(float): list
    Returns:
        sum: float
    """
    x = 0
    for item in input_list:
        x += item
    return x
