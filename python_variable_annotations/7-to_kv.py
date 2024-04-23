#!/usr/bin/env python3
"""
Function takes str(k) and int/float (v) and returns a tuple
Tuple first element: str(k), second element: square int/float (v)
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """return tuple"""
    return (k, v * v)
