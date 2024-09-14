from models.house import House
from conditions.condition import Condition


def generate_conditions_empty_or_not_empty(house: House):
    conditions: list[Condition] = []

    # Bedroom
    if house.bedroom.count_objects() > 0:
        conditions.append(Condition("The bedroom must not be empty.", 1))
    else:
        conditions.append(Condition("The bedroom must be empty.", 1))

    # Bathroom
    if house.bathroom.count_objects() > 0:
        conditions.append(Condition("The bathroom must not be empty.", 1))
    else:
        conditions.append(Condition("The bathroom must be empty.", 1))

    # Living Room
    if house.living_room.count_objects() > 0:
        conditions.append(Condition("The living room must not be empty.", 1))
    else:
        conditions.append(Condition("The living room must be empty.", 1))

    # Kitchen
    if house.kitchen.count_objects() > 0:
        conditions.append(Condition("The kitchen must not be empty.", 1))
    else:
        conditions.append(Condition("The kitchen must be empty.", 1))

    # Upstairs
    if house.upstairs.count_objects() > 0:
        conditions.append(Condition("The upstairs must not be empty.", 1))
    else:
        conditions.append(Condition("The upstairs must be empty.", 1))

    # Downstairs
    if house.downstairs.count_objects() > 0:
        conditions.append(Condition("The downstairs must not be empty.", 1))
    else:
        conditions.append(Condition("The downstairs must be empty.", 1))

    return conditions


def generate_conditions_the_house_contains(house: House):
    conditions: list[Condition] = []

    

    return conditions
