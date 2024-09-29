from decorum_generator.conditions.condition import ConditionsGenerator
from decorum_generator.conditions.utils import format_object_text, number_to_times


class NotContainUnlessRepeated(ConditionsGenerator):
    def generate(self, house) -> None:
        object_counts = house.get_object_counts(include_nonexistent=True)

        for object, specific_obj_count in object_counts.items():
            # object type
            object_type_count = house.count_objects(object_type=object.object_type)
            subject_str = format_object_text(1, object_type=object.object_type)
            if object_type_count == specific_obj_count:
                self.generate_condition(specific_obj_count, subject_str)

            # color
            color_count = house.count_objects(color=object.color)
            subject_str = format_object_text(1, color=object.color)
            if color_count == specific_obj_count:
                self.generate_condition(specific_obj_count, subject_str)

            # style
            style_count = house.count_objects(style=object.style)
            subject_str = format_object_text(1, style=object.style)
            if style_count == specific_obj_count:
                self.generate_condition(specific_obj_count, subject_str)

    def generate_condition(self, count, subject_str):
        if count >= 2 and count <= 4:
            times_str = number_to_times(count)
            condition_str = f"The house must not contain a {subject_str} unless it contains that specific {subject_str} exactly {times_str}."
            self.add_condition(condition_str, 5)
        elif count == 0:
            condition_str = f"The house must not contain a {subject_str} unless it contains that specific {subject_str} exactly twice."
            self.add_condition(condition_str, 5)
