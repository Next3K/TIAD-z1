from abc import ABC, abstractmethod


class Algorithm:

    def __init__(self, stop_criterion: str):
        self.stop_criterion: str = stop_criterion

    @abstractmethod
    def find_solution(self, function, min_x: float, max_x: float, min_y: float, max_y: float) -> float:
        pass
