import math
import random


class Wolf:
    def __init__(self, minimum: float, maximum: float, dimension: int):
        self.position: [float] = [random.uniform(minimum, maximum) for _ in range(dimension)]
        self.current_score = math.inf
        self.A = 2.0 * (2.0 * random.uniform(0, 1) - 1)
        self.B = random.uniform(0, 1)

    def update_score(self, new_score):
        self.current_score = new_score

    def update_positions(self, position):
        self.position = position
