from abc import ABC, abstractmethod
from random import *

from constants.quantifiers import Quantifiers
from models.house import House


class Condition:
    def __init__(self, condition: str, difficulty_points: int):
        self.condition = condition
        self.difficulty_points = difficulty_points

    def __str__(self):
        return self.condition

    def __repr__(self):
        return f"({self.condition} {self.difficulty_points} pts)"

    def __hash__(self):
        return hash(self.condition)

    def __eq__(self, other: object):
        if not other or not isinstance(other, Condition):
            return False
        return self.condition == other.condition


class ConditionsGenerator(ABC):
    conditions: list[Condition] = None

    def __init__(self) -> None:
        self.conditions = []

    def add_condition(self, condition_string: str, difficulty_points: int) -> None:
        self.conditions.append(Condition(condition_string, difficulty_points))

    def get_random_quantifier(self) -> Quantifiers:
        return choice(list(Quantifiers))

    @abstractmethod
    def generate(self, house: House) -> None: ...
