from decorum_generator.conditions.condition import Condition
from decorum_generator.conditions.conditions_generator import ConditionsGenerator
from decorum_generator.models.house import House

from pulp import LpMaximize, LpProblem, LpVariable, lpSum


class GameGenerator:
    num_of_players: int
    total_diffilculty_points: int
    starting_house: House
    solution_house: House
    conditions: list[Condition]

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
            print(subclass.__name__, conds)
            self.conditions.extend(conds)

    def pick_conditions(self) -> list:
        knapsack_problem = LpProblem("Knapsack Problem", LpMaximize)

        # Decision variable: 0/1 for each condition selected?
        x = LpVariable.dicts("condition", self.conditions, 0, 1, cat="Integer")
        # Objective function: maximize total value
        knapsack_problem += (
            lpSum([x[c] * c.difficulty_points for c in self.conditions]),
            "Total_Difficulty_Points",
        )

        # Constraint: total difficulty points should be less than or equal to the total difficulty points
        knapsack_problem += (
            lpSum([x[c] * c.difficulty_points for c in self.conditions])
            <= self.total_diffilculty_points,
            "Total_Difficulty_Points_Constraint",
        )

        # # Decision variable: number of sets
        # y = LpVariable("num_of_sets", 0, cat="Integer")
        # # Constraint: the number of selected conditions must be multiplier of number of players
        # knapsack_problem += (
        #     lpSum([x[c] for c in self.conditions]) == y * self.num_of_players,
        #     "Number_of_Selected_Conditions_Constraint",
        # )

        knapsack_problem.solve()

        selected_conditions = [c for c in self.conditions if x[c].value() == 1]

        return selected_conditions
