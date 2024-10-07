from pprint import pprint
from decorum_generator.models.scenario import ScenarioGenerator


def test_any():
    game = ScenarioGenerator(3, 72)
    print(game.solution_house.get_display())

    game.generate_conditions()
    pprint(game.conditions)

    game.pick_conditions()
    pprint(game.players_conditions)


if __name__ == "__main__":
    test_any()
