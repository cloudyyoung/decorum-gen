from decorum_generator.conditions.conditions_generator import ConditionsGenerator
from decorum_generator.constants.quantifiers import Quantifiers


class HouseEmptySlots(ConditionsGenerator):
    def generate(self, house) -> None:
        no_empty_slots = house.count_empty_slots()

        if no_empty_slots > 0:
            group = self.create_condition_group()

            for quantifier in list(Quantifiers):
                group.add(
                    f"The house must contain {quantifier} {no_empty_slots} empty slots.",
                    2,
                )
