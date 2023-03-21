from Algorithm import Algorithm
from statistics import mean, stdev
import math

from functions import Equation


class Conductor:
    def __init__(self, number_of_runs: int, algorithm: Algorithm, function: Equation):
        self.algorithm: Algorithm = algorithm
        self.solutions: [float] = []
        self.best_solution = math.inf

        # conduct experiments
        for i in range(number_of_runs):
            solution: float = algorithm.find_solution(function)
            if solution is not None and solution is not -math.inf and solution is not math.inf:
                self.solutions.append(solution)

        self.best_solution = min(self.solutions)
        self.average_solution = mean(self.solutions)
        self.standard_deviation = stdev(self.solutions)
        self.part_successful = len(self.solutions) / number_of_runs
