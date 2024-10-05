from decorum_generator.conditions.conditions_generator import ConditionsGenerator
from decorum_generator.conditions.utils import format_object_text
from decorum_generator.constants.colors import Colors
from decorum_generator.constants.objects import ObjectTypes
from decorum_generator.constants.styles import Styles


class ContainsAll(ConditionsGenerator):
    def generate(self, house) -> None:
        # Each object type
        for object_type in list(ObjectTypes):
            objects = house.get_objects(object_type=object_type)
            unique_objects = set(objects)
            no_unique_objects = len(unique_objects)

            if no_unique_objects == 4:
                object_str = format_object_text(4, object_type=object_type)
                condition_str = f"The house must contain all 4 {object_str}."
                self.add_condition(condition_str, 4)

        # Each color
        for color in list(Colors):
            objects = house.get_objects(color=color)
            unique_objects = set(objects)
            no_unique_objects = len(unique_objects)

            if no_unique_objects == 3:
                object_str = format_object_text(3, color=color)
                condition_str = f"The house must contain all 3 {object_str}."
                self.add_condition(condition_str, 4)

        # Each style
        for style in list(Styles):
            objects = house.get_objects(style=style)
            unique_objects = set(objects)
            no_unique_objects = len(unique_objects)

            if no_unique_objects == 3:
                object_str = format_object_text(1, style=style)
                condition_str = (
                    f"The house must contain each {object_str} at least once."
                )
                self.add_condition(condition_str, 4)
