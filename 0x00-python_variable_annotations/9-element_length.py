#!/usr/bin/env python3
"""a module that shows a type-annotated function"""
from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """a function that return values with the appropriate types"""
    return [(i, len(i)) for i in lst]
