import numpy as np

m = eval(input())
n = eval(input())
tolerance = eval(input())

matrix1 = np.array(np.random.randint(-10, 10, (m, n)), dtype = float)
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