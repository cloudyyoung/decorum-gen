from abc import ABC
import random
from typing import Self
from constants.colors import Colors
from models.color import Red, Yellow, Blue, Green
from models.feature import Feature


class WallColor(Feature, ABC):
    color: Colors

    def __eq__(self, other: Self) -> bool:
        return self.color == other.color

    def __hash__(self) -> int:
        return hash(self.color)

    def __str__(self) -> str:
        return f"{self.color} wall color"

    @staticmethod
    def get_random():
        subclasses = WallColor.__subclasses__()
        subclass = random.choice(subclasses)
        return subclass()


class RedWallColor(WallColor, Red):
    color = Colors.RED


class YellowWallColor(WallColor, Yellow):
    color = Colors.YELLOW


class BlueWallColor(WallColor, Blue):
    color = Colors.BLUE


class GreenWallColor(WallColor, Green):
    color = Colors.GREEN
