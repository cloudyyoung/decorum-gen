from random import shuffle
from pulp import LpMaximize, LpProblem, LpVariable, lpSum, PULP_CBC_CMD

from decorum_generator.conditions.condition import Condition
from decorum_generator.conditions.conditions_generator import ConditionsGenerator
from decorum_generator.models.house import House


class GameGenerator:
    num_of_players: int
    total_difficulty_points: int

    starting_house: House
    solution_house: House

    conditions: list[Condition]
    players_conditions: list[list[Condition]]

    def __init__(self, num_of_players: int, total_difficulty_points: int) -> None:
        self.num_of_players = num_of_players
        self.total_difficulty_points = total_difficulty_points

        self.starting_house = House()
        self.starting_house.randomize()

        self.solution_house = House()
        self.solution_house.randomize()

        self.conditions = []

    def generate_conditions(self) -> list:
        self.conditions = []

        subclasses = ConditionsGenerator.__subclasses__()
        for subclass in subclasses:
            generator = subclass(self.solution_house)
            generator.generate()
            conds = generator.pick()
            self.conditions.extend(conds)

        self.conditions = list(set(self.conditions))

    def pick_conditions(self) -> list:
        shuffled_conditions = self.conditions.copy()
        difficulty_points_per_player = (
            self.total_difficulty_points // self.num_of_players
        )

        self.players_conditions = [[] for _ in range(self.num_of_players)]

        for t in range(self.num_of_players):
            shuffle(shuffled_conditions)
            conditions = self.__pick_conditions_for_single_player(
                shuffled_conditions, difficulty_points_per_player
            )

            # Remove selected conditions from the list
            for c in conditions:
                shuffled_conditions.remove(c)

            self.players_conditions[t] = conditions

    def __pick_conditions_for_single_player(
        self, conditions: list[Condition], difficulty_points: int
    ) -> list:
        knapsack_problem = LpProblem("Knapsack_Problem", LpMaximize)

        # Decision variable: 0/1 for each condition selected?
        x = LpVariable.dicts("condition", conditions, 0, 1, cat="Integer")

        # Objective function: maximize total value
        knapsack_problem += (
            lpSum([x[c] * c.difficulty_points for c in conditions]),
            "Total_Difficulty_Points",
        )

        # Constraint: total difficulty points should be less than or equal to the total difficulty points
        knapsack_problem += (
            lpSum([x[c] * c.difficulty_points for c in conditions])
            <= difficulty_points,
            "Total_Difficulty_Points_Constraint",
        )

        solver = PULP_CBC_CMD(msg=False)
        knapsack_problem.solve(solver)

        selected_conditions = [c for c in conditions if x[c].value() == 1]
        return selected_conditions
