from random import uniform
import random
import math

from Algorithm import Algorithm
from functions import should_stop


class DifferentialEvolution(Algorithm):

    def find_solution(self, function, min_x: float, max_x: float, min_y: float, max_y: float) -> float:

        solution = -math.inf
        population: [[float]] = [[uniform(min_x, max_x), uniform(min_y, max_y)] for _ in range(self.pop_size)]
        iteration = 0

        while True:
            mutants = []
            # mutation
            for _ in population:
                x1, x2, x3 = random.sample(population, 3)
                v = [(x1[i] + self.F * (x2[i] - x3[i])) for i in range(len(x1))]
                mutants.append(v)

            # cross-over
            d = random.randrange(len(mutants[0]))
            end_pop = [
                [(mutants[parent_iter][k] if uniform(0, 1) < self.CR or k == d else population[parent_iter][k]) for k in
                 range(len(population[0]))] for parent_iter in range(len(population))]

            # get new, fitter population
            new_population = [
                (end_pop[i] if function(end_pop[i][0], end_pop[i][1]) > function(population[i][0], population[i][1])
                 else population[i])
                for i in range(len(population))]

            population = new_population

            # remember current best solution
            tmp_best_solution = max(list(map(lambda specimen: function(specimen[0], specimen[1]), population)))
            diff = abs(tmp_best_solution - solution)
            solution = max(tmp_best_solution, solution)

            # check stop criterion
            iteration += 1
            if should_stop(iteration, diff, self.stop_criterion, self.MAX_ITERATIONS, self.DELTA):
                break

        # get best score
        return solution

    def __init__(self, stop_criterion: str, F: float = 0.5, pop_size: int = 50, CR: float = 0.5):
        super().__init__(stop_criterion)
        self.F = F
        self.pop_size = pop_size
        self.CR = CR

