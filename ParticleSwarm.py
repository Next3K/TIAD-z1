from Algorithm import Algorithm


class ParticleSwarm(Algorithm):

    def find_solution(self, function, min_x: float, max_x: float, min_y: float, max_y: float) -> float:
        pass

    def __init__(self, x: float, y: float, stop_criterion: str):
        super().__init__(stop_criterion)
        self.x = x
        self.y = y
