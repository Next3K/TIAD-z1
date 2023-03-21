from Algorithm import Algorithm
from DifferentialEvolution import DifferentialEvolution
from Conductor import Conductor
from ParticleSwarm import ParticleSwarm
import functions
from StopCriterion import StopCriterion

if __name__ == '__main__':
    print('Program is starting!')

    # DE parameters
    f = 0.5
    pop_size = 100
    cr = 0.5

    # PSO parameters
    swarm_size: int = 80
    inertion: float = 0.2
    social_constant: float = 0.45
    cognitive_constant: float = 0.35

    stop_criterion = StopCriterion("iterations")
    function = functions.FunctionTwo()

    algorithm_de: Algorithm = DifferentialEvolution(stop_criterion, f, pop_size, cr)
    algorithm_pso: Algorithm = ParticleSwarm(stop_criterion, swarm_size, inertion, social_constant, cognitive_constant)

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
