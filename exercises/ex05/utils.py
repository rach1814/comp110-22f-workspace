"""List utility functions for unit tests."""
__author__ = "730334012"


def only_evens(xs: list[int]) -> list[int]:
    """Returns a list of even numbers from a given list."""
    i: int = 0
    evens: list[int] = list()
    while i < len(xs):
        if xs[i] % 2 == 0:
            evens.append(xs[i])
        i += 1
    return evens


def concat(xs: list[int], ys: list[int]) -> list[int]:
    """Returns two lists combined, one after the other."""
    xsys: list[int] = xs
    xsys.append(ys)
    return xsys


def sub(xs: list[int], si: int, ei: int) -> list[int]:
    """Returns a list of integers taken from given list starting at an index and ending at another index."""
    if si < 0:
        si = 0

    if ei > len(xs):
        ei = len(xs) - 1

    subset: list[int] = list()
    if len(xs) == 0:
        print(subset)

    if si > len(xs):
        print(subset)
    
    if ei < 0:
        print(subset)

    i: int = si
    while i < ei:
        subset.append(xs[i])
        i += 1
    return subset