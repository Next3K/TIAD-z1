class StopCriterion:
    def __init__(self, criterion: str, delta=0.01):
        self.criterion = criterion
        self.max_iterations_bound = 1000
        self.max_iterations = 300
        self.solution_delta = delta
        self.max_solution_stuck_iterations = 20
        self.best_solution = None
        self.leader_iterations = 0

    def should_stop(self, iteration: int, solution: float) -> bool:
        # stop in case of never ending run
        if iteration >= self.max_iterations_bound:
            return True

        # stop according to chosen stop criterion
        if self.criterion == "iterations":
            return iteration >= self.max_iterations
        elif self.criterion == "delta":
            # first iteration
            if iteration == 1:
                self.best_solution = solution
                self.leader_iterations = 1
                return False

            # non-first iteration, take note of the best solution changes
            if solution > self.best_solution:
                diff = abs(solution - self.best_solution)
                self.best_solution = solution
                self.leader_iterations = self.leader_iterations + 1 if diff < delta else 1
            else:
                self.leader_iterations += 1
            # check how long the best solution is stagnating
            return self.leader_iterations >= self.max_solution_stuck_iterations
        else:
            raise ValueError(f"Expected delta/iterations got \"{self.criterion}\" instead")
