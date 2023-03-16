import numpy as np

n = eval(input())       # the dimension of the matrix

matrix = np.array(np.random.randint(-10, 10, (n, n)), dtype = float)
A_lower = np.zeros((n, n))

for i in range(0, n):

    for j in range(i + 1, n):

        matrix[i][j] = 0

        A_lower = matrix.copy()

print(np.round(A_lower))

A = np.dot(A_lower, A_lower.T)      # the symmetric matrix

for j in range(0, n):

    temp = A[j][j] - np.sum(A_lower[j][ : j] * A_lower[j][ : j])

    if(temp > 0):

        matrix[j][j] = np.sqrt(temp)

        for i in range(j + 1, n):

            matrix[i][j] = (A[i][j] - np.sum(matrix[i][ : j] * matrix[j][ : j])) / matrix[j][j]

    else:

        print(j, "Error")

        break

print(np.round(matrix, 3))      # the lower matrix be decomposite of A
print(np.round(np.linalg.norm(A - np.dot(matrix, matrix.T))))