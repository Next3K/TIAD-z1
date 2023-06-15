import math
import random


class Wolf:
    def __init__(self, minimum: float, maximum: float, dimension: int):
        self.position: [float] = [random.uniform(minimum, maximum) for _ in range(dimension)]
        self.particle_best_positions: [float] = [self.position[i] for i in range(dimension)]
        # self.velocity: [float] = [0 for _ in range(dimension)]
        self.best_score = math.inf
        self.current_score = math.inf
        self.maximum = maximum
        self.minimum = minimum
        self.dimension: int = dimension

    def update_score(self, new_score):
        self.current_score = new_score
        # check if we get an improvement
        if new_score < self.best_score:
            self.best_score = new_score
            self.particle_best_positions = [number for number in self.position]

    def update_positions(self):
        pass
