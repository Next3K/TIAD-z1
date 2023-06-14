from Algorithm import Algorithm
from StopCriterion import StopCriterion
from functions import Equation


class Elo(Algorithm):
    def __init__(self, stop_criterion: StopCriterion):
        super().__init__(stop_criterion)
        self.stop_criterion: StopCriterion = stop_criterion

    def find_solution(self, function: Equation) -> (float, [[float]]):
        pass
