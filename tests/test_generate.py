from pprint import pprint
from decorum_generator.conditions.condition import ConditionsGenerator
from decorum_generator.models.house import House
from decorum_generator.models.object import *
import random

# random.seed(123)


def test_any():
    house = House()
    house.get_random()
    # house.bathroom.wall_hanging = RedModernWallHanging()
    # house.bedroom.wall_hanging = GreenAntiqueWallHanging()
    # house.kitchen.wall_hanging = BlueRetroWallHanging()
    house.living_room.wall_hanging = YellowUnsualWallHanging()
    house.bedroom.lamp = YellowAntiqueLamp()
    # house.kitchen.curio = RedUnusualCurio()
    # house.living_room.wall_hanging = RedModernWallHanging()
    house.kitchen.curio = YellowRetroCurio()
    print(house.get_display())

    conds = ConditionsGenerator.generate_all_conditions(house)

    # with open("conditions.txt", "w") as f:
    #     f.write(house.get_display())

    #     f.write("\n\nConditions\n\n")
    #     for c in conds:
    #         f.write(f"({c} {c.difficulty_points} pts)\n")

    # Randomly draw 12 conditions
    random.shuffle(conds)
    random.shuffle(conds)
    random.shuffle(conds)
    random.shuffle(conds)
    random.shuffle(conds)
    random.shuffle(conds)
    pprint(conds[:12])
