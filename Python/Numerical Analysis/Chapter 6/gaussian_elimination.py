import numpy as np

A = np.array([[1, 1 / 2, 1 / 3, 1 / 4, 1 / 6], 
             [1 / 2, 1 / 3, 1 / 4, 1 / 5, 1 / 7], 
             [1 / 3, 1 / 4, 1 / 5, 1 / 6, 1 / 8], 
             [1 / 4, 1 / 5, 1 / 6, 1 / 7, 1 / 9]])

m = eval(input())
tolerance = eval(input())


A_prime = A.copy()      # original matrix

rank = 0

for j in range(0, m):

    pivot_position = rank + np.argmax(abs(A[rank : , j]))      # find the pivot position

    pivot = A[pivot_position][j]

    if(abs(pivot) < tolerance):

        break

    if(pivot_position > rank):      #swap rows

        A[[rank, pivot_position]] = A[[pivot_position, rank]]

    for i in range(rank + 1, m):

        scalar = A[i][j] / A[rank][j]

        A[i][j : ] = A[i][j : ] - A[rank][j : ] * scalar

    rank = rank + 1

    if(rank >= m):

        print(np.round(A, 3))

        break

if(rank == m):

    x = np.zeros(m)

    for i in range(rank - 1, -1, -1):

        x[i] = A[i][m] - (sum(A[i][i + 1 : m] * x[i + 1 : m])) / A[i][i]

    print(np.round(x, 3))

    print(np.linalg.norm(np.dot(A_prime[ : , : m], x) - A_prime[ : , m]))