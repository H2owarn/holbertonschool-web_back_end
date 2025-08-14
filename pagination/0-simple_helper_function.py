#!/usr/bin/env python3
"""
This module takes two integer arguments page
and page_size. and return a tuple of
size two containing a start index and
an end index corresponding

"""


def index_range(page: int, page_size: int) -> tuple:
    """ Return a tuple
    Args:
    page(int): number
    page_size(int): number

    Return:
    a tuple of size two containing a start index and an end index corresponding
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
