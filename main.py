from Algorithm import Algorithm
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

    # function
    function = functions.Sphere(dimensions=20)

    stop_criterion_iterations = StopCriterion("iterations")
    stop_criterion_delta = StopCriterion("iterations", delta=function.accuracy)

    # PSO parameters
    swarm_size: int = 30
    inertion: float = 0.8
    mutation_probability: float = 0.01
    social_constant: float = 1.2
    cognitive_constant: float = 1.2

    # standard PSO
    algorithm_pso: Algorithm = ParticleSwarm(stop_criterion_iterations,
                                             swarm_size,
                                             inertion,
                                             social_constant,
                                             cognitive_constant,
                                             False)

    # standard PSO with genetic function
    algorithm_gpso: Algorithm = ParticleSwarm(stop_criterion_iterations,
                                              swarm_size,
                                              inertion,
                                              social_constant,
                                              cognitive_constant,
                                              True,
                                              0.01)

    conductor_pso = Conductor(30, algorithm_pso, function)
    conductor_gpso = Conductor(30, algorithm_gpso, function)

    print("PSO algorithm:")
    print(
        f"Best solution: {conductor_pso.best_solution},"
        f" avg solution: {conductor_pso.average_solution},"
        f" part success: {conductor_pso.part_successful},"
        f" standard deviation: {conductor_pso.standard_deviation}")
    print_chart(conductor_pso.trace_list, "PSO")

    print("GPSO algorithm:")
    print(
        f"Best solution: {conductor_gpso.best_solution},"
        f" avg solution: {conductor_gpso.average_solution},"
        f" part success: {conductor_gpso.part_successful},"
        f" standard deviation: {conductor_gpso.standard_deviation}")
    print_chart(conductor_gpso.trace_list, "GPSO")
