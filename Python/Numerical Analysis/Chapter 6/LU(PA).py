import numpy as np

m = eval(input())
n = eval(input())
tolerance = eval(input())

A = np.array([[-7, -3, 9, -7, -8, 2], [-4, -5, 5, 7, 0, 1], [7, -3, -7, -9, -4, 8], [7, -3, -7, -9, -4, 8]], dtype = float)

original_matrix = A.copy()

print("A = \n", original_matrix)

# matrix represention
E = [i for i in range(min(m, n))]       # matrix representation of P

rank = 0

for j in range(0, n):

    # find the pivot position
    pivot_position = rank + np.argmax(abs(A[rank : , j]))

    pivot = A[pivot_position][j]

    if(abs(pivot) < tolerance):

        break;

    # swap rows
    if(pivot_position > rank):

        A[[rank, pivot_position]] = A[[pivot_position, rank]]

        E[rank] = pivot_position

    # elimination
    for i in range(rank + 1, m):

        scalar = A[i][j] / A[rank][j]

        A[i][j : ] = A[i][j : ] - A[rank][j : ] * scalar

        A[i][rank] = scalar

        print(np.round(A, 3))

    rank = rank + 1

    if(rank >= min(m, n)):

        # the process of calculation
        print(np.round(A, 3))

        break

P = np.identity(m)
L = np.identity(m)
U = np.zeros((m, n), dtype = float)

for i in range(min(m, n)):

    P[[i, E[i]]] = P[[E[i] , i]]

print("P = \n", P)

for i in range(0, rank):

    L[i + 1 : , i] = A[i + 1 : , i]

    A[i + 1 : , i] = 0

print("L = \n", np.round(L, 3))

for i in range(0, m):

    for j in range(i, n):

        U[i][j] = A[i][j]

print("U = \n", np.round(U, 3))

P_dot_A = np.copy(original_matrix)

for i in range(len(E)):

    P_dot_A[[i, E[i]]] = P_dot_A[[E[i], i]]

print(np.linalg.norm(P_dot_A - np.dot(L, A)))