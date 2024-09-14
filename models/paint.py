from abc import ABC
import random
from typing import Self
from constants.colors import Colors
from models.color import Red, Yellow, Blue, Green
from models.feature import Feature


class Paint(Feature, ABC):
    color: Colors = None

    def __eq__(self, other: Self) -> bool:
        return self.color == other.color

    @staticmethod
    def get_random():
        subclasses = Paint.__subclasses__()
        subclass = random.choice(subclasses)
        return subclass()


class RedPaint(Paint, Red):
    color = Colors.RED


class YellowPaint(Paint, Yellow):
    color = Colors.YELLOW


class BluePaint(Paint, Blue):
    color = Colors.BLUE


class GreenPaint(Paint, Green):
    color = Colors.GREEN
