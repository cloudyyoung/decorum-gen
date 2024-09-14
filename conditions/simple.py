from itertools import product
from constants.objects import ObjectTypes
from constants.styles import Styles
from models.color import *
from models.house import House
from conditions.condition import Condition


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


def generate_conditions_the_house_contains(house: House):
    conditions: list[Condition] = []
    QUANTIFIERS = ["at least", "at most", "exactly"]

    no_objects = house.count_objects()
    for quantifier in QUANTIFIERS:
        conditions.append(
            Condition(f"The house must contain {quantifier} {no_objects} objects.", 1)
        )

    for color in list(Colors):
        no_objects = house.count_objects(color=color)
        for quantifier in QUANTIFIERS:
            conditions.append(
                Condition(
                    f"The house must contain {quantifier} {no_objects} {color} objects.",
                    2,
                )
            )

    for style in list(Styles):
        no_objects = house.count_objects(style=style)
        for quantifier in QUANTIFIERS:
            conditions.append(
                Condition(
                    f"The house must contain {quantifier} {no_objects} {style} objects.",
                    2,
                )
            )

    for object_type in list(ObjectTypes):
        no_objects = house.count_objects(object_type=object_type)
        for quantifier in QUANTIFIERS:
            conditions.append(
                Condition(
                    f"The house must contain {quantifier} {no_objects} {object_type}(s).",
                    2,
                )
            )

    for color, style in zip(list(Colors), list(Styles)):
        no_objects = house.count_objects(color=color, style=style)
        for quantifier in QUANTIFIERS:
            conditions.append(
                Condition(
                    f"The house must contain {quantifier} {no_objects} {color} {style} objects.",
                    2,
                )
            )

    for color, object_type in zip(list(Colors), list(ObjectTypes)):
        no_objects = house.count_objects(color=color, object_type=object_type)
        for quantifier in QUANTIFIERS:
            conditions.append(
                Condition(
                    f"The house must contain {quantifier} {no_objects} {color} {object_type}(s).",
                    2,
                )
            )

    for style, object_type in product(list(Styles), list(ObjectTypes)):
        no_objects = house.count_objects(style=style, object_type=object_type)
        for quantifier in QUANTIFIERS:
            conditions.append(
                Condition(
                    f"The house must contain {quantifier} {no_objects} {style} {object_type}(s).",
                    2,
                )
            )

    for color, style, object_type in product(
        list(Colors), list(Styles), list(ObjectTypes)
    ):
        no_objects = house.count_objects(
            color=color, style=style, object_type=object_type
        )
        for quantifier in QUANTIFIERS:
            conditions.append(
                Condition(
                    f"The house must contain {quantifier} {no_objects} {color} {style} {object_type}(s).",
                    3,
                )
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
