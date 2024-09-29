from conditions.condition import ConditionsGenerator


class NoOfEmptyRooms(ConditionsGenerator):
    def generate(self, house) -> None:
        no_empty_rooms = house.count_empty_rooms()
        if no_empty_rooms > 1:
            quantifier = self.get_random_quantifier()
            condition_str = (
                f"The house must contain {quantifier} {no_empty_rooms} empty rooms."
            )
            self.add_condition(condition_str, 2)
        elif no_empty_rooms == 1:
            quantifier = self.get_random_quantifier()
            condition_str = f"The house must contain {quantifier} 1 empty room."
            self.add_condition(condition_str, 2)
        else:
            condition_str = "The house must not contain any empty rooms."
            self.add_condition(condition_str, 2)
