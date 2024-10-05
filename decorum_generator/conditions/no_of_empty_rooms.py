from decorum_generator.conditions.conditions_generator import ConditionsGenerator
from decorum_generator.constants.quantifiers import Quantifiers


class NoOfEmptyRooms(ConditionsGenerator):
    def generate(self) -> None:
        no_empty_rooms = self.house.count_empty_rooms()

        if no_empty_rooms > 1:
            group = self.create_condition_group()
            for quantifier in list(Quantifiers):
                condition_str = (
                    f"The house must contain {quantifier} {no_empty_rooms} empty rooms."
                )
                group.add(condition_str, 2)
        elif no_empty_rooms == 1:
            group = self.create_condition_group()
            for quantifier in list(Quantifiers):
                condition_str = f"The house must contain {quantifier} 1 empty room."
                group.add(condition_str, 2)
        else:
            condition_str = "The house must not contain any empty rooms."
            self.add_condition(condition_str, 2)
