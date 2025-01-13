import numpy as np

def solve_linear_equations(coefficients, constants):
    coefficients_matrix = np.array(coefficients)
    constants_matrix = np.array(constants)

    try:
        solution = np.linalg.solve(coefficients_matrix, constants_matrix)
        return solution
    except np.linalg.LinAlgError:
        return "The system of equations has no unique solution."

coefficients = [
    [2, -1, 3],
    [1, 2, -1],
    [3, -2, 1]
]
constants = [5, 6, 2]

solution = solve_linear_equations(coefficients, constants)
print("Solution: \n[x y z] = ", solution)
