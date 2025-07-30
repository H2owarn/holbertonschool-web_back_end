#!/usr/bin/env python3
import math

"""
This module defines the `floor` function,
which takes a floating-point number as input
and returns its floor value using `math.floor`.

The returned value is the greatest integer less than
or equal to the input float.
"""

def floor(n: float) -> int:
    """Return the floor value of a float.

    Args:
        n (float): The input floating-point number.

    Returns:
        int: The largest integer less than or equal to n.
    """
    return math.floor(n)
