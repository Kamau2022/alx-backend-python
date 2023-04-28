#!/usr/bin/env python3
"""a module that defines a type-annonated function"""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """a function that returns a union"""
    if lst:
        return lst[0]
    else:
        return None
