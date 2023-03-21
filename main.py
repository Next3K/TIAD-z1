from Algorithm import Algorithm
from DifferentialEvolution import DifferentialEvolution
from Conductor import Conductor
from ParticleSwarm import ParticleSwarm
import functions
from StopCriterion import StopCriterion

if __name__ == '__main__':
    print('Program is starting!')

    function = functions.Ackley()
    stop_criterion_iterations = StopCriterion("iterations")
    stop_criterion_delta = StopCriterion("iterations", delta=function.accuracy)

    # DE parameters
    f = 0.5
    pop_size = 5 * function.dimensions
    cr = 0.5

    # PSO parameters
    swarm_size: int = 5 * function.dimensions
    inertion: float = 0.5
    social_constant: float = 2
    cognitive_constant: float = 1.2

    algorithm_de: Algorithm = DifferentialEvolution(stop_criterion_iterations, f, pop_size, cr)
    algorithm_pso: Algorithm = ParticleSwarm(stop_criterion_iterations,
                                             swarm_size,
                                             inertion,
                                             social_constant,
                                             cognitive_constant)

    conductor_pso = Conductor(30, algorithm_pso, function)
    conductor_de = Conductor(30, algorithm_de, function)

    print("PSO algorithm:")
    print(
        f"Best solution: {conductor_pso.best_solution},"
        f" avg solution: {conductor_pso.average_solution},"
        f" part success: {conductor_pso.part_successful},"
        f" standard deviation: {conductor_pso.standard_deviation}")

    print("DE algorithm:")
    print(
        f"Best solution: {conductor_de.best_solution},"
        f" avg solution: {conductor_de.average_solution},"
        f" part success: {conductor_de.part_successful},"
        f" standard deviation: {conductor_de.standard_deviation}")
