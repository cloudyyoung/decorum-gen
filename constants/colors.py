from enum import StrEnum


class Colors(StrEnum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"
    YELLOW = "yellow"


class WarmColors:
    RED = Colors.RED
    YELLOW = Colors.YELLOW


class CoolColors:
    BLUE = Colors.BLUE
    GREEN = Colors.GREEN
