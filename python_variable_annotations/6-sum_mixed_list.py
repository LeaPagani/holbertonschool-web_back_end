#!/usr/bin/env python3
"""takes list of floats and ints and returns their sum as a float"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """return sum of list floats & ints"""
    return sum(mxd_lst)
