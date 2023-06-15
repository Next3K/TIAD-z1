import math
import random

from Algorithm import Algorithm
from StopCriterion import StopCriterion
from Wolf import Wolf
from functions import Equation


class WolfPack(Algorithm):
    def __init__(self, stop_criterion: StopCriterion, num_population: int):
        super().__init__(stop_criterion)
        self.stop_criterion: StopCriterion = stop_criterion

        # algo specific args
        self.num_population: int = num_population
        self.a = 2.0

    def find_solution(self, function: Equation) -> (float, [[float]]):
        global_solution = math.inf
        min_val = function.min
        max_val = function.max
        dimensions = function.dimensions

        # pack initialization
        wolf_pack: [Wolf] = [Wolf(min_val, max_val, dimensions) for _ in range(self.num_population)]
        wolf_pack = self.sort_pack(wolf_pack=wolf_pack)

        xa: Wolf = wolf_pack[0]
        xb: Wolf = wolf_pack[1]
        xc: Wolf = wolf_pack[2]

        iteration: int = 0
        while iteration <= self.stop_criterion.max_iterations:
            for i in range(len(wolf_pack)):
                wolf = wolf_pack[i]
                A = self.a * (2 * random.uniform(0, 1) - 1)
                C = 2 * random.uniform(0, 1)

                d_alfa: [float] = [x - y for x, y in zip([C * xa.position[i] for i in range(dimensions)],
                                                         wolf.position)]
                d_beta: [float] = [x - y for x, y in zip([C * xb.position[i] for i in range(dimensions)],
                                                         wolf.position)]
                d_gamma: [float] = [x - y for x, y in zip([C * xc.position[i] for i in range(dimensions)],
                                                          wolf.position)]

                x_alfa: [float] = [x - y for x, y in zip(xa.position, [A * d_alfa[i] for i in range(dimensions)])]
                x_beta: [float] = [x - y for x, y in zip(xb.position, [A * d_beta[i] for i in range(dimensions)])]
                x_gamma: [float] = [x - y for x, y in zip(xc.position, [A * d_gamma[i] for i in range(dimensions)])]

                x_k = [(a + b + c) / 3 for a, b, c in zip(x_alfa, x_beta, x_gamma)]
                wolf.update_positions(x_k)
                wolf.update_score(function.calculate(x_k))

                if wolf.current_score < xa.current_score:
                    xa = wolf
                elif xa.current_score < wolf.current_score < xb.current_score:
                    xb = wolf
                elif xb.current_score < wolf.current_score < xc.current_score:
                    xc = wolf

            self.a = 2.0 - (2.0 * (iteration / self.stop_criterion.max_iterations))
            iteration += 1

    def sort_pack(self, wolf_pack: [Wolf], function: Equation):
        for wolf in wolf_pack:
            evaluation = function.calculate(wolf.position)
            wolf.update_score(evaluation)
        wolf_pack.sort(key=lambda x: x.current_score)
        return wolf_pack


def distance(list1, list2):
    squares = [(p - q) ** 2 for p, q in zip(list1, list2)]
    return sum(squares) ** .5
