from Algorithm import Algorithm
from statistics import mean, stdev
import math


class Conductor:
    def __init__(self, N: int, algorithm: Algorithm, function, min_x: float, max_x: float, min_y: float, max_y: float):
        self.N: int = N
        self.algorithm: Algorithm = algorithm
        self.solutions: [float] = []
        self.best_solution = -math.inf
        self.average_solution: float = 0
        self.standard_deviation: float = 0
        self.part_successful: float = 0

        # conduct experiments
        for i in range(N):
            solution: float = algorithm.find_solution(function, min_x, max_x, min_y, max_y)
            if solution is not None and solution is not -math.inf and solution is not math.inf:
                self.solutions.append(solution)

        self.best_solution = max(self.solutions)
        self.average_solution = mean(self.solutions)
        self.standard_deviation = stdev(self.solutions)
        self.part_successful = len(self.solutions) / N
