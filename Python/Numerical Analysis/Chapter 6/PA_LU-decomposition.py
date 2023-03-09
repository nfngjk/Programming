import numpy as np

m = eval(input())
n = eval(input())
tolerance = eval(input())

A = np.array([[-7, -3, 9, -7, -8, 2], [-4, -5, 5, 7, 0, 1], [7, -3, -7, -9, -4, 8], [7, -3, -7, -9, -4, 8]], dtype = float)

original_matrix = A.copy()      # original matrix

E = [i for i in range(0, min(m, n))]        # matrix representation

rank = 0

for j in range(0, n):

    pivot_position = rank + np.argmax(abs(A[rank : , j]))      # find the pivot position

    pivot = A[pivot_position][j]

    if(abs(pivot) < tolerance):

        break

    if(pivot_position > rank):      #swap rows

        A[[rank, pivot_position]] = A[[pivot_position, rank]]

        E[rank] = pivot_position

    for i in range(rank + 1, m):        # elimination

        scalar = A[i][j] / A[rank][j]

        A[i][j : ] = A[i][j : ] - A[rank][j : ] * scalar
        # A[i][rank] = scalar

        print(np.round(A, 4))

    rank = rank + 1

    if(rank >= min(m, n)):

        print(np.round(A, 4))

        break

P = np.identity(m)
L = np.identity(m)

for j in range(0, rank):

    L[j + 1 : , j] = A[j + 1 : , j]

    A[j + 1 : , j] = 0

print(np.round(L, 3))

for i in range(min(m, n)):

    P[[i, E[i]]] = P[[E[i], i]]

print(P)

P_dot_A = np.copy(original_matrix)

for i in range(len(E)):

    P_dot_A[[i, E[i]]] = P_dot_A[[E[i], i]]

print(np.linalg.norm(P_dot_A - np.dot(L, A)))