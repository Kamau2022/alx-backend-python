#!/usr/bin/env python3

"""a module that defines a type-annotated function"""

input_list: list[float]
def sum_list(input_list: input_list) -> input_list:
    """a function that which takes a list input_list of 
       floats as argument
    Args:
       input_list(float): list
    Returns:
        sum: float
    """
    return [i + input_list for i in input_list]
