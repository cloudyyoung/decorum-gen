from enum import StrEnum
from random import choice


class Colors(StrEnum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"
    YELLOW = "yellow"

    def get_random():
        return choice(list(Colors))


class WarmColors:
    RED = Colors.RED
    YELLOW = Colors.YELLOW


class CoolColors:
    BLUE = Colors.BLUE
    GREEN = Colors.GREEN
