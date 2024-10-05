from itertools import combinations
from decorum_generator.conditions.conditions_generator import ConditionsGenerator


class IdenticalFeatures(ConditionsGenerator):
    def generate(self) -> None:
        has_identical_features = False

        group = self.create_condition_group()

        for room1, room2 in combinations(self.house.rooms, 2):
            if room1 == room2:
                has_identical_features = True
                condition_str = f"The {room1} and the {room2} features must be identical (same objects and wall color)."
                group.add(condition_str, 5)

        if has_identical_features:
            condition_str = "The features in any of two rooms in the house must be identical (same objects and wall color)."
            group.add(condition_str, 6)
