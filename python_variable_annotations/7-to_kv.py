#!/usr/bin/env python3
"""
Module takes teo arguments and return
a tuple. the first is string and
the second element is the square of the input
"""

from typing import Tuple
import math


def to_kv(k: str, v: float) -> Tuple[str, float]:
    """Return tuple
        Args:
        k [str] : The first argument
        v [float]: The second argument

    Returns:
        tuple[k [str], the square of the int/float v]
    """
    return (k, math.pow(v, 2))
