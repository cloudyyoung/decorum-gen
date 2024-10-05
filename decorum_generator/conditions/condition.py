from random import choice, sample


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
