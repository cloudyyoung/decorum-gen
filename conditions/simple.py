from itertools import product
from conditions.utils import format_object_text
from constants.objects import ObjectTypes
from constants.styles import Styles
from models.color import *
from models.house import House
from conditions.condition import Condition
from models.room import Room
from models.room_group import RoomGroup


def generate_conditions_empty_or_not_empty(house: House):
    conditions: list[Condition] = []

    for room in house.rooms:
        if room.count_objects() > 0:
            conditions.append(Condition(f"The {room} must not be empty.", 1))
        else:
            conditions.append(Condition(f"The {room} must be empty.", 1))

    for room_group in house.room_groups:
        if room_group.count_objects() > 0:
            conditions.append(Condition(f"The {room_group} must not be empty.", 1))
        else:
            conditions.append(Condition(f"The {room_group} must be empty.", 1))

    return conditions


def generate_conditions_house_contains(house: House):
    conditions = []
    conditions += generate_conditions_room_contains(house)
    for room in house.rooms:
        conditions += generate_conditions_room_contains(room)
    for room_group in house.room_groups:
        conditions += generate_conditions_room_contains(room_group)
    return conditions


def generate_conditions_room_contains(room: Room | RoomGroup):
    conditions: list[Condition] = []
    QUANTIFIERS = ["at least", "at most", "exactly"]

    def generate_condition(quantity, object_type=None, color=None, style=None):
        conditions_value = [object_type, color, style].count(None)
        difficulty_points = max(1, 3 - conditions_value)
        subject_str = format_object_text(quantity, object_type, color, style)

        if quantity == 0:
            condition_str = f"The {room} must contain no {subject_str}."
            condition = Condition(condition_str, difficulty_points)
            conditions.append(condition)
        else:
            for quantifier in QUANTIFIERS:
                condition_str = (
                    f"The {room} must contain {quantifier} {quantity} {subject_str}."
                )
                condition = Condition(condition_str, difficulty_points)
                conditions.append(condition)

    generate_condition(room.count_objects())

    for color in list(Colors):
        no_objects = room.count_objects(color=color)
        generate_condition(no_objects, color=color)

    for style in list(Styles):
        no_objects = room.count_objects(style=style)
        generate_condition(no_objects, style=style)

    for object_type in list(ObjectTypes):
        no_objects = room.count_objects(object_type=object_type)
        generate_condition(no_objects, object_type=object_type)

    for color, style in product(list(Colors), list(Styles)):
        no_objects = room.count_objects(color=color, style=style)
        generate_condition(no_objects, color=color, style=style)

    for color, object_type in product(list(Colors), list(ObjectTypes)):
        no_objects = room.count_objects(color=color, object_type=object_type)
        generate_condition(no_objects, color=color, object_type=object_type)

    for style, object_type in product(list(Styles), list(ObjectTypes)):
        no_objects = room.count_objects(style=style, object_type=object_type)
        generate_condition(no_objects, style=style, object_type=object_type)

    for color, style, object_type in product(
        list(Colors), list(Styles), list(ObjectTypes)
    ):
        no_objects = room.count_objects(
            color=color, style=style, object_type=object_type
        )
        generate_condition(
            no_objects, color=color, style=style, object_type=object_type
        )
    return conditions


def generate_conditions_only_room_empty(house: House):
    conditions: list[Condition] = []

    no_empty_rooms = house.count_empty()
    if no_empty_rooms == 1:
        # Find the empty room
        empty_room = None
        for room in house.rooms:
            if room.is_empty():
                empty_room = room
                break

        conditions.append(
            Condition(f"The {empty_room} must be the only empty room.", 2)
        )

    return conditions


def generate_conditions_no_of_empty_rooms(house: House):
    conditions: list[Condition] = []

    no_empty_rooms = house.count_empty()
    if no_empty_rooms > 0:
        conditions.append(
            Condition(
                f"The house must contain at least {no_empty_rooms} empty rooms.", 2
            )
        )
        conditions.append(
            Condition(
                f"The house must contain at most {no_empty_rooms} empty rooms.", 2
            )
        )
        conditions.append(
            Condition(
                f"The house must contain exactly {no_empty_rooms} empty rooms.", 2
            )
        )
    else:
        conditions.append(Condition("The house must not contain any empty rooms.", 2))

    return conditions
