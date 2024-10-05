from decorum_generator.conditions.conditions_generator import ConditionsGenerator
from decorum_generator.conditions.utils import format_object_text, number_to_times
from decorum_generator.constants.colors import Colors
from decorum_generator.constants.objects import ObjectTypes
from decorum_generator.constants.quantifiers import Quantifiers
from decorum_generator.constants.styles import Styles
from decorum_generator.models.house import House
from decorum_generator.models.room_group import RoomGroup


class CommonFeatures(ConditionsGenerator):
    def generate(self, house) -> None:
        self.generate_common_features(house)

        for room_group in house.room_groups:
            self.generate_common_features(room_group)

    def generate_common_features(self, room_group: RoomGroup | House) -> None:
        # Each color
        for color in list(Colors):
            no_objects = room_group.count_common_objects(color=color)
            self.generate_condition_object_each_room(
                no_objects,
                room_group,
                color=color,
            )
            self.generate_condition_feature_each_room(
                no_objects,
                room_group,
                color=color,
            )

        # Each style
        for style in list(Styles):
            no_objects = room_group.count_common_objects(style=style)
            self.generate_condition_object_each_room(
                no_objects, room_group, style=style
            )

        # Each object type
        for object_type in list(ObjectTypes):
            no_objects = room_group.count_common_objects(object_type=object_type)
            self.generate_condition_object_each_room(
                no_objects,
                room_group,
                object_type=object_type,
            )

    def generate_condition_object_each_room(
        self, quantity, room_group, object_type=None, color=None, style=None
    ):
        conditions_value = [object_type, color, style].count(None)
        subject_str = format_object_text(quantity, object_type, color, style)

        if isinstance(room_group, House):
            room_group_str = "Each room"
        else:
            room_group_str = f"The {room_group}"

        if quantity > 0:
            quantifier = Quantifiers.AT_LEAST
            difficulty_points = max(1, conditions_value) + 1

            if quantity == 1 and object_type:
                condition_str = f"{room_group_str} must contain a {subject_str}."
                self.add_condition(condition_str, 1)
            elif quantity == 3:
                condition_str = f"{room_group_str} must contain no empty slot."
                self.add_condition(condition_str, 1)
            else:
                condition_str = f"{room_group_str} must contain {quantifier} {quantity} {subject_str}."
                self.add_condition(condition_str, difficulty_points)

    def generate_condition_feature_each_room(self, quantity, room_group, color):
        if isinstance(room_group, House):
            room_group_str = "Each room"
        else:
            room_group_str = f"The {room_group}"

        if quantity > 0:
            quantifier = Quantifiers.AT_LEAST
            difficulty_points = quantity

            if quantity == 1:
                condition_str = f"{room_group_str} must contain {color} (as objects and/or wall color) {quantifier} once."
                self.add_condition(condition_str, 1)
            else:
                difficulty_points += 1
                times_str = number_to_times(quantity)
                condition_str = f"{room_group_str} must contain {color} (as objects and/or wall color) {quantifier} {times_str}."
                self.add_condition(condition_str, difficulty_points)
