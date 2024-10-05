from itertools import product
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
    def generate(self, house: House) -> None:
        # Individual rooms
        for room in house.rooms:
            self.generate_room_contains(room)

        # Room groups
        for room_group in house.room_groups:
            self.generate_room_contains(room_group)

    def generate_room_contains(self, room: Room | RoomGroup) -> None:
        # Each color
        for color in list(Colors):
            no_objects = room.count_objects(color=color)
            self.generate_condition(room, no_objects, color=color)

        # Each style
        for style in list(Styles):
            no_objects = room.count_objects(style=style)
            self.generate_condition(room, no_objects, style=style)

        # Each object type
        for object_type in list(ObjectTypes):
            no_objects = room.count_objects(object_type=object_type)
            self.generate_condition(room, no_objects, object_type=object_type)

        # Each combination of color and style
        for color, style in product(list(Colors), list(Styles)):
            no_objects = room.count_objects(color=color, style=style)
            self.generate_condition(room, no_objects, color=color, style=style)

        # Each combination of color and object type
        for color, object_type in product(list(Colors), list(ObjectTypes)):
            no_objects = room.count_objects(color=color, object_type=object_type)
            self.generate_condition(
                room,
                no_objects,
                color=color,
                object_type=object_type,
            )

        # Each combination of style and object type
        for style, object_type in product(list(Styles), list(ObjectTypes)):
            no_objects = room.count_objects(style=style, object_type=object_type)
            self.generate_condition(
                room,
                no_objects,
                style=style,
                object_type=object_type,
            )

        # Each specific object
        for color, style, object_type in product(
            list(Colors), list(Styles), list(ObjectTypes)
        ):
            no_objects = room.count_objects(object_type, color, style)
            self.generate_condition(no_objects, room, object_type, color, style)

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
            self.generate_none_of_objects(
                room,
                subject_str,
                missing_condition_components,
            )

        else:
            self.generate_some_objects(
                room,
                quantity,
                subject_str,
                missing_condition_components,
            )

    def generate_none_of_objects(
        self,
        room: Room | RoomGroup,
        subject_str: str,
        missing_condition_components: int,
    ):
        is_specific_object = missing_condition_components == 0
        if is_specific_object:
            difficulty_points = 1
            condition_str = f"The {room} must not contain {subject_str}."
            self.add_condition(condition_str, difficulty_points)
            return

        difficulty_points = max(1, missing_condition_components)
        condition_str = f"The {room} must not contain any {subject_str}."
        self.add_condition(condition_str, difficulty_points)

    def generate_some_objects(
        self,
        room: Room | RoomGroup,
        quantity: int,
        subject_str: str,
        missing_condition_components: int,
    ):
        is_specific_object = missing_condition_components == 0
        if is_specific_object:
            difficulty_points = 1
            condition_str = f"The {room} must contain a {subject_str}."
            self.add_condition(condition_str, difficulty_points)
            return

        if isinstance(room, House):
            # House only gets "at least" conditions
            quantifier = Quantifiers.AT_LEAST
        else:
            quantifier = self.get_random_quantifier()

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
        self.add_condition(condition_str, difficulty_points)
