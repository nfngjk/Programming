import numpy as np

m = eval(input())
tolerance = eval(input())

A = np.array([[3, 3, -3, 2, -4], [-9, 3, 6, -4, -6], [3, 7, -9, 6, -5], [2, -9, -8, 5, -5]], dtype = float)

original_A = A.copy()      # original matrix

rank = 0

for j in range(0, m):

    pivot_position = rank + np.argmax(abs(A[rank : , j]))      # find the pivot position

    pivot = A[pivot_position][j]

    if(abs(pivot) < tolerance):

        continue

    if(pivot_position > rank):      # swap rows

        A[[rank, pivot_position]] = A[[pivot_position, rank]]

    for i in range(rank + 1, m):        # elimination

        scalar = A[i][j] / A[rank][j]

        A[i][j : ] = A[i][j : ] - A[rank][j : ] * scalar

        print(np.round(A, 4))

    rank = rank + 1

    if(rank >= m):

        print(np.round(A, 4))

        break

if(rank == m):

    x = np.zeros(m)

    for i in range(rank - 1, -1, -1):

        x[i] = A[i][m] - (sum(A[i][i + 1 : m] * x[i + 1 : m])) / A[i][i]        # solve Ax = b

    print(np.round(x, 4))

    print(np.linalg.norm(np.dot(original_A[ : , : m], x) - original_A[ : , m]))