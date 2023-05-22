#!/usr/bin/env python3
"""a module on Unittests and Integration Tests
"""
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)

import unittest
from parameterized import parameterized


def access_nested_map(nested_map: Mapping, path: Sequence) -> Any:
    """Access nested map with key path.
    Parameters
    ----------
    nested_map: Mapping
        A nested map
    path: Sequence
        a sequence of key representing a path to the value
    Example
    -------
    >>> nested_map = {"a": {"b": {"c": 1}}}
    >>> access_nested_map(nested_map, ["a", "b", "c"])
    1
    """
    for key in path:
        if not isinstance(nested_map, Mapping):
            raise KeyError(key)
        nested_map = nested_map[key]

    return nested_map


class TestAccessNestedMap(unittest.TestCase):
    """class that inherits from unittest.TestCase
    """
    @parameterized.expand([
        {"a": 1}, ("a",),
        {"a": {"b": 2}}, ("a",),
        {"a": {"b": 2}}, ("a", "b")
        ])
    def access_nested_map(nested_map: Mapping, path: Sequence) -> Any:
        """a function to be tested
        """

        result = access_nested_map(nested_map, path)

        self.assertEqual(result, expected_result)
