import math
import random

from Algorithm import Algorithm
from StopCriterion import StopCriterion
from functions import Equation
from particle import Particle


class ParticleSwarm(Algorithm):

    def find_solution(self, function: Equation) -> float:
        global_solution = math.inf

        min_val = function.min
        max_val = function.max
        dimensions = function.dimensions

        # initialize particles
        particles: [Particle] = [Particle(min_val, max_val, dimensions) for _ in range(self.swarm_size)]

        iteration = 0
        while True:
            current_best_solution = math.inf
            current_best_position = None

            # set scores
            for particle in particles:
                calculated_score = function.calculate(particle.position)
                particle.update_score(calculated_score)

                if calculated_score < current_best_solution:
                    current_best_solution = calculated_score
                    current_best_position = [position for position in particle.position]

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

            # check stop criterion
            iteration += 1
            if self.stop_criterion.should_stop(iteration=iteration, solution=global_solution):
                break

        return global_solution

    def __init__(self,
                 stop_criterion: StopCriterion,
                 swarm_size: int = 80,
                 inertion: float = 0.2,
                 social_constant: float = 0.45,
                 cognitive_constant: float = 0.35):

        super().__init__(stop_criterion)
        self.swarm_size = swarm_size
        self.inertion = inertion
        self.social_constant = social_constant
        self.cognitive_constant = cognitive_constant
