"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730334012"


class Simpy:
    values: list[float]

    def __init__(self, values: list[float]):
        """Initializes values attribute of Simpy obj."""
        self.values = values

    def __repr__(self) -> str:
        """Converts Simpy object to str representation for Python."""
        return f"Simpy({self.values})"

    def fill(self, value: float, fill_in: int ) -> None:
        """Fill a Simpy's values with a specific number of repeating values."""
        while len(self.values) < fill_in:
            self.values.append(value)

    def arange(self, start: float, stop: float, step: float = 1.0 ) -> None:
        """Fills in the values attribute with a range of values."""
        assert step != 0.0
        i = start
        if step > 0:
            while i < stop:
                self.values.append(i)
                i += step

        if step < 0:
            while i > stop:
                self.values.append(i)
                i += step

    def sum(self) -> float:
        """Computes and returns the sum of all items in the values attribute."""
        total = 0
        total = sum(self.values)
        return total
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Makes it so that rhs operand of addition expression can be either a Simpy object or a float."""
        result = Simpy([])
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for item in range(len(self.values)):
                result.values.append(self.values[item] + rhs.values[item])
            return result

        if isinstance(rhs, float):
            for item in range(len(self.values)):
                result.values.append(self.values[item] + rhs)
            return result

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Makes it so that rhs operand of exponential expression can be either a Simpy object or a float."""
        result = Simpy([])
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for item in range(len(self.values)):
                result.values.append(self.values[item] ** rhs.values[item])
            return result

        if isinstance(rhs, float):
            for item in range(len(self.values)):
                result.values.append(self.values[item] ** rhs)
            return result

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Produces a mask based on equality of items in a list"""
        result: list[bool] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for item in range(len(self.values)):
                if item == rhs.values[item]:
                    result.append(True)
                else:
                    result.append(False)
            return result

        if isinstance(rhs, float):
            for item in range(len(self.values)):
                if item == rhs:
                    result.append(True)
                else:
                    result.append(False)
            return result







    