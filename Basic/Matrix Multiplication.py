def matrix_multiplication(A, B):
    n = len(A)

    result = [[0 for _ in range(n)] for _ in range(n)]

    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]

    return result

A=[[1, 2, 3],
    [5, 6, 7],
    [4, 8, 9]
]
B=[[8, -6, 4],
    [1, 2, 5],
    [6, 8, 9]
]
result = matrix_multiplication(A, B)
print("\n Matrix A:")
for row in A:
    print(row)

print("\n Matrix B:")
for row in B:
    print(row)

print("\n AxB:")
for row in result:
    print(row)
