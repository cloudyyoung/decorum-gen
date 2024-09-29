from itertools import combinations
from decorum_generator.conditions.condition import ConditionsGenerator


class IdenticalFeatures(ConditionsGenerator):
    def generate(self, house) -> None:
        has_identical_features = False

        for room1, room2 in combinations(house.rooms, 2):
            if room1 == room2:
                has_identical_features = True
                condition_str = f"The {room1} and the {room2} features must be identical (same objects and wall color)."
                self.add_condition(condition_str, 5)

        if has_identical_features:
            condition_str = "The features in any of two rooms in the house must be identical (same objects and wall color)."
            self.add_condition(condition_str, 6)
