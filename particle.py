import math
import random


class Particle:
    def __init__(self, min_x: float, max_x: float, min_y: float, max_y: float):
        self.position: [float] = [random.uniform(min_x, max_x), random.uniform(min_y, max_y)]
        self.particle_best_position: [float] = [self.position[0], self.position[1]]
        self.velocity: [float] = [0, 0]
        self.best_score = -math.inf
        self.current_score = -math.inf

    def update_score(self, new_score):
        if self.best_score < new_score:
            self.best_score = new_score
            self.particle_best_position = [self.position[0], self.position[1]]
        self.current_score = new_score

    def update_positions(self):
        for dim in range(len(self.velocity)):
            self.position[dim] += self.velocity[dim]
