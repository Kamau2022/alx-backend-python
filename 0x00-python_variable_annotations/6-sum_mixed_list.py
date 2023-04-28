#!/usr/bin/env python3

"""a module that defines a type-annotated function"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """a function that which takes a list mxd_lst of
       floats and int as argument
    Args:
       mxd_lst(float): list
    Returns:
        sum: float
    """
    x: float = 0
    for item in mxd_lst:
        x += item
    return x
