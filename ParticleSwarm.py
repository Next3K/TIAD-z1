import math
import random

from Algorithm import Algorithm
from particle import Particle


class ParticleSwarm(Algorithm):

    def find_solution(self, function, min_x: float, max_x: float, min_y: float, max_y: float) -> float:
        solution = -math.inf
        best_coordinates = []

        # initialize particles
        particles: [Particle] = [Particle(min_x, max_x, min_y, max_y) for _ in range(self.swarm_size)]

        iteration = 0
        while True:
            current_iteration_solution = solution

            # set scores
            for particle in particles:
                calculated_score = function(particle.position[0], particle.position[1])
                particle.update_score(calculated_score)

                if calculated_score > current_iteration_solution:
                    current_iteration_solution = calculated_score
                    best_coordinates = [particle.position[0], particle.position[1]]

            # update particle velocities
            for particle in particles:
                for dim in range(len(particle.velocity)):
                    inertion_component = self.inertion * particle.velocity[dim]
                    cognitive_component = self.cognitive_constant * random.uniform(0, 1) * (
                            particle.particle_best_position[dim] - particle.position[dim])
                    social_component = self.social_constant * random.uniform(0, 1) * (
                            best_coordinates[dim] - particle.position[dim])
                    particle.velocity[dim] = inertion_component + cognitive_component + social_component

            # update particle positions
            for particle in particles:
                particle.update_positions()

            # calculate solution progress
            diff = abs(current_iteration_solution - solution)
            solution = max(current_iteration_solution, solution)

            # check stop criterion
            if self.stop_criterion == "iterations" and iteration > 250:
                iteration += 1
                break
            elif self.stop_criterion == "delta" and diff < 0.02:
                break

        return solution

    def __init__(self,
                 stop_criterion: str,
                 swarm_size: int = 80,
                 inertion: float = 0.2,
                 social_constant: float = 0.45,
                 cognitive_constant: float = 0.35):

        super().__init__(stop_criterion)
        self.swarm_size = swarm_size
        self.inertion = inertion
        self.social_constant = social_constant
        self.cognitive_constant = cognitive_constant
