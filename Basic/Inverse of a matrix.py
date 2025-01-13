import numpy as np

def inverse_matrix(matrix):
    try:
        inv_matrix = np.linalg.inv(matrix)
        return inv_matrix
    except np.linalg.LinAlgError:
        return "Matrix is singular and cannot be inverted."

matrix = np.array([
    [1, 2, 3],
    [0, 1, 4],
    [5, 6, 0]
])
print("Matrix:\n",matrix)
inv_matrix = inverse_matrix(matrix)
print("\nInverse of the matrix:\n",inv_matrix)