import numpy as np

def calculate_eigenvalues(matrix):
    eigenvalues,_= np.linalg.eig(matrix)
    return eigenvalues

matrix = np.array([
    [1, 1, 1],
    [1, -3, -3],
    [2, 4, 4]
])


eigenvalues = calculate_eigenvalues(matrix)
print("The eigenvalues of the matrix are:\n", eigenvalues)
