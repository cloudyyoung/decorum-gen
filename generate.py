from models.house import House
from models.object import *
from models.paint import *
from models.color import *
from models.style import *

from conditions.simple import *

house = House()
house.get_random()
print(house.get_display())

conds = generate_conditions_empty_or_not_empty(house)
print(conds)

conds = generate_conditions_the_house_contains(house)
print(conds)
