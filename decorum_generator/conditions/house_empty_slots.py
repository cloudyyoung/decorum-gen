from decorum_generator.conditions.conditions_generator import ConditionsGenerator
from decorum_generator.conditions.utils import QUANTIFIERS


class HouseEmptySlots(ConditionsGenerator):
    def generate(self, house) -> None:
        no_empty_slots = house.count_empty_slots()

        if no_empty_slots > 0:
            quantifier = QUANTIFIERS[2]
            self.add_condition(
                f"The house must contain {quantifier} {no_empty_slots} empty slots.",
                2,
            )
