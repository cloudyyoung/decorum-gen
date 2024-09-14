from itertools import product
from random import randint
from conditions.utils import format_object_text, number_to_times
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
    quantifiers = ["at least", "at most", "exactly"]

    def generate_condition(quantity, object_type=None, color=None, style=None):
        conditions_value = [object_type, color, style].count(None)
        subject_str = format_object_text(quantity, object_type, color, style)

        if quantity == 0:
            difficulty_points = max(1, conditions_value + 1)
            condition_str = f"The {room} must not contain any {subject_str}."
            condition = Condition(condition_str, difficulty_points)
            conditions.append(condition)
        else:
            quantifier = quantifiers[randint(0, 2)]
            difficulty_points = max(1, 3 - conditions_value)

            if conditions_value == 0:
                difficulty_points = 1
                condition_str = f"The {room} must contain a {subject_str}."
            else:
                if quantifier == "exactly":
                    difficulty_points = max(2, difficulty_points)
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

    quantifiers = ["at least", "at most", "exactly"]
    no_empty_rooms = house.count_empty()
    if no_empty_rooms > 1:
        quantifier = quantifiers[randint(0, 2)]
        condition_str = (
            f"The house must contain {quantifier} {no_empty_rooms} empty rooms."
        )
        conditions.append(Condition(condition_str, 2))
    elif no_empty_rooms == 1:
        quantifier = quantifiers[randint(0, 2)]
        condition_str = f"The house must contain {quantifier} 1 empty room."
        conditions.append(Condition(condition_str, 2))
    else:
        conditions.append(Condition("The house must not contain any empty rooms.", 2))

    return conditions


def generate_conditions_contain_each_object_type(house: House):
    conditions: list[Condition] = []

    no_wall_hanging = house.count_objects(object_type=ObjectTypes.WALL_HANGING)
    no_lamp = house.count_objects(object_type=ObjectTypes.LAMP)
    no_curio = house.count_objects(object_type=ObjectTypes.CURIO)

    smallest_no = min(no_wall_hanging, no_lamp, no_curio)
    largest_no = max(no_wall_hanging, no_lamp, no_curio)

    if smallest_no > 0:
        condition_str = (
            f"The house must contain at least {smallest_no} of each object type."
        )
        conditions.append(Condition(condition_str, 3))

    if largest_no > 0:
        condition_str = (
            f"The house must contain at most {largest_no} of each object type."
        )
        conditions.append(Condition(condition_str, 3))

    if no_wall_hanging == no_lamp == no_curio:
        condition_str = "The house must contain the same number of each object type."
        conditions.append(Condition(condition_str, 4))

        condition_str = (
            f"The house must contain exactly {no_wall_hanging} of each object type."
        )
        conditions.append(Condition(condition_str, 3))

    return conditions


def generate_condition_contain_each_color(house: House):
    conditions: list[Condition] = []

    no_red = house.count_objects(color=Colors.RED)
    no_green = house.count_objects(color=Colors.GREEN)
    no_blue = house.count_objects(color=Colors.BLUE)
    no_yellow = house.count_objects(color=Colors.YELLOW)

    smallest_no = min(no_red, no_green, no_blue, no_yellow)
    largest_no = max(no_red, no_green, no_blue, no_yellow)

    if smallest_no > 0:
        condition_str = f"The house must contain at least {smallest_no} of each color."
        conditions.append(Condition(condition_str, 3))

    if largest_no > 0:
        condition_str = f"The house must contain at most {largest_no} of each color."
        conditions.append(Condition(condition_str, 3))

    if no_red == no_green == no_blue == no_yellow:
        condition_str = "The house must contain the same number of each color."
        conditions.append(Condition(condition_str, 4))

        condition_str = f"The house must contain exactly {no_red} of each color."
        conditions.append(Condition(condition_str, 3))

    return conditions


def generate_condition_contain_each_style(house: House):
    conditions: list[Condition] = []

    no_modern = house.count_objects(style=Styles.MODERN)
    no_antique = house.count_objects(style=Styles.ANTIQUE)
    no_retro = house.count_objects(style=Styles.RETRO)
    no_unusual = house.count_objects(style=Styles.UNUSUAL)

    smallest_no = min(no_modern, no_antique, no_retro, no_unusual)
    largest_no = max(no_modern, no_antique, no_retro, no_unusual)

    if smallest_no > 0:
        condition_str = f"The house must contain at least {smallest_no} of each style."
        conditions.append(Condition(condition_str, 4))

    if largest_no > 0:
        condition_str = f"The house must contain at most {largest_no} of each style."
        conditions.append(Condition(condition_str, 4))

    if no_modern == no_antique == no_retro == no_unusual:
        condition_str = "The house must contain the same number of each style."
        conditions.append(Condition(condition_str, 5))

        condition_str = f"The house must contain exactly {no_modern} of each style."
        conditions.append(Condition(condition_str, 4))

    return conditions


def generate_conditions_not_contain_unless_repeated(house: House):
    conditions: list[Condition] = []

    def generate_condition(count, subject_str):
        if count >= 2 and count <= 4:
            times_str = number_to_times(count)
            condition_str = f"The house must not contain a {subject_str} unless it contains that specific {subject_str} exactly {times_str}."
            conditions.append(Condition(condition_str, 5))
        elif count == 0:
            condition_str = f"The house must not contain a {subject_str} unless it contains that specific {subject_str} exactly twice."
            conditions.append(Condition(condition_str, 5))

    object_counts = house.get_object_counts(include_nonexistent=True)

    for object, specific_obj_count in object_counts.items():
        # object type
        object_type_count = house.count_objects(object_type=object.object_type)
        subject_str = format_object_text(1, object_type=object.object_type)
        if object_type_count == specific_obj_count:
            generate_condition(specific_obj_count, subject_str)

        # color
        color_count = house.count_objects(color=object.color)
        subject_str = format_object_text(1, color=object.color)
        if color_count == specific_obj_count:
            generate_condition(specific_obj_count, subject_str)

        # style
        style_count = house.count_objects(style=object.style)
        subject_str = format_object_text(1, style=object.style)
        if style_count == specific_obj_count:
            generate_condition(specific_obj_count, subject_str)

    # Remove duplicates in conditions
    conditions = list(set(conditions))
    return conditions
