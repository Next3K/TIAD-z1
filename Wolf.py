import math
import random


class Wolf:
    def __init__(self, minimum: float, maximum: float, dimension: int):
        self.position: [float] = [random.uniform(minimum, maximum) for _ in range(dimension)]
        self.current_score = math.inf
        self.A = 2.0 * (2.0 * random.uniform(0, 1) - 1)
        self.C = random.uniform(0, 1)

    def update(self, new_score, position):
        self.current_score = new_score
        self.position = position
