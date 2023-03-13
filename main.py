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
        x, y = input("Provide DE parameters: 1) Pop size ").split()
        return DifferentialEvolution(x, y, stop_criterion)
    elif choice == 2:
        x, y = input("Provide PSO parameters: 1) Pop size ").split()
        return ParticleSwarm(x, y, stop_criterion)
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

    conductor = Conductor(30, algorithm, function, -1, 1, -1, 1)
