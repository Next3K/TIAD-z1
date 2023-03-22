import math
from abc import ABC, abstractmethod


class Equation(ABC):
    def __init__(self, minimum: float, maximum: float, dimensions: int, accuracy: float):
        self.min = minimum
        self.max = maximum
        self.dimensions = dimensions
        self.accuracy = accuracy

    @abstractmethod
    def calculate(self, x: [float]) -> float:
        pass


class Sphere(Equation):
    def calculate(self, x: [float]) -> float:
        if len(x) != self.dimensions:
            raise ValueError(f"Expected {self.dimensions} elements, got: {len(x)}")

        total = 0
        for i in range(self.dimensions):
            total += (x[i]**2)

        return total

    def __init__(self, minimum: float = -100, maximum: float = 100, dimensions: int = 20, accuracy: float = 0.0001):
        super().__init__(minimum=minimum, maximum=maximum, dimensions=dimensions, accuracy=accuracy)


class FunctionTwo(Equation):
    def calculate(self, x: [float]) -> float:
        if len(x) != self.dimensions:
            raise ValueError(f"Expected {self.dimensions} elements, got: {len(x)}")

        total = 0
        for i in range(self.dimensions):
            total += (x[i] - i)**2
        return total

    def __init__(self, minimum: float = -100, maximum: float = 100, dimensions: int = 20, accuracy: float = 0.0001):
        super().__init__(minimum=minimum, maximum=maximum, dimensions=dimensions, accuracy=accuracy)


class Rosenbrock(Equation):
    def calculate(self, x: [float]) -> float:
        if len(x) != self.dimensions:
            raise ValueError(f"Expected {self.dimensions} elements, got: {len(x)}")

        total = 0
        for i in range(self.dimensions - 1):
            total += (100 * (x[i + 1] - x[i] ** 2) ** 2 + (x[i] - 1) ** 2)
        return total

    def __init__(self, minimum: float = -2.048, maximum: float = 2.048, dimensions: int = 20, accuracy: float = 30):
        super().__init__(minimum=minimum, maximum=maximum, dimensions=dimensions, accuracy=accuracy)


class Griewank(Equation):
    def calculate(self, x: [float]) -> float:
        if len(x) != self.dimensions:
            raise ValueError(f"Expected {self.dimensions} elements, got: {len(x)}")

        one = 0
        two = 1
        for i in range(self.dimensions):
            one += x[i] ** 2
            two *= math.cos(float(x[i]) / math.sqrt(i))
        return 1 + (float(one) / 4000.0) - float(two)

    def __init__(self, minimum: float = -600, maximum: float = 600, dimensions: int = 20, accuracy: float = 0.1):
        super().__init__(minimum=minimum, maximum=maximum, dimensions=dimensions, accuracy=accuracy)


class Rastrigin(Equation):
    def calculate(self, x: [float]) -> float:
        if len(x) != self.dimensions:
            raise ValueError(f"Expected {self.dimensions} elements, got: {len(x)}")

        total = 0
        for i in range(self.dimensions):
            total += (x[i] ** 2 - 10 * math.cos(2 * math.pi * x[i]) + 10)
        return total

    def __init__(self, minimum: float = -5.12, maximum: float = 5.12, dimensions: int = 20, accuracy: float = 30):
        super().__init__(minimum=minimum, maximum=maximum, dimensions=dimensions, accuracy=accuracy)


class Ackley(Equation):
    def calculate(self, x: [float]) -> float:
        if len(x) != self.dimensions:
            raise ValueError(f"Expected {self.dimensions} elements, got: {len(x)}")

        n = self.dimensions
        one = 0
        two = 0
        for i in range(n):
            one += (x[i] ** 2)
            two += (math.cos(2 * math.pi * x[i]))
        return -20 * math.exp(-0.2 * math.sqrt(one / n)) - math.exp(two / n) + 20 + math.e

    def __init__(self, minimum: float = -32, maximum: float = 32, dimensions: int = 20, accuracy: float = 0.0001):
        super().__init__(minimum=minimum, maximum=maximum, dimensions=dimensions, accuracy=accuracy)


class Easom(Equation):
    def calculate(self, x: [float]) -> float:
        if len(x) != self.dimensions:
            raise ValueError(f"Expected {self.dimensions} elements, got: {len(x)}")
        return -math.cos(x[0]) * math.cos(x[1]) * math.exp(-(x[0] - math.pi)**2 - (x[1] - math.pi)**2)

    def __init__(self, minimum: float = -10, maximum: float = 10, dimensions: int = 2, accuracy: float = 0.000001):
        super().__init__(minimum=minimum, maximum=maximum, dimensions=dimensions, accuracy=accuracy)


class Brown(Equation):
    def calculate(self, x: [float]) -> float:
        if len(x) != self.dimensions:
            raise ValueError(f"Expected {self.dimensions} elements, got: {len(x)}")

        total = 0
        for i in range(self.dimensions - 1):
            total += math.pow(x[i] ** 2, x[i + 1] ** 2 + 1) + math.pow(x[i + 1] ** 2, x[i] ** 2 + 1)
        return total

    def __init__(self, minimum: float = -1, maximum: float = 4, dimensions: int = 20, accuracy: float = 0.001):
        super().__init__(minimum=minimum, maximum=maximum, dimensions=dimensions, accuracy=accuracy)


class Schwefel(Equation):
    def calculate(self, x: [float]) -> float:
        if len(x) != self.dimensions:
            raise ValueError(f"Expected {self.dimensions} elements, got: {len(x)}")

        n = self.dimensions
        one = 0
        two = 1
        for i in range(n):
            one += (x[i] ** 2)
            two *= abs(x[i])
        return one + two

    def __init__(self, minimum: float = -10, maximum: float = 10, dimensions: int = 20, accuracy: float = 0.000001):
        super().__init__(minimum=minimum, maximum=maximum, dimensions=dimensions, accuracy=accuracy)


class Zakharov(Equation):
    def calculate(self, x: [float]) -> float:
        if len(x) != self.dimensions:
            raise ValueError(f"Expected {self.dimensions} elements, got: {len(x)}")

        n = self.dimensions
        one = 0
        two = 0
        for i in range(n):
            one += x[i]
            two += i * x[i] / 2
        return -one + math.pow(two, 2) + math.pow(two, 4)

    def __init__(self, minimum: float = -10, maximum: float = 10, dimensions: int = 20, accuracy: float = 0.001):
        super().__init__(minimum=minimum, maximum=maximum, dimensions=dimensions, accuracy=accuracy)


# not implemented
class SchafferSixteen(Equation):
    def calculate(self, x: [float]) -> float:
        if len(x) != self.dimensions:
            raise ValueError(f"Expected {self.dimensions} elements, got: {len(x)}")
        return 0

    def __init__(self, minimum: float = -100, maximum: float = 100, dimensions: int = 2, accuracy: float = 0.00001):
        super().__init__(minimum=minimum, maximum=maximum, dimensions=dimensions, accuracy=accuracy)


# not implemented
class LeeYao(Equation):
    def calculate(self, x: [float]) -> float:
        if len(x) != self.dimensions:
            raise ValueError(f"Expected {self.dimensions} elements, got: {len(x)}")
        return 0

    def __init__(self, minimum: float = -10, maximum: float = 10, dimensions: int = 20, accuracy: float = 0.01):
        super().__init__(minimum=minimum, maximum=maximum, dimensions=dimensions, accuracy=accuracy)


# not implemented
class Corana(Equation):
    def calculate(self, x: [float]) -> float:
        if len(x) != self.dimensions:
            raise ValueError(f"Expected {self.dimensions} elements, got: {len(x)}")
        return 0

    def __init__(self, minimum: float = -1000, maximum: float = 1000, dimensions: int = 4, accuracy: float = 0.000001):
        super().__init__(minimum=minimum, maximum=maximum, dimensions=dimensions, accuracy=accuracy)


def should_stop(iteration: int, diff: float, stop_criterion: str, max_iterations, delta) -> bool:
    if stop_criterion == "iterations":
        if iteration >= max_iterations:
            print(f"Total iterations: {iteration}")
            return True
    elif stop_criterion == "delta":
        if diff < delta and iteration >= 10:
            print(f"Total iterations: {iteration}")
            return True
    return False
