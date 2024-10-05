from pprint import pprint
from decorum_generator.conditions.conditions_generator import ConditionsGenerator
from decorum_generator.models.house import House
from decorum_generator.models.object import *
import random

# random.seed(123)


def test_any():
    house = House()
    house.randomize()
    # house.bathroom.wall_hanging = RedModernWallHanging()
    # house.bedroom.wall_hanging = GreenAntiqueWallHanging()
    # house.kitchen.wall_hanging = BlueRetroWallHanging()
    # house.living_room.wall_hanging = YellowUnsualWallHanging()
    # house.bedroom.lamp = YellowAntiqueLamp()
    # house.kitchen.curio = RedUnusualCurio()
    # house.living_room.wall_hanging = RedModernWallHanging()
    house.kitchen.curio = YellowRetroCurio()
    print(house.get_display())

    conds = ConditionsGenerator.generate_conditions(house)
    # conds = ConditionsGenerator.pick_conditions(house, 3, 120)
    pprint(conds)


if __name__ == "__main__":
    test_any()
