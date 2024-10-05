from decorum_generator.conditions.conditions_generator import ConditionsGenerator
from decorum_generator.conditions.utils import format_object_text, number_to_times
from decorum_generator.constants.colors import Colors
from decorum_generator.constants.objects import ObjectTypes
from decorum_generator.constants.styles import Styles
from decorum_generator.models.house import House


class ContainsKinds(ConditionsGenerator):
    def generate(self, house: House) -> None:
        self.generate_object_types(house)
        self.generate_colors(house)
        self.generate_styles(house)

    def generate_object_types(self, house: House) -> None:
        no_wall_hanging = house.count_objects(object_type=ObjectTypes.WALL_HANGING)
        no_lamp = house.count_objects(object_type=ObjectTypes.LAMP)
        no_curio = house.count_objects(object_type=ObjectTypes.CURIO)

        smallest_no = min(no_wall_hanging, no_lamp, no_curio)
        largest_no = max(no_wall_hanging, no_lamp, no_curio)

        if smallest_no > 0:
            condition_str = (
                f"The house must contain at least {smallest_no} of each object type."
            )
            self.add_condition(condition_str, 3)

        if largest_no > 0:
            condition_str = (
                f"The house must contain at most {largest_no} of each object type."
            )
            self.add_condition(condition_str, 3)

        # Same number of each object type
        if no_wall_hanging == no_lamp == no_curio:
            condition_str = (
                "The house must contain the same number of each object type."
            )
            self.add_condition(condition_str, 5)

            condition_str = (
                f"The house must contain exactly {no_wall_hanging} of each object type."
            )
            self.add_condition(condition_str, 3)

    def generate_colors(self, house: House) -> None:
        no_red = house.count_objects(color=Colors.RED)
        no_green = house.count_objects(color=Colors.GREEN)
        no_blue = house.count_objects(color=Colors.BLUE)
        no_yellow = house.count_objects(color=Colors.YELLOW)

        smallest_no = min(no_red, no_green, no_blue, no_yellow)
        largest_no = max(no_red, no_green, no_blue, no_yellow)

        if smallest_no > 0:
            if smallest_no <= 2:  # Once and Twice
                times_str = number_to_times(smallest_no)
                condition_str = (
                    f"The house must contain each color at least {times_str}."
                )
                self.add_condition(condition_str, 3)
            else:  # 3 times or more
                subject_str = format_object_text(smallest_no)
                condition_str = f"The house must contain at least {smallest_no} {subject_str} of each color."
                self.add_condition(condition_str, 3)

        if largest_no > 0:
            subject_str = format_object_text(largest_no)
            condition_str = f"The house must contain at most {largest_no} {subject_str} of each color."
            self.add_condition(condition_str, 3)

        if no_red == no_green == no_blue == no_yellow:
            condition_str = "The house must contain the same number of each color."
            self.add_condition(condition_str, 4)

            subject_str = format_object_text(no_red)
            condition_str = (
                f"The house must contain exactly {no_red} {subject_str} of each color."
            )
            self.add_condition(condition_str, 3)

    def generate_styles(self, house: House) -> None:
        no_modern = house.count_objects(style=Styles.MODERN)
        no_antique = house.count_objects(style=Styles.ANTIQUE)
        no_retro = house.count_objects(style=Styles.RETRO)
        no_unusual = house.count_objects(style=Styles.UNUSUAL)

        smallest_no = min(no_modern, no_antique, no_retro, no_unusual)
        largest_no = max(no_modern, no_antique, no_retro, no_unusual)

        if smallest_no > 0:
            condition_str = (
                f"The house must contain at least {smallest_no} of each style."
            )
            self.add_condition(condition_str, 4)

        if largest_no > 0:
            condition_str = (
                f"The house must contain at most {largest_no} of each style."
            )
            self.add_condition(condition_str, 4)

        if no_modern == no_antique == no_retro == no_unusual:
            condition_str = "The house must contain the same number of each style."
            self.add_condition(condition_str, 5)

            condition_str = f"The house must contain exactly {no_modern} of each style."
            self.add_condition(condition_str, 4)
