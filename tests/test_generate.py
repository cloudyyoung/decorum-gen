from pprint import pprint
from decorum_generator.models.game import GameGenerator


def test_any():
    game = GameGenerator(3, 40)
    print(game.solution_house.get_display())

    game.generate_conditions()
    pprint(game.conditions)

    conds = game.pick_conditions()
    pprint(conds)

if __name__ == "__main__":
    test_any()
