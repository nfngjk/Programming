import numpy as np

m = eval(input())
tolerance = eval(input())

A = np.array(np.random.randint(-10, 10, (m, m + 1)), dtype = float)

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