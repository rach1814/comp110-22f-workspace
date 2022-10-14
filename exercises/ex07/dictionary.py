"""EX07 - Dictionary functions to be tested."""

__author__ = "730334012"


def invert(iss: dict[str, str]) -> dict[str, str]:
    """Function that will invert the keys and values of a list. keys become values and values become keys."""
    result: dict[str, str] = {}
    for key in iss:
        if iss[key] in result:  # if value in original is key in result then error
            raise KeyError("cannot have duplicate keys.")
        result[iss[key]] = key
    return result


def favorite_color(fc: dict[str, str]) -> str:
    """Function that will return the color that appears most frequently."""
    result: dict[str, str] = {}
    favcolor: str = ""
    maximum: int = 0
    for name in fc:
        if fc[name] in result:
            result[fc[name]] += 1
        else:
            result[fc[name]] = 1
    for key in result:
        if result[key] > maximum:
            maximum = result[key]
            favcolor = key
    return favcolor


def count(cc: list[str]) -> dict[str, int]:
    """Function to count the number of times a value appears in the input list."""
    result: dict[str, int] = {}
    for item in cc:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result
