#!/usr/bin/env python3
import math

"""
This module provides a single function, `floor`,
which takes a float and returns its floor value
as an integer using the math module.
"""


def floor(n: float) -> int:
    """Return the floor value of a float.

    Args:
        n (float): The input number.

    Returns:
        int: The largest integer less
        than or equal to the input.
    """
    return math.floor(n)
