from abc import ABC, abstractmethod
from random import *
from typing import Iterable
from pulp import LpMaximize, LpProblem, LpVariable, lpSum

from decorum_generator.constants.quantifiers import Quantifiers
from decorum_generator.models.house import House


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


class ConditionGroup(list[Condition]):
    def pick_condition(self) -> Condition:
        return choice(self)

    def pick_conditions(self, num_of_conditions: int) -> Condition:
        return sample(self, num_of_conditions)[0]


class ConditionsGenerator(ABC):
    conditions: list[Condition | ConditionGroup] = None

    def __init__(self) -> None:
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
    def generate(self, house: House) -> None: ...

    @staticmethod
    def generate_conditions(house: House) -> list:
        subclasses = ConditionsGenerator.__subclasses__()
        print(subclasses)
        conditions = []
        for subclass in subclasses:
            generator = subclass()
            generator.generate(house)
            conditions.extend(generator.conditions)
        return conditions

    @staticmethod
    def pick_conditions(
        house: House, num_of_players: int, total_diffilculty_points: int
    ) -> list:
        conditions = ConditionsGenerator.generate_conditions(house)

        for t in range(0, num_of_players):
            knapsack_problem = LpProblem("Knapsack Problem", LpMaximize)

            # Decision variable: 0/1 for each condition selected?
            x = LpVariable.dicts("condition", conditions, 0, 1, cat="Integer")
            # Objective function: maximize total value
            knapsack_problem += (
                lpSum([x[c] * c.difficulty_points for c in conditions]),
                "Total_Difficulty_Points",
            )

            # Constraint: total difficulty points should be less than or equal to the total difficulty points
            knapsack_problem += (
                lpSum([x[c] * c.difficulty_points for c in conditions])
                <= total_diffilculty_points,
                "Total_Difficulty_Points_Constraint",
            )

            # Decision variable: number of sets
            y = LpVariable("num_of_sets", 0, cat="Integer")
            # Constraint: the number of selected conditions must be multiplier of number of players
            knapsack_problem += (
                lpSum([x[c] for c in conditions]) == y * num_of_players,
                "Number_of_Selected_Conditions_Constraint",
            )

            knapsack_problem.solve()

            selected_conditions = [c for c in conditions if x[c].value() == 1]

            return selected_conditions
