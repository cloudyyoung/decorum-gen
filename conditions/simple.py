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

    no_objects = house.count_objects()
    conditions.append(
        Condition(f"The house must contain at least {no_objects} objects.", 2)
    )
    conditions.append(
        Condition(f"The house must contain at most {no_objects} objects.", 2)
    )
    conditions.append(
        Condition(f"The house must contain exactly {no_objects} objects.", 2)
    )

    # colors = ["Red", "Green"]
    # for color in colors:
    #     no_objects = house.count_objects(color=color)
    #     for quantifier in ["at least", "at most", "exactly"]:
    #         conditions.append(
    #             Condition(
    #                 f"The house must contain {quantifier} {no_objects} {color.lower()} objects.",
    #                 2,
    #             )
    #         )

    return conditions
