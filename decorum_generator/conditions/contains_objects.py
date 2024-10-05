from itertools import product
from decorum_generator.conditions.condition import ConditionGroup
from decorum_generator.conditions.conditions_generator import ConditionsGenerator
from decorum_generator.conditions.utils import format_object_text
from decorum_generator.constants.colors import Colors
from decorum_generator.constants.objects import ObjectTypes
from decorum_generator.constants.quantifiers import Quantifiers
from decorum_generator.constants.styles import Styles
from decorum_generator.models.house import House
from decorum_generator.models.room import Room
from decorum_generator.models.room_group import RoomGroup


class ContainsObjects(ConditionsGenerator):
    def generate(self) -> None:
        # Individual rooms
        for room in self.house.rooms:
            self.generate_room_contains(room)

        # Room groups
        for room_group in self.house.room_groups:
            self.generate_room_contains(room_group)

    def generate_room_contains(self, room: Room | RoomGroup) -> None:
        # Each color
        color_group = ConditionGroup(4)
        for color in list(Colors):
            no_objects = room.count_objects(color=color)
            group = self.generate_condition(room, no_objects, color=color)
            color_group.append(group)

        # Each style
        style_group = ConditionGroup(4)
        for style in list(Styles):
            no_objects = room.count_objects(style=style)
            group = self.generate_condition(room, no_objects, style=style)
            style_group.append(group)

        # Each object type
        object_type_group = ConditionGroup(4)
        for object_type in list(ObjectTypes):
            no_objects = room.count_objects(object_type=object_type)
            group = self.generate_condition(room, no_objects, object_type=object_type)
            object_type_group.append(group)

        # Each combination of color and style
        color_style_group = ConditionGroup(4)
        for color, style in product(list(Colors), list(Styles)):
            no_objects = room.count_objects(color=color, style=style)
            group = self.generate_condition(room, no_objects, color=color, style=style)
            color_style_group.append(group)

        # Each combination of color and object type
        color_object_type_group = ConditionGroup(4)
        for color, object_type in product(list(Colors), list(ObjectTypes)):
            no_objects = room.count_objects(color=color, object_type=object_type)
            group = self.generate_condition(
                room,
                no_objects,
                color=color,
                object_type=object_type,
            )
            color_object_type_group.append(group)

        # Each combination of style and object type
        style_object_type_group = ConditionGroup(4)
        for style, object_type in product(list(Styles), list(ObjectTypes)):
            no_objects = room.count_objects(style=style, object_type=object_type)
            group = self.generate_condition(
                room,
                no_objects,
                style=style,
                object_type=object_type,
            )
            style_object_type_group.append(group)

        # Each specific object
        color_style_object_type_group = ConditionGroup(4)
        for color, style, object_type in product(
            list(Colors), list(Styles), list(ObjectTypes)
        ):
            no_objects = room.count_objects(object_type, color, style)
            group = self.generate_condition(room, no_objects, object_type, color, style)
            color_style_object_type_group.append(group)

        parent_group = self.create_condition_group(10)
        parent_group.append(color_group)
        parent_group.append(style_group)
        parent_group.append(object_type_group)
        parent_group.append(color_style_group)
        parent_group.append(color_object_type_group)
        parent_group.append(style_object_type_group)
        parent_group.append(color_style_object_type_group)

    def generate_condition(
        self,
        room: Room | RoomGroup,
        quantity: int,
        object_type=None,
        color=None,
        style=None,
    ):
        missing_condition_components = [object_type, color, style].count(None)
        subject_str = format_object_text(quantity, object_type, color, style)

        if quantity == 0:
            group = self.generate_none_of_objects(
                room,
                subject_str,
                missing_condition_components,
            )

        else:
            group = self.generate_some_objects(
                room,
                quantity,
                subject_str,
                missing_condition_components,
            )

        return group

    def generate_none_of_objects(
        self,
        room: Room | RoomGroup,
        subject_str: str,
        missing_condition_components: int,
    ):
        group = ConditionGroup()

        is_specific_object = missing_condition_components == 0
        if is_specific_object:
            difficulty_points = 1
            condition_str = f"The {room} must not contain {subject_str}."
            group.add(condition_str, difficulty_points)
        else:
            difficulty_points = max(1, missing_condition_components)
            condition_str = f"The {room} must not contain any {subject_str}."
            group.add(condition_str, difficulty_points)

    def generate_some_objects(
        self,
        room: Room | RoomGroup,
        quantity: int,
        subject_str: str,
        missing_condition_components: int,
    ):
        group = ConditionGroup()

        is_specific_object = missing_condition_components == 0
        if is_specific_object:
            difficulty_points = 1
            condition_str = f"The {room} must contain a {subject_str}."
            group.add(condition_str, difficulty_points)
            return group

        quantifiers = list(Quantifiers)
        if isinstance(room, House):  # House only gets "at least" conditions
            quantifiers = [Quantifiers.AT_LEAST]

        for quantifier in quantifiers:
            difficulty_points = max(1, 3 - missing_condition_components)

            if quantity >= 5 and quantifier == Quantifiers.AT_LEAST:
                difficulty_points += 1
            elif quantity >= 5 and quantifier == Quantifiers.EXACTLY:
                difficulty_points += 2

            if quantifier == Quantifiers.EXACTLY:
                difficulty_points = max(2, difficulty_points)

            condition_str = (
                f"The {room} must contain {quantifier} {quantity} {subject_str}."
            )
            group.add(condition_str, difficulty_points)

        return group
