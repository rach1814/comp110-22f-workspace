"""EX07 - Unit tests used to test functions in dictionary.py ."""
__author__ = "730334012"

from exercises.ex07.dictionary import invert, favorite_color, count


def test_invert() -> None:
    """Test for common use case."""
    assert invert({"rachel": "lopez"}) == {"lopez": "rachel"}


def test_invert_2() -> None:
    """Test for edge case."""
    assert invert({}) == {}


def test_invert_3() -> None:
    """Test for longer common use case."""
    assert invert({"yes": "no", "up": "down", "sun": "moon"}) == {"no": "yes", "down": "up", "moon": "sun"}


def test_favorite_color_1() -> None:
    """Test for common use case."""
    x: dict[str, str] = {"Rachel": "green", "Kris": "green", "Scout": "blue"}
    assert favorite_color(x) == "green"


def test_favorite_color_2() -> None:
    """Test for if there is a tie for the most popular color."""
    assert favorite_color({"Rachel": "green", "Kris": "green", "Scout": "blue", "Dani": "blue"}) == "green"


def test_favorite_color_3() -> None:
    """Test for edge case, if input list is empty."""
    assert favorite_color({}) == ""


def test_count_1() -> None:
    """Test for common use case."""
    ds: list[str] = ["blue", "blue", "yellow"]
    assert count(ds) == {"blue": 2, "yellow": 1}


def test_count_2() -> None:
    """Test for edge case, if input list is empty."""
    ds: list[str] = []
    assert count(ds) == {}


def test_count_3() -> None:
    """Test for longer common use case."""
    ds: list[str] = ["frog", "toad", "frog", "fly", "flower", "toad", "fly", "frog"]
    assert count(ds) == {"frog": 3, "toad": 2, "fly": 2, "flower": 1}