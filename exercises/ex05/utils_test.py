"""Unit tests for utility functions in utils.py."""
__author__ = "730334012"

from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens() -> None:
    """Testing only_evens function."""
    xs: list[int] = [111, 28, 64, 97]
    assert only_evens(xs) == [28, 64]

