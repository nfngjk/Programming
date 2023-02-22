import numpy as np

np.random.seed(123)

m = eval(input())
tolerance = eval(input())

A = np.array(np.random.randint(-10, 10, (m, m + 1)), dtype = float)
A_prime = A.copy()

print(A)

rank = 0

for j in range(0, m + 1):

    pivot_position = rank + np.argmax(abs(A[rank : ][j]))      # find the max argument position

    pivot = A[pivot_position][j]

    if(abs(pivot) < tolerance):

        break

    if(pivot_position > rank):      #swap rows

        A[[rank, pivot_position]] = A[[pivot_position, rank]]

        print(A)

    for i in range(rank + 1, m):

        scalar = A[i][j] / A[rank][j]

        A[i][j : ] = A[i][j : ] - A[rank][j : ] * scalar

    rank = rank + 1

    if(rank >= m):

        break

        print(np.round(A, 3))

if(rank == m):

    x = np.zeros(m)

    for i in range(rank - 1, -1, -1):

        x[i] = A[i][m] - (sum(A[i][i + 1 : m] * x[i + 1 : m])) / A[i][j]

    print(np.linalg.norm(np.dot(A_prime[ : ][ : m], x) - A[ : ][m]))