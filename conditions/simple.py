from itertools import combinations, product
from random import randint
from conditions.utils import QUANTIFIERS, format_object_text, number_to_times
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

    def generate_condition(quantity, object_type=None, color=None, style=None):
        conditions_value = [object_type, color, style].count(None)
        subject_str = format_object_text(quantity, object_type, color, style)

        if quantity == 0:
            if conditions_value == 0:
                difficulty_points = 1
                condition_str = f"The {room} must not contain {subject_str}."
            else:
                difficulty_points = max(1, conditions_value + 1)
                condition_str = f"The {room} must not contain any {subject_str}."
            condition = Condition(condition_str, difficulty_points)
            conditions.append(condition)
        else:
            if isinstance(room, House):
                quantifier = "at least"
            else:
                quantifier = QUANTIFIERS[randint(0, 2)]

            if conditions_value == 0:
                difficulty_points = 1
                condition_str = f"The {room} must contain a {subject_str}."
            else:
                difficulty_points = max(1, 3 - conditions_value)

                if quantity >= 5 and quantifier == "at least":
                    difficulty_points += 1

                if quantity >= 5 and quantifier == "exactly":
                    difficulty_points += 2

                if quantifier == "exactly":
                    difficulty_points = max(2, difficulty_points)

                condition_str = (
                    f"The {room} must contain {quantifier} {quantity} {subject_str}."
                )
            condition = Condition(condition_str, difficulty_points)
            conditions.append(condition)

    # generate_condition(room.count_objects())

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
        conditions.append(Condition(condition_str, 5))

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
        if randint(0, 1):
            times_str = number_to_times(smallest_no)
            condition_str = f"The house must contain each color at least {times_str}."
        else:
            subject_str = format_object_text(smallest_no)
            condition_str = f"The house must contain at least {smallest_no} {subject_str} of each color."
        conditions.append(Condition(condition_str, 3))

    if largest_no > 0:
        subject_str = format_object_text(largest_no)
        condition_str = (
            f"The house must contain at most {largest_no} {subject_str} of each color."
        )
        conditions.append(Condition(condition_str, 3))

    if no_red == no_green == no_blue == no_yellow:
        condition_str = "The house must contain the same number of each color."
        conditions.append(Condition(condition_str, 4))

        subject_str = format_object_text(no_red)
        condition_str = (
            f"The house must contain exactly {no_red} {subject_str} of each color."
        )
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


def generate_conditions_house_wall_color_match_object_color(house: House):
    conditions: list[Condition] = []
    for room in house.rooms:
        conditions += generate_conditions_room_wall_color_match_object_color(room)
    for room_group in house.room_groups:
        conditions += generate_conditions_room_wall_color_match_object_color(room_group)
    return conditions


def generate_conditions_room_wall_color_match_object_color(room: Room | RoomGroup):
    conditions: list[Condition] = []

    if isinstance(room, RoomGroup) and not room.is_identical_wall_colors():
        return conditions

    if isinstance(room, RoomGroup):
        wall_color = room.rooms[0].wall_color
        suffix = "s"
    else:
        wall_color = room.wall_color
        suffix = ""

    matching_objects = room.get_objects(color=wall_color)
    no_matching_objects = len(matching_objects)
    no_room_objects = room.count_objects()

    if no_matching_objects == no_room_objects:
        condition_str = f"The wall color{suffix} of the {room} must match the color of all the objects in the room{suffix}."
        conditions.append(Condition(condition_str, 4))
    elif no_matching_objects >= 1:
        condition_str = f"The wall color{suffix} of the {room} must match the color of one of the objects in the room{suffix}."
        conditions.append(Condition(condition_str, 3))

    if no_matching_objects >= 1:
        for matching_obj in matching_objects:
            subject_str = format_object_text(2, object_type=matching_obj.object_type)
            condition_str = f"The wall color{suffix} of the {room} must match the color of the {subject_str} in the room{suffix}."
            conditions.append(Condition(condition_str, 3))

            subject_str = format_object_text(2, style=matching_obj.style)
            condition_str = f"The wall color{suffix} of the {room} must match the color of one of the {subject_str} in the room{suffix}."
            conditions.append(Condition(condition_str, 4))

    return conditions


def generate_conditions_identical_features(house: House):
    conditions: list[Condition] = []

    for room1, room2 in combinations(house.rooms, 2):
        if room1 == room2:
            condition_str = f"The {room1} and the {room2} features must be identical (same objects and wall color)."
            conditions.append(Condition(condition_str, 6))

    # TODO: "The features in any of two rooms must be identical (same objects and wall color)", 7

    return conditions


def generate_conditions_all_same(house: House):
    conditions: list[Condition] = []

    for room in house.rooms:
        no_room_objects = room.count_objects()

        if room.is_identical_object_colors() and room.is_identical_object_styles():
            condition_str = (
                f"Objects in the {room} must all have the same color and style."
            )
            conditions.append(Condition(condition_str, 1 + no_room_objects))
        elif room.is_identical_object_colors():
            condition_str = f"Objects in the {room} must all have the same color."
            conditions.append(Condition(condition_str, 1 + no_room_objects))
        elif room.is_identical_object_styles():
            condition_str = f"Objects in the {room} must all have the same style."
            conditions.append(Condition(condition_str, 1 + no_room_objects))
        elif room.is_identical_colors():
            condition_str = (
                f"Objects and wall color in the {room} must all have the same color."
            )
            conditions.append(Condition(condition_str, 1 + no_room_objects))

    return conditions


def generate_conditions_each_of_style(house: House):
    conditions: list[Condition] = []

    for style in list(Styles):
        objects = house.get_objects(style=style)
        objects = set(objects)

        if len(objects) == 3:
            object_str = format_object_text(1, style=style)
            condition_str = f"The house must contain each {object_str} at least once."
            conditions.append(Condition(condition_str, 4))

    return conditions


def generate_conditions_each_of_object_type(house: House):
    conditions: list[Condition] = []

    for object_type in list(ObjectTypes):
        objects = house.get_objects(object_type=object_type)
        objects = set(objects)

        if len(objects) == 4:
            object_str = format_object_text(4, object_type=object_type)
            condition_str = f"The house must contain all 4 {object_str}."
            conditions.append(Condition(condition_str, 4))

    return conditions


def generate_conditions_each_of_color(house: House):
    conditions: list[Condition] = []

    for color in list(Colors):
        objects = house.get_objects(color=color)
        objects = set(objects)

        if len(objects) == 3:
            object_str = format_object_text(3, color=color)
            condition_str = f"The house must contain all 3 {object_str}."
            conditions.append(Condition(condition_str, 4))

    return conditions


def generate_conditions_house_common_features(house: House):
    conditions: list[Condition] = []
    conditions += generate_conditions_common_feature_each_room(house)
    for room_group in house.room_groups:
        conditions += generate_conditions_common_feature_each_room(room_group)
    return conditions


def generate_conditions_common_feature_each_room(room_group: House | RoomGroup):
    conditions: list[Condition] = []

    def generate_condition_object_each_room(
        quantity, object_type=None, color=None, style=None
    ):
        conditions_value = [object_type, color, style].count(None)
        subject_str = format_object_text(quantity, object_type, color, style)

        if isinstance(room_group, House):
            room_group_str = "Each room"
        else:
            room_group_str = f"The {room_group}"

        if quantity == 0:
            # TODO: Add condition statement here
            ...
        else:
            quantifier = QUANTIFIERS[0]
            difficulty_points = max(1, conditions_value) + 1

            if quantity == 1 and object_type:
                condition_str = f"{room_group_str} must contain a {subject_str}."
                conditions.append(Condition(condition_str, 1))
            elif quantity == 3:
                condition_str = f"{room_group_str} must contain no empty slot."
                conditions.append(Condition(condition_str, 1))
            else:
                condition_str = f"{room_group_str} must contain {quantifier} {quantity} {subject_str}."
                condition = Condition(condition_str, difficulty_points)
                conditions.append(condition)

    def generate_condition_feature_each_room(quantity, color):
        if isinstance(room_group, House):
            room_group_str = "Each room"
        else:
            room_group_str = f"The {room_group}"

        if quantity == 0:
            ...
        else:
            quantifier = QUANTIFIERS[0]
            difficulty_points = quantity

            if quantity == 1:
                condition_str = f"{room_group_str} must contain {color} (as objects and/or wall color) {quantifier} once."
                conditions.append(Condition(condition_str, difficulty_points))
            else:
                difficulty_points += 1
                times_str = number_to_times(quantity)
                condition_str = f"{room_group_str} must contain {color} (as objects and/or wall color) {quantifier} {times_str}."
                condition = Condition(condition_str, difficulty_points)
                conditions.append(condition)

    # generate_condition_each_room(room_group.count_common_objects())

    for color in list(Colors):
        no_objects = room_group.count_common_objects(color=color)
        generate_condition_object_each_room(no_objects, color=color)
        generate_condition_feature_each_room(no_objects, color=color)

    for style in list(Styles):
        no_objects = room_group.count_common_objects(style=style)
        generate_condition_object_each_room(no_objects, style=style)

    for object_type in list(ObjectTypes):
        no_objects = room_group.count_common_objects(object_type=object_type)
        generate_condition_object_each_room(no_objects, object_type=object_type)

    # Remove duplicates in conditions
    conditions = list(set(conditions))
    return conditions
