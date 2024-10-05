from pprint import pprint
from decorum_generator.models.game import GameGenerator


def test_any():
    game = GameGenerator(3, 20)
    print(game.solution_house.get_display())

    game.generate_conditions()
    pprint(game.conditions)

    with open("test_any.txt", "w") as f:
        f.write(game.solution_house.get_display())
        f.write("\n")
        f.write("\n".join([str(c.__repr__()) for c in game.conditions]))


if __name__ == "__main__":
    test_any()
