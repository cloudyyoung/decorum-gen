from random import sample


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


class ConditionGroup(list[Condition | "ConditionGroup"]):
    @property
    def flattened(self) -> list[Condition]:
        conditions = []
        for condition in self:
            if isinstance(condition, "ConditionGroup"):
                conditions.extend(condition.flattened)
            else:
                conditions.append(condition)
        return conditions

    def add(self, condition_str, difficulty_points):
        self.append(Condition(condition_str, difficulty_points))

    def pick(self, num_of_conditions: int = 1) -> Condition:
        return sample(self.flattened, num_of_conditions)[0]
