import math
import random

from Algorithm import Algorithm
from StopCriterion import StopCriterion
from Wolf import Wolf
from functions import Equation
import copy


class WolfPack(Algorithm):
    def __init__(self, stop_criterion: StopCriterion, num_population: int, mutation_probability: float = 0.02):
        super().__init__(stop_criterion)
        self.stop_criterion: StopCriterion = stop_criterion

        # algo specific args
        self.num_population: int = num_population
        self.a = 2.0
        assert 0 < mutation_probability < 1
        self.MUTATION_PROBABILITY = mutation_probability

    def find_solution(self, function: Equation) -> (float, [[float]]):
        a = self.a
        global_solution: float = math.inf
        min_val = function.min
        max_val = function.max
        dimensions = function.dimensions

        # pack initialization
        wolf_pack: [Wolf] = [Wolf(min_val, max_val, dimensions) for _ in range(self.num_population)]
        # wolf_pack = self.sort_pack(wolf_pack=wolf_pack, function=function)
        for wolf in wolf_pack:
            wolf.current_score = function.calculate(wolf.position)

        trace_list: [[float]] = []
        iteration: int = 0

        # sort wolf pack according to the scores
        wolf_pack = sorted(wolf_pack, key=lambda temp: temp.current_score)
        alpha_wolf, beta_wolf, gamma_wolf = copy.copy(wolf_pack[: 3])

        while iteration <= self.stop_criterion.max_iterations:

            a = 2 * (1 - iteration / self.stop_criterion.max_iterations)

            # patterns for wolves START computation
            patterns: [[float]] = []
            for i in range(len(wolf_pack)):
                # calculate pattern for given wolf
                pattern: [float] = [(random.choice([alpha_wolf, beta_wolf, gamma_wolf]).position[k] +
                                     wolf_pack[i].position[k]) * 0.5
                                    for k in range(dimensions)]

                # perform mutation
                pattern = [random.uniform(min_val, max_val)
                           if random.uniform(0, 1) < self.MUTATION_PROBABILITY else pattern[k]
                           for k in range(dimensions)]

                pattern.append(pattern)

            for i in range(len(wolf_pack)):
                current_pattern = patterns[i]
                pattern_eval = function.calculate(current_pattern)
                wolf_eval = wolf_pack[i].current_score
                if pattern_eval < wolf_eval:
                    wolf_pack[i].update(pattern_eval, current_pattern)

            # sort wolf pack according to the scores
            wolf_pack = sorted(wolf_pack, key=lambda temp: temp.current_score)
            alpha_wolf, beta_wolf, gamma_wolf = copy.copy(wolf_pack[: 3])
            # patterns for wolves END computation

            for i in range(len(wolf_pack)):
                A1, A2, A3 = a * (2 * random.randint(0, 1) - 1), a * (2 * random.randint(0, 1) - 1), a * (
                        2 * random.randint(0, 1) - 1)
                C1, C2, C3 = 2 * random.randint(0, 1), 2 * random.randint(0, 1), 2 * random.randint(0, 1)
                X_alfa = []
                X_beta = []
                X_gamma = []
                X_wolf = []

                for j in range(dimensions):
                    X_alfa.append(0.0)
                    X_beta.append(0.0)
                    X_gamma.append(0.0)
                    X_wolf.append(0.0)

                for j in range(dimensions):
                    X_alfa[j] = alpha_wolf.position[j] - A1 * abs(
                        C1 * alpha_wolf.position[j] - wolf_pack[i].position[j])
                    X_beta[j] = beta_wolf.position[j] - A2 * abs(C2 * beta_wolf.position[j] - wolf_pack[i].position[j])
                    X_gamma[j] = gamma_wolf.position[j] - A3 * abs(
                        C3 * gamma_wolf.position[j] - wolf_pack[i].position[j])
                    X_wolf[j] += X_alfa[j] + X_beta[j] + X_gamma[j]

                for j in range(dimensions):
                    X_wolf[j] /= 3.0

                F_wolf = function.calculate(X_wolf)

                if F_wolf < wolf_pack[i].current_score:
                    wolf_pack[i].update(F_wolf, X_wolf)

                if wolf_pack[i].current_score < global_solution:
                    global_solution = wolf_pack[i].current_score

            wolf_pack = sorted(wolf_pack, key=lambda temp: temp.current_score)
            alpha_wolf, beta_wolf, gamma_wolf = copy.copy(wolf_pack[: 3])

            iteration += 1

            wolf_scores = [wolf.current_score for wolf in wolf_pack]
            trace_list.append(wolf_scores)

        return global_solution, trace_list


def distance(list1, list2):
    squares = [(p - q) ** 2 for p, q in zip(list1, list2)]
    return sum(squares) ** .5
