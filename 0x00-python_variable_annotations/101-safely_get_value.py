#!/usr/bin/env python3
"""a module that defines a type-annonated functions"""
from typing import Mapping, Any, Union, TypeVar
T = TypeVar("T")


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None]) -> Union[Any, T]:
    """a function that returns a union"""
    if key in dct:
        return dct[key]
    else:
        return default
