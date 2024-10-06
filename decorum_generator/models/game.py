from random import shuffle
from pulp import LpMaximize, LpProblem, LpVariable, lpSum, PULP_CBC_CMD

from decorum_generator.conditions.condition import Condition
from decorum_generator.conditions.conditions_generator import ConditionsGenerator
from decorum_generator.models.house import House


class GameGenerator:
    num_of_players: int
    total_diffilculty_points: int

    starting_house: House
    solution_house: House

    conditions: list[Condition]
    selected_conditions: list[Condition]
    players_conditions: list[list[Condition]]

    def __init__(self, num_of_players: int, total_diffilculty_points: int) -> None:
        self.num_of_players = num_of_players
        self.total_diffilculty_points = total_diffilculty_points

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
        return self.conditions

    def pick_conditions(self) -> list:
        shuffled_conditions = self.conditions.copy()
        shuffle(shuffled_conditions)

        knapsack_problem = LpProblem("Knapsack_Problem", LpMaximize)

        # Decision variable: 0/1 for each condition selected?
        x = LpVariable.dicts("condition", shuffled_conditions, 0, 1, cat="Integer")
        # Objective function: maximize total value
        knapsack_problem += (
            lpSum([x[c] * c.difficulty_points for c in shuffled_conditions]),
            "Total_Difficulty_Points",
        )

        # Constraint: total difficulty points should be less than or equal to the total difficulty points
        knapsack_problem += (
            lpSum([x[c] * c.difficulty_points for c in shuffled_conditions])
            <= self.total_diffilculty_points,
            "Total_Difficulty_Points_Constraint",
        )

        solver = PULP_CBC_CMD(msg=False)
        knapsack_problem.solve(solver)

        selected_conditions = [c for c in shuffled_conditions if x[c].value() == 1]
        self.selected_conditions = selected_conditions
        return self.selected_conditions

    def distribute_conditions(self) -> list:
        self.players_conditions = [[] for _ in range(self.num_of_players)]

        for i, condition in enumerate(self.selected_conditions):
            self.players_conditions[i % self.num_of_players].append(condition)

        return self.players_conditions
