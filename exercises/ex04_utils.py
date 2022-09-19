"""ex04 list utility functions."""
__author__ = "730334012"

all_list: list[int] = list()


def all(a: list[int], b: int) -> bool:
    """Returns true if all numbers match b."""
    i: int = 0
    if len(a) == 0:
        return False
    while i < len(a):
        if a[i] != b:
            return False 
        else:
            i += 1
    return True


def max(c: list[int]) -> int:
    """Returns largest number in list."""
    if len(c) == 0:
        raise ValueError("max() arg is an empty List")

    maximum = c[0]
    i: int = 1
    while i < len(c):
        if c[i] > maximum:
            maximum = c[i]
        i += 1
    return maximum


def is_equal(d: list[int], e: list[int]) -> bool:
    """Returns true if both lists match completely."""
    i: int = 0
    if len(d) == len(e):
        while i < len(e):
            if d[i] != e[i]:
                return False 
            else:
                i += 1
        return True
    else:
        return False