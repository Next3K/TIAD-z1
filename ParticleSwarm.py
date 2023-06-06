import math
import random

from Algorithm import Algorithm
from StopCriterion import StopCriterion
from functions import Equation
from particle import Particle


def apply_pattern(particles: [Particle],
                  function: Equation,
                  global_best_position: [float],
                  maximum: float,
                  minimum: float,
                  mutation_probability=0.01) -> [Particle]:
    pattern: [[float]] = []
    for particle in particles:
        positions = []
        random_particle: Particle = random.choice(particles)
        for i in range(len(particle.position)):
            if function.calculate(particle.particle_best_positions) < function.calculate(
                    random_particle.particle_best_positions):
                rd = random.uniform(0, 1)
                positions.append(
                    rd * particle.particle_best_positions[i] + (1 - rd) * global_best_position[i])
            else:
                positions.append(random_particle.particle_best_positions[i])
        pattern.append(positions)

    # mutation
    for sub_pattern in pattern:
        for i in range(len(sub_pattern)):
            if random.uniform(0, 1) < mutation_probability:
                sub_pattern[i] = random.uniform(minimum, maximum)

    # choice
    for i in range(len(particles)):
        old_value = particles[i].current_score
        new_value = function.calculate(pattern[i])
        if new_value < old_value:
            particles[i].position = pattern[i]
            particles[i].current_score = new_value

    return particles


class ParticleSwarm(Algorithm):

    def find_solution(self, function: Equation) -> (float, [[float]]):
        global_solution = math.inf

        min_val = function.min
        max_val = function.max
        dimensions = function.dimensions

        # initialize particles
        particles: [Particle] = [Particle(min_val, max_val, dimensions) for _ in range(self.swarm_size)]

        iteration = 0
        trace_list: [[float]] = []
        while True:
            current_best_solution = math.inf
            current_best_position = None

            # empty list of scores
            current_scores_list: [float] = []
            # calculate scores
            for particle in particles:
                calculated_score = function.calculate(particle.position)
                particle.update_score(calculated_score)

                current_scores_list.append(calculated_score)

                if calculated_score < current_best_solution:
                    current_best_solution = calculated_score
                    current_best_position = [position for position in particle.position]
            trace_list.append(current_scores_list)

            # update particle velocities
            for particle in particles:
                for dim in range(dimensions):
                    inertion_component = self.inertion * particle.velocity[dim]
                    cognitive_component = self.cognitive_constant * random.uniform(0, 1) * (
                            particle.particle_best_positions[dim] - particle.position[dim])
                    social_component = self.social_constant * random.uniform(0, 1) * (
                            current_best_position[dim] - particle.position[dim])
                    particle.velocity[dim] = inertion_component + cognitive_component + social_component

            # update particle positions
            for particle in particles:
                particle.update_positions()

            global_solution = min(current_best_solution, global_solution)

            # apply pattern
            apply_pattern(particles, function, current_best_position, min_val, max_val, self.mutation_probability)

            # check stop criterion
            iteration += 1
            if self.stop_criterion.should_stop(iteration=iteration, solution=global_solution):
                break

        return global_solution, trace_list

    def __init__(self,
                 stop_criterion: StopCriterion,
                 swarm_size: int = 80,
                 inertion: float = 0.2,
                 mutation_probability: float = 0.01,
                 social_constant: float = 0.45,
                 cognitive_constant: float = 0.35):

        super().__init__(stop_criterion)
        self.swarm_size = swarm_size
        self.inertion = inertion
        self.social_constant = social_constant
        self.cognitive_constant = cognitive_constant
        self.mutation_probability = mutation_probability
