#!/usr/bin/env python3
"""
Module takes a list mxd_lst of integers
and floats and returns their sum as a float.
"""

from typing import List

def sum_list(input_list: List[float]) -> float:
    """Return sum
        Args:
        input_list list[float]: The input list.

    Returns:
        sum
    """
    return sum(input_list)
