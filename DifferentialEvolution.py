from random import uniform
import random
import math
from StopCriterion import StopCriterion
from Algorithm import Algorithm
from functions import Equation


class DifferentialEvolution(Algorithm):

    def find_solution(self, function: Equation) -> (float, [[float]]):

        global_solution = math.inf
        min_val = function.min
        max_val = function.max
        dimensions = function.dimensions

        population: [[float]] = [[uniform(min_val, max_val) for _ in range(dimensions)] for _ in range(self.pop_size)]

        iteration = 0
        trace_list: [[float]] = []
        while True:
            mutants = []
            # mutation
            for _ in population:
                x1, x2, x3 = random.sample(population, 3)
                mutant = []
                for i in range(dimensions):
                    new_value = (x1[i] + self.F * (x2[i] - x3[i]))
                    # respect search boundaries
                    if new_value > max_val:
                        new_value = max_val
                    elif new_value < min_val:
                        new_value = min_val
                    mutant.append(new_value)
                mutants.append(mutant)

            # cross-over
            genome_length = len(mutants[0])
            d = random.randrange(genome_length)
            end_pop = []
            for specimen_num in range(self.pop_size):
                end_pop.append(
                    [(mutants[specimen_num][k] if uniform(0, 1) < self.CR or k == d else population[specimen_num][k])
                     for
                     k in
                     range(genome_length)])

            # empty list of scores
            current_scores_list: [float] = []

            # get new, fitter population
            new_population: [[float]] = []
            tmp_best_solution: float = math.inf
            for i in range(len(population)):
                first_score = function.calculate(end_pop[i])
                second_score = function.calculate(population[i])
                better_score = min(first_score, second_score)
                current_scores_list.append(better_score)
                tmp_best_solution = min(better_score, tmp_best_solution)
                new_population.append(end_pop[i] if first_score < second_score else population[i])

            # remember all scores in this iterations
            trace_list.append(current_scores_list)

            # next generation
            population = new_population

            # update global best global_solution in this run
            global_solution = min(tmp_best_solution, global_solution)

            # check stop criterion
            iteration += 1
            if self.stop_criterion.should_stop(iteration=iteration, solution=global_solution):
                break
        return global_solution, trace_list

    def __init__(self, stop_criterion: StopCriterion, F: float = 0.5, pop_size: int = 50, CR: float = 0.5):
        super().__init__(stop_criterion)
        self.F = F
        self.pop_size = pop_size
        self.CR = CR
