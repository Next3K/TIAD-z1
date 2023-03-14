import sys

from Algorithm import Algorithm
from DifferentialEvolution import DifferentialEvolution
from Experimentator import Conductor
from ParticleSwarm import ParticleSwarm
from functions import function_one
from functions import function_two
from functions import function_three


# choose algorithm
def get_algorithm(choice: int, stop_criterion: str):
    if choice == 1:
        print("Chosen algorithm: DE")
        answer = input("Do you want to provide parameters? (y/n)")
        if answer == "y":
            f, pop_size, cr = input("Provide DE parameters: 1) F 2) Population size 3) CR ").split()
            return DifferentialEvolution(stop_criterion, F=float(f), pop_size=int(pop_size), CR=float(cr))
        else:
            return DifferentialEvolution(stop_criterion)
    elif choice == 2:
        print("Chosen algorithm: PSO")
        answer = input("Do you want to provide parameters? (y/n)")
        if answer == "y":
            swarm_size, inertion, social_constant, cognitive_constant = input(
                "Provide PSO parameters: 1) swarm size 2) inertion 3) social constant 4) cognitive constant ").split()
            return ParticleSwarm(stop_criterion,
                                 swarm_size=int(swarm_size),
                                 inertion=float(inertion),
                                 social_constant=float(social_constant),
                                 cognitive_constant=float(cognitive_constant))
        else:
            return ParticleSwarm(stop_criterion)
    else:
        raise Exception("Invalid algorithm numer")


# choose function
def get_function(choice):
    if choice == 1:
        print("Chosen function: Goldstein–Price")
        return function_one
    elif choice == 2:
        print("Chosen function: Booth")
        return function_two
    elif choice == 3:
        print("Chosen function: Himmelblau")
        return function_three
    else:
        raise Exception("Invalid function numer")


# choose stop criterion
def get_stop_criterion(choice: int) -> str:
    if choice == 1:
        print("Chosen criterion: iterations")
        return "iterations"
    elif choice == 2:
        print("Chosen criterion: delta")
        return "delta"
    else:
        raise Exception("Invalid criterion numer")


if __name__ == '__main__':
    print('Program is starting!')

    algorithm_choice: int = int(sys.argv[1])
    reward_function_choice: int = int(sys.argv[2])
    stop_criterion_choice: int = int(sys.argv[3])

    stop_criterion_name: str = get_stop_criterion(stop_criterion_choice)
    algorithm: Algorithm = get_algorithm(algorithm_choice, stop_criterion_name)
    function = get_function(reward_function_choice)

    conductor = Conductor(30, algorithm, function, -5, 5, -5, 5)

    print(
        f"Best solution: {conductor.best_solution},"
        f" avg solution: {conductor.average_solution},"
        f" part success: {conductor.part_successful},"
        f" standard deviation: {conductor.standard_deviation}")
