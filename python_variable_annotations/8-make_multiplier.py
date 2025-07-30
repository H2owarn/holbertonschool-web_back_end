#!/usr/bin/env python3
"""
Module takes takes a float multiplier
as argument and returns a function
that multiplies a float by multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def multiply(value: float) -> float:
          return value * multiplier
    """Return multiplies a float
        Args:
        v [float]: The input number

    Returns:
        multiplies a float
    """
    return multiply
