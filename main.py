from Algorithm import Algorithm
from DifferentialEvolution import DifferentialEvolution
from Conductor import Conductor
from ParticleSwarm import ParticleSwarm
import functions
import matplotlib.pyplot as plt
from StopCriterion import StopCriterion


def print_chart(data: [[float]], name: str):
    x = [i for i in range(len(data))]
    y = data
    plt.xlabel("Iterations")
    plt.ylabel("Function value")
    plt.title(f"Graph for {name}")
    for i in range(len(y[0])):
        plt.plot(x, [pt[i] for pt in y])
    plt.show()


if __name__ == '__main__':
    print('Program is starting!')

    function = functions.Sphere()
    stop_criterion_iterations = StopCriterion("iterations")
    stop_criterion_delta = StopCriterion("iterations", delta=function.accuracy)

    # PSO parameters
    swarm_size: int = 3 * function.dimensions
    inertion: float = 0.8
    social_constant: float = 1.2
    cognitive_constant: float = 1.2

    # DE parameters
    f = 0.8
    pop_size = 3 * function.dimensions
    cr = 0.3

    algorithm_de: Algorithm = DifferentialEvolution(stop_criterion_iterations, f, pop_size, cr)
    algorithm_pso: Algorithm = ParticleSwarm(stop_criterion_iterations,
                                             swarm_size,
                                             inertion,
                                             social_constant,
                                             cognitive_constant)

    # conductor_pso = Conductor(30, algorithm_pso, function)
    # print("PSO algorithm:")
    # print(
    #     f"Best solution: {conductor_pso.best_solution},"
    #     f" avg solution: {conductor_pso.average_solution},"
    #     f" part success: {conductor_pso.part_successful},"
    #     f" standard deviation: {conductor_pso.standard_deviation}")

    conductor_de = Conductor(30, algorithm_de, function)
    print("DE algorithm:")
    print(
        f"Best solution: {conductor_de.best_solution},"
        f" avg solution: {conductor_de.average_solution},"
        f" part success: {conductor_de.part_successful},"
        f" standard deviation: {conductor_de.standard_deviation}")

    # print_chart(conductor_pso.trace_list, "PSO")
    print_chart(conductor_de.trace_list, "DE")
