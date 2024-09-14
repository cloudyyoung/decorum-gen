from pprint import pprint
from models.house import House
from models.object import *
import random

from conditions.simple import *

house = House()
house.get_random()
print(house.get_display())
house.bathroom.wall_hanging = RedModernWallHanging()
house.bedroom.lamp = RedRetroLamp()
house.kitchen.curio = RedUnusualCurio()
house.living_room.wall_hanging = RedModernWallHanging()

conds = []
conds += generate_conditions_empty_or_not_empty(house)

conds += generate_conditions_house_contains(house)

conds += generate_conditions_only_room_empty(house)

conds += generate_conditions_no_of_empty_rooms(house)

conds += generate_conditions_contain_each_object_type(house)
conds += generate_condition_contain_each_color(house)
conds += generate_condition_contain_each_style(house)

conds += generate_conditions_not_contain_unless_repeated(house)

conds += generate_conditions_house_wall_color_match_object_color(house)

conds += generate_conditions_identical_features(house)

conds += generate_conditions_all_same(house)

conds += generate_conditions_each_of_style(house)
conds += generate_conditions_each_of_object_type(house)
conds += generate_conditions_each_of_color(house)

conds += generate_conditions_house_common_features(house)


with open("conditions.txt", "w") as f:
    f.write(house.get_display())

    f.write("\n\nConditions\n\n")
    for c in conds:
        f.write(f"({c} {c.difficulty_points} pts)\n")

# Randomly draw 12 conditions
random.shuffle(conds)
random.shuffle(conds)
random.shuffle(conds)
pprint(conds[:12])
