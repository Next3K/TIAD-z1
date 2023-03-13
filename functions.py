# Goldstein–Price function
def function_one(x: float, y: float) -> float:
    return -((1 + (x + y + 1) ** 2 * (19 - 14 * x + 3 * x ** 2 - 14 * y + 6 * x * y + 3 * y ** 2)) *
             (30 + (2 * x - 3 * y) ** 2 * (18 - 32 * x + 12 * x ** 2 + 48 * y - 36 * x * y + 27 * y ** 2)))


# Booth function
def function_two(x: float, y: float) -> float:
    return -((x + 2 * y - 7) ** 2 + (2 * x + y - 5) ** 2)


# Himmelblau function
def function_three(x: float, y: float) -> float:
    return -((x ** 2 + y - 11) ** 2 + (x + y ** 2 - 7) ** 2)
