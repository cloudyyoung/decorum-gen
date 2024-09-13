from abc import ABC
import random
from models.color import Red, Yellow, Blue, Green
from models.feature import Feature


class Paint(Feature, ABC):
    @staticmethod 
    def get_random():
        subclasses = Paint.__subclasses__()
        subclass = random.choice(subclasses)
        return subclass()


class RedPaint(Paint, Red): ...


class YellowPaint(Paint, Yellow): ...


class BluePaint(Paint, Blue): ...


class GreenPaint(Paint, Green): ...
