import numpy as np

m = eval(input())
n = eval(input())
tolerance = eval(input())

matrix1 = np.array([[3, 3, 6, 6, 3, 8, 3], [4, 2, 6, 6, 6 ,6, 4], [5, 1, 6, 0, 9, 0, 1], [-2, 2, 0, 3, -6, 0, 1], [0, -3, -3, -6, 3, -9, -3]], dtype = float)
matrix2 = np.zeros((min(m, n), min(m, n)))

rank = 0

for j in range(0, n):

    temp = matrix1[ : ][j]

    if(rank >= min(m, n)):

        break

    for i in range(0, j):
        
        temp = temp - np.dot(matrix2[ : ][i], matrix1[ : ][j]) * matrix2[ : ][i]

    norm = np.linalg.norm(temp)

    if(norm > tolerance):

        matrix2[ : ][rank] = temp / norm

        rank = rank + 1

print(np.linalg.norm(np.dot(matrix2[ : ][ : rank], matrix2[ : ][ : rank].T) - np.identity(min(m, n))))