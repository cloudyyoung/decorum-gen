from abc import ABC

from decorum_generator.constants.colors import Colors


class Color(ABC): ...


class Red(Color, ABC):
    color = Colors.RED


class Yellow(Color, ABC):
    color = Colors.YELLOW


class Blue(Color, ABC):
    color = Colors.BLUE


class Green(Color, ABC):
    color = Colors.GREEN
