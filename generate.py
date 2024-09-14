from pprint import pprint
from models.house import House
from models.object import *
from models.paint import *
from models.color import *
from models.style import *

from conditions.simple import *

house = House()
house.get_random()
print(house.get_display())

conds = []
conds += generate_conditions_empty_or_not_empty(house)

conds += generate_conditions_house_contains(house)

conds += generate_conditions_only_room_empty(house)

conds += generate_conditions_no_of_empty_rooms(house)

with open("conditions.txt", "w") as f:
    f.write(house.get_display())

    f.write("\n\nConditions\n\n")
    for c in conds:
        f.write(f"({c} {c.difficulty_points} pts)\n")
        pprint(c)
