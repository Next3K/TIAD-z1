from Algorithm import Algorithm
from statistics import mean, stdev
import math

from functions import Equation


class Conductor:
    def __init__(self, number_of_runs: int, algorithm: Algorithm, function: Equation):
        self.algorithm: Algorithm = algorithm
        self.solutions: [float] = []
        self.best_solution = math.inf
        self.trace_list: [[float]] = None

        # conduct experiments
        for i in range(number_of_runs):
            solution, trace_list = algorithm.find_solution(function)
            if solution is not None and solution is not -math.inf and solution is not math.inf:
                self.solutions.append(solution)
                if solution < self.best_solution:
                    self.best_solution = solution
                    self.trace_list = trace_list

        self.average_solution = mean(self.solutions)
        self.standard_deviation = stdev(self.solutions)
        self.part_successful = len(self.solutions) / number_of_runs
