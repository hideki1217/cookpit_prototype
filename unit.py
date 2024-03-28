from dataclasses import dataclass
from typing import Literal


class Weight:
    Unit = Literal["g", "kg"]
    def __init__(self, value: float, unit: Unit) -> None:
        if unit == "g":
            self._value_g = value
        if unit == "kg":
            self._value_g = value * 1000

    def __call__(self, unit: Unit):
        if unit == "g":
            return self._value_g
        if unit == "kg":
            return self("g") / 1000
        raise KeyError


class Count:
    def __init__(self, value: int) -> None:
        self._value = value

    def __call__(self):
        return self._value


class Volume:
    Unit = Literal["ml", "l", "tbsp", "tsp"]
    def __init__(self, value, unit: Unit) -> None:
        if unit == "ml":
            self._value_ml = value
        if unit == "l":
            self._value_ml = value * 1000
        if unit == "tbsp":
            self._value_ml = value * 15
        if unit == "tsp":
            self._value_ml = value * 5

    def __call__(self, unit: Unit):
        if unit == "ml":
            return self._value_ml
        if unit == "l":
            return self("ml") / 1000
        if unit == "tbsp":
            return self("ml") / 15
        if unit == "tsp":
            return self("ml") / 5
        raise KeyError


Amount = Weight | Count | Volume


class Timespan:
    Unit = Literal["s", "m", "h"]
    def __init__(self, value, unit: Unit) -> None:
        if unit == "s":
            self._time_s = value
        if unit == "m":
            self._time_s = value * 60
        if unit == "h":
            self._time_s = value * 60 * 60

    def __call__(self, unit: Unit):
        if unit == "s":
            return self._time_s
        if unit == "m":
            return self("s") / 60
        if unit == "h":
            return self("m") / 60
        raise KeyError
