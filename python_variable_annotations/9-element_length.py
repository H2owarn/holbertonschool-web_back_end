#!/usr/bin/env python3
"""
 return values with the appropriate types

"""
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:

    """Return i in lst
        Args :
        lst: Iterable[Sequence]

        Return:
        List[Tuple[Sequence, int]]
    """
    return [(i, len(i)) for i in lst]
