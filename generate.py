from models.house import House
from models.object import *
from models.paint import *
from models.color import *
from models.style import *

house = House.get_random()
print(house.get_display())
