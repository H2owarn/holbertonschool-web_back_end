#!/usr/bin/env python3
"""
This module show simple pagination

"""

import csv
import math
from typing import List

def index_range(page: int = 1, page_size: int = 10) -> tuple:
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



class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "/root/holbertonschool-web_back_end/pagination/Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:

        "Page must be a positive integer"
        assert isinstance(page, int) and page > 0
        "Page size must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0

        # calculate slice boundaries
        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        # return paginated data

        if start_index >= len(dataset):
            return []
        return dataset[start_index:end_index]
