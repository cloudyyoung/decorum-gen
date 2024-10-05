from abc import ABC, abstractmethod
from random import choice
from typing import Iterable
from decorum_generator.conditions.condition import Condition, ConditionGroup
from decorum_generator.constants.quantifiers import Quantifiers
from decorum_generator.models.house import House


class ConditionsGenerator(ABC):
    house: House
    conditions: list[Condition | ConditionGroup]

    def __init__(self, house: House) -> None:
        self.house = house
        self.conditions = []

    def add_condition(self, condition_string: str, difficulty_points: int) -> None:
        """
        Add a single condition to the conditions list
        """
        self.conditions.append(Condition(condition_string, difficulty_points))

    def add_conditions(self, *conditions: tuple[str, int]) -> None:
        """
        Add multiple conditions to the conditions list as a condition group
        """
        condition_group = ConditionGroup()

        for condition, difficulty_points in conditions:
            condition_group.append(Condition(condition, difficulty_points))

        if len(condition_group) > 0:
            self.conditions.append(condition_group)

    def add_condition_group(
        self, condition_group: ConditionGroup | Iterable[tuple[str, int]]
    ) -> None:
        """
        Add a condition group to the conditions list, or a list of conditions as a condition group
        """
        if isinstance(condition_group, ConditionGroup):
            self.conditions.append(condition_group)

        condition_group = ConditionGroup()

        for condition, difficulty_points in condition_group:
            condition_group.append(Condition(condition, difficulty_points))

        if len(condition_group) > 0:
            self.conditions.append(condition_group)

    def get_random_quantifier(self) -> Quantifiers:
        return choice(list(Quantifiers))

    @abstractmethod
    def generate(self) -> None: ...

    @abstractmethod
    def pick(self) -> list[Condition]: ...
