from abc import ABC, abstractmethod

from StopCriterion import StopCriterion
from functions import Equation


class Algorithm:

    def __init__(self, stop_criterion: StopCriterion):
        self.stop_criterion: StopCriterion = stop_criterion

    @abstractmethod
    def find_solution(self, function: Equation) -> (float, [[float]]):
        pass
