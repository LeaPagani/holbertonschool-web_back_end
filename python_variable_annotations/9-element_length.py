#!/usr/bin/env python3
"""
Function takes a List and returns the list
followed by the element length
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """return obj and length"""
    return [(i, len(i)) for i in lst]
