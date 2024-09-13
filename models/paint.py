from abc import ABC
from models.color import Red, Yellow, Blue, Green
from models.feature import Feature


class Paint(Feature, ABC): ...


class RedPaint(Paint, Red): ...


class YellowPaint(Paint, Yellow): ...


class BluePaint(Paint, Blue): ...


class GreenPaint(Paint, Green): ...
